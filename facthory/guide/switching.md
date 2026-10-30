# Switching to Facthory Grid

Facthory Grid is a free, open-source spreadsheet app for macOS, Windows and Linux. It opens and
saves `.xlsx` workbooks, has the ribbon, formula bar and shortcuts you already know, and runs
entirely on your computer: no account, no subscription, no telemetry, and it works offline.

This guide is for people moving over from Microsoft Excel. It covers installing, opening your
workbooks, what is the same, what is different or missing today, and where to get help.

> **An early release.** Facthory Grid follows its upstream project closely, and upstream calls the
> app **alpha**: the core workflow (open an `.xlsx`, enter data and formulas, format, sort and
> filter, chart, pivot, print to PDF, save) works end to end, but large workbooks and some
> advanced content are not handled yet. Keep the originals of workbooks that matter until you have
> checked them.

Facthory Grid is based on GridCraft by the ArtCraft team.

> **Draft note (remove before publishing):** add Facthory's own fidelity result here once W6
> reports it: "On Facthory's test set of N real-world workbooks, X% open, recalculate, save and
> reopen without visible change."

## 1. Install

Download from [facthory.com/grid](https://facthory.com/grid) or the
[GitHub releases](https://github.com/FACTHORYAI/grid/releases/latest). Each release lists a
SHA-256 checksum for every file; the downloads page explains how to check one.

| System | File | How |
| ------ | ---- | --- |
| **macOS** 11 or later, Apple silicon or Intel | `facthorygrid-<version>-macos-universal.dmg` | Open the DMG and drag Facthory Grid to Applications. Signed and notarized by Bandpey GmbH; macOS only asks the usual first-launch question for downloaded apps. |
| **Windows** 10 or later (x64), Windows 11 on ARM | `facthorygrid-<version>-windows-x64.msi` or `…-windows-arm64.msi` | Run the installer (it needs administrator rights and installs for all users). It offers an optional desktop shortcut. Signed by Bandpey GmbH. |
| **Linux** x86_64 or ARM64 | `.AppImage`, `.deb`, `.rpm` or `.tar.gz` | See below. |

On Linux:

```sh
# AppImage: runs on most distributions, no install needed
chmod +x facthorygrid-<version>-linux-x86_64.AppImage && ./facthorygrid-<version>-linux-x86_64.AppImage

# Debian, Ubuntu, Mint, Pop!_OS
sudo apt install ./facthorygrid-<version>-linux-x86_64.deb

# Fedora, openSUSE
sudo dnf install ./facthorygrid-<version>-linux-x86_64.rpm
```

Use `aarch64` in place of `x86_64` on ARM64 machines. The Linux builds need glibc 2.35 or newer
(Ubuntu 22.04, Debian 12, Fedora 36 or newer).

The Microsoft Store listing is coming soon.

> **Draft note:** Flatpak comes through Flathub (W10, with the sandboxed builds); add its row then.

**You can keep Microsoft Office installed.** The installers offer Facthory Grid under "Open with"
for spreadsheet files without taking over your defaults, so nothing changes until you choose.

## 2. Open your workbooks

- **File › Open**, drag a file onto the window, or right-click a file and choose **Open With ›
  Facthory Grid**.
- Opens and saves: `.xlsx`, `.xlsm` (macros kept, never run), `.xltx` and `.xltm` templates,
  `.csv` and `.tsv`.
- Imports, then saves as `.xlsx`:
  - legacy 97-2003 `.xls`: values, formulas, number formats, merged cells, column widths, row
    heights and names; not yet fonts, fills, borders, charts, pictures or comments. Open these from
    **File › Open**; they are not registered with your system yet.
  - `.xlsb` and `.ods`: values only (formulas come in as their last saved results, no formatting).
- Exports: PDF, CSV and a web page (HTML).
- Password-protected `.xlsx` workbooks open with their password, but are saved without one for
  now.

### Make Facthory Grid your default

Facthory Grid has no in-app button for this yet; use your system's settings.

- **Windows**: right-click an `.xlsx`, choose **Open with › Choose another app**, select Facthory
  Grid and tick **Always**. Or open **Settings › Apps › Default apps**, find Facthory Grid and
  pick it for `.xlsx`, `.xlsm`, `.csv` and `.tsv`.
- **macOS**: select an `.xlsx` in Finder, choose **File › Get Info**, pick Facthory Grid under
  **Open with**, then click **Change All**.
- **Linux**: in your file manager, **Properties › Open With › Set as default**, or run:

  ```sh
  xdg-mime default com.facthory.grid.desktop \
    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  ```

## 3. What looks and works the same

- **The ribbon.** File, Home, Insert, Draw, Page Layout, Formulas, Data, Review, View and Automate,
  plus Table Design, Chart Design, Format and the two PivotTable tabs. Of the 291 ribbon commands
  in the project's catalogue, **275 (94.5%) are implemented** (measured;
  [docs/parity-checklist.md](https://github.com/FACTHORYAI/grid/blob/main/docs/parity-checklist.md)).
- **The grid as you know it.** Formula bar, Name Box, sheet tabs, the fill handle, pointing at
  cells while typing a formula (with coloured references), Format Cells, Paste Special, frozen
  panes, Page Break Preview and Page Layout view.
- **Formulas.** **513 of Excel's 523 worksheet functions** are present and **504 (96.4%) fully
  work** (measured; [docs/function-parity.md](https://github.com/FACTHORYAI/grid/blob/main/docs/function-parity.md)),
  including XLOOKUP, dynamic arrays and spilling, LET, LAMBDA, MAP, REDUCE, SCAN, BYROW and BYCOL,
  and structured table references. Numbers compare at 15 significant digits, as in Excel.
- **Data tools.** Tables, sort and AutoFilter, conditional formatting with colour scales and data
  bars, data validation, Flash Fill, outlining and subtotals, PivotTables (field list, filters,
  date grouping, show values as), Forecast Sheet, and Solver (linear, nonlinear and evolutionary
  methods).
- **Charts and sparklines.** Seventeen chart types with the Chart Design tab and a Format pane.
- **Keyboard.** The common shortcuts were checked one by one against Microsoft's published list:
  clipboard, undo, formatting (Ctrl+1, Ctrl+B, the Ctrl+Shift number formats), navigation, F2,
  F4, F9, Ctrl+Enter, Ctrl+Shift+Enter, Alt+= AutoSum, Ctrl+T, Ctrl+Shift+L and more. Press **Alt**
  or **F10** for key tips on every ribbon tab. The ones still missing are listed in
  [docs/ui-parity.md](https://github.com/FACTHORYAI/grid/blob/main/docs/ui-parity.md) (Shortcut
  audit). On a Mac, ⌘ takes the place of Ctrl.
- **Comments and notes**, including threaded comments with replies.
- **Printing** to your printer with printer choice, copies, duplex and grayscale, and PDF export.
- **AutoSave** (the title-bar switch, off by default) saves an `.xlsx` workbook that already has a
  file shortly after each change.

## 4. What is different or missing today

These come from the project's own gap list
([docs/gaps.md](https://github.com/FACTHORYAI/grid/blob/main/docs/gaps.md)) and parity documents.

- **Not yet proven on real-world files.** Upstream has not yet confirmed, across a real set of
  workbooks, that Excel opens everything Facthory Grid saves without a repair prompt.
- **Large workbooks.** Files around 100 MB don't open yet, and recalculation uses one processor
  core.
- **Some content is simplified or dropped on save:** slicers, timelines and the data model (Power
  Pivot) are not kept. 2-D charts keep their type and data, but axis scaling, label options, error
  bars and per-point formatting are lost, 3-D charts are not supported, and charts can't be resized
  yet. Custom XML, external links, connections, query tables, form and ActiveX controls and
  embedded objects are carried through unchanged (not yet checked in Excel).
- **No Power Query** (Get & Transform), external data refresh or data model relationships; no
  Stocks or Geography data types, Maps, Analyze Data, SmartArt, WordArt, equations or signature
  lines.
- **Macros are kept but never run.** VBA in `.xlsm` survives a save; there are no Office add-ins or
  Office Scripts.
- **Text in some scripts.** Arabic and Devanagari text is not shaped yet. PDF export uses the
  standard PDF fonts rather than your workbook's fonts, so a PDF looks a little different from the
  screen.
- **Formula language.** Formulas use English function names with commas between arguments in
  every language except Spanish (choose Español under **View › Interface language**). Files are
  unaffected: they always store the standard form.
- **Interface language.** English, with partial translations (the ribbon and some dialogs) in
  several languages.
- **Analysis ToolPak** has 13 of its 19 tools; Solver lacks its Options dialog and some reports.
- **Known stability reports**, among them a startup crash on some Intel UHD graphics on Windows. If
  the app doesn't start on Windows, see the troubleshooting note on the
  [downloads page](https://facthory.com/grid).

Upstream's own estimates, for orientation: about **63%** ready for someone who uses the core
features, about **50%** for a typical analyst or finance user (estimates;
[ROADMAP.md](https://github.com/FACTHORYAI/grid/blob/main/ROADMAP.md)).

## 5. Fonts

Facthory Grid includes no fonts of its own and never Microsoft's. It uses the fonts installed on
your computer and picks the closest match for the workbook's font.

- Windows includes Calibri and Arial, so most workbooks get their own fonts there.
- Where Calibri is missing, Facthory Grid uses **Carlito**, an open font with the same
  measurements, if it is installed, so column widths and wrapping stay the same; otherwise it falls
  back to Arial, Liberation Sans or another system font.
- On Linux, install Carlito and Liberation for the best match (Debian or Ubuntu:
  `sudo apt install fonts-crosextra-carlito fonts-liberation2`).
- Aptos, the newer Microsoft 365 default, has no open font with the same measurements, so text in
  Aptos can be slightly wider or narrower than in Excel.
- Only regular and bold weights are drawn so far; light or semibold faces show as regular.

## 6. Sharing files back and forth

Save as `.xlsx` and send the file as usual: people who use Microsoft Excel open it as any other
Excel workbook. Formulas, formats, styles, tables, conditional formatting, validation, comments,
PivotTables, sparklines and print settings travel both ways.

To keep round trips smooth:

- Keep the original of an important workbook until you have compared it once.
- Avoid editing workbooks that rely on slicers, timelines, Power Pivot or detailed chart
  formatting; open them to read, and make changes in Excel if they must survive.
- Send a PDF when the printed layout must be exact.
- A workbook you received with a password is saved without it; add the password again in Excel
  before you send it on.

## 7. Working together

Facthory Grid is a desktop app for working with Office files on your computer. **It does not do
real-time co-editing**, and it does not join co-authoring sessions in Microsoft 365. Share files
as above, and use comments to discuss changes.

To work together, use [Facthory's workspace](https://facthory.com), where your team's projects
and docs live and are edited together. Opening and saving files directly in Facthory projects is
planned.

## 8. Automation: CLI and MCP

Every ribbon button, menu item and dialog in Facthory Grid is a command that scripts and AI agents
can run.

- **Command line** (`facthorygrid-cli`):

  ```sh
  facthorygrid-cli info book.xlsx                          # sheets, ranges, tables, charts, names
  facthorygrid-cli cat book.xlsx --range A1:F20            # print a range as a table
  facthorygrid-cli eval '=PMT(5%/12,360,-300000)'          # evaluate a formula
  facthorygrid-cli convert book.xlsx data.csv --sheet Sales   # also .tsv, .json, .html
  facthorygrid-cli run --in book.xlsx --cmd 'home.bold={"range":"A1:C1"}' --out book.xlsx
  ```

- **MCP server** for local AI agents, headless or connected to the window you are looking at.
  Tools include `read_range`, `write_range`, `set_cell`, `evaluate_formula`, `format_range`,
  `insert_chart`, `create_table`, `sort_range`, `filter` and `execute_command`:

  ```sh
  claude mcp add facthory-grid -- facthorygrid-cli mcp
  facthorygrid --control 7979 &   # then let the agent drive the open app:
  claude mcp add facthory-grid-app -- facthorygrid-cli mcp --connect 7979
  ```

Where the CLI is: on Linux the `.deb` and `.rpm` install `facthorygrid-cli` on your `PATH` (the
`.tar.gz` has it in `bin/`); on Windows it is in `C:\Program Files\Facthory Grid\` (add that folder
to `PATH` to call it by name); on macOS it is inside the app,
`/Applications/Facthory Grid.app/Contents/MacOS/facthorygrid-cli`, and also a separate download,
`facthorygrid-cli-<version>-macos-universal.zip`. Details:
[docs/cli.md](https://github.com/FACTHORYAI/grid/blob/main/docs/cli.md) and
[docs/mcp.md](https://github.com/FACTHORYAI/grid/blob/main/docs/mcp.md).

## 9. Getting help

- **About › Report a problem on GitHub** in the app (on a Mac also in the Help menu), or [open an
  issue on GitHub](https://github.com/FACTHORYAI/grid/issues). Search first; someone may have hit
  it too.
- Attach the log file: `~/.config/facthorygrid/logs/` on Linux,
  `~/Library/Application Support/Facthory Grid/logs/` on macOS, `%APPDATA%\Facthory Grid\logs\` on
  Windows.
- Never attach a confidential workbook to a public issue; describe it or make a small sample.

## FAQ

**Is it really free?** Yes. Facthory Grid is open source under MIT or Apache-2.0, with no
subscription and no paid tier.

**Do I need an account?** No. Nothing to sign in to.

**Does it send my data anywhere?** No. It works offline and has no telemetry or crash reporting.

**Can I use it next to Microsoft Office?** Yes. Installing it changes none of your defaults.

**Will my formulas give the same results?** They should: the functions follow Excel's documented
behaviour and compare numbers at Excel's precision. Upstream knows of no open calculation bug, but
an independent check against Excel-computed results is still to come, so check critical numbers.

**Can I run my macros?** No. VBA is preserved in `.xlsm` files but not run.

**Can I open a 100 MB workbook?** Not yet (section 4).

**Can several people edit one workbook at the same time?** Not in Facthory Grid. Use Facthory's
workspace for that (section 7).

**How do I update?** Facthory Grid checks for a new version once a day, downloads it in the
background and installs it when you quit (or right away with **Restart now**); your settings are
kept. Linux `.deb` and `.rpm` installs update with your package manager.

---

Microsoft, Microsoft Office, Microsoft 365 and Excel are trademarks of the Microsoft group of
companies. Facthory Grid is not affiliated with, sponsored or endorsed by Microsoft. Facthory Grid
is published by Bandpey GmbH.
