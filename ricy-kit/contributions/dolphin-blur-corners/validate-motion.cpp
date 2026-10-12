// SPDX-License-Identifier: MIT
// Isolated Qt/KIO paint and lifetime fixture; never changes desktop settings.
#include "motion.h"
#include <QMainWindow>
#include <QToolButton>
#include <QTabWidget>
#include <QTest>
#include <QStyleFactory>
#include <QProxyStyle>
#include <KFilePlacesView>
#include <KFilePlacesModel>

class NoMotionStyle : public QProxyStyle {
public:
    NoMotionStyle() : QProxyStyle(QStyleFactory::create("Fusion")) {}
    int styleHint(StyleHint hint, const QStyleOption *option = nullptr,
                  const QWidget *widget = nullptr, QStyleHintReturn *result = nullptr) const override {
        if (hint == SH_Widget_Animate || hint == SH_Widget_Animation_Duration) return 0;
        return QProxyStyle::styleHint(hint, option, widget, result);
    }
};
class PaintCounter : public QObject {
public:
    int count = 0;
    bool eventFilter(QObject *, QEvent *event) override {
        if (event->type() == QEvent::Paint) ++count;
        return false;
    }
};
void require(bool condition, const char *message) {
    if (!condition) { fprintf(stderr, "FAIL %s\n", message); std::exit(1); }
}
QColor pixel(QWidget *widget) {
    const QImage image = widget->grab().toImage();
    return image.pixelColor(qRound(8 * image.devicePixelRatio()),
                            qRound(widget->height()/2.0 * image.devicePixelRatio()));
}
void enter(QWidget *widget) {
    const QPointF point(widget->rect().center());
    widget->setAttribute(Qt::WA_UnderMouse, true);
    QEnterEvent event(point, point, widget->mapToGlobal(point.toPoint()));
    QApplication::sendEvent(widget, &event);
    widget->update();
}
void leave(QWidget *widget) {
    widget->setAttribute(Qt::WA_UnderMouse, false);
    QEvent event(QEvent::Leave);
    QApplication::sendEvent(widget, &event);
    widget->update();
}
int main(int argc, char **argv) {
    QApplication app(argc, argv);
    app.setStyle(QStyleFactory::create("Fusion"));
    app.setStyleSheet("QToolButton {background:#313244;border:1px solid transparent;border-radius:6px;padding:8px;}"
                     "QToolButton:hover {background:#977dba;} QToolButton:checked {background:#cba6f7;}"
                     "QToolButton:focus {border-color:#cba6f7;}");
    QMainWindow window;
    auto *toolbar = new QToolBar(&window);
    window.addToolBar(toolbar);
    auto *button = new QToolButton;
    button->setText("Split"); button->setCheckable(true);
    toolbar->addWidget(button);
    auto *editor = new QLineEdit;
    editor->setText("Native path"); editor->setClearButtonEnabled(true);
    toolbar->addWidget(editor);
    // Exercise the opposite polish order too: clear-button before editor.
    for (auto *child : editor->findChildren<QAbstractButton *>()) installChromeMotion(child);
    installChromeMotion(editor);
    for (auto *child : editor->findChildren<QAbstractButton *>())
        require(!child->graphicsEffect(), "path editor has no nested effects");
    installChromeMotion(button);
    auto *effect = dynamic_cast<ChromeMotion *>(button->graphicsEffect());
    require(effect, "toolbar motion installed");
    auto *tabs = new QTabWidget;
    tabs->addTab(new QWidget, "Documents"); tabs->addTab(new QWidget, "Images");
    window.setCentralWidget(tabs);
    installChromeMotion(tabs->tabBar());
    auto *tabEffect = dynamic_cast<ChromeMotion *>(tabs->tabBar()->graphicsEffect());
    require(tabEffect, "tab motion installed");
    window.resize(600, 220); window.show(); QTest::qWait(60);
    leave(button); QTest::qWait(200);
    const QRect geometry = button->geometry();
    const QColor normal = pixel(button);
    enter(button); QTest::qWait(45);
    require(effect->running(), "hover is interpolating");
    const QColor mid = pixel(button);
    require(mid != normal, "mid-frame differs from initial paint");
    const qreal interrupted = effect->progress();
    leave(button);
    require(effect->running() && effect->progress() == 0, "interruption starts from presented frame");
    const QColor resumed = pixel(button);
    require(qAbs(resumed.red()-mid.red()) <= 2, "interruption has no visual snap");
    require(interrupted > 0 && interrupted < 1, "interruption occurred during transition");
    for (int i=0;i<30;++i) { enter(button); QTest::qWait(4); leave(button); QTest::qWait(4); }
    QTest::qWait(220);
    require(!effect->running() && effect->progress() == 1, "stable hover state is idle");
    require(pixel(button) == normal, "hover exit returns exact QSS final paint");
    PaintCounter idlePaints;
    button->installEventFilter(&idlePaints);
    QTest::qWait(300);
    require(idlePaints.count <= 1, "stable control has no repeating effect repaints");
    button->removeEventFilter(&idlePaints);
    QTest::mousePress(button, Qt::MouseButton::LeftButton);
    QTest::qWait(20);
    require(effect->running() && effect->duration() == MotionFast, "native button press uses fast paint transition");
    QTest::mouseRelease(button, Qt::MouseButton::LeftButton);
    QTest::qWait(220);
    require(button->isChecked() && !effect->running(), "native button release/checked semantics retained");
    button->setChecked(false); QTest::qWait(220);
    button->setChecked(true); QTest::qWait(40);
    require(effect->running(), "checked state is interpolating");
    QTest::qWait(220); require(!effect->running(), "checked state settles");
    tabs->setCurrentIndex(1); QTest::qWait(40);
    require(tabEffect->running(), "active-tab state interpolates");
    tabs->setCurrentIndex(0); QTest::qWait(220);
    require(!tabEffect->running(), "rapid tab changes settle");
    require(button->geometry() == geometry, "motion changes no hit geometry");
    editor->setFocus(); QTest::qWait(40);
    auto *editorEffect = dynamic_cast<ChromeMotion *>(editor->graphicsEffect());
    require(editorEffect && editorEffect->running(), "keyboard path focus interpolates");
    button->setFocus(); QTest::qWait(220);
    require(!editorEffect->running() && editor->text() == "Native path", "focus exit preserves editor text");
    button->setChecked(false);
    app.setStyle(new NoMotionStyle);
    QTest::qWait(30); enter(button); QTest::qWait(10);
    require(!effect->running() && effect->progress() == 1, "native motion disabled is immediate");
    require(pixel(button) == QColor("#977dba"), "disabled motion reaches exact final state");
    app.setStyle(QStyleFactory::create("Fusion"));
    QTest::qWait(30);
    auto *places = new KFilePlacesView;
    auto *model = new KFilePlacesModel(places);
    places->setModel(model);
    installChromeMotion(places);
    places->resize(300, 460); places->show(); QTest::qWait(80);
    auto *placeEffect = dynamic_cast<ChromeMotion *>(places->viewport()->graphicsEffect());
    require(placeEffect && places->itemDelegate(), "native Places delegate preserved");
    auto *delegate = places->itemDelegate();
    if (model->rowCount() > 1) {
        places->selectionModel()->select(model->index(1,0), QItemSelectionModel::ClearAndSelect);
        QTest::qWait(40); require(placeEffect->running(), "native Places selection interpolates");
        places->selectionModel()->select(model->index(0,0), QItemSelectionModel::ClearAndSelect);
        QTest::qWait(40);
        model->dataChanged(model->index(0,0),model->index(0,0));
        require(!placeEffect->running(), "native Places content/state update settles immediately");
        QTest::qWait(220); require(!placeEffect->running(), "Places selection settles");
    }
    require(places->itemDelegate() == delegate, "motion does not replace Places delegate");
    for(int i=0;i<30;++i) {
        auto *temporary = new QToolButton(toolbar);
        installChromeMotion(temporary); temporary->show(); QTest::qWait(1);
        enter(temporary); delete temporary; // A live transition dies with its control.
    }
    delete places;
    fprintf(stderr,"PASS paint interpolation/reversal/exact final states, native tabs/Places, motion disable, stable geometry and transition destruction; scale%g\n",window.devicePixelRatioF());
    window.grab().save(qEnvironmentVariable("RICY_MOTION_FIXTURE"));
    return 0;
}
