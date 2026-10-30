//! Updates in Facthory Grid: part of the Facthory patch set (`facthory/update/`), copied over
//! upstream's `updates_ui.rs` when the brand is applied. Upstream's update flow (craft-update)
//! checks and installs the upstream apps' releases, so it is not built in. The app updates itself
//! through `facthory_update` instead, which reads our releases' feed once a day and installs a new
//! version as the app quits. Help ▸ Check for Updates… opens the latest release's page.

use crate::SheetApp;

const RELEASES: &str = "https://github.com/FACTHORYAI/grid/releases/latest";

#[derive(Default)]
pub(crate) struct Runtime {
    /// Help ▸ Check for Updates… was chosen; the next frame opens the releases page.
    open_releases: bool,
}

/// Upstream's check at start (`manual` false) does nothing: `facthory_update` decides when to check.
pub(crate) fn start(app: &mut SheetApp, manual: bool) {
    if manual {
        app.updates_rt.open_releases = true;
    }
}

pub(crate) fn tick(_app: &mut SheetApp, _ctx: &egui::Context) {}

pub(crate) fn show(app: &mut SheetApp, _ctx: &egui::Context) {
    // The native app opens pages through its services: its egui has no browser integration.
    if std::mem::take(&mut app.updates_rt.open_releases)
        && let Some(open) = &app.services.open_url
    {
        open(RELEASES);
    }
}
