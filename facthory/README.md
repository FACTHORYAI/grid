# Facthory Grid: the Facthory patch set

This repository is a downstream distribution of
[GridCraft](https://github.com/storytold/gridcraft): `main` is GridCraft's history plus the files
listed here, and every GridCraft release is merged into it. Nothing in GridCraft's own files is
edited in the repository; the brand is applied to a fresh checkout when the app is built, so
upstream merges never conflict with it.

## The patch set

Files Facthory adds to upstream's tree, and nothing else:

| Path | What it is |
| ---- | ---------- |
| `facthory/brand.toml` | The brand as data: names, app ids, links, publisher, the exact edits, the installer GUID namespace, the mark check |
| `facthory/rebrand.py` | Applies `brand.toml` to a checkout (`apply`) and checks shipped files for upstream marks (`check`) |
| `facthory/icons/grid.svg` | The Facthory Grid icon (original artwork) |
| `facthory/icons/render.py` | Renders the icon set (`facthory/icons/app-icon/`, committed) with resvg, and credits it in `ATTRIBUTION.md` |
| `facthory/README.md` | This list |
| `.github/README.md` | The repository's front page |
| `.github/workflows/facthory.yml` | The branded build: apply, upstream's gate on the branded tree, release build, mark check |
| `.github/workflows/facthory-release.yml` | Signed installers for macOS, Windows and Linux from a tag `v<version>`, as a draft release |
| `facthory/release.py` | Collects a release's files and writes `SHA256SUMS`, the update feed `latest.json` and the notes |
| `facthory/dmg/background.svg` | The disk image window, from upstream's, in our colours and with our name |
| `facthory/update/facthory_update.rs` | The updater, copied into the app at build time (see Updates) |

And two upstream files changed:

| Path | Change | Why |
| ---- | ------ | --- |
| `.github/dependabot.yml` | Removed | Dependency updates reach us with upstream's releases; our own bump PRs would only diverge from upstream's lockfile |
| `ATTRIBUTION.md` | One block under the title (`<!-- facthory:begin … end -->`), written by `facthory/icons/render.py` | Upstream's `cargo xtask assets` needs a row for every image in the repository, ours included; upstream seldom edits the top of the file, and after a merge that touches it, `render.py --attribution` rewrites the block |

## What the brand changes in a build

`facthory/rebrand.py apply` makes these changes, all declared in `brand.toml`:

- **Name**: GridCraft becomes Facthory Grid in the interface, the CLI, the MCP server, file
  metadata the app writes, the installers and the Linux metadata.
- **Identifiers**: `ai.storyteller.gridcraft` becomes `com.facthory.grid` (bundle id, desktop id,
  AppStream id, icon names); crates, binaries and folders `gridcraft*` become `facthorygrid*`;
  environment variables `GRIDCRAFT_*` become `FACTHORY_GRID_*`; Windows ProgIDs `FacthoryGrid.*`.
- **Publisher**: Bandpey GmbH in the Windows file properties, the MSI and the Linux packages.
- **Windows Installer**: the UpgradeCode and every component GUID derive from our namespace, so
  Facthory Grid never upgrades, replaces or shares components with an installed GridCraft.
- **Icons**: our own set (`facthory/icons/app-icon/`) replaces upstream's whole
  `assets/app-icon/` folder, its icon README and icon licence included; their `ATTRIBUTION.md`
  rows go with them.
- **Links**: website `facthory.com/grid`, source `github.com/FACTHORYAI/grid`; the Discord links
  in About and the macOS Help menu become "Report a problem on GitHub" and open our issue
  tracker.
- **Marks removed**: `docs/brand/` (the ArtCraft name, wordmark and logos) is deleted.
- **Credits kept**: the About box says "Based on GridCraft by the ArtCraft team" and shows
  upstream's copyright next to ours; `LICENSE-*` and `NOTICE` are never touched; `ATTRIBUTION.md`
  keeps every upstream credit and lists our icon as ours.

Telemetry and crash reporting: GridCraft has none, so there is nothing to turn off. Updates:
GridCraft has no built-in updater; ours reads the update feed of our releases (see Updates).

## Releases

A tag `v<version>` (the version in `Cargo.toml`, normally upstream's release it merges) runs
`.github/workflows/facthory-release.yml`: each platform brands a fresh checkout and runs
upstream's packaging scripts, which sign with the secrets of the environment `release`
(`bandpey-hq/github-infra`):

| Platform | Files | Signing |
| -------- | ----- | ------- |
| macOS | `facthorygrid-<v>-macos-universal.dmg`, CLI zip | Developer ID, notarized and stapled |
| Windows | `facthorygrid-<v>-windows-x64.msi` and `-arm64.msi`, portable zips | Authenticode |
| Linux | AppImage (with `.zsync`), `.deb`, `.rpm`, `.tar.gz`; x86_64 and aarch64 | SHA-256 sums |

The result is a draft GitHub release with `SHA256SUMS` and `latest.json`; a person checks it and
publishes it. A manual run of the workflow builds the same files, unsigned when the secrets are
missing, as workflow artifacts.

`latest.json`, at `releases/latest/download/latest.json`, is the update feed: the version and,
per platform, the file the app updates itself from with its size and SHA-256.

## Updates

`facthory/update/facthory_update.rs` is copied into the app when the brand is applied, and
`main.rs` gets four calls to it (`brand.toml`): start, the notice, and the install as the app
quits. Once a day it reads `latest.json`. When that names a newer version, it downloads this
platform's file in the background and checks its size and SHA-256 against the feed. On macOS
and Windows it also checks that the system accepts the file's signature and that the signer is
the one who signed the running app. A notice then says the update installs when the app quits,
with "Restart now":

| Copy | How it updates |
| ---- | -------------- |
| macOS app in a writable folder | The new bundle takes the old one's place after the app quits |
| Windows, installed with the MSI | The MSI upgrades it after the app quits (with the administrator prompt) |
| Linux AppImage in a writable folder | The new AppImage takes the old one's name |
| `.deb`, `.rpm`, portable zips, tarballs, unsigned builds | A notice with a link to the release |

Downloads use the system's `curl`, so the app carries no TLS stack. Only builds made by the
release workflow (`FACTHORY_UPDATE_FEED`) check. Updates are off in runs without preferences,
with `FACTHORY_UPDATES=off` in the environment, or with `{"enabled": false}` in `update.json` in
the settings folder; "Skip this version" is kept there too.

## The check

`facthory/rebrand.py check [built files]` fails when an upstream mark (ArtCraft, GridCraft, the
sibling apps, upstream's domains and publisher) is left in the shipped text (`packaging/`,
`assets/`, build scripts) or in the built binaries, outside the credits `brand.toml` allows.
The branded build runs it on the release binaries.

## When upstream changes

Every rule in `brand.toml` states how many matches it expects. When upstream moves or rewords a
string the brand edits, `apply` fails and names the rule; adjust the rule, not upstream's file.
New upstream text that names GridCraft is rebranded by the tokens without a change here; new
marks the tokens miss fail the check.

## Icons

```sh
cargo install resvg
python3 facthory/icons/render.py
```
