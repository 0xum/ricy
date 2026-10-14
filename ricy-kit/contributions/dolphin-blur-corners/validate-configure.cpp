// SPDX-License-Identifier: MIT
// Native KPageDialog fixture; no Dolphin preferences or file operations.
#include "ui.cpp"
#include <KPageDialog>
#include <KPageWidget>
#include <QCheckBox>
#include <QLineEdit>
#include <QPushButton>
#include <QListView>
#include <QVBoxLayout>
#include <QFormLayout>
#include <QTest>
#include <QFile>
#include <cstdio>

class DolphinSettingsDialog : public KPageDialog {
    Q_OBJECT
public:
    DolphinSettingsDialog() {
        setFaceType(KPageDialog::List);
        setStandardButtons(QDialogButtonBox::Ok | QDialogButtonBox::Apply |
                           QDialogButtonBox::Cancel | QDialogButtonBox::RestoreDefaults);
    }
};
static void require(bool result, const char *message) {
    if (!result) { fprintf(stderr,"FAIL %s\n",message); std::exit(1); }
}
int main(int argc, char **argv) {
    QCoreApplication::setApplicationName("dolphin");
    QApplication app(argc,argv);
    QFile sheet(argv[1]); require(sheet.open(QIODevice::ReadOnly),"production QSS available");
    app.setStyleSheet(QString::fromUtf8(sheet.readAll()));
    RicyDolphinUi helper;
    DolphinSettingsDialog dialog;
    auto *interface = new QWidget;
    auto *layout = new QVBoxLayout(interface);
    auto *tabs = new QTabWidget;
    layout->addWidget(tabs);
    QCheckBox *check = nullptr;
    QComboBox *combo = nullptr;
    for (const auto &name : {"Folders & Tabs","Previews","Confirmations","Panels","Status & Location bars"}) {
        auto *page = new QWidget;
        auto *form = new QFormLayout(page);
        auto *checkbox = new QCheckBox("Show close button on tabs");
        form->addRow("Tab width:",checkbox);
        auto *line = new QLineEdit("System location"); line->setEnabled(false);
        form->addRow("Startup:",line);
        auto *selector=new QComboBox;
        selector->addItems({"Close the active pane","Close the inactive pane","Close the right pane"});
        form->addRow("Split view:",selector);
        tabs->addTab(page,name);
        if (!check) check=checkbox;
        if (!combo) combo=selector;
    }
    auto *first = dialog.addPage(interface,"Interface");
    first->setIcon(QIcon::fromTheme("folder"));
    KPageWidgetItem *last = nullptr;
    for (const auto &name : {"View","Context Menu","Trash","User Feedback"}) {
        auto *page = new QWidget;
        auto *form = new QFormLayout(page);
        form->addRow("Preference:",new QCheckBox("Native setting"));
        last=dialog.addPage(page,name);
        last->setIcon(QIcon::fromTheme("configure"));
    }
    dialog.resize(1000,760); dialog.show(); QTest::qWait(100);
    require(dialog.property("ricyConfigure").toBool(),"Configure scope detected");
    auto *panel=dialog.findChild<QWidget *>("ricyShellPanel");
    require(panel && panel->testAttribute(Qt::WA_TransparentForMouseEvents) &&
            panel->focusPolicy()==Qt::NoFocus,"L backing cannot receive input/focus");
    auto *pages=dialog.findChild<KPageWidget *>();
    require(pages && pages->model()->rowCount()==5,"native page model preserved");
    QWidget *card=nullptr,*navigation=nullptr;
    for(auto *widget:dialog.findChildren<QWidget *>()) {
        if(widget->property("ricyConfigureCard").toBool())card=widget;
        if(widget->property("ricyConfigureNavigation").toBool())navigation=widget;
    }
    require(card && navigation,"native content card and sidebar identified");
    require(interface->layout()->contentsMargins()==QMargins(12,12,12,12),"central native page has existing 12px inset");
    auto *arrow=combo->findChild<QWidget *>("ricyFieldArrows");
    require(arrow && arrow->isVisible() && arrow->testAttribute(Qt::WA_TransparentForMouseEvents),
            "selector chevron is visible and cannot intercept native clicks");
    require(arrow->width()==24 && combo->rect().contains(arrow->geometry()),"chevron fits Qt's native 24px dropdown slot");
    const QImage arrowImage=arrow->grab().toImage();
    int ink=0;
    for(int y=0;y<arrowImage.height();++y) for(int x=0;x<arrowImage.width();++x)
        if(arrowImage.pixelColor(x,y).lightness()>160) ++ink;
    require(ink>=8,"small stroked chevron remains legible");
    const QPoint cardTop=card->mapTo(&dialog,QPoint());
    const QPoint navRight=navigation->mapTo(&dialog,QPoint(navigation->width(),0));
    require(cardTop.x()-navRight.x()==8,"sidebar/card retain 8px gutter");
    const QImage capture=dialog.grab().toImage();
    if(qEnvironmentVariableIsSet("RICY_CONFIGURE_FIXTURE")) {
        capture.save(qEnvironmentVariable("RICY_CONFIGURE_FIXTURE"));
    }
    const qreal ratio=capture.devicePixelRatio();
    auto pixel=[&](QPoint point){return capture.pixelColor(qRound(point.x()*ratio),qRound(point.y()*ratio));};
    const QColor outer=pixel(QPoint(2,2));
    require(outer.alpha()==178 && qAbs(outer.red()-24)<=1 && qAbs(outer.blue()-37)<=1,"outer backing uses main-window glass alpha");
    require(pixel(QPoint(dialog.width()-24,16))==QColor("#313244"),"top arm uses existing card surface");
    require(pixel(QPoint(16,dialog.height()-24))==QColor("#313244"),"sidebar arm joins header backing");
    require(pixel(cardTop+QPoint(8,card->height()-8))==QColor("#313244"),"central page has solid card backing");
    require(pixel(QPoint(cardTop.x()-4,cardTop.y()+24)).alpha()==178,"card/L gutter exposes glass without a solid overpaint");
    pages->setCurrentPage(last); QTest::qWait(30);
    require(pages->currentPage()==last,"native sidebar navigation works");
    pages->setCurrentPage(first); tabs->setCurrentIndex(2);QTest::qWait(30);
    require(tabs->currentIndex()==2,"native tabs navigate unchanged");
    auto *searchContainer=pages->findChild<QWidget *>("KPageView::Search");
    auto *search=searchContainer ? searchContainer->findChild<QLineEdit *>() : nullptr;
    auto *list=qobject_cast<QListView *>(navigation);
    require(search && list,"native searchable sidebar present");
    search->setText("Native setting"); QTest::qWait(450);
    require(list->isRowHidden(0) && !list->isRowHidden(1),"native search filtering works");
    search->clear(); QTest::qWait(450);
    require(!list->isRowHidden(0),"clearing search restores native pages");
    dialog.resize(920,700);QTest::qWait(30);
    require(panel->size()==pages->size(),"backing follows native dialog resize");
    dialog.setLayoutDirection(Qt::RightToLeft);QTest::qWait(30);
    const QPoint navLeft=navigation->mapTo(&dialog,QPoint());
    const QPoint cardRight=card->mapTo(&dialog,QPoint(card->width(),0));
    require(navLeft.x()-cardRight.x()==8,"native RTL layout retains card/sidebar gutter");
    const QImage rtl=dialog.grab().toImage();
    require(rtl.pixelColor(qRound((dialog.width()-16)*ratio),qRound((dialog.height()-24)*ratio))==QColor("#313244"),"RTL mirrors the L backing");
    dialog.setLayoutDirection(Qt::LeftToRight);QTest::qWait(30);
    pages->setCurrentPage(first);
    tabs->setCurrentIndex(0); check->setFocus(); QTest::keyClick(check,Qt::Key_Space);
    require(check->isChecked(),"keyboard setting control remains interactive");
    QTest::mouseClick(combo,Qt::LeftButton,Qt::NoModifier,arrow->geometry().center());QTest::qWait(40);
    QWidget *popup=nullptr;
    for(auto *widget:combo->findChildren<QWidget *>())
        if(widget->property("ricyConfigurePopup").toBool()) popup=widget;
    require(popup && popup->isVisible(),"native selector popup remains available");
    require(popup->windowOpacity()==1,"Configure popover does not reduce window opacity");
    require(popup->contentsMargins()==QMargins(12,12,12,12),"popover reserves the existing menu's 12px inset");
    const QImage popupImage=popup->grab().toImage();
    const qreal popupRatio=popupImage.devicePixelRatio();
    require(popupImage.pixelColor(qRound(10*popupRatio),qRound((popup->height()-10)*popupRatio))==QColor("#313244"),
            "popover paints a solid card without a gradient/translucent backing");
    bool selectedPair=false;
    for(int y=0;y<popupImage.height();++y) for(int x=0;x<popupImage.width();++x)
        if(popupImage.pixelColor(x,y)==QColor("#cba6f7")) selectedPair=true;
    require(selectedPair && combo->view()->palette().color(QPalette::HighlightedText)==QColor("#11111b"),
            "popover selection retains the established accent/foreground pair");
    require(popupImage.pixelColor(qRound(popup->width()/2.0*popupRatio),0)==QColor("#46485c"),
            "popover has the existing one-pixel outline");
    if(qEnvironmentVariableIsSet("RICY_CONFIGURE_FIXTURE"))
        popupImage.save(qEnvironmentVariable("RICY_CONFIGURE_FIXTURE")+".popup.png");
    QTest::keyClick(combo->view(),Qt::Key_Escape);QTest::qWait(20);
    require(combo->currentIndex()==0 && !popup->isVisible(),"Escape dismisses without changing the selector");
    combo->setFocus();QTest::keyClick(combo,Qt::Key_Down);
    require(combo->currentIndex()==1,"native selector keyboard selection remains intact");
    int applyCount=0;
    auto *buttons=dialog.findChild<QDialogButtonBox *>();
    require(buttons,"native dialog buttons present");
    QObject::connect(buttons->button(QDialogButtonBox::Apply),&QPushButton::clicked,[&]{++applyCount;});
    QTest::mouseClick(buttons->button(QDialogButtonBox::Apply),Qt::LeftButton);
    require(applyCount==1 && dialog.isVisible(),"Apply action remains native and keeps dialog open");
    QDialog auxiliary;
    auto *auxLayout=new QFormLayout(&auxiliary);
    auto *integer=new QSpinBox;
    integer->setRange(0,3);integer->setValue(1);
    auto *decimal=new QDoubleSpinBox;
    decimal->setRange(0,1);decimal->setSingleStep(0.25);decimal->setValue(0.5);
    auto *hiddenSteps=new QSpinBox;
    hiddenSteps->setButtonSymbols(QAbstractSpinBox::NoButtons);
    auto *auxCombo=new QComboBox;auxCombo->addItems({"First","Second"});
    auxLayout->addRow("Count:",integer);auxLayout->addRow("Ratio:",decimal);
    auxLayout->addRow("No step buttons:",hiddenSteps);auxLayout->addRow("Choice:",auxCombo);
    auxiliary.resize(440,240);auxiliary.show();QTest::qWait(40);
    require(!auxiliary.property("ricyConfigure").toBool() &&
            !auxiliary.findChild<QWidget *>("ricyShellPanel"),"other dialogs remain outside Configure adaptation");
    for(auto *field:{static_cast<QWidget *>(integer),static_cast<QWidget *>(decimal),static_cast<QWidget *>(auxCombo)}) {
        auto *glyphs=field->findChild<QWidget *>("ricyFieldArrows",Qt::FindDirectChildrenOnly);
        require(glyphs && glyphs->isVisible() && glyphs->testAttribute(Qt::WA_TransparentForMouseEvents),
                "numeric/selector arrows are consistent outside Configure");
    }
    auto *hiddenGlyphs=hiddenSteps->findChild<QWidget *>("ricyFieldArrows");
    require(hiddenGlyphs && !hiddenGlyphs->isVisible(),"native NoButtons mode remains unchanged");
    auto stepRect=[](QAbstractSpinBox *spin,QStyle::SubControl control){
        QStyleOptionSpinBox option;option.initFrom(spin);option.frame=spin->hasFrame();
        option.buttonSymbols=spin->buttonSymbols();option.stepEnabled=QAbstractSpinBox::StepUpEnabled|QAbstractSpinBox::StepDownEnabled;
        return spin->style()->subControlRect(QStyle::CC_SpinBox,&option,control,spin);
    };
    const QRect up=stepRect(integer,QStyle::SC_SpinBoxUp),down=stepRect(integer,QStyle::SC_SpinBoxDown);
    require(integer->rect().contains(up) && integer->rect().contains(down) && !up.intersects(down),
            "numeric step hit slots retain native nonoverlapping geometry");
    QTest::mouseClick(integer,Qt::LeftButton,Qt::NoModifier,up.center());
    require(integer->value()==2,"native increment action retained");
    QTest::mouseClick(integer,Qt::LeftButton,Qt::NoModifier,down.center());
    require(integer->value()==1,"native decrement action retained");
    integer->setValue(3);QTest::mouseClick(integer,Qt::LeftButton,Qt::NoModifier,up.center());
    require(integer->value()==3,"native maximum limit remains enforced");
    decimal->setFocus();QTest::keyClick(decimal,Qt::Key_Up);
    require(qAbs(decimal->value()-0.75)<0.001,"native fractional keyboard step retained");
    if(qEnvironmentVariableIsSet("RICY_CONFIGURE_FIXTURE"))
        auxiliary.grab().save(qEnvironmentVariable("RICY_CONFIGURE_FIXTURE")+".fields.png");
    QTest::mouseClick(buttons->button(QDialogButtonBox::Cancel),Qt::LeftButton);
    require(!dialog.isVisible() && dialog.result()==QDialog::Rejected,"Cancel still rejects native dialog");
    fprintf(stderr,"PASS native Configure L/glass/cards, outlined solid popover, field arrows/numeric steps, resize/RTL, search, keyboard, Apply/Cancel and auxiliary layout exclusion at scale %g\n",ratio);
    return 0;
}
#include "validate-configure.moc"
