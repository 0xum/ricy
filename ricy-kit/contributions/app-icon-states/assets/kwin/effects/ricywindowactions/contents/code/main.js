/*
    This file is part of the KDE project.

    SPDX-FileCopyrightText: 2018 Vlad Zahorodnii <vlad.zahorodnii@kde.org>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

"use strict";

// Ricy: preserve the KDE reversible animation; provide a monitor-local target
// when Noctalia has not published a Plasma task manager icon geometry.
function ricyIconRect(window) {
    const icon = window.iconGeometry;
    if (icon && icon.width > 0 && icon.height > 0) {
        return icon;
    }
    const screen = window.screen;
    const rect = screen ? screen.geometry : null;
    if (!rect || rect.width <= 0 || rect.height <= 0) {
        return null;
    }
    const size = 18;
    const frame = window.geometry;
    return {
        x: Math.max(rect.x, Math.min(rect.x + rect.width - size, frame.x + frame.width / 2 - size / 2)),
        y: rect.y + rect.height - 22 - size / 2,
        width: size,
        height: size
    };
}

var ricyWindowActions = {
    duration: animationTime(240),
    loadConfig: function () {
        ricyWindowActions.duration = animationTime(240);
    },
    slotWindowMinimized: function (window) {
        if (effects.hasActiveFullScreenEffect || !window.normalWindow || window.skipTaskbar) {
            return;
        }

        var iconRect = ricyIconRect(window);
        if (!iconRect) {
            return;
        }

        if (window.unminimizeAnimation) {
            if (redirect(window.unminimizeAnimation, Effect.Backward)) {
                return;
            }
            cancel(window.unminimizeAnimation);
            delete window.unminimizeAnimation;
        }

        if (window.minimizeAnimation) {
            if (redirect(window.minimizeAnimation, Effect.Forward)) {
                return;
            }
            cancel(window.minimizeAnimation);
        }

        var windowRect = window.geometry;

        window.setData(Effect.WindowForceBlurRole, true);

        window.minimizeAnimation = animate({
            window: window,
            curve: QEasingCurve.InCubic,
            duration: ricyWindowActions.duration,
            keepAlive: false,
            animations: [
                {
                    type: Effect.Size,
                    from: {
                        value1: windowRect.width,
                        value2: windowRect.height
                    },
                    to: {
                        value1: iconRect.width,
                        value2: iconRect.height
                    }
                },
                {
                    type: Effect.Translation,
                    from: {
                        value1: 0.0,
                        value2: 0.0
                    },
                    to: {
                        value1: iconRect.x - windowRect.x -
                            (windowRect.width - iconRect.width) / 2,
                        value2: iconRect.y - windowRect.y -
                            (windowRect.height - iconRect.height) / 2,
                    }
                },
                {
                    type: Effect.Opacity,
                    from: 1.0,
                    to: 0.0
                }
            ]
        });
    },
    slotWindowUnminimized: function (window) {
        if (effects.hasActiveFullScreenEffect || !window.normalWindow || window.skipTaskbar) {
            return;
        }

        var iconRect = ricyIconRect(window);
        if (!iconRect) {
            return;
        }

        if (window.minimizeAnimation) {
            if (redirect(window.minimizeAnimation, Effect.Backward)) {
                return;
            }
            cancel(window.minimizeAnimation);
            delete window.minimizeAnimation;
        }

        if (window.unminimizeAnimation) {
            if (redirect(window.unminimizeAnimation, Effect.Forward)) {
                return;
            }
            cancel(window.unminimizeAnimation);
        }

        var windowRect = window.geometry;

        window.setData(Effect.WindowForceBlurRole, true);

        window.unminimizeAnimation = animate({
            window: window,
            curve: QEasingCurve.OutCubic,
            duration: ricyWindowActions.duration,
            keepAlive: false,
            animations: [
                {
                    type: Effect.Size,
                    from: {
                        value1: iconRect.width,
                        value2: iconRect.height
                    },
                    to: {
                        value1: windowRect.width,
                        value2: windowRect.height
                    }
                },
                {
                    type: Effect.Translation,
                    from: {
                        value1: iconRect.x - windowRect.x -
                            (windowRect.width - iconRect.width) / 2,
                        value2: iconRect.y - windowRect.y -
                            (windowRect.height - iconRect.height) / 2,
                    },
                    to: {
                        value1: 0.0,
                        value2: 0.0
                    }
                },
                {
                    type: Effect.Opacity,
                    from: 0.0,
                    to: 1.0
                }
            ]
        });
    },
    slotWindowAdded: function (window) {
        window.minimizedChanged.connect(() => {
            if (window.minimized) {
                ricyWindowActions.slotWindowMinimized(window);
            } else {
                ricyWindowActions.slotWindowUnminimized(window);
            }
        });
    },
    restoreForceBlurState: function(window) {
        window.setData(Effect.WindowForceBlurRole, null);
    },
    init: function () {
        effect.configChanged.connect(ricyWindowActions.loadConfig);
        effect.animationEnded.connect(this.restoreForceBlurState.bind(this));

        effects.windowAdded.connect(ricyWindowActions.slotWindowAdded);
        for (const window of effects.stackingOrder) {
            ricyWindowActions.slotWindowAdded(window);
        }
    }
};

ricyWindowActions.init();
