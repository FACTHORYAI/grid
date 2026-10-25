# The fidelity corpus (W6)

How faithfully Facthory Grid opens, saves and draws real `.xlsx` files that Excel wrote, as a
pass rate per step. Part of the Facthory patch set (`facthory/README.md`).

## The files

`corpus.toml` lists 97 files (36.9 MB), each one pinned by URL (a commit or a fixed
public-sector address) and SHA-256. **None is committed**: upstream's rule ("never commit files
produced by Excel") holds, and the runner fetches them into a cache and checks them against
their pin.

- **Microsoft-made:** each file was written by Excel, checked by `docProps/app.xml` and by
  traces only Office writes (`scan.py`).
- **Licences:** MIT 65, Apache-2.0 28, US federal government work, not subject to copyright in the US (17 U.S.C. 105) 3, US federal government work, not subject to copyright in the US (17 U.S.C. 105); EIA: 'U.S. government publications are in the public domain' 1. Each entry records its licence and where it was read.
- **Tiers:** `smoke` (20 small, feature-dense files whose renders may be published) and
  `full` (all).
- **Review:** `publish_renders = "review"` (22 files: user attachments, logos, names) need a
  content check before even our renders of them are shown publicly.
- **Mirrors:** public-sector entries marked `mirror = "required"` change at their origin; a copy
  belongs in our own bucket once it exists.

## Running it

```sh
python3 facthory/rebrand.py apply      # on a fresh checkout
cargo build --release -p facthorygrid-cli
python3 facthory/corpus/fidelity.py --cli target/release/facthorygrid-cli --tier smoke
```

`.github/workflows/facthory-fidelity.yml` runs it weekly over every file, by hand over a tier,
and on pull requests that change the corpus over the smoke tier. The pass rates are the job's
summary; `report.json` and `report.md` are its artifact.

| Step | Passes when |
| ---- | ----------- |
| open | `check`: the workbook opens |
| calc | our recalculation equals the values Excel cached in the file |
| roundtrip | `check`'s round trip: our save needs no repair and keeps every category it compares (values, formulas, number formats, merges, names, tables, conditional formats, validations, charts, comments, hyperlinks, pivots…) |
| render | `convert` to PDF |
| pages | with `--reference`: our PDF has as many pages as Excel's |

A crash (a panic or a signal) or a step over the time limit fails the file. A file passes when
every step it ran passed.

## Microsoft's renders

Comparing with Excel's own output needs Excel. A person with a Microsoft 365 licence
exports each file on one fixed Windows machine: black-box, open, export, close, never looking
inside Office. The environment is held constant and recorded per run:
- the default printer (Microsoft Print to PDF) and its resolution;
- the Office build, with updates paused;
- the fonts, by hash;
- the proofing languages and regional format.

The exports go to a private bucket, never into git. `fidelity.py --reference DIR`, with
`DIR/<id>.pdf`, then compares page counts. `facthorygrid-cli check --json` already compares against Excel's cached values; a reference re-save by Excel after a full recalculation gives it a fresh oracle. PDFs compare by page count, and visually with page's `visual-diff` method. Reports publish our renders and the
scores; Excel's pages and diff overlays stay private.

## The bar for "ready" (proposed; the owner sets it after the first full run)

- **Open and round trip:** at least 98% of files open, none crashes, no `package` difference (nothing Excel would repair).
- **Calc:** no mismatch on non-volatile cells.
- **Render:** print pages match Excel's.

## Adding files

Run `scan.py` (`python3 -I facthory/corpus/scan.py DIR > files.jsonl`) to see each candidate's
producer, Office traces, SHA-256 and features. Add an entry only for a file Excel wrote, under
a licence that allows keeping and showing it. Pin a commit or a stable URL.

Thin spots a commissioned set, made in Microsoft 365 and released by Bandpey under CC0, would
fill: right-to-left and CJK content, Aptos and the 2023 theme, embedded fonts, large documents.
