#!/usr/bin/env python3
"""Tests of facthory/dmg/image.sh, the disk image step of the macOS package, on any machine: the
macOS tools (hdiutil, codesign, ditto, xattr, spctl) are stubs in a temporary PATH that log their
calls, so what is tested is the helper's logic: the image is built with `create -srcfolder`, the app
inside the finished image and a copy of it are checked strictly, a failure is returned after the
image is detached, with the attributes listed, and nothing is built or checked twice.

  env -i PATH="$PATH" HOME="$HOME" python3 facthory/test_dmg_image.py
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HELPER = Path(__file__).resolve().parent / "dmg" / "image.sh"

# Each stub appends its command line to $LOG. FAIL_ON names what makes it exit 1: "codesign" fails
# when its target path contains $CODESIGN_FAIL_IN; hdiutil fails for the verb in $HDIUTIL_FAIL.
STUBS = {
    "hdiutil": """#!/bin/bash
echo "hdiutil $*" >>"$LOG"
verb="$1"
[ "$verb" = "${HDIUTIL_FAIL:-}" ] && exit 1
if [ "$verb" = attach ]; then
  # the mount point is the argument after -mountpoint; the app is a directory inside it
  while [ $# -gt 0 ]; do [ "$1" = -mountpoint ] && mp="$2"; shift; done
  mkdir -p "$mp/$APP_NAME/Contents"
fi
exit 0
""",
    "codesign": """#!/bin/bash
echo "codesign $*" >>"$LOG"
target="${@: -1}"
case "$target" in *"${CODESIGN_FAIL_IN:-@@never@@}"*) echo "codesign: Disallowed xattr com.apple.FinderInfo" >&2; exit 1;; esac
exit 0
""",
    "ditto": """#!/bin/bash
echo "ditto $*" >>"$LOG"
cp -R "$1" "$2"
""",
    "xattr": """#!/bin/bash
echo "xattr $*" >>"$LOG"
echo "$2: com.apple.FinderInfo:"
""",
    "spctl": """#!/bin/bash
echo "spctl $*" >>"$LOG"
[ -n "${SPCTL_FAIL:-}" ] && exit 1
exit 0
""",
    "sleep": "#!/bin/bash\necho \"sleep $*\" >>\"$LOG\"\n",
}


class Run:
    def __init__(self, returncode: int, stdout: str, stderr: str, log: list[str]):
        self.returncode, self.stdout, self.stderr, self.log = returncode, stdout, stderr, log

    def calls(self, prefix: str) -> list[str]:
        return [line for line in self.log if line.startswith(prefix)]


class ImageStep(unittest.TestCase):
    def run_bash(self, script: str, **env: str) -> Run:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bindir = tmp_path / "bin"
            bindir.mkdir()
            for name, body in STUBS.items():
                path = bindir / name
                path.write_text(body)
                path.chmod(0o755)
            log = tmp_path / "log"
            log.write_text("")
            full = (
                'set -euo pipefail\nwarn() { echo "warning: $*" >&2; }\n'
                f'. "{HELPER}"\n'
                f'scratch="{tmp_path}/scratch"\n' + script
            )
            proc = subprocess.run(
                ["bash", "-c", full],
                capture_output=True,
                text=True,
                env={"PATH": f"{bindir}:/usr/bin:/bin", "LOG": str(log), "APP_NAME": "Facthory Test.app", **env},
            )
            return Run(proc.returncode, proc.stdout, proc.stderr, log.read_text().splitlines())

    def test_the_image_is_built_with_create_srcfolder_and_never_makehybrid(self) -> None:
        r = self.run_bash('build_dmg_image /stage "Facthory Test" /out/x.dmg')
        self.assertEqual(r.returncode, 0, r.stderr)
        creates = r.calls("hdiutil create")
        self.assertEqual(len(creates), 1)
        self.assertIn("-srcfolder /stage", creates[0])
        self.assertIn("-volname Facthory Test", creates[0])
        self.assertFalse(r.calls("hdiutil makehybrid"))
        self.assertFalse(r.calls("hdiutil convert"))

    def test_a_failing_create_is_retried_five_times_then_fails(self) -> None:
        r = self.run_bash('build_dmg_image /stage "Facthory Test" /out/x.dmg', HDIUTIL_FAIL="create")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(len(r.calls("hdiutil create")), 5)
        self.assertIn("hdiutil create failed 5 times", r.stderr)

    def test_a_good_app_passes_in_the_image_and_in_a_copy(self) -> None:
        r = self.run_bash('verify_dmg_app /out/x.dmg "Facthory Test.app" "$scratch" 0')
        self.assertEqual(r.returncode, 0, r.stderr)
        verified = r.calls("codesign --verify --deep --strict")
        self.assertEqual(len(verified), 2, "the app inside the image, then a copy of it")
        self.assertIn("mount/Facthory Test.app", verified[0])
        self.assertIn("copy/Facthory Test.app", verified[1])
        self.assertTrue(r.calls("hdiutil attach -readonly"))
        self.assertTrue(r.calls("hdiutil detach"))
        self.assertFalse(r.calls("spctl"), "only a notarized image is assessed by Gatekeeper")

    def test_an_attribute_inside_the_image_fails_the_step_after_detaching(self) -> None:
        r = self.run_bash('verify_dmg_app /out/x.dmg "Facthory Test.app" "$scratch" 0', CODESIGN_FAIL_IN="/mount/")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("fails strict verification", r.stderr)
        self.assertTrue(r.calls("xattr -lr"), "the attributes found are listed")
        self.assertTrue(r.calls("hdiutil detach"), "the image is detached even when the check fails")
        self.assertFalse(r.calls("ditto"), "nothing is copied out of an image that already fails")

    def test_an_attribute_that_appears_only_after_copying_out_fails_the_step(self) -> None:
        r = self.run_bash('verify_dmg_app /out/x.dmg "Facthory Test.app" "$scratch" 0', CODESIGN_FAIL_IN="/copy/")
        self.assertNotEqual(r.returncode, 0)
        self.assertTrue(r.calls("hdiutil detach"))
        self.assertIn("fails strict verification", r.stderr)

    def test_the_step_stops_a_script_that_set_e(self) -> None:
        r = self.run_bash(
            'verify_dmg_app /out/x.dmg "Facthory Test.app" "$scratch" 0\necho "notarizing the image"',
            CODESIGN_FAIL_IN="/mount/",
        )
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("notarizing the image", r.stdout, "the build stops before the image is notarized")

    def test_a_notarized_image_is_also_assessed_by_gatekeeper(self) -> None:
        ok = self.run_bash('verify_dmg_app /out/x.dmg "Facthory Test.app" "$scratch" 1')
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertEqual(len(ok.calls("spctl --assess --type execute")), 1)
        bad = self.run_bash('verify_dmg_app /out/x.dmg "Facthory Test.app" "$scratch" 1', SPCTL_FAIL="1")
        self.assertNotEqual(bad.returncode, 0)
        self.assertTrue(bad.calls("hdiutil detach"))

    def test_an_image_that_cannot_be_attached_fails_without_checking_anything(self) -> None:
        r = self.run_bash('verify_dmg_app /out/x.dmg "Facthory Test.app" "$scratch" 0', HDIUTIL_FAIL="attach")
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(r.calls("codesign"))


if __name__ == "__main__":
    sys.exit(unittest.main(verbosity=2))
