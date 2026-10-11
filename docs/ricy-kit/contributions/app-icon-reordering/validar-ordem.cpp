#include "shell/bar/widgets/taskbar_order.h"

#include <iostream>
#include <limits>
#include <numeric>
#include <stdexcept>

using List = std::vector<std::string>;
int count = 0;
void check(bool passed, const char* message) {
  if (!passed) throw std::runtime_error(message);
  ++count;
  std::cout << "PASS: " << message << '\n';
}

List sorted(List visible, const List& saved) {
  const auto ranks = taskbar_order::ranks(saved);
  const auto rank = [&ranks](const std::string& value) {
    const auto it = ranks.find(value);
    return it == ranks.end() ? std::numeric_limits<std::size_t>::max() : it->second;
  };
  std::stable_sort(visible.begin(), visible.end(), [&](const auto& a, const auto& b) { return rank(a) < rank(b); });
  return visible;
}

int main() {
  using namespace taskbar_order;
  List order{"brave", "codex", "konsole"};
  check(move(order, 0, 2) && order == List{"codex", "konsole", "brave"}, "arrastar primeiro para último");
  check(move(order, 2, 0) && order == List{"brave", "codex", "konsole"}, "arrastar último para primeiro");
  check(!move(order, 1, 1) && order == List{"brave", "codex", "konsole"}, "mesma posição não grava alteração");
  check(!move(order, 4, 0) && !move(order, 0, 3), "índice inválido não modifica ordem");
  check(target(1, 3, 14, 30) == 1 && target(1, 3, 16, 30) == 2, "troca de slot cruza metade da distância");
  check(target(1, 3, -16, 30) == 0, "arraste para trás funciona");
  check(target(1, 3, 100000, 30) == 2 && target(1, 3, -100000, 30) == 0, "viagem limitada às extremidades");
  check(target(1, 3, 10, 0) == 1 && target(1, 0, 10, 30) == 1, "layout sem tamanho permanece seguro");
  check(target(1, 3, std::numeric_limits<float>::infinity(), 30) == 1, "coordenada não finita é ignorada");
  check(target(1, 3, 32, 60) == target(1, 3, 16, 30), "escala do monitor preserva o alvo");
  const auto ids = keys({"app", "app", "other"});
  check(ids == List{"3:app:0", "3:app:1", "5:other:0"}, "janelas do mesmo app recebem slots distintos");
  check(keys({"app"}, {"3:app:1"}) == List{"3:app:1"}, "fechar outra janela preserva identidade restante");
  check(keys({"app", "app"}, {"", "3:app:0"}) == List{"3:app:1", "3:app:0"}, "janela nova não colide com slot retido");
  check(keys({"new"}, {"3:old:0"}) == List{"3:new:0"}, "identidade anterior de outro aplicativo não é reutilizada");
  check(keys({"", ""}) == List{"0::0", "0::1"}, "janelas sem app id também são distintas");
  check(keys({"a:1", "a"}) == List{"3:a:1:0", "1:a:0"}, "separadores no app id não causam colisão");
  check(merge({}, order) == order, "primeiro arraste cria preferência persistente");
  check(merge({"brave", "closed", "codex"}, {"codex", "brave"}) == List{"codex", "closed", "brave"}, "app fechado ou em outro monitor mantém slot");
  check(merge({"brave", "brave", "closed"}, {"brave", "codex"}) == List{"brave", "closed", "codex"}, "preferência duplicada é normalizada");
  check(sorted({"new1", "brave", "new2", "codex"}, {"codex", "closed", "brave"}) == List{"codex", "brave", "new1", "new2"}, "apps novos entram ao final em ordem estável");
  check(sorted({"brave", "codex"}, {"codex", "brave"}) == List{"codex", "brave"}, "modelo reconstruído reaplica preferência");
  List permutation{"a", "b", "c", "d"};
  bool all = true;
  do {
    const auto saved = merge({"a", "hidden1", "b", "hidden2", "c"}, permutation);
    all = all && sorted({"a", "b", "c", "d"}, saved) == permutation;
    all = all && std::count(saved.begin(), saved.end(), "hidden1") == 1;
    all = all && std::count(saved.begin(), saved.end(), "hidden2") == 1;
  } while (std::next_permutation(permutation.begin(), permutation.end()));
  check(all, "24 permutações mantêm ordem visível e apps ausentes");
  std::cout << count << " cenários passaram. Nenhuma janela real foi manipulada.\n";
}
