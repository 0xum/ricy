#!/usr/bin/env python3
"""Execute the actual effect JS in QJSEngine; does not manipulate session windows."""
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
    ('minimize contracts from 1 to 0.85 and fades from 1 to 0', 'ricyWindowActions.slotWindowMinimized(window);latest().animations[0].type===Effect.Scale && latest().animations[0].from===1 && latest().animations[0].to===0.85 && latest().animations[1].from===1 && latest().animations[1].to===0'),
    ('restore expands from 0.85 to 1 and fades in from 0 to 1', 'ricyWindowActions.slotWindowUnminimized(window);latest().animations[0].from===0.85 && latest().animations[0].to===1 && latest().animations[1].from===0 && latest().animations[1].to===1'),
    ('different easing curves for entering and leaving', 'ricyWindowActions.slotWindowMinimized(window);var a=latest().curve;ricyWindowActions.abort(window);ricyWindowActions.slotWindowUnminimized(window);a===QEasingCurve.InCubic && latest().curve===QEasingCurve.OutCubic'),
    ('real geometry does not change and there is no translation', 'var original=JSON.stringify(window.geometry);ricyWindowActions.slotWindowUnminimized(window);JSON.stringify(window.geometry)===original && latest().animations.length===2'),
    ('animation also works without icon or monitor geometry', 'window.iconGeometry=null;window.screen=null;ricyWindowActions.slotWindowMinimized(window);configs.length===1'),
    ('Global speed preference is respected', 'factor=0.25;effect.configChanged.emit();ricyWindowActions.slotWindowMinimized(window);latest().duration===80'),
    ('duration and scale configuration is respected', 'config={Duration:480,Scale:0.9};effect.configChanged.emit();ricyWindowActions.slotWindowUnminimized(window);latest().duration===480 && latest().animations[0].from===0.9'),
    ('invalid duration returns to default', 'config={Duration:-5};effect.configChanged.emit();ricyWindowActions.duration===320'),
    ('scale is limited to the valid range', 'config={Scale:0.1};effect.configChanged.emit();var low=ricyWindowActions.scale;config.Scale=3;effect.configChanged.emit();low===0.5 && ricyWindowActions.scale===1'),
    ('Scale NaN uses default', 'config={Scale:"invalid"};effect.configChanged.emit();ricyWindowActions.scale===0.85'),
    ('an in-progress restore reverses without a jump', 'ricyWindowActions.slotWindowMinimized(window);var ids=window.ricyActionAnimation;ricyWindowActions.slotWindowUnminimized(window);configs.length===1 && redirects[0].direction===Effect.Backward && window.ricyActionAnimation===ids'),
    ('second reversal returns to initial direction', 'ricyWindowActions.slotWindowMinimized(window);ricyWindowActions.slotWindowUnminimized(window);ricyWindowActions.slotWindowMinimized(window);configs.length===1 && redirects[1].direction===Effect.Forward'),
    ('repeated event does not create parallel animation', 'ricyWindowActions.slotWindowUnminimized(window);ricyWindowActions.slotWindowUnminimized(window);configs.length===1 && redirects[0].direction===Effect.Forward'),
    ('reversal failure cancels and starts in the new direction', 'ricyWindowActions.slotWindowMinimized(window);redirectWorks=false;ricyWindowActions.slotWindowUnminimized(window);cancels.length===1 && configs.length===2 && latest().animations[0].from===0.85'),
    ('blur continues until both animation tracks finish', 'ricyWindowActions.slotWindowMinimized(window);var ids=window.ricyActionAnimation.slice();effect.animationEnded.emit(window,ids[0]);var held=lastRole()===true;effect.animationEnded.emit(window,ids[1]);held && lastRole()===null && !window.ricyActionAnimation'),
    ('end of another animation does not release blur', 'ricyWindowActions.slotWindowMinimized(window);effect.animationEnded.emit(window,999);lastRole()===true && window.ricyActionAnimation.length===2'),
    ('Replaced animation end is ignored', 'ricyWindowActions.slotWindowMinimized(window);var old=window.ricyActionAnimation.slice();redirectWorks=false;ricyWindowActions.slotWindowUnminimized(window);effect.animationEnded.emit(window,old[0]);effect.animationEnded.emit(window,old[1]);lastRole()===true && window.ricyActionAnimation.length===2'),
    ('closing cancels minimize/restore in progress', 'ricyWindowActions.slotWindowUnminimized(window);effects.windowClosed.emit(window);cancels.length===1 && !window.ricyActionAnimation && lastRole()===null'),
    ('blur from the closing Scale effect remains preserved', 'ricyWindowActions.slotWindowUnminimized(window);window.scaleOutAnimation=[10,11];effects.windowClosed.emit(window);cancels.length===1 && lastRole()===true'),
    ('existing normal window receives the minimization signal', 'window.minimized=true;window.minimizedChanged.emit();configs.length===1 && latest().animations[0].to===0.85'),
    ('new window receives restore signal', 'var added=w();effects.windowAdded.emit(added);added.minimizedChanged.emit();configs.length===1 && latest().window===added && latest().animations[0].to===1'),
    ('panels do not receive animation of applications', 'window.normalWindow=false;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
    ('windows outside the taskbar are ignored', 'window.skipTaskbar=true;ricyWindowActions.slotWindowUnminimized(window);configs.length===0'),
    ('full-screen effect retains priority', 'effects.hasActiveFullScreenEffect=true;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
    ('empty geometry does not leave forced blur enabled', 'window.geometry.width=0;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
    ('minimization does not keep a closed window alive', 'ricyWindowActions.slotWindowMinimized(window);latest().keepAlive===false'),
]
for label, check in cases:
    engine = QJSEngine()
    value = engine.evaluate(setup + '\n' + source)
    assert not value.isError(), value.toString()
    value = engine.evaluate(check)
    assert not value.isError() and value.toBool(), label + ': ' + value.toString()
    print('PASS: ' + label)

settings = runpy.run_path(str(base / 'apply-animations.py'))['settings']
assert settings[('Effect-scale', 'Duration')] == '320'
assert settings[('Effect-scale', 'InScale')] == settings[('Effect-scale', 'OutScale')] == '0.85'
assert settings[('Effect-ricywindowactions', 'Duration')] == '320'
assert settings[('Effect-ricywindowactions', 'Scale')] == '0.85'
assert settings[('Plugins', 'fadeEnabled')] == settings[('Plugins', 'squashEnabled')] == 'false'
assert ('KDE', 'AnimationDurationFactor') not in settings
print('PASS: installation coordinates the four states and preserves global speed')
xml = ET.parse(base / 'assets/kwin/effects/ricywindowactions/contents/config/main.xml')
entries = {item.attrib['name']: item for item in xml.iter() if item.tag.endswith('entry')}
assert set(entries) == {'Duration', 'Scale'}
metadata = json.loads((base / 'assets/kwin/effects/ricywindowactions/metadata.json').read_text())
assert metadata['KPlugin']['Id'] == 'ricywindowactions'
print('PASS: package maintains effect identity and configuration schema')
print(f'{len(cases)+2} scenarios passed; no real window was manipulated.')
