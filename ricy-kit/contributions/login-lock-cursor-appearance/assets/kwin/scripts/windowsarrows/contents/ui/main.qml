import QtQml
import org.kde.kwin as KWin
import "../native" as Native
import "../code/main.js" as Arrows
QtObject {
    id: root
    property var sequenceWindow: null
    function endSequence() { sequenceWindow = null; }
    function handle(direction) {
        if (!sequenceWindow) sequenceWindow = KWin.Workspace.activeWindow;
        var w = sequenceWindow;
        if (!w || !w.normalWindow) return;
        if (w.minimized) {
            if (direction === "down") return;
            w.minimized = false;
            KWin.Workspace.activeWindow = w;
            if (direction === "up") return;
        }
        KWin.Workspace.activeWindow = w;
        if (direction === "up") Arrows.upNormal(w);
        else if (direction === "down") Arrows.downNormal(w);
        else if (direction === "left") KWin.Workspace.slotWindowQuickTileLeft();
        else if (direction === "right") KWin.Workspace.slotWindowQuickTileRight();
    }
    property var modifierState: Native.ModifierState {
        onMetaHeldChanged: if (!metaHeld) root.endSequence()
        onPointerInteraction: root.endSequence()
    }
    property var removed: Connections {
        target: KWin.Workspace
        function onWindowRemoved(w) { if (root.sequenceWindow === w) root.endSequence(); }
    }
    property var upKey: KWin.ShortcutHandler {
        name: "WindowsArrowsUp"
        text: "Maximizar ou encaixar acima conforme o estado"
        sequence: "Meta+Up"
        onActivated: root.handle("up")
    }
    property var downKey: KWin.ShortcutHandler {
        name: "WindowsArrowsDown"
        text: "Restaurar, encaixar abaixo ou minimizar conforme o estado"
        sequence: "Meta+Down"
        onActivated: root.handle("down")
    }
    property var leftKey: KWin.ShortcutHandler {
        name: "WindowsArrowsLeft"
        text: "Encaixar à esquerda na mesma sequência de Super"
        sequence: "Meta+Left"
        onActivated: root.handle("left")
    }
    property var rightKey: KWin.ShortcutHandler {
        name: "WindowsArrowsRight"
        text: "Encaixar à direita na mesma sequência de Super"
        sequence: "Meta+Right"
        onActivated: root.handle("right")
    }
    Component.onCompleted: { Arrows.configure(KWin.Workspace); console.warn("PINNED_SEQUENCE_LOADED"); }
}
