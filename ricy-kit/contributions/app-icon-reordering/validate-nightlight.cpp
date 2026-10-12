// Exercise the compiled service on a private bus; never contact the user's KWin.
#include "system/gamma_service.h"
#include "wayland/wayland_connection.h"
#include "dbus/session_bus.h"
#include <atomic>
#include <iostream>
#include <stdexcept>
#include <thread>

void require(bool value, const char* label) {
  if (!value) throw std::runtime_error(label);
}

class KwinFixture {
public:
  std::atomic<bool> available{true}, enabled{true}, inhibited{false}, running{true}, daylight{false};
  std::atomic<int> toggles{0};
  std::atomic<std::uint32_t> temperature{4500};
  std::unique_ptr<sdbus::IConnection> bus = sdbus::createSessionBusConnection(sdbus::ServiceName{"org.kde.KWin"});
  std::unique_ptr<sdbus::IObject> night = sdbus::createObject(*bus, sdbus::ObjectPath{"/org/kde/KWin/NightLight"});
  std::unique_ptr<sdbus::IObject> shortcut = sdbus::createObject(*bus, sdbus::ObjectPath{"/component/kwin"});
  KwinFixture() {
    bus->requestName(sdbus::ServiceName{"org.kde.kglobalaccel"});
    night->addVTable(
      sdbus::registerProperty("available").withGetter([this] { return available.load(); }),
      sdbus::registerProperty("enabled").withGetter([this] { return enabled.load(); }),
      sdbus::registerProperty("inhibited").withGetter([this] { return inhibited.load(); }),
      sdbus::registerProperty("running").withGetter([this] { return running.load(); }),
      sdbus::registerProperty("currentTemperature").withGetter([this] { return temperature.load(); })
    ).forInterface("org.kde.KWin.NightLight");
    shortcut->addVTable(sdbus::registerMethod("invokeShortcut").implementedAs([this](const std::string& name) {
      require(name == "Toggle Night Color", "uses native KWin action");
      inhibited = !inhibited.load();
      ++toggles;
    })).forInterface("org.kde.kglobalaccel.Component");
    bus->enterEventLoopAsync();
  }
  ~KwinFixture() { bus->leaveEventLoop(); }
};

int main() {
  WaylandConnection wayland;
  SessionBus bus;
  GammaService service(wayland);
  service.startKwin(bus);
  require(!service.usesKwin() && !service.available(), "absent KWin leaves Wayland backend unchanged");
  KwinFixture kwin;
  int changes = 0;
  service.setChangeCallback([&] { ++changes; });
  service.startKwin(bus);
  require(service.available() && service.enabled() && service.active(), "initial night state follows KWin");
  service.toggleEnabled();
  require(!service.enabled() && !service.active() && kwin.inhibited && kwin.enabled, "pause preserves scheduled enable");
  service.toggleEnabled();
  require(service.enabled() && service.active() && !kwin.inhibited, "resume releases native pause");
  require(kwin.toggles == 2, "one native action per click");
  service.setEnabled(true);
  require(kwin.toggles == 2, "idempotent enable");
  kwin.daylight = true;
  kwin.temperature = 6500;
  service.reevaluateSchedule();
  require(service.enabled() && !service.active(), "scheduled daytime remains distinguishable");
  kwin.inhibited = true;
  kwin.night->emitPropertiesChangedSignal("org.kde.KWin.NightLight", {sdbus::PropertyName{"inhibited"}});
  for (int i=0; i<50 && service.enabled(); ++i) {
    std::this_thread::sleep_for(std::chrono::milliseconds(10));
    bus.processPendingEvents();
  }
  require(!service.enabled(), "external inhibition updates through PropertiesChanged");
  kwin.inhibited = false;
  NightLightConfig config;
  config.enabled = false;
  config.force = true;
  service.reload(config, LocationConfig{});
  require(service.enabled() && !service.forceEnabled(), "Noctalia reload cannot override KWin settings");
  service.toggleEnabled();
  require(kwin.inhibited, "Noctalia force configuration cannot intercept KWin toggle");
  kwin.available = false;
  service.reevaluateSchedule();
  require(!service.available() && !service.active(), "unsupported display disables control");
  service.toggleEnabled();
  require(kwin.toggles == 3, "unavailable backend does not invoke action");
  kwin.bus->releaseName(sdbus::ServiceName{"org.kde.KWin"});
  service.reevaluateSchedule();
  require(!service.available() && !service.enabled(), "service loss clears cached state");
  kwin.bus->requestName(sdbus::ServiceName{"org.kde.KWin"});
  kwin.available = true;
  kwin.inhibited = false;
  kwin.daylight = false;
  kwin.temperature = 4500;
  service.reevaluateSchedule();
  require(service.available() && service.active(), "KWin return restores state");
  require(changes >= 8, "state changes refresh shell consumers");
  std::cout << "PASS native KWin night/day, toggle, external signal, reload, unavailable/loss/recovery scenarios\n";
}
