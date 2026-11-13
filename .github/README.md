<p align="center">
  <img src="../facthory/icons/app-icon/hicolor/256x256/apps/com.facthory.grid.png" width="128" height="128" alt="Facthory Grid icon: a chrome table in the Grid colour">
</p>

# Facthory Grid

An open-source spreadsheet app for macOS, Windows and Linux that opens and saves `.xlsx`
workbooks, from [Facthory](https://facthory.com). Formulas and functions, tables, conditional
formatting and charts; `.xlsx` and CSV files, and import of `.xls`, `.xlsb` and `.ods`. Every
command is also available to scripts and AI agents through a command-line tool and an MCP server.

Facthory Grid is based on [GridCraft](https://github.com/storytold/gridcraft) by the ArtCraft
team, and follows it closely: this repository carries GridCraft's history, merges every GridCraft
release, and offers fixes back. Facthory's changes are a small set of brand files in
[`facthory/`](../facthory/README.md), applied when the app is built.

Downloads arrive with the first release. Until then, build it from source.

## Build

```sh
python3 facthory/rebrand.py apply   # on a fresh checkout: the Facthory brand
cargo build --release -p facthorygrid -p facthorygrid-cli
```

`facthory/rebrand.py apply` rewrites the checkout in place (names, app ids, icons, links,
installer identities); run it on a clean clone, not on a tree you commit from. Without it you
build GridCraft as upstream ships it. The Linux build needs the packages listed in
[`.github/workflows/facthory.yml`](workflows/facthory.yml).

## Report a problem

[Open an issue](https://github.com/FACTHORYAI/grid/issues). Problems that also occur in
GridCraft are reported there too, so the fix reaches both.

## Licence

MIT OR Apache-2.0, as upstream: [`LICENSE-MIT`](../LICENSE-MIT), [`LICENSE-APACHE`](../LICENSE-APACHE),
[`NOTICE`](../NOTICE) and [`ATTRIBUTION.md`](../ATTRIBUTION.md). Copyright © Bandpey GmbH for the
Facthory changes; GridCraft is copyright © the ArtCraft Team and the GridCraft contributors.
"ArtCraft" and its logos are trademarks of the ArtCraft Team; Facthory Grid is not an ArtCraft
product and is not endorsed by the ArtCraft Team.
