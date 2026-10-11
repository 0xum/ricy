#!/usr/bin/env python3
"""Validate real KDE signals/serialization and KWin animation in an isolated JS engine."""
from pathlib import Path
import argparse,re,os
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtQml import QJSEngine

def evaluate(setup,source,check):
 engine=QJSEngine();engine.evaluate('Array.prototype.at=function(i){return this[i<0 ? this.length+i : i];};');v=engine.evaluate(setup+'\n'+source)
 assert not v.isError(),v.toString()
 v=engine.evaluate(check);assert not v.isError() and v.toBool(),v.toString()

def main():
 app=QCoreApplication([]);parser=argparse.ArgumentParser();parser.add_argument('--fonte',type=Path,default=Path(os.environ.get('XDG_CACHE_HOME',Path.home()/'.cache'))/'ricy-noctalia-src-5.2.1');args=parser.parse_args()
 cpp=(args.fonte/'src/compositors/kde/kwin_active_window.cpp').read_text();source=re.search(r'kScriptSource = R"js\(\n(.*?)\n\)js"',cpp,re.S).group(1)
 setup='''function signal(){return {callbacks:[],connect:function(cb){this.callbacks.push(cb);},emit:function(arg){for(const cb of this.callbacks)cb(arg);}};}
 var reports=[];function callDBus(bus,path,iface,method,...args){reports.push({method:method,args:args});}function print(){}
 function w(id){return {normalWindow:true,internalId:id,resourceClass:"app",caption:"Same",minimized:false,desktops:[{id:"desktop"}],output:{name:"DP-1"},minimizedChanged:signal(),captionChanged:signal(),desktopsChanged:signal(),outputChanged:signal()};}
 var windows=[w("a"),w("b")];var workspace={activeWindow:windows[0],windowList:function(){return windows;},windowActivated:signal(),windowAdded:signal(),windowRemoved:signal()};var virtualDesktopInfo={desktopIds:["desktop"]};
 function last(method){return reports.filter(r=>r.method===method).at(-1).args;}
 '''
 cases=[
 ('serialization includes minimized flag','last("notifyWindowList")[0].split("\\x1F")[0].split("\\x1e")[5]==="0"'),
 ('minimizedChanged sends new state and clears stale focus','windows[0].minimized=true;windows[0].minimizedChanged.emit();last("notifyWindowList")[0].split("\\x1F")[0].split("\\x1e")[5]==="1" && last("notifyActiveWindow")[2]===""'),
 ('restore event updates list and active UUID','windows[0].minimized=true;windows[0].minimizedChanged.emit();windows[0].minimized=false;windows[0].minimizedChanged.emit();last("notifyWindowList")[0].split("\\x1F")[0].split("\\x1e")[5]==="0" && last("notifyActiveWindow")[2]==="a"'),
 ('minimized active event cannot revive purple dot','windows[0].minimized=true;workspace.windowActivated.emit(windows[0]);last("notifyActiveWindow")[2]===""'),
 ('focus follows exact UUID despite equal title','workspace.activeWindow=windows[1];workspace.windowActivated.emit(windows[1]);last("notifyActiveWindow")[2]==="b"'),
 ('minimizing inactive window retains other focus','windows[1].minimized=true;windows[1].minimizedChanged.emit();last("notifyActiveWindow")[2]==="a"'),
 ('new window receives minimized signal wiring','var added=w("new");windows.push(added);workspace.windowAdded.emit(added);added.minimized=true;added.minimizedChanged.emit();last("notifyWindowList")[0].split("\\x1F").at(-1).split("\\x1e")[5]==="1"'),
 ]
 for label,check in cases:evaluate(setup,source,check);print('PASS: '+label)
 effect=(Path(__file__).parent/'assets/kwin/effects/ricywindowactions/contents/code/main.js').read_text()
 setup='''function signal(){return {connect:function(){}};}var Effect={Size:1,Translation:2,Opacity:3,WindowForceBlurRole:4,Backward:5,Forward:6};var QEasingCurve={InCubic:1,OutCubic:2};var configs=[];var cancels=0;var redirects=0;var doRedirect=true;var effects={hasActiveFullScreenEffect:false,stackingOrder:[],windowAdded:signal()};var effect={configChanged:signal(),animationEnded:signal()};function animationTime(ms){return ms;}function animate(config){configs.push(config);return [configs.length];}function cancel(){cancels++;}function redirect(){redirects++;return doRedirect;}var roles=[];var window={normalWindow:true,skipTaskbar:false,iconGeometry:{width:0,height:0},geometry:{x:2100,y:100,width:800,height:600},screen:{geometry:{x:1920,y:0,width:1920,height:1080}},setData:function(role,value){roles.push(value);}};
 '''
 effectsCases=[
 ('missing icon geometry animates on correct monitor','ricyWindowActions.slotWindowMinimized(window);configs.length===1 && configs[0].duration===240 && ricyIconRect(window).x>=1920 && ricyIconRect(window).y===1049'),
 ('native icon geometry is preferred','window.iconGeometry={x:1,y:2,width:30,height:30};ricyIconRect(window).x===1 && ricyIconRect(window).width===30'),
 ('restore reverses ongoing animation','ricyWindowActions.slotWindowMinimized(window);ricyWindowActions.slotWindowUnminimized(window);redirects===1 && configs.length===1'),
 ('failed reversal cancels then starts restore','ricyWindowActions.slotWindowMinimized(window);doRedirect=false;ricyWindowActions.slotWindowUnminimized(window);cancels===1 && configs.length===2 && configs[1].curve===QEasingCurve.OutCubic'),
 ('non-app windows are excluded','window.normalWindow=false;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
 ('full-screen effect suppresses animation','effects.hasActiveFullScreenEffect=true;ricyWindowActions.slotWindowMinimized(window);configs.length===0'),
 ('missing output does not leave forced blur','window.screen=null;ricyWindowActions.slotWindowMinimized(window);configs.length===0 && roles.length===0'),
 ('blur role released at completion','ricyWindowActions.slotWindowMinimized(window);ricyWindowActions.restoreForceBlurState(window);roles.at(-1)===null'),
 ]
 for label,check in effectsCases:evaluate(setup,effect,check);print('PASS: '+label)
 print(f'{len(cases)+len(effectsCases)} scenarios passed; no real windows.')
if __name__=='__main__':main()
