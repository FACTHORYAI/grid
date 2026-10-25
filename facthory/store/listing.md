# Microsoft Store listing: Facthory Grid

Draft for W9, 2026-10-25. Listing language: English (United States). Product type in Partner Center: **EXE or MSI app**. Everything in a `text` block is ready to paste; the counts beside each heading were measured on the block. Field limits are from Partner Center's MSI/EXE submission checklist ([create-app-submission](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/msi/create-app-submission), updated 2026-08-24) and Store Policies 7.20 ([store-policies](https://learn.microsoft.com/en-us/windows/apps/publish/store-policies), effective 2026-10-22).

Facts come from the app's own docs (this repository: README, ROADMAP, docs/file-format-parity.md, docs/function-parity.md, docs/xlsb-import.md, docs/ods-import.md, docs/cell-pictures.md, docs/localization-parity.md) and the brand patch set (`facthory/brand.toml`). The tree still says GridCraft; this listing uses only the Facthory name, except the credit.

## Blockers before this listing can be submitted

| # | Blocker | Owner |
| - | ------- | ----- |
| 1 | Counsel signs off "Facthory Grid" (W0 and the opposition against FACTHORY). Reserve the name only after that | Owner |
| 2 | `https://facthory.com/grid` and the privacy policy page are live (website field, installer "About" link, description) | Owner publishes; Claude can draft the pages |
| 3 | A signed Facthory Grid MSI (x64 and ARM64) on an immutable, versioned GitHub release URL ([the MSI requirements](https://github.com/FACTHORYAI/page/blob/main/facthory/launch/msi-requirements.md)) | Claude (pipeline) and owner (signing identity) |
| 4 | ~~The in-app updater (W4) ships in that MSI~~ Done: FACTHORYAI/grid#5. The Store does not update MSI apps, so the updater must stay on in the Store's copy (it is: the Store installs the same MSI) | Resolved |
| 5 | Screenshots rendered from the branded build | Claude |

## Product name

| Field | Limit | Value |
| ----- | ----- | ----- |
| Product name | Must be a reserved name; up to 256 characters; no marketing or descriptive text (Policy 10.1.1) | `Facthory Grid` |

Never "Grid" alone, never with "Excel" (§14.6).

## Short description (<!--n:short-->210<!--/--> characters; limit 1,000, keep under 270)

<!-- block:short -->
```text
Build, calculate and chart spreadsheets in a familiar ribbon interface. Facthory Grid opens and saves .xlsx workbooks, works fully offline, needs no account and collects no data about you. Free and open source.
```

## Description (<!--n:desc-->3,158<!--/--> characters; limit 10,000; plain text, no URLs or HTML)

<!-- block:desc -->
```text
Facthory Grid is a free, open-source spreadsheet app for Windows. It opens and saves .xlsx workbooks, works fully offline and needs no account. The ribbon, formula bar, sheet tabs, fill handle and keyboard shortcuts work the way spreadsheet users expect.

WHAT YOU CAN DO TODAY
• Calculate: a fast calculation engine with more than 500 worksheet functions, dynamic arrays that spill into neighbouring cells, LET and LAMBDA with MAP, REDUCE, SCAN, BYROW and BYCOL, and structured references to tables.
• Enter and edit: point-and-click formula entry with coloured references, a Name Box, autofill, pattern-based fill, paste special, sort and filter, data validation, grouping and subtotals.
• Format: number formats, cell styles and themes, borders and fills, conditional formatting with colour scales, data bars and icon sets, frozen panes.
• Analyse: tables, pivot tables with a field list, filters, date grouping and "show values as", plus sparklines.
• Chart: seventeen chart types with design and formatting panes; selecting a chart outlines its source data.
• Pictures: floating pictures and shapes, and static pictures placed inside cells that move with the data.
• Print and share: page break preview, print settings, direct printing and PDF export.
• Files: .xlsx is the native format, and styles, formulas, tables, conditional formats, comments, hyperlinks, charts, pictures, pivot tables and print settings are kept when you save. Opens and saves CSV and TSV. Opens legacy .xls workbooks with their values, formulas and number formats, and imports the worksheet data of .xlsb and .ods files.
• Automate: every command can also be run from a command-line tool or a built-in MCP server, so scripts and AI agents that you run on your own computer can read, write and format workbooks. No AI is built into the app.
• Dark mode.

PRIVATE BY DESIGN
Facthory Grid has no telemetry, no crash reporting, no advertising and no account. Your workbooks stay on your computer, and the app does not send them anywhere. The only connection it makes on its own is a daily check with its release page on GitHub for a newer version.

GOOD TO KNOW
Facthory Grid is an early release and still maturing. Very large workbooks (around 100 MB) do not open yet. Some chart settings and complex workbooks from other spreadsheet apps may not come through a save exactly as they were. Legacy .xls files open without their cell formatting, charts and pictures, and are saved as .xlsx; .xlsb and .ods files are imported as values rather than formulas. Macros are not run, and external data connections and functions that depend on online services are not available. Arabic and Devanagari text is not yet shaped correctly. The interface is in English, with translations into other languages in progress. Keep a copy of important workbooks while you try it, and tell us what does not work: every report helps.

OPEN SOURCE
Facthory Grid is open source under the MIT License or the Apache License 2.0, at your option. It is published by Bandpey GmbH (Facthory), Munich, and is based on GridCraft by the ArtCraft team. Source code, release notes and the issue tracker are on GitHub.
```

Notes on the text:
- No Microsoft product name appears; formats are named by extension. LET, LAMBDA, MAP, REDUCE, SCAN, BYROW and BYCOL are worksheet function names shared by several spreadsheet apps. "Flash Fill" and "PivotTable" (Microsoft's names) are written as "pattern-based fill" and "pivot tables".
- The limitations come from `ROADMAP.md` ("Why alpha": 100 MB workbooks, chart round trip, Arabic and Devanagari shaping, no corpus verification), `docs/file-format-parity.md` (`.xls` reads no formatting, charts or pictures; XLSB and ODS values only) and `docs/function-parity.md` (WEBSERVICE and FILTERXML are stubs; cloud functions absent).
- Interface languages: 18 catalogs exist in `crates/ui-egui/src/i18n`, but `ROADMAP.md` rates localization at about 10 %, so the listing promises English only. Revisit when a language is complete.
- "Early release": upstream calls it alpha, about 50 % ready for real work (`ROADMAP.md`).

## Product features (<!--lines:features-->10<!--/--> features, longest <!--max:features-->88<!--/--> characters; limit 20 features of 200 characters, no bullets)

<!-- block:features -->
```text
Opens and saves .xlsx workbooks; also CSV and TSV
Opens legacy .xls workbooks and imports worksheet data from .xlsb and .ods files
More than 500 worksheet functions, dynamic arrays, LET and LAMBDA
Tables, pivot tables, sparklines and seventeen chart types
Conditional formatting, data validation, sort, filter, grouping and subtotals
Familiar ribbon, formula bar, sheet tabs and keyboard shortcuts
Page break preview, direct printing and PDF export
Works fully offline: no account, no telemetry, no crash reporting
Scripts and local AI agents can read and write workbooks through a CLI and an MCP server
Free and open source under MIT or Apache-2.0
```

## Search terms (<!--lines:keywords-->7<!--/--> terms, <!--words:keywords-->10<!--/--> unique words, longest <!--max:keywords-->12<!--/--> characters; limit 7 terms, 40 characters each, 21 unique words; Policy 10.1.3: no pricing terms, no other products' titles)

<!-- block:keywords -->
```text
spreadsheet
xlsx editor
csv editor
formulas
pivot tables
charts
open source
```

Left out on purpose: "free" (pricing term), every Microsoft, Google, Apple or LibreOffice product name, and "office".

## Category (Properties page)

| Field | Value | Why |
| ----- | ----- | --- |
| Category | **Productivity** | Microsoft's description lists "data viewing and sorting" ([categories](https://learn.microsoft.com/en-us/windows/apps/publish/publish-your-app/msi/categories-and-subcategories)) |
| Secondary category | **Business**, subcategory **Data + analytics** | The closest subcategory for a spreadsheet |

## System requirements

Properties page checkboxes:

| Item | Minimum | Recommended |
| ---- | ------- | ----------- |
| Keyboard | ✓ | ✓ |
| Mouse | ✓ | ✓ |
| Touch screen, camera, NFC, Bluetooth LE, telephony, microphone | — | — |
| Memory | leave blank until measured | leave blank until measured |
| DirectX | leave blank (falls back to OpenGL or software) | DirectX 12 |
| Dedicated GPU memory, processor, graphics | leave blank | leave blank |

Do not tick "pen and ink" or "tested to meet accessibility guidelines" (not tested on Windows with Narrator and high contrast).

Additional system requirements, minimum (<!--lines:addmin-->2<!--/--> items, longest <!--max:addmin-->95<!--/--> characters; limit 11 of 200 characters):

<!-- block:addmin -->
```text
Windows 10 or Windows 11, 64-bit (x64 or ARM64)
A graphics adapter with DirectX 12 or OpenGL; older PCs fall back to a slower software renderer
```

Recommended (<!--lines:addrec-->1<!--/--> item):

<!-- block:addrec -->
```text
A multi-core processor and a current DirectX 12 driver for large workbooks
```

Memory and disk space: measure on the release build (installed size; working set with the sales sample and with a 50 MB workbook) before filling these in.

## What's new in this version (limit 1,500 characters)

Leave blank on the first submission. Template for updates:

```text
Facthory Grid <version>

New
• <one line per user-visible addition>

Fixed
• <one line per user-visible fix>

Known issues
• <only if something new is known to be broken>

Full release notes are on GitHub under release v<version>.
```

## Copyright, licence terms, developer

| Field | Limit | Value |
| ----- | ----- | ----- |
| Copyright and trademark info (<!--n:copyright-->127<!--/--> chars) | 200 | see block |
| Applicable license terms (<!--n:license-->763<!--/--> chars) | 10,000, **required** | see block |
| Developed by (<!--n:devby-->64<!--/--> chars) | 255 | see block |

<!-- block:copyright -->
```text
© 2026 Bandpey GmbH. Based on GridCraft, © 2026 ArtCraft Team and the GridCraft contributors. Licensed under MIT OR Apache-2.0.
```

<!-- block:license -->
```text
Facthory Grid is free and open-source software. You may use, copy, modify and distribute it under the terms of either the MIT License or the Apache License, Version 2.0, at your option.

MIT License: https://github.com/FACTHORYAI/grid/blob/main/LICENSE-MIT
Apache License 2.0: https://github.com/FACTHORYAI/grid/blob/main/LICENSE-APACHE
Notices: https://github.com/FACTHORYAI/grid/blob/main/NOTICE
Third-party fonts and assets and their licences: https://github.com/FACTHORYAI/grid/blob/main/ATTRIBUTION.md

The software is provided "as is", without warranty of any kind, as both licences state. Facthory Grid is based on GridCraft by the ArtCraft team; their copyright and licence notices are kept. The Facthory name and logos are not licensed under these terms.
```

<!-- block:devby -->
```text
Bandpey GmbH (Facthory), based on GridCraft by the ArtCraft team
```

## Support info (Properties page)

| Field | Value |
| ----- | ----- |
| Does this product access, collect or transmit personal information? | **Yes** (Policy 10.5.1: Win32 products always need a privacy policy) |
| Privacy policy URL | `https://facthory.com/privacy/apps` (**to publish**; or paste the text from [the privacy policy draft](https://github.com/FACTHORYAI/page/blob/main/facthory/launch/privacy-policy.md) into Partner Center) |
| Website | `https://facthory.com/grid` (**to publish**) |
| Support contact info | `https://github.com/FACTHORYAI/grid/issues` |
| Contact details (phone, address) | from [the owner checklist](https://github.com/FACTHORYAI/page/blob/main/facthory/launch/owner-checklist.md), step 3 |

## Screenshots

PNG, landscape, at least 1366 × 768 (render at 1920 × 1080 or 2560 × 1440), at most 50 MB, 1 required, up to 10, captions up to 200 characters, key content in the top two-thirds, no added logos or marketing text. Render from the **branded** build with the headless snapshot example (`cargo run --release -p facthorygrid-ui-egui --example snapshot -- --sample sales`, after `facthory/rebrand.py apply`), English interface, built-in samples only (sales, budget, grades).

| # | Shows | Caption (longest <!--max:captions-->81<!--/--> chars) |
| - | ----- | ------- |
| 1 | The sales sample: accounting formats, cell styles, a colour scale, frozen header row and a bar chart | `Format numbers, highlight trends with conditional formatting and chart your data.` |
| 2 | A formula using LET or a dynamic array that spills, with coloured reference highlighting in the grid and the formula bar | `More than 500 functions, dynamic arrays, LET and LAMBDA.` |
| 3 | A pivot table with the field list open | `Summarise data with pivot tables, filters and date grouping.` |
| 4 | Chart selected, chart design tab and format pane open, source range outlined | `Seventeen chart types with design and formatting panes.` |
| 5 | Page Break Preview of the budget sample with the print area outlined | `Preview page breaks, then print or export to PDF.` |
| 6 | Dark mode with the Insert tab | `Dark mode, with tables, charts, sparklines and pictures on the Insert tab.` |

<!-- block:captions -->
```text
Format numbers, highlight trends with conditional formatting and chart your data.
More than 500 functions, dynamic arrays, LET and LAMBDA.
Summarise data with pivot tables, filters and date grouping.
Seventeen chart types with design and formatting panes.
Preview page breaks, then print or export to PDF.
Dark mode, with tables, charts, sparklines and pictures on the Insert tab.
```

## Store logos

| Asset | Size (PNG, ≤ 50 MB) | Status for MSI apps | Source |
| ----- | ------------------- | ------------------- | ------ |
| 1:1 box art | 2160 × 2160 (or 1080 × 1080) | **Required** | Render the Facthory Grid icon SVG from `facthory/icons/` with resvg; no text in the bottom third |
| 2:3 poster art | 1440 × 2160 (or 720 × 1080) | Recommended | Same icon; "Facthory Grid" in the top two-thirds if text is used (contrast at least 4.5:1) |
| 1:1 app tile icon | 300 × 300 | Only if the MSI listing page offers the slot (the MSI listing CSV has no column for it) | `facthory/icons/app-icon/` render |

The icon must not resemble Microsoft's green "X" (§14.5). Sources as in [Facthory Page's listing](https://github.com/FACTHORYAI/page/blob/main/facthory/store/listing.md).

## Packages page

| Field | x64 package | ARM64 package |
| ----- | ----------- | ------------- |
| Package URL | `https://github.com/FACTHORYAI/grid/releases/download/v<version>/facthorygrid-<version>-windows-x64.msi` | `…/facthorygrid-<version>-windows-arm64.msi` |
| Architecture | x64 | arm64 |
| App type | MSI (`/qn`) | MSI |
| Languages | English (en-us) | English (en-us) |

The local Grid checkout has no `facthory-release.yml` yet (Page's builds signed x64 and ARM64 MSIs and drafts the GitHub release); W4 adds the same workflow to Grid before the first submission.

## Notes for certification (<!--n:notes-->1,374<!--/--> characters; limit 2,000)

<!-- block:notes -->
```text
Facthory Grid is a desktop spreadsheet app delivered as a per-machine MSI; a UAC prompt during install is expected. A silent install creates no desktop shortcut (only the Start menu entry). No account, sign-in or server is needed and the app works fully offline.

How to test: start Facthory Grid from the Start menu and open a new workbook. Enter numbers and a formula such as =SUM(A1:A5), format the cells, insert a chart from the Insert tab, then use File > Save As to save an .xlsx file and File > Export to create a PDF.

Network: the app does not connect to any server of ours. If update checks are on, it asks GitHub's release feed for this app whether a newer version exists. Hyperlinks in cells open in the default browser after the user clicks them.

No generative AI is built in. The command-line tool facthorygrid-cli.exe, installed next to the app, includes an MCP server: a local automation interface that scripts or AI agents the user runs can use. It talks over standard input and output, and the app's optional control channel listens only on 127.0.0.1, only when started with --control, and requires a key.

Uninstall through Settings > Apps removes all installed files and registry entries. Per-user settings and logs the app created in %APPDATA%\Facthory Grid are left in place, as is usual for user data.

Contact: <support email>. Notes written <date>.
```
