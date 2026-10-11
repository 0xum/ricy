#include <QQmlExtensionPlugin>
#include <qqml.h>
#include <input.h>
class ModifierState : public QObject {
    Q_OBJECT
    Q_PROPERTY(bool metaHeld READ metaHeld NOTIFY metaHeldChanged)
public:
    explicit ModifierState(QObject *parent=nullptr): QObject(parent) {
        auto *input=KWin::input();
        held=input->keyboardModifiers().testFlag(Qt::MetaModifier);
        connect(input, &KWin::InputRedirection::keyboardModifiersChanged, this,
            [this](Qt::KeyboardModifiers current, Qt::KeyboardModifiers) {
                bool next=current.testFlag(Qt::MetaModifier);
                if (held != next) { held=next; emit metaHeldChanged(); }
            });
        connect(input, &KWin::InputRedirection::pointerButtonStateChanged, this, [this,input]() {
            if (input->qtButtonStates() != Qt::NoButton) emit pointerInteraction();
        });
    }
    bool metaHeld() const { return held; }
signals:
    void metaHeldChanged();
    void pointerInteraction();
private:
    bool held=false;
};
class WindowSequencePlugin : public QQmlExtensionPlugin {
    Q_OBJECT
    Q_PLUGIN_METADATA(IID QQmlExtensionInterface_iid)
public:
    void registerTypes(const char *uri) override { qmlRegisterType<ModifierState>(uri, 1, 0, "ModifierState"); }
};
#include "windowsequence.moc"
