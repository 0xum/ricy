#include "shell/bar/widgets/taskbar_widget.h"
#include "config/config_service.h"
#include "shell/bar/widgets/taskbar_widget_definition.h"
#include "core/deferred_call.h"
#include "render/scene/input_area.h"
#include "shell/bar/widgets/taskbar_order.h"
#include "wayland/wayland_connection.h"
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
    widget.m_tasks = {{.handleKey = 1, .idLower = "example.brave"}, {.handleKey = 2, .idLower = "example.codex"}};
    widget.applyAppOrder(widget.m_tasks);
    require(widget.reorderEnabled(), "dois apps não fixados podem ser arrastados");
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
    require(!widget.commitDragReorder(), "mudança do modelo invalida commit antigo");
    widget.endDrag(false);
    prepare();
    widget.m_drag.armed = true;
    widget.endDrag(false);
    require(!widget.m_suppressTileClick, "segurar sem arrastar preserva clique");
    prepare();
    widget.beginDrag();
    widget.m_drag.currentMain = 10;
    widget.updateDragTarget();
    widget.moveDragTile();
    require(widget.m_drag.targetIndex == 0 && area.x() == 0, "arraste nativo move ícone e escolhe slot anterior");
    widget.endDrag(false);
    require(widget.m_suppressTileClick && !widget.m_drag.active && widget.m_drag.area == nullptr, "cancelamento encerra gesto e suprime ativação");
    flush();
    prepare();
    widget.beginDrag();
    widget.m_drag.currentMain = 10;
    widget.updateDragTarget();
    widget.endDrag(true);
    require(widget.m_suppressTileClick, "soltar arraste não ativa ou minimiza aplicativo");
    flush();
  }
};
int main() {
  WaylandConnection connection;
  CompositorPlatform platform(connection);
  ConfigService config;
  {
    TaskbarWidget widget(platform, config, nullptr, {}, {.barPosition="bottom", .widgetName="taskbar"});
    TaskbarWidgetTestAccess::run(widget);
  }
  flush();
  std::ifstream file(std::string(std::getenv("NOCTALIA_STATE_HOME")) + "/noctalia/settings.toml");
  std::string settings((std::istreambuf_iterator<char>(file)), {});
  require(settings.find("app_order") != std::string::npos && settings.find("pinned") == std::string::npos, "ConfigService grava app_order sem fixar apps");
  const auto codex = settings.find("13:example.codex:0");
  const auto brave = settings.find("13:example.brave:0");
  require(codex != std::string::npos && brave != std::string::npos && codex < brave, "preferência salva segue ordem de soltura");
  ConfigService fresh;
  require(fresh.buildMergedUserConfig().find("app_order") != std::string::npos, "instância nova recupera ordem gravada");
  const auto found = fresh.config().widgets.find("taskbar");
  require(found != fresh.config().widgets.end(), "configuração nova contém widget taskbar");
  const auto options = taskbarWidgetDefinition().resolve(&found->second, "widget.taskbar");
  require(options.appOrder == std::vector<std::string>{"13:example.codex:0", "13:example.brave:0"}, "schema e definição decodificam ordem persistida");
  std::cout << "11 cenários nativos passaram, em perfil temporário sem conexão ao compositor.\n";
}
