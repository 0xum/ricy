// SPDX-License-Identifier: MIT
// Isolated Qt/KIO paint and lifetime fixture; never changes desktop settings.
#include "ui.cpp"
#include <QMainWindow>
#include <QFile>
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
QColor placeBackground(KFilePlacesView *view, const QModelIndex &index) {
    const QRect rect = view->visualRect(index);
    require(rect.isValid(), "Places row is visible");
    const QImage image = view->viewport()->grab().toImage();
    const qreal scale = image.devicePixelRatio();
    return image.pixelColor(qRound((rect.right()-18)*scale),
                            qRound((rect.bottom()-8)*scale));
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
    QCoreApplication::setApplicationName(QStringLiteral("dolphin"));
    QApplication app(argc, argv);
    app.setStyle(new ChipStyle(QStyleFactory::create("Fusion")));
    app.setStyleSheet("QToolButton {background:#313244;border:1px solid transparent;border-radius:6px;padding:8px;}"
                     "QToolButton:hover {background:#977dba;} QToolButton:checked {background:#cba6f7;}"
                     "QToolButton:focus {border-color:#cba6f7;}");
    QMainWindow window;
    // Native dock separators must dispatch to the same thin line as split
    // panes, rather than falling back to an invisible/native broad separator.
    for (bool vertical : {false,true}) {
        for (int state = 0; state < 3; ++state) {
            QImage image(vertical ? QSize(4,160) : QSize(160,4),QImage::Format_ARGB32_Premultiplied);
            image.fill(Qt::transparent);
            QStyleOption option;
            option.initFrom(&window);
            option.rect = image.rect();
            option.state = QStyle::State_Enabled;
            if (!vertical) option.state |= QStyle::State_Horizontal;
            if (state) option.state |= QStyle::State_MouseOver;
            window.setProperty("ricyDockDragging",state == 2);
            {
                QPainter painter(&image);
                window.style()->drawPrimitive(QStyle::PE_IndicatorDockWidgetResizeHandle,&option,&painter,&window);
            }
            QColor expected(state == 2 ? "#cba6f7" : state == 1 ? "#a6adc8" : "#242435");
            if (state == 1) expected.setAlpha(128);
            const QColor actual = image.pixelColor(vertical ? 1 : 80,vertical ? 80 : 1);
            // Premultiplied half-alpha channels round to adjacent RGB values.
            require(qAbs(actual.red()-expected.red()) <= 1 &&
                    qAbs(actual.green()-expected.green()) <= 1 &&
                    qAbs(actual.blue()-expected.blue()) <= 1 && actual.alpha() == expected.alpha(),
                    "native dock divider normal/hover/drag paint");
            require(image.pixelColor(vertical ? 1 : 4,vertical ? 4 : 1).alpha() == 0,
                    "dock divider retains 12px end inset");
            require(image.pixelColor(vertical ? 0 : 80,vertical ? 80 : 0).alpha() == 0,
                    "dock divider retains thin 2px stroke");
        }
    }
    window.setProperty("ricyDockDragging",false);
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
    app.setStyle(new ChipStyle(QStyleFactory::create("Fusion")));
    QTest::qWait(30);
    auto *places = new KFilePlacesView;
    auto *model = new KFilePlacesModel(places);
    places->setModel(model);
    places->setItemDelegateForColumn(0, new PlacesResultPaint(places->itemDelegate(), places));
    installChromeMotion(places);
    places->resize(300, 460); places->show(); QTest::qWait(80);
    auto *placeEffect = dynamic_cast<ChromeMotion *>(places->viewport()->graphicsEffect());
    require(placeEffect && places->itemDelegate(), "native Places delegate preserved");
    auto *delegate = places->itemDelegate();
    if (model->rowCount() > 1) {
        places->selectionModel()->select(model->index(1,0), QItemSelectionModel::ClearAndSelect);
        QTest::qWait(40); require(placeEffect->running(), "native Places selection interpolates");
        QTest::qWait(220);
        const QColor selected = placeBackground(places, model->index(1,0));
        require(selected == QColor("#cba6f7"), "Places final selection uses the approved accent");
        // Focus transitions render the already-selected row into an offscreen
        // image too. Its unchanged selection must not turn native gray mid-frame.
        enter(places->viewport());
        QTest::qWait(40);
        require(placeEffect->running(), "Places hover captures the selected viewport");
        const QColor during = placeBackground(places, model->index(1,0));
        fprintf(stderr,"Places colors: final=%s mid=%s\n",qPrintable(selected.name()),qPrintable(during.name()));
        places->viewport()->grab().save(qEnvironmentVariable("RICY_PLACES_FIXTURE"));
        require(qAbs(during.red()-selected.red()) <= 1 &&
                qAbs(during.green()-selected.green()) <= 1 &&
                qAbs(during.blue()-selected.blue()) <= 1 && during.alpha() >= 254,
                "Places offscreen transition preserves selected accent");
        const QColor untouched = placeBackground(places, model->index(3,0));
        for (int i=0; i<24; ++i) {
            const QPointF point(places->visualRect(model->index(2+i%2,0)).center());
            QMouseEvent move(QEvent::MouseMove, point, places->viewport()->mapToGlobal(point.toPoint()),
                             Qt::NoButton, Qt::NoButton, Qt::NoModifier);
            app.sendEvent(places->viewport(), &move);
            QTest::qWait(12);
            const QColor frame = placeBackground(places, model->index(1,0));
            require(qAbs(frame.red()-selected.red()) <= 2 &&
                    qAbs(frame.green()-selected.green()) <= 2 &&
                    qAbs(frame.blue()-selected.blue()) <= 2 && frame.alpha() >= 253,
                    "rapid Places hover preserves common selection color/opacity");
        }
        leave(places->viewport()); QTest::qWait(220);
        require(placeBackground(places, model->index(3,0)) == untouched,
                "Places hover leaves no residual backing after settling");
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
    // Verify actual Qt dock layout dispatch under the production stylesheet.
    QFile stylesheet(QString::fromLocal8Bit(argv[1]));
    require(stylesheet.open(QIODevice::ReadOnly), "production dock stylesheet available");
    app.setStyleSheet(QString::fromUtf8(stylesheet.readAll()));
    auto dolphinConfig = KSharedConfig::openConfig(QStringLiteral("dolphinrc"));
    KConfigGroup general(dolphinConfig,QStringLiteral("General"));
    general.writeEntry("ShowSelectionToggle",true);
    require(dolphinConfig->sync(),"isolated native selection preference fixture saved");
    RicyDolphinUi dockHelper;
    require(!general.readEntry("ShowSelectionToggle",true)
        && !KConfigGroup(KSharedConfig::openConfig(),QStringLiteral("General")).readEntry("ShowSelectionToggle",true),
        "Ricy disables hover badge through the native shared preference");
    general.writeEntry("UnrelatedFixtureValue",QStringLiteral("preserved"));
    require(dolphinConfig->sync(),"unrelated native preference save succeeds");
    KConfig diskConfig(QStringLiteral("dolphinrc"));
    KConfigGroup saved(&diskConfig,QStringLiteral("General"));
    require(saved.readEntry("ShowSelectionToggle",false)
        && saved.readEntry("UnrelatedFixtureValue",QString()) == QStringLiteral("preserved"),
        "Ricy hover-badge override never persists alongside unrelated preference saves");
    fprintf(stderr,"PASS process-local hover-badge preference and independent Plasma/disk value preservation\n");
    QMainWindow dockWindow;
    auto *dock = new QDockWidget("Information", &dockWindow);
    dock->setFeatures(QDockWidget::DockWidgetClosable | QDockWidget::DockWidgetMovable);
    dock->setWidget(new QWidget);
    dockWindow.addDockWidget(Qt::RightDockWidgetArea,dock);
    dockWindow.resize(600,400); dockWindow.show(); QTest::qWait(50);
    auto *close = dock->findChild<QAbstractButton *>("qt_dockwidget_closebutton");
    require(close && close->isVisible() && close->size() == QSize(24,24),
            "native dock close button retains rounded 24px hit area");
    require(dock->rect().contains(close->geometry()), "close button fits native title area");
    const int topGap = close->y();
    const int bottomGap = dock->widget()->y()+4-close->geometry().bottom()-1;
    require(qAbs(topGap-bottomGap) <= 1,
            "close button balances title-top and card-top gaps within pixel rounding");
    auto closeHasColor = [close](const QColor &color) {
        const QImage image = close->grab().toImage();
        for (int y=0; y<image.height(); ++y)
            for (int x=0; x<image.width(); ++x)
                if (image.pixelColor(x,y) == color) return true;
        return false;
    };
    leave(close); QTest::qWait(20);
    const QImage closeImage = close->grab().toImage();
    QRect glyphBounds;
    for (int y=0; y<closeImage.height(); ++y)
        for (int x=0; x<closeImage.width(); ++x)
            if (closeImage.pixelColor(x,y) == QColor("#cdd6f4"))
                glyphBounds = glyphBounds.united(QRect(x,y,1,1));
    require(!glyphBounds.isEmpty() && glyphBounds.width() >= 6*closeImage.devicePixelRatio(),
            "Tabler close stroke remains legible without Qt icon reduction");
    require(qAbs(glyphBounds.center().x()+0.5-closeImage.width()/2.0) <= 1 &&
            qAbs(glyphBounds.center().y()+0.5-closeImage.height()/2.0) <= 1,
            "Tabler close glyph is centered horizontally and vertically");
    QTest::mouseMove(close,close->rect().center()); enter(close); QTest::qWait(30);
    require(closeHasColor(QColor("#977dba")), "native dock close hover uses existing fill");
    require(closeHasColor(QColor("#000000")), "hover close glyph uses on-hover foreground");
    QTest::mousePress(close,Qt::LeftButton); QTest::qWait(20);
    require(closeHasColor(QColor("#cba6f7")), "native dock close press uses existing accent");
    require(closeHasColor(QColor("#11111b")), "pressed close glyph uses on-accent foreground");
    QTest::mouseRelease(close,Qt::LeftButton); QTest::qWait(20);
    require(!dock->isVisible(), "native dock close signal still hides panel");
    dock->toggleViewAction()->trigger(); QTest::qWait(20);
    require(dock->isVisible(), "native toggle action reopens panel");
    dock->setLayoutDirection(Qt::RightToLeft); QTest::qWait(20);
    require(close->x() == 8 && dock->rect().contains(close->geometry()),
            "dock close control mirrors within RTL title area");
    fprintf(stderr,"PASS native dock 24px close geometry, balanced vertical gaps, centered smaller Tabler glyph, paired hover/press colors, close/reopen and RTL under production QSS\n");
    return 0;
}
