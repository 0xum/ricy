// Exercise the compiled KDE inventory and taskbar reconciliation on a private bus.
// Preload dependencies before exposing only fixture state in these two classes.
#include "wayland/wayland_connection.h"
#include "compositors/workspace_backend.h"
#include "compositors/keyboard_backend.h"
#include "dbus/session_bus.h"
#include <chrono>
#include <functional>
#include <optional>
#include <poll.h>
#include <string_view>
#define private public
#include "compositors/compositor_platform.h"
#include "compositors/kde/kwin_active_window.h"
#undef private
#include "shell/bar/widgets/taskbar_widget.h"
#include "config/config_service.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <mutex>
#include <stdexcept>

void require(bool ok, const char* label) {
  if (!ok) throw std::runtime_error(label);
}

std::size_t modelScenarios = 0;

// Only the private test bus owns this name; no compositor is started.
class KwinFixture {
  std::unique_ptr<sdbus::IConnection> bus = sdbus::createSessionBusConnection(sdbus::ServiceName{"org.kde.KWin"});
  std::unique_ptr<sdbus::IObject> scripting = sdbus::createObject(*bus, sdbus::ObjectPath{"/Scripting"});
  std::unique_ptr<sdbus::IObject> script = sdbus::createObject(*bus, sdbus::ObjectPath{"/Scripting/Script1"});
  std::mutex mutex;
  std::string source;
public:
  KwinFixture() {
    scripting->addVTable(
        sdbus::registerMethod("unloadScript").implementedAs([](const std::string&) { return true; }),
        sdbus::registerMethod("loadScript").implementedAs([this](const std::string& path, const std::string&) {
          std::ifstream input(path);
          std::lock_guard lock(mutex);
          source.assign(std::istreambuf_iterator<char>(input), {});
          return std::int32_t{1};
        })
    ).forInterface("org.kde.kwin.Scripting");
    script->addVTable(sdbus::registerMethod("run").implementedAs([] {})).forInterface("org.kde.kwin.Script");
    bus->enterEventLoopAsync();
  }
  ~KwinFixture() { bus->leaveEventLoop(); }
  bool targets(const std::string& uuid) {
    std::lock_guard lock(mutex);
    return source.find("const targetUuid = \"" + uuid + "\";") != std::string::npos;
  }
};

class TaskbarWidgetTestAccess {
public:
  static void check(TaskbarWidget& widget, const std::vector<ToplevelInfo>& inventory, KwinFixture& kwin) {
    widget.updateModels();
    require(widget.m_tasks.size() == inventory.size(), "each window retains its own task");
    for (const auto& window : inventory) {
      const auto key = static_cast<std::uintptr_t>(std::hash<std::string>{}(window.identifier));
      const auto task = std::ranges::find_if(widget.m_tasks, [&](const auto& candidate) {
        return candidate.handleKey == (key == 0 ? 1 : key);
      });
      require(task != widget.m_tasks.end(), "task remains keyed by its original KWin UUID");
      require(widget.workspaceBindingWindowId(*task) == window.identifier,
              "monitor reconciliation cannot replace the clicked window UUID");
      widget.activateTaskModel(*task, true);
      require(kwin.targets(window.identifier), "left-click action sends the clicked window UUID to KWin");
      widget.activateTaskModel(*task);
      require(kwin.targets(window.identifier), "ordinary focus sends the same window UUID to KWin");
      widget.closeTaskModel(*task);
      require(kwin.targets(window.identifier), "single-window close sends the same window UUID to KWin");
    }
    ++modelScenarios;
  }
};

std::string record(const std::string& uuid, const std::string& app, const std::string& title,
                   const std::string& output, bool minimized = false) {
  return uuid + '\x1e' + app + '\x1e' + title + '\x1e' + "desktop" + '\x1e' + output
      + '\x1e' + (minimized ? "1" : "0");
}

int main() try {
  KwinFixture kwin;
  SessionBus bus;
  WaylandConnection connection;
  CompositorPlatform platform(connection);
  platform.m_kwinActiveWindow = std::make_unique<compositors::kde::KwinActiveWindow>(bus);
  auto& adapter = *platform.m_kwinActiveWindow;
  // Do not start/register the adapter. Input and KWin action endpoints are synthetic.
  adapter.m_scriptInstalled = true;
  auto& outputs = const_cast<std::vector<WaylandOutput>&>(connection.outputs());
  int leftToken = 0, rightToken = 0;
  auto* left = reinterpret_cast<wl_output*>(&leftToken);
  auto* right = reinterpret_cast<wl_output*>(&rightToken);
  outputs.push_back({.connectorName = "LEFT", .output = left});
  outputs.push_back({.connectorName = "RIGHT", .output = right});
  // Clear synthetic handles before Wayland cleanup, including on a failed assertion.
  struct Cleanup {
    std::vector<WaylandOutput>& outputs;
    compositors::kde::KwinActiveWindow& adapter;
    ~Cleanup() { outputs.clear(); adapter.m_scriptInstalled = false; }
  } cleanup{outputs, adapter};
  ConfigService config;
  for (const std::string app : {"brave", "org.kde.dolphin"}) {
    for (const bool duplicateTitle : {false, true}) {
      adapter.onNotifyWindowList(record("left-window", app, "Document", "LEFT") + '\x1f'
          + record("right-window", app, duplicateTitle ? "Document" : "Other document", "RIGHT"));
      adapter.onNotifyActiveWindow("Document", app, "left-window");
      const auto inventory = adapter.windowsForApp(app, app);
      require(inventory.size() == 2, "KWin reports two windows of the same application");
      for (auto* output : {left, right}) {
        TaskbarWidget widget(platform, config, output, {}, {.widgetName = "taskbar"});
        TaskbarWidgetTestAccess::check(widget, inventory, kwin);
        // Reversed discovery, retitled and minimized windows must keep their own UUIDs.
        adapter.onNotifyWindowList(record("right-window", app, "Retitled", "RIGHT", true) + '\x1f'
            + record("left-window", app, "Document", "LEFT"));
        TaskbarWidgetTestAccess::check(widget, adapter.windowsForApp(app, app), kwin);
        // Both windows can also share a monitor without sharing an action target.
        adapter.onNotifyWindowList(record("right-window", app, "Document", "LEFT") + '\x1f'
            + record("left-window", app, "Document", "LEFT"));
        TaskbarWidgetTestAccess::check(widget, adapter.windowsForApp(app, app), kwin);
        // A monitor move updates placement without substituting another window.
        adapter.onNotifyWindowList(record("right-window", app, "Retitled", "LEFT", true) + '\x1f'
            + record("left-window", app, "Document", "RIGHT"));
        TaskbarWidgetTestAccess::check(widget, adapter.windowsForApp(app, app), kwin);
      }
    }
  }
  std::cout << "PASS: " << modelScenarios << " compiled KDE UUID reconciliation scenarios for Brave/Dolphin, "
               "duplicate titles, one/two monitors, "
               "discovery changes, minimization and monitor moves. No real window was manipulated.\n";
  return 0;
} catch (const std::exception& error) {
  std::cerr << "FAIL: " << error.what() << '\n';
  return 1;
}
