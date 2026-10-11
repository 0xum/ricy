var workspace = null;
function configure(value) { workspace = value; }
function tileState(w) {
    if (!w.tile) return null;
    var r = w.tile.relativeGeometry;
    if (!r) return null;
    var side = r.width < 0.75 ? (r.x < 0.25 ? "Left" : "Right") : "";
    var vertical = r.height < 0.75 ? (r.y < 0.25 ? "Top" : "Bottom") : "";
    return {side: side, vertical: vertical};
}
function applyTile(w, target) {
    // Unmanage the previous tile so KWin does not combine opposing edges.
    if (w.tile) w.tile.unmanage(w);
    workspace["slotWindowQuickTile" + target]();
}
function upNormal(w) {
    if (!w || !w.normalWindow || !w.maximizable) return;
    if (w.maximizeMode === 3) return;
    var t = tileState(w);
    if (t && t.side) {
        if (t.vertical === "Bottom") applyTile(w, t.side);
        else if (t.vertical !== "Top") applyTile(w, "Top" + t.side);
        else w.setMaximize(true, true);
    } else if (t && t.vertical === "Bottom") applyTile(w, "Top");
    else w.setMaximize(true, true);
}
function downNormal(w) {
    if (!w || !w.normalWindow) return;
    if (w.maximizeMode !== 0) { w.setMaximize(false, false); return; }
    var t = tileState(w);
    if (t && t.side && t.vertical === "Top") applyTile(w, t.side);
    else if (t && t.side && !t.vertical) applyTile(w, "Bottom" + t.side);
    else if (t && !t.side && t.vertical === "Top") applyTile(w, "Bottom");
    else if (w.tile) w.tile.unmanage(w);
    else if (w.minimizable) w.minimized = true;
}
