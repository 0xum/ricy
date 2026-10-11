// SPDX-License-Identifier: MIT
// Ricy: uses KWin 6.7.5 native clipping; does not create rendering passes.
#include <effect/effect.h>
#include <effect/effecthandler.h>
#include <effect/effectwindow.h>
#include <window.h>
#include <scene/borderradius.h>
#include <QHash>
#include <QDBusConnection>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
namespace KWin {
class RicyDolphinCorners : public Effect {
 Q_OBJECT
 Q_CLASSINFO("D-Bus Interface", "org.ricy.DolphinRounding")
 struct State { BorderRadius original; bool updating=false; };
 QHash<Window *,State> states;
 void update(Window *w) {
  auto it=states.find(w); if(it==states.end() || it->updating) return;
  it->updating=true;
  const bool square=w->isFullScreen() || w->maximizeMode()!=MaximizeRestore || w->quickTileMode()!=QuickTileMode(0);
  w->setBorderRadius(square ? BorderRadius() : BorderRadius(16));
  it->updating=false; effects->addRepaintFull();
 }
 void watch(EffectWindow *ew) {
  Window *w=ew->window();
  if((w->resourceClass()!=QStringLiteral("dolphin") && w->resourceClass()!=QStringLiteral("org.kde.dolphin")) || !(ew->isNormalWindow() || ew->isDialog()) || states.contains(w)) return;
  states.insert(w,{w->borderRadius(),false});
  connect(w,&Window::borderRadiusChanged,this,[this,w]() {
   auto it=states.find(w); if(it==states.end() || it->updating) return;
   it->original=w->borderRadius(); update(w);
  });
  connect(w,&Window::maximizedChanged,this,[this,w]() { update(w); });
  connect(w,&Window::fullScreenChanged,this,[this,w]() { update(w); });
  connect(w,&Window::quickTileModeChanged,this,[this,w]() { update(w); });
  connect(w,&QObject::destroyed,this,[this,w]() { states.remove(w); });
  update(w);
 }
public:
 RicyDolphinCorners() {
  QDBusConnection::sessionBus().registerObject("/RicyDolphinRounding",this,QDBusConnection::ExportAllSlots);
  connect(effects,&EffectsHandler::windowAdded,this,[this](EffectWindow *w) { watch(w); });
  for(auto *w:effects->stackingOrder()) watch(w);
 }
 ~RicyDolphinCorners() override {
  QDBusConnection::sessionBus().unregisterObject("/RicyDolphinRounding");
  for(auto it=states.begin();it!=states.end();++it) {
   it->updating=true; it.key()->setBorderRadius(it->original); effects->addRepaintFull();
  }
 }
 bool isActive() const override { return false; }
public Q_SLOTS:
 QString status() const {
  QJsonArray a;
  for(auto *ew:effects->stackingOrder()) {
   Window *w=ew->window();
   if(w->resourceName()!=QStringLiteral("dolphin") && !w->resourceClass().contains(QStringLiteral("dolphin"))) continue;
   a.append(QJsonObject{{"class",w->resourceClass()},{"normal",ew->isNormalWindow()},{"dialog",ew->isDialog()},{"tracked",states.contains(w)},{"radius",w->borderRadius().topLeft()},{"maximize",int(w->maximizeMode())},{"tile",int(w->quickTileMode())}});
  }
  return QString::fromUtf8(QJsonDocument(a).toJson(QJsonDocument::Compact));
 }

};
KWIN_EFFECT_FACTORY_SUPPORTED_ENABLED(RicyDolphinCorners,"metadata.json", return effects->isOpenGLCompositing();, return false;)
}
#include "corners.moc"
