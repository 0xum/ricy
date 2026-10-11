/*
    This file is part of the KDE project.
    SPDX-FileCopyrightText: 2018 Vlad Zahorodnii <vlad.zahorodnii@kde.org>
    SPDX-License-Identifier: GPL-2.0-or-later
*/

"use strict";

// Ricy: centered fade + expansion, using KDE's reversible animation API.
// No taskbar icon geometry is required; the actual window geometry stays intact.
var ricyWindowActions = {
    duration: animationTime(320),
    scale: 0.85,
    loadConfig: function () {
        var duration = Number(effect.readConfig("Duration", 320));
        var scale = Number(effect.readConfig("Scale", 0.85));
        this.duration = animationTime(isFinite(duration) && duration > 0 ? duration : 320);
        this.scale = isFinite(scale) ? Math.max(0.5, Math.min(1, scale)) : 0.85;
    },
    eligible: function (window) {
        var rect = window.geometry;
        return !effects.hasActiveFullScreenEffect && window.normalWindow && !window.skipTaskbar
            && rect && rect.width > 0 && rect.height > 0;
    },
    releaseBlur: function (window) {
        // Native Scale may already own the closing transition. Its completion
        // restores blur; do not clear the role underneath that animation.
        if (!window.scaleOutAnimation) {
            window.setData(Effect.WindowForceBlurRole, null);
        }
    },
    abort: function (window) {
        if (window.ricyActionAnimation) {
            var ids = window.ricyActionAnimation;
            delete window.ricyActionAnimation;
            delete window.ricyActionOriginMinimized;
            cancel(ids);
            this.releaseBlur(window);
        }
    },
    animateWindow: function (window, minimized) {
        if (!this.eligible(window)) {
            return;
        }
        if (window.ricyActionAnimation) {
            var direction = window.ricyActionOriginMinimized === minimized ? Effect.Forward : Effect.Backward;
            if (redirect(window.ricyActionAnimation, direction)) {
                return;
            }
            this.abort(window);
        }
        window.setData(Effect.WindowForceBlurRole, true);
        window.ricyActionOriginMinimized = minimized;
        window.ricyActionAnimation = animate({
            window: window,
            curve: minimized ? QEasingCurve.InCubic : QEasingCurve.OutCubic,
            duration: this.duration,
            keepAlive: false,
            animations: [
                { type: Effect.Scale, from: minimized ? 1 : this.scale, to: minimized ? this.scale : 1 },
                { type: Effect.Opacity, from: minimized ? 1 : 0, to: minimized ? 0 : 1 }
            ]
        });
    },
    slotWindowMinimized: function (window) {
        this.animateWindow(window, true);
    },
    slotWindowUnminimized: function (window) {
        this.animateWindow(window, false);
    },
    slotWindowAdded: function (window) {
        window.minimizedChanged.connect(function () {
            ricyWindowActions.animateWindow(window, window.minimized);
        });
    },
    animationEnded: function (window, id) {
        var ids = window.ricyActionAnimation;
        if (!ids || ids.indexOf(id) < 0) {
            return;
        }
        // Grouped animations report one completion per track. Ignore old IDs
        // after a canceled/replaced animation, and release only after both end.
        window.ricyActionAnimation = ids.filter(function (current) { return current !== id; });
        if (window.ricyActionAnimation.length === 0) {
            delete window.ricyActionAnimation;
            delete window.ricyActionOriginMinimized;
            this.releaseBlur(window);
        }
    },
    init: function () {
        effect.configChanged.connect(this.loadConfig.bind(this));
        effect.animationEnded.connect(this.animationEnded.bind(this));
        effects.windowClosed.connect(this.abort.bind(this));
        effects.windowAdded.connect(this.slotWindowAdded.bind(this));
        this.loadConfig();
        for (const window of effects.stackingOrder) {
            this.slotWindowAdded(window);
        }
    }
};

ricyWindowActions.init();
