#include "shell/bar/widgets/taskbar_widget.h"
#include "config/config_service.h"
#include "shell/bar/widgets/taskbar_widget_definition.h"
#include "core/deferred_call.h"
#include "render/scene/input_area.h"
#include "shell/bar/widgets/taskbar_order.h"
#include "wayland/wayland_connection.h"
#include "shell/bar/widget_factory.h"
#include "shell/bar/widget_gesture_defaults.h"
#include "shell/settings/widget_settings_registry.h"
#include "cli/schema_msg.h"
#include "shell/settings/settings_registry.h"
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>

void require(bool ok, const char* label) {
  if (!ok) throw std::runtime_error(label);
  std::cout << "PASS: " << label << '\n';
}
void flush() { for (auto& callback : DeferredCall::takePending()) callback(); }
class TaskbarWidgetTestAccess {
public:
  static void run(TaskbarWidget& widget) {
    require(!widget.m_groupByWorkspace && !widget.m_showWorkspaceLabel,
            "legacy grouping and labels cannot expose desktops");
    widget.m_tasks = {{.handleKey = 1, .idLower = "example.brave"}, {.handleKey = 2, .idLower = "example.codex"}};
    widget.applyAppOrder(widget.m_tasks);
    require(widget.reorderEnabled(), "two unfixed apps can be dragged");
    widget.m_tilePitchMain = 30;
    InputArea area;
    area.setPosition(30, 0);
    area.setFrameSize(24, 24);
    auto prepare = [&] {
      widget.m_drag.area = &area;
      widget.m_drag.generation = widget.m_taskGeneration;
      widget.m_drag.sourceIndex = widget.m_drag.targetIndex = 1;
      widget.m_drag.startMain = widget.m_drag.currentMain = 40;
      widget.m_drag.tileCount = widget.m_tasks.size();
    };
    prepare();
    ++widget.m_drag.generation;
    widget.m_drag.targetIndex = 0;
    require(!widget.commitDragReorder(), "model change invalidates old commit");
    widget.endDrag(false);
    prepare();
    widget.m_drag.armed = true;
    widget.endDrag(false);
    require(!widget.m_suppressTileClick, "hold without drag preserves click");
    prepare();
    widget.beginDrag();
    widget.m_drag.currentMain = 10;
    widget.updateDragTarget();
    widget.moveDragTile();
    require(widget.m_drag.targetIndex == 0 && area.x() == 0, "native drag moves icon and choose previous slot");
    widget.endDrag(false);
    require(widget.m_suppressTileClick && !widget.m_drag.active && widget.m_drag.area == nullptr, "cancellation closes gesture and suppress activation");
    flush();
    prepare();
    widget.beginDrag();
    widget.m_drag.currentMain = 10;
    widget.updateDragTarget();
    widget.endDrag(true);
    require(widget.m_suppressTileClick, "drop non-active drag or minimize application");
    flush();
  }
};
int main() {
  WaylandConnection connection;
  CompositorPlatform platform(connection);
  ConfigService config;
  WidgetFactory factory({.platform = platform, .config = config});
  require(factory.create("workspaces", nullptr) == nullptr, "workspace widget is disabled");
  require(factory.create("legacy_desktops", nullptr) == nullptr, "named workspace alias is disabled");
  const auto picker = settings::widgetPickerEntries(config.config());
  require(std::ranges::none_of(picker, [](const auto& entry) {
            return entry.value == "workspaces" || entry.value == "legacy_desktops";
          }), "workspace widget and named alias are absent from the picker");
  require(settings::widgetSettingSpecs("workspaces", nullptr, "Noto Sans", false).empty(),
          "legacy workspace widget has no settings controls");
  const auto specs = settings::widgetSettingSpecs("taskbar", nullptr, "Noto Sans", false);
  std::size_t hidden = 0;
  for (const auto& spec : specs) {
    if (spec.requiresCapability == settings::WidgetSettingCapability::TaskbarWorkspaceGrouping) {
      ++hidden;
      require(!settings::widgetSettingIsVisible(config.config(), "taskbar", spec, specs,
                                               {.taskbarWorkspaceGrouping = true}),
              "desktop setting stays hidden even on a capable compositor");
    }
  }
  require(hidden >= 8, "desktop setting regression covers groups and labels");
  require(noctalia::bar::gestureDefaultsForType("workspaces").empty(), "no workspace scroll bindings");
  const auto registry = settings::buildSettingsRegistry(config.config(), nullptr);
  require(std::ranges::none_of(registry, [](const auto& entry) {
            return std::ranges::find(entry.path, "show_on_workspace_switch") != entry.path.end()
                || std::ranges::find(entry.path, "current_workspace_only") != entry.path.end();
          }), "global settings search exposes no desktop reveal or filter option");
  for (const auto command : {"workspace-switch", "workspace-alert-add", "workspace-alert-add-window",
                             "workspace-alert-clear", "workspace-alert-clear-all", "workspace-alert-status"}) {
    require(noctalia::cli::findMsgCommand(command) == nullptr, "workspace command is absent from CLI discovery");
  }
  {
    TaskbarWidget widget(platform, config, nullptr, {}, {.barPosition="bottom", .widgetName="taskbar"});
    TaskbarWidgetTestAccess::run(widget);
  }
  flush();
  std::ifstream file(std::string(std::getenv("NOCTALIA_STATE_HOME")) + "/noctalia/settings.toml");
  std::string settings((std::istreambuf_iterator<char>(file)), {});
  require(settings.find("app_order") != std::string::npos && settings.find("pinned") == std::string::npos, "ConfigService saves app_order without fixing apps");
  const auto codex = settings.find("13:example.codex:0");
  const auto brave = settings.find("13:example.brave:0");
  require(codex != std::string::npos && brave != std::string::npos && codex < brave, "Save preference follows release order");
  ConfigService fresh;
  require(fresh.buildMergedUserConfig().find("app_order") != std::string::npos, "new instance recovers saved order");
  const auto found = fresh.config().widgets.find("taskbar");
  require(found != fresh.config().widgets.end(), "new configuration contains taskbar widget");
  const auto options = taskbarWidgetDefinition().resolve(&found->second, "widget.taskbar");
  require(options.appOrder == std::vector<std::string>{"13:example.codex:0", "13:example.brave:0"}, "schema and definition decode order persisted");
  std::cout << "Native single-space and drag scenarios passed in a temporary profile without a compositor connection.\n";
}
