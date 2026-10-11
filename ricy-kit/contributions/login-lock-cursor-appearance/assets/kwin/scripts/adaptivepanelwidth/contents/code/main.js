// Keep the bottom panel compact until a visible window reaches its area.
const PANEL_ID = 33;
const OUTPUT_NAME = "HDMI-A-1";
const COMPACT_WIDTH = 1450;
const NEAR_BOTTOM_PX = 120;

const connectedWindows = new Set();
let lastRequestedMode = null;

function panelOutput() {
    for (const output of workspace.screens) {
        if (output.name === OUTPUT_NAME) {
            return output;
        }
    }
    return null;
}

function windowNeedsWidePanel(window, output) {
    if (!window.normalWindow || window.minimized || window.hidden || window.fullScreen) {
        return false;
    }
    if (window.output !== output) {
        return false;
    }

    const desktop = workspace.currentDesktopForScreen(output);
    if (window.desktops.length && !window.desktops.includes(desktop)) {
        return false;
    }
    if (window.activities.length && !window.activities.includes(workspace.currentActivity)) {
        return false;
    }

    const screen = output.geometry;
    const frame = window.frameGeometry;
    const compactLeft = screen.x + (screen.width - COMPACT_WIDTH) / 2;
    const compactRight = compactLeft + COMPACT_WIDTH;
    const overlapsPanel = frame.x < compactRight && frame.x + frame.width > compactLeft;
    const nearBottom = frame.y + frame.height >= screen.y + screen.height - NEAR_BOTTOM_PX;
    return overlapsPanel && nearBottom;
}

function updatePanel() {
    const output = panelOutput();
    if (!output) {
        return;
    }
    const expanded = workspace.windowList().some(window => windowNeedsWidePanel(window, output));
    const mode = expanded ? "fill" : "custom";
    if (mode === lastRequestedMode) {
        return;
    }

    lastRequestedMode = mode;
    const script = `var panel = panelById(${PANEL_ID});
        if (panel) {
            panel.lengthMode = "${mode}";
            if ("${mode}" === "custom") {
                panel.minimumLength = ${COMPACT_WIDTH};
                panel.maximumLength = ${COMPACT_WIDTH};
            }
            print(panel.lengthMode);
        } else {
            print("missing");
        }`;

    callDBus("org.kde.plasmashell", "/PlasmaShell", "org.kde.PlasmaShell",
        "evaluateScript", script, result => {
            if (String(result).trim() !== mode) {
                lastRequestedMode = null;
                console.info("adaptivepanelwidth: panel update failed: " + result);
            } else {
                console.info("adaptivepanelwidth: panel mode " + mode);
            }
        });
}

function watchWindow(window) {
    if (connectedWindows.has(window)) {
        return;
    }
    connectedWindows.add(window);
    window.frameGeometryChanged.connect(updatePanel);
    window.maximizedChanged.connect(updatePanel);
    window.minimizedChanged.connect(updatePanel);
    window.hiddenChanged.connect(updatePanel);
    window.fullScreenChanged.connect(updatePanel);
    window.outputChanged.connect(updatePanel);
    window.desktopsChanged.connect(updatePanel);
    window.activitiesChanged.connect(updatePanel);
    window.closed.connect(() => {
        connectedWindows.delete(window);
        updatePanel();
    });
}

workspace.windowList().forEach(watchWindow);
workspace.windowAdded.connect(window => {
    watchWindow(window);
    updatePanel();
});
workspace.windowRemoved.connect(updatePanel);
workspace.currentDesktopChanged.connect(updatePanel);
workspace.currentActivityChanged.connect(updatePanel);
workspace.screensChanged.connect(updatePanel);
updatePanel();
