#!/usr/bin/env python3
"""Executa o JS real do efeito em QJSEngine; não manipula janelas da sessão."""
from pathlib import Path
import json
import runpy
import xml.etree.ElementTree as ET
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtQml import QJSEngine

base = Path(__file__).resolve().parent
app = QCoreApplication([])
source = (base / 'assets/kwin/effects/ricywindowactions/contents/code/main.js').read_text()
setup = '''
function signal() { return {callbacks:[], connect:function(cb){this.callbacks.push(cb);}, emit:function(...args){for(const cb of this.callbacks) cb(...args);}}; }
var Effect={Scale:1,Opacity:2,WindowForceBlurRole:3,Forward:4,Backward:5};
var QEasingCurve={InCubic:1,OutCubic:2};
var configs=[],cancels=[],redirects=[],roles=[],config={},nextId=1,redirectWorks=true,factor=1;
function animationTime(ms){return ms*factor;}
function animate(config){configs.push(config);return [nextId++,nextId++];}
function cancel(ids){cancels.push(ids);}
function redirect(ids,direction){redirects.push({ids:ids,direction:direction});return redirectWorks;}
var effect={configChanged:signal(),animationEnded:signal(),readConfig:function(key,fallback){return key in config?config[key]:fallback;}};
function w(){return {normalWindow:true,skipTaskbar:false,minimized:false,geometry:{x:2100,y:100,width:800,height:600},minimizedChanged:signal(),setData:function(role,value){roles.push({role:role,value:value});}};}
var window=w();
var effects={hasActiveFullScreenEffect:false,stackingOrder:[window],windowAdded:signal(),windowClosed:signal()};
function latest(){return configs[configs.length-1];}
function lastRole(){return roles[roles.length-1].value;}
'''
cases = [
    ('minimizar contrai 1→0,85 e esmaece 1→0', 'ricyWindowActions.slotWindowMinimized(window);latest().animations[0].type===Effect.Scale && latest().animations[0].from===1 && latest().animations[0].to===0.85 && latest().animations[1].from===1 && latest().animations[1].to===0'),
    ('restaurar expande 0,85→1 e aparece 0→1', 'ricyWindowActions.slotWindowUnminimized(window);latest().animations[0].from===0.85 && latest().animations[0].to===1 && latest().animations[1].from===0 && latest().animations[1].to===1'),
    ('curvas de entrada/saída distintas', 'ricyWindowActions.slotWindowMinimized(window);var a=latest().curve;ricyWindowActions.abort(window);ricyWindowActions.slotWindowUnminimized(window);a===QEasingCurve.InCubic && latest().curve===QEasingCurve.OutCubic'),
    ('geometria real não muda e não há translação', 'var original=JSON.stringify(window.geometry);ricyWindowActions.slotWindowUnminimized(window);JSON.stringify(window.geometry)===original && latest().animations.length===2'),
    ('sem geometria de ícone ou monitor também anima', 'window.iconGeometry=null;window.screen=null;ricyWindowActions.slotWindowMinimized(window);configs.length===1'),
    ('preferência global de velocidade é respeitada', 'factor=0.25;effect.configChanged.emit();ricyWindowActions.slotWindowMinimized(window);latest().duration===80'),
    ('configuração de duração e escala é respeitada', 'config={Duration:480,Scale:0.9};effect.configChanged.emit();ricyWindowActions.slotWindowUnminimized(window);latest().duration===480 && latest().animations[0].from===0.9'),
    ('duração inválida retorna ao padrão', 'config={Duration:-5};effect.configChanged.emit();ricyWindowActions.duration===320'),
    ('escala é limitada ao intervalo válido', 'config={Scale:0.1};effect.configChanged.emit();var low=ricyWindowActions.scale;config.Scale=3;effect.configChanged.emit();low===0.5 && ricyWindowActions.scale===1'),
    ('NaN em escala usa padrão', 'config={Scale:"invalid"};effect.configChanged.emit();ricyWindowActions.scale===0.85'),
    ('restaurar em curso reverte sem salto', 'ricyWindowActions.slotWindowMinimized(window);var ids=window.ricyActionAnimation;ricyWindowActions.slotWindowUnminimized(window);configs.length===1 && redirects[0].direction===Effect.Backward && window.ricyActionAnimation===ids'),
    ('segunda reversão retorna ao sentido inicial', 'ricyWindowActions.slotWindowMinimized(window);ricyWindowActions.slotWindowUnminimized(window);ricyWindowActions.slotWindowMinimized(window);configs.length===1 && redirects[1].direction===Effect.Forward'),
    ('evento repetido não cria animação paralela', 'ricyWindowActions.slotWindowUnminimized(window);ricyWindowActions.slotWindowUnminimized(window);configs.length===1 && redirects[0].direction===Effect.Forward'),
    ('falha ao reverter cancela e inicia novo sentido', 'ricyWindowActions.slotWindowMinimized(window);redirectWorks=false;ricyWindowActions.slotWindowUnminimized(window);cancels.length===1 && configs.length===2 && latest().animations[0].from===0.85'),
    ('blur continua até as duas trilhas terminarem', 'ricyWindowActions.slotWindowMinimized(window);var ids=window.ricyActionAnimation.slice();effect.animationEnded.emit(window,ids[0]);var held=lastRole()===true;effect.animationEnded.emit(window,ids[1]);held && lastRole()===null && !window.ricyActionAnimation'),
    ('fim de outra animação não libera blur', 'ricyWindowActions.slotWindowMinimized(window);effect.animationEnded.emit(window,999);lastRole()===true && window.ricyActionAnimation.length===2'),
    ('fim de animação substituída é ignorado', 'ricyWindowActions.slotWindowMinimized(window);var old=window.ricyActionAnimation.slice();redirectWorks=false;ricyWindowActions.slotWindowUnminimized(window);effect.animationEnded.emit(window,old[0]);effect.animationEnded.emit(window,old[1]);lastRole()===true && window.ricyActionAnimation.length===2'),
    ('fechamento cancela minimizar/restaurar em curso', 'ricyWindowActions.slotWindowUnminimized(window);effects.windowClosed.emit(window);cancels.length===1 && !window.ricyActionAnimation && lastRole()===null'),
    ('blur do Scale de fechamento permanece preservado', 'ricyWindowActions.slotWindowUnminimized(window);window.scaleOutAnimation=[10,11];effects.windowClosed.emit(window);cancels.length===1 && lastRole()===true'),
    ('janela comum existente recebe sinal de minimização', 'window.minimized=true;window.minimizedChanged.emit();configs.length===1 && latest().animations[0].to===0.85'),
    ('janela nova recebe sinal de restauração', 'var added=w();effects.windowAdded.emit(added);added.minimizedChanged.emit();configs.length===1 && latest().window===added && latest().animations[0].to===1'),
    ('painéis não recebem animação de aplicativos', 'window.normalWindow=false;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
    ('janelas fora da taskbar são ignoradas', 'window.skipTaskbar=true;ricyWindowActions.slotWindowUnminimized(window);configs.length===0'),
    ('efeito de tela cheia mantém prioridade', 'effects.hasActiveFullScreenEffect=true;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
    ('geometria vazia não deixa blur forçado', 'window.geometry.width=0;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
    ('minimização não mantém janela fechada viva', 'ricyWindowActions.slotWindowMinimized(window);latest().keepAlive===false'),
]
for label, check in cases:
    engine = QJSEngine()
    value = engine.evaluate(setup + '\n' + source)
    assert not value.isError(), value.toString()
    value = engine.evaluate(check)
    assert not value.isError() and value.toBool(), label + ': ' + value.toString()
    print('PASS: ' + label)

settings = runpy.run_path(str(base / 'aplicar-animacoes.py'))['settings']
assert settings[('Effect-scale', 'Duration')] == '320'
assert settings[('Effect-scale', 'InScale')] == settings[('Effect-scale', 'OutScale')] == '0.85'
assert settings[('Effect-ricywindowactions', 'Duration')] == '320'
assert settings[('Effect-ricywindowactions', 'Scale')] == '0.85'
assert settings[('Plugins', 'fadeEnabled')] == settings[('Plugins', 'squashEnabled')] == 'false'
assert ('KDE', 'AnimationDurationFactor') not in settings
print('PASS: instalação coordena os quatro estados e preserva velocidade global')
xml = ET.parse(base / 'assets/kwin/effects/ricywindowactions/contents/config/main.xml')
entries = {item.attrib['name']: item for item in xml.iter() if item.tag.endswith('entry')}
assert set(entries) == {'Duration', 'Scale'}
metadata = json.loads((base / 'assets/kwin/effects/ricywindowactions/metadata.json').read_text())
assert metadata['KPlugin']['Id'] == 'ricywindowactions'
print('PASS: pacote mantém identidade do efeito e schema de configuração')
print(f'{len(cases)+2} cenários passaram; nenhuma janela real foi manipulada.')
