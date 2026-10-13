// SPDX-License-Identifier: MIT
// Isolated native Konsole part: no user profile or desktop configuration writes.
#include "ui.cpp"
#include <KParts/PartLoader>
#include <KParts/ReadOnlyPart>
#include <KPluginMetaData>
#include <kde_terminal_interface.h>
#include <QVBoxLayout>
#include <QTest>
#include <QAccessible>
#include <QFile>
#include <QScrollBar>

// Reproduce Dolphin's ownership boundary around the actual Konsole part.
class TerminalPanel : public QWidget { Q_OBJECT };
void requireTerminal(bool condition,const char *message) {
    if (!condition) { fprintf(stderr,"FAIL %s\n",message); std::exit(1); }
}
QWidget *displayFor(QWidget *root) {
    for (auto *child : root->findChildren<QWidget *>())
        if (child->inherits("Konsole::TerminalDisplay")) return child;
    return nullptr;
}
int main(int argc,char **argv) {
    QCoreApplication::setApplicationName("dolphin");
    QApplication app(argc,argv);
    app.setStyle(QStyleFactory::create("Fusion"));
    if (argc > 1) {
        QFile stylesheet(QString::fromLocal8Bit(argv[1]));
        requireTerminal(stylesheet.open(QIODevice::ReadOnly),"production stylesheet available");
        app.setStyleSheet(QString::fromUtf8(stylesheet.readAll()));
    }
    TerminalPanel panel;
    auto *layout = new QVBoxLayout(&panel);
    auto part = KParts::PartLoader::instantiatePart<KParts::ReadOnlyPart>(
        KPluginMetaData("/usr/lib/qt6/plugins/kf6/parts/konsolepart.so"),&panel,&panel);
    requireTerminal(bool(part),"native Konsole part available");
    layout->addWidget(part.plugin->widget());
    auto *terminal = qobject_cast<TerminalInterface *>(part.plugin);
    requireTerminal(terminal,"native terminal interface available");
    terminal->startProgram("/bin/sh",{QStringLiteral("sh")});
    panel.resize(720,320); panel.show(); QTest::qWait(180);
    auto *display = displayFor(&panel);
    requireTerminal(display,"native TerminalDisplay found");
    auto *card = display->parentWidget();
    QPalette cardPalette = card->palette();
    const QColor cardColor("#313244");
    cardPalette.setColor(QPalette::Window,cardColor);
    card->setPalette(cardPalette); card->setAutoFillBackground(true);
    const QVariant font = terminal->profileProperty("Font");
    const QVariant colors = terminal->profileProperty("ColorScheme");
    const QPoint corner = display->mapTo(card,QPoint(0,0))*display->devicePixelRatioF();
    const QImage before = display->grab().toImage();
    RicyDolphinUi helper;
    QEvent show(QEvent::Show); QApplication::sendEvent(display,&show); QTest::qWait(80);
    auto *surface = display->findChild<QWidget *>("ricyTerminalInset",Qt::FindDirectChildrenOnly);
    requireTerminal(surface && surface->testAttribute(Qt::WA_TransparentForMouseEvents)
                    && surface->focusPolicy() == Qt::NoFocus,"inset overlay preserves native input/focus");
    requireTerminal(!display->mask().contains(QPoint(0,0)) && display->mask().contains(display->rect().center()),
                    "rounded terminal surface clips corners only");
    const QImage after = display->grab().toImage();
    const int x = after.width()/2, y = after.height()/2;
    requireTerminal(before.pixelColor(x,y) == after.pixelColor(x,y),"terminal center background preserved");
    requireTerminal(after.pixelColor(x,1).lightness() < before.pixelColor(x,1).lightness(),
                    "shadow stays inside the native terminal edge");
    // A widget grab includes its own opaque backing regardless of its mask.
    // Capture its parent to verify that child clipping exposes the card.
    const QImage cardImage = card->grab().toImage();
    display->hide();
    const QColor exposedCard = card->grab().toImage().pixelColor(corner);
    display->show(); QTest::qWait(50);
    requireTerminal(cardImage.pixelColor(corner) == exposedCard,"rounded corner exposes outer card");
    display->setFocus();
    QTest::keyClicks(display,"printf '%s-%s\\n' RICY TERMINAL-CHECK");
    QTest::keyClick(display,Qt::Key_Return); QTest::qWait(100);
    auto *accessible = QAccessible::queryAccessibleInterface(display);
    requireTerminal(accessible && accessible->textInterface(),"native terminal accessible text retained");
    auto *text = accessible->textInterface();
    requireTerminal(text->text(0,text->characterCount()).contains("RICY-TERMINAL-CHECK"),
                    "native terminal keyboard input reaches shell and returns output");
    QTest::keyClicks(display,"seq 1 80");
    QTest::keyClick(display,Qt::Key_Return); QTest::qWait(150);
    requireTerminal(text->text(0,text->characterCount()).contains("80"),"repeated output reaches native screen");
    auto *scroll = display->findChild<QScrollBar *>();
    requireTerminal(scroll && scroll->maximum() > 0,"native output history remains scrollable");
    scroll->setValue(scroll->minimum()); QTest::qWait(50);
    requireTerminal(text->text(0,text->characterCount()).contains("RICY-TERMINAL-CHECK"),
                    "native scrollback retains earlier terminal output");
    scroll->setValue(scroll->maximum()); QTest::qWait(50);
    requireTerminal(surface->geometry() == display->rect(),"native scrolling leaves inset layer stationary");
    panel.resize(640,260); QTest::qWait(80);
    requireTerminal(surface->geometry() == display->rect() && !display->mask().contains(QPoint(0,0)),
                    "terminal clipping and shadow follow resize");
    requireTerminal(font == terminal->profileProperty("Font") && colors == terminal->profileProperty("ColorScheme"),
                    "native terminal font/color profile unchanged");
    requireTerminal(!embeddedTerminal(&panel),"terminal treatment excludes other widgets");
    QWidget standalone;
    auto otherPart = KParts::PartLoader::instantiatePart<KParts::ReadOnlyPart>(
        KPluginMetaData("/usr/lib/qt6/plugins/kf6/parts/konsolepart.so"),&standalone,&standalone);
    requireTerminal(bool(otherPart),"standalone native part available");
    otherPart.plugin->widget()->setParent(&standalone);
    auto *otherDisplay = displayFor(&standalone);
    requireTerminal(otherDisplay,"standalone native TerminalDisplay found");
    QApplication::sendEvent(otherDisplay,&show);
    requireTerminal(!embeddedTerminal(otherDisplay) && otherDisplay->mask().isEmpty()
        && !otherDisplay->findChild<QWidget *>("ricyTerminalInset"),"standalone Konsole display remains untreated");
    QTest::qWait(900); // Let the native transient resize label disappear before capture.
    if (!qEnvironmentVariable("RICY_TERMINAL_CAPTURE").isEmpty())
        panel.grab().save(qEnvironmentVariable("RICY_TERMINAL_CAPTURE"));
    fprintf(stderr,"PASS native Konsole part corners/inset shadow, center/profile preservation, keyboard/shell output, scrollback and resize; scale%g\n",display->devicePixelRatioF());
    return 0;
}
#include "validate-terminal.moc"
