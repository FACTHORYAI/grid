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
| `facthory/sync.py` | Merges the next upstream release (W3), resolving the two known conflicts below |
| `facthory/README.md` | This list |
| `.github/README.md` | The repository's front page |
| `.github/workflows/facthory.yml` | The branded build: apply, upstream's gate on the branded tree, release build, mark check |
| `.github/workflows/upstream-sync.yml` | Every three hours: merge the next upstream release on `sync/<tag>`, open its pull request, merge it when the branded build passes |

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
GridCraft has no built-in updater; ours comes with the signed releases.

## The check

`facthory/rebrand.py check [built files]` fails when an upstream mark (ArtCraft, GridCraft, the
sibling apps, upstream's domains and publisher) is left in the shipped text (`packaging/`,
`assets/`, build scripts) or in the built binaries, outside the credits `brand.toml` allows.
The branded build runs it on the release binaries.

## Upstream sync

`.github/workflows/upstream-sync.yml` runs as the GitHub App **facthory-office-sync**
(bandpey-hq/github-infra, `apps/office-sync.json`), because upstream's releases change its own
workflows and the Actions token may not push those. Its key is a secret of the environment
`upstream-sync`, which only `main` may use; until the App exists, the workflow does nothing.

1. Every three hours, `facthory/sync.py merge` takes the oldest upstream release `main` lacks
   and merges it on `sync/<tag>`. A change upstream made to a file we removed keeps it removed;
   a conflict in `ATTRIBUTION.md` takes upstream's file and writes our block again. Any other
   conflict opens an issue and stops there.
2. The App opens the pull request; the checks run on it as on any other.
3. When the Facthory Grid build passes on exactly that commit, the workflow merges it. When it
   fails, it says so on the pull request: usually a rule in `brand.toml` that upstream's change
   no longer matches. Fix the rule on the branch; the merge follows the green build.

One sync pull request is open at a time, so releases land in order.

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
