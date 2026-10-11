#include "shell/bar/widgets/taskbar_icon_motion.h"
#include "render/animation/animation_manager.h"
#include "render/animation/motion_service.h"

#include <array>
#include <cassert>
#include <iostream>

using namespace taskbar_icon_motion;

bool near(float a, float b) { return std::abs(a - b) < 0.0001F; }
bool equal(Frame a, Frame b) {
  return near(a.scaleX, b.scaleX) && near(a.scaleY, b.scaleY) && near(a.opacity, b.opacity) && near(a.lift, b.lift);
}
int main() {
  int count = 0;
  auto passed = [&](const char* label) { ++count; std::cout << "PASS: " << label << '\n'; };
  const State idle{false,false,false}, active{true,true,false}, background{true,false,false}, minimized{true,false,true};
  assert(transition(idle, active) == Action::Launch); passed("abrir identifica launch");
  assert(transition(background, active) == Action::Focus); passed("foco identifica pulso");
  assert(transition(minimized, active) == Action::Restore); passed("restauração tem prioridade sobre foco");
  assert(transition(active, minimized) == Action::Minimize); passed("minimização tem prioridade sobre perda de foco");
  assert(transition(active, background) == Action::Background); passed("segundo plano tem resposta própria");
  assert(transition(active, idle) == Action::Close); passed("fechar tem prioridade sobre perda de foco");
  for (const State state : {idle,active,background,minimized}) assert(transition(state,state)==Action::None);
  passed("estado estável não repete animação");
  assert(transition(minimized,background)==Action::Restore); passed("restaurar sem foco também faz bounce");
  assert(transition(idle,idle)==Action::None); passed("fixado ocioso permanece parado");
  const std::array actions{Action::Launch,Action::Focus,Action::Restore,Action::Minimize,Action::Background,Action::Close};
  for (Action action : actions) {
    assert(duration(action)>0.0F);
    assert(equal(sample(action,0.0F),Frame{})); assert(equal(sample(action,1.0F),Frame{}));
    for (int i=0;i<=1000;++i) {
      const Frame f=sample(action,static_cast<float>(i)/1000.0F);
      assert(std::isfinite(f.scaleX) && std::isfinite(f.scaleY) && std::isfinite(f.opacity) && std::isfinite(f.lift));
      assert(f.scaleX>=0.80F && f.scaleX<=1.11F && f.scaleY>=0.80F && f.scaleY<=1.11F);
      assert(f.opacity>=0.59F && f.opacity<=1.0F && std::abs(f.lift)<=4.0F);
    }
  }
  passed("todas as animações são finitas e voltam ao repouso");
  assert(sample(Action::Focus,0.5F).scaleX>1.0F && near(sample(Action::Focus,0.5F).lift,0.0F));
  passed("foco pulsa sem deslocar");
  assert(sample(Action::Restore,0.25F).lift>sample(Action::Restore,0.75F).lift && sample(Action::Restore,0.75F).lift>0.0F);
  passed("bounce tem dois saltos amortecidos");
  const Frame squash=sample(Action::Minimize,0.5F);assert(squash.scaleX>1.0F && squash.scaleY<1.0F && squash.lift<0.0F);
  passed("minimizar comprime e desloca para a barra");
  assert(sample(Action::Close,0.5F).scaleX<sample(Action::Background,0.5F).scaleX && sample(Action::Close,0.5F).opacity<sample(Action::Background,0.5F).opacity);
  passed("fechar difere de segundo plano");
  const Frame interrupted=sample(Action::Restore,0.23F);
  assert(equal(sample(Action::Minimize,0.0F,interrupted),interrupted));assert(equal(sample(Action::Minimize,1.0F,interrupted),Frame{}));
  passed("interrupção mantém continuidade e termina neutra");
  assert(equal(sample(Action::Focus,-1.0F),Frame{}) && equal(sample(Action::Focus,2.0F),Frame{}));
  passed("progresso fora do intervalo é limitado");
  auto& motion=MotionService::instance();motion.setEnabled(true);motion.setSpeed(1.0F);
  AnimationManager manager;int ownerA=0,ownerB=0,callsA=0,callsB=0;
  manager.animate(0,1,300,Easing::Linear,[&](float){++callsA;},{},&ownerA);
  manager.animate(0,1,300,Easing::Linear,[&](float){++callsB;},{},&ownerB);
  manager.cancelForOwner(&ownerA);manager.tick(0);assert(callsA==0 && callsB==1 && manager.hasActive());
  passed("cancelar um ícone preserva outro");
  manager.cancelForOwner(&ownerB);assert(!manager.hasActive());passed("cancelamento libera animações do proprietário");
  Frame disabled;motion.setEnabled(false);
  manager.animate(0,1,duration(Action::Restore),Easing::Linear,[&](float p){disabled=sample(Action::Restore,p);},{},&ownerA);
  assert(equal(disabled,Frame{}) && !manager.hasActive());passed("movimento desabilitado termina sem bounce");
  motion.setEnabled(true);Frame reduced;
  manager.animate(0,1,duration(Action::Focus),Easing::Linear,[&](float p){reduced=sample(Action::Focus,p);},{},&ownerA);
  motion.setEnabled(false);assert(equal(reduced,Frame{}));manager.tick(0);assert(!manager.hasActive());
  passed("desabilitar movimento em curso restaura repouso");
  std::cout << count << " cenários passaram. Nenhuma janela real foi manipulada.\n";
}
