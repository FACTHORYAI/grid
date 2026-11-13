# shellcheck shell=bash
# Facthory's disk image step, sourced by packaging/macos/package.sh (the brand rules in
# facthory/brand.toml put it there; it is copied to packaging/macos/facthory-image.sh).
#
# Why it exists. Upstream builds the image with `hdiutil makehybrid -hfs` + `convert`. makehybrid
# gives every file and folder in the image a com.apple.FinderInfo attribute, so the app's seal is
# intact in the build but `codesign --verify --deep --strict` fails on the app inside the mounted
# image and on any copy made from it ("resource fork, Finder information, or similar detritus not
# allowed"). The failure showed only in a run that signs, because that is the only run whose
# install check verifies the signatures (facthory/install_check.py, --signed). `create -srcfolder`
# copies the staged files as they are, and a check of the app inside the finished image catches
# what the build's own check of the app before packaging cannot see.
#
# What it gives package.sh:
#   build_dmg_image <stage> <volume name> <dmg>
#       the image of the staged folder, with attached-device retries (`create -srcfolder` fails now
#       and then on CI runners with "Resource busy")
#   verify_dmg_app <dmg> <app name> <scratch dir> <notarized: 0|1>
#       mounts the image read-only and runs the strict, deep signature check of the app inside it
#       and of a ditto copy of it (what an installer's user ends up with). Returns non-zero after
#       detaching the image, and prints the attributes found, so the build stops before the image
#       is notarized, stapled or uploaded.
# Needs from package.sh: `warn` (packaging env), and the macOS tools hdiutil, codesign, ditto,
# xattr; spctl when notarized.

# Retries an hdiutil verb that attaches a device. Usage: hdiutil_retry <verb> <args...>; five
# tries with growing pauses.
hdiutil_retry() {
  local verb="$1"
  local attempt
  for attempt in 1 2 3 4 5; do
    if hdiutil "$@"; then
      return 0
    fi
    if [[ "$attempt" = 5 ]]; then
      echo "error: hdiutil $verb failed 5 times" >&2
      return 1
    fi
    warn "hdiutil $verb failed (attempt $attempt of 5); retrying in $((attempt * 10))s"
    sleep $((attempt * 10))
  done
  return 1
}

# The image of a staged folder. The volume name has no version: the staged .DS_Store finds the
# background through an alias that includes it.
build_dmg_image() {
  local stage="$1" volname="$2" dmg="$3"
  rm -f "$dmg"
  hdiutil_retry create -srcfolder "$stage" -volname "$volname" -fs HFS+ -format UDZO \
    -imagekey zlib-level=9 -ov "$dmg"
}

verify_dmg_app() {
  local dmg="$1" app="$2" scratch="$3" notarized="${4:-0}"
  local mount="$scratch/mount" copy="$scratch/copy" rc=0
  mkdir -p "$mount" "$copy"
  hdiutil_retry attach -readonly -nobrowse -noautoopen -mountpoint "$mount" "$dmg" >/dev/null || return 1
  echo "==> strict signature check of $app inside $(basename "$dmg")"
  codesign --verify --deep --strict --verbose=2 "$mount/$app" || rc=1
  if [[ "$rc" = 0 ]]; then
    ditto "$mount/$app" "$copy/$app" || rc=1
  fi
  if [[ "$rc" = 0 ]]; then
    echo "==> strict signature check of a ditto copy of it"
    codesign --verify --deep --strict --verbose=2 "$copy/$app" || rc=1
  fi
  if [[ "$rc" = 0 ]] && [[ "$notarized" = 1 ]]; then
    spctl --assess --type execute -vvv "$copy/$app" || rc=1
  fi
  if [[ "$rc" != 0 ]]; then
    echo "error: $app in $(basename "$dmg") fails strict verification; extended attributes:" >&2
    xattr -lr "$mount/$app" >&2 || true
  fi
  hdiutil_retry detach "$mount" >/dev/null || hdiutil detach "$mount" -force >/dev/null || rc=1
  rm -rf "$copy"
  return "$rc"
}
