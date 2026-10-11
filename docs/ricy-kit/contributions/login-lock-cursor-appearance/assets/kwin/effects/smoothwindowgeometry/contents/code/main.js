"use strict";
function manage(w) {
    w.windowFrameGeometryChanged.connect(function(window, oldGeometry) {
        if (!window.normalWindow || !window.visible || window.deleted || window.minimized || window.fullScreen || window.move || window.resize) return;
        var g = window.geometry;
        if (g.width <= 0 || g.height <= 0 || oldGeometry.width <= 0 || oldGeometry.height <= 0) return;
        if (g.width === oldGeometry.width && g.height === oldGeometry.height && g.x === oldGeometry.x && g.y === oldGeometry.y) return;
        if (window.smoothGeometryAnimation) { cancel(window.smoothGeometryAnimation); delete window.smoothGeometryAnimation; }
        window.setData(Effect.WindowForceBlurRole, true);
        window.smoothGeometryAnimation = animate({
            window: window,
            duration: animationTime(180),
            animations: [
                {type: Effect.Size, from: {value1: oldGeometry.width, value2: oldGeometry.height}, to: {value1: g.width, value2: g.height}, curve: QEasingCurve.OutCubic},
                {type: Effect.Translation, from: {value1: oldGeometry.x - g.x - (g.width - oldGeometry.width)/2, value2: oldGeometry.y - g.y - (g.height - oldGeometry.height)/2}, to: {value1:0,value2:0}, curve: QEasingCurve.OutCubic}
            ]
        });
    });
}
effect.animationEnded.connect(function(w, id) {
    // Each member of a grouped animation emits a completion signal.
    if (w.smoothGeometryAnimation && w.smoothGeometryAnimation.indexOf(id) >= 0) {
        w.setData(Effect.WindowForceBlurRole, null);
    }
});
effects.windowAdded.connect(manage);
for (var i=0; i<effects.stackingOrder.length; i++) manage(effects.stackingOrder[i]);
