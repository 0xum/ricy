#!/usr/bin/env python3
"""Run real KDE adapter JS scripts in isolated scenarios without touching session windows."""
import argparse,json,re,os
from pathlib import Path
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtQml import QJSEngine

def script_source(source,method,uuid,app_id,title,warp=False,toggle=False):
 start=source.index('  void KwinActiveWindow::'+method+'(')
 match=re.search(r'R"js\(\n(.*?)\n\)js"',source[start:],re.S)
 if match is None: raise ValueError('Script not found: '+method)
 script=match.group(1).replace('{{','{').replace('}}','}')
 values=iter([json.dumps(uuid),json.dumps(app_id),json.dumps(title)]+(['true' if warp else 'false','true' if toggle else 'false'] if method=='activateWindow' else []))
 return re.sub(r'\{\}',lambda _:next(values),script)

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--fonte',type=Path,default=Path(os.environ.get('XDG_CACHE_HOME',Path.home()/'.cache'))/'ricy-noctalia-src-5.2.1')
 args=parser.parse_args();source=(args.fonte/'src/compositors/kde/kwin_active_window.cpp').read_text()
 app=QCoreApplication([])
 setup='''var windows = [
 {normalWindow:true,minimizable:true,internalId:"other",resourceClass:"app",caption:"same",minimized:true,closed:false,closeWindow:function(){this.closed=true;}},
 {normalWindow:true,minimizable:true,internalId:"target",resourceClass:"app",caption:"same",minimized:true,closed:false,closeWindow:function(){this.closed=true;}}
 ];
 var workspace={activeWindow:null,windowList:function(){return windows;}};
 var warpCalls=0;function callDBus(){warpCalls++;}
 '''
 cases=[
  ('restore UUID excludes same-caption window','activateWindow','target','',False,'workspace.activeWindow===windows[1] && !windows[1].minimized && windows[0].minimized'),
  ('restore by class/caption without UUID','activateWindow','','',False,'workspace.activeWindow===windows[0] && !windows[0].minimized && windows[1].minimized'),
  ('stale UUID does not activate another window','activateWindow','gone','',False,'workspace.activeWindow===null && windows[0].minimized && windows[1].minimized'),
  ('restore preserves requested pointer warp','activateWindow','target','',True,'workspace.activeWindow===windows[1] && !windows[1].minimized && warpCalls===1'),
  ('close UUID excludes same-caption window','closeWindow','target','',False,'windows[1].closed && !windows[0].closed'),
  ('close by class/caption without UUID','closeWindow','','',False,'windows[0].closed && !windows[1].closed'),
  ('stale UUID does not close another window','closeWindow','gone','',False,'!windows[0].closed && !windows[1].closed'),
  ('missing close API does not minimize instead','closeWindow','target','windows[1].minimized=false;delete windows[1].closeWindow;',False,'!windows[1].minimized && !windows[0].closed'),
  ('non-normal window is excluded','closeWindow','target','windows[1].normalWindow=false;',False,'!windows[1].closed && !windows[0].closed'),
  ('toggle focused window minimizes','activateWindow','target','windows[1].minimized=false;workspace.activeWindow=windows[1];',False,'windows[1].minimized && windows[0].minimized',True),
  ('toggle minimized window restores even if focus is stale','activateWindow','target','workspace.activeWindow=windows[1];',False,'!windows[1].minimized && workspace.activeWindow===windows[1]',True),
  ('toggle visible inactive window focuses','activateWindow','target','windows[1].minimized=false;windows[0].minimized=false;workspace.activeWindow=windows[0];',False,'!windows[1].minimized && workspace.activeWindow===windows[1] && !windows[0].minimized',True),
  ('toggle respects non-minimizable window','activateWindow','target','windows[1].minimized=false;windows[1].minimizable=false;workspace.activeWindow=windows[1];',False,'!windows[1].minimized && workspace.activeWindow===windows[1]',True),
  ('ordinary activation never minimizes','activateWindow','target','windows[1].minimized=false;workspace.activeWindow=windows[1];',False,'!windows[1].minimized && workspace.activeWindow===windows[1]',False),
  ('toggle stale UUID leaves focus untouched','activateWindow','gone','windows[0].minimized=false;workspace.activeWindow=windows[0];',False,'!windows[0].minimized && windows[1].minimized && workspace.activeWindow===windows[0]',True),
  ('toggle does not minimize another same-caption window','activateWindow','target','windows[0].minimized=false;workspace.activeWindow=windows[0];',False,'!windows[0].minimized && !windows[1].minimized && workspace.activeWindow===windows[1]',True),
  ('minimize does not warp pointer','activateWindow','target','windows[1].minimized=false;workspace.activeWindow=windows[1];',True,'windows[1].minimized && warpCalls===0',True),
 ]
 for case in cases:
  label,method,uuid,extra,warp,check=case[:6];toggle=case[6] if len(case)>6 else False
  engine=QJSEngine();value=engine.evaluate(setup+extra+'\n'+script_source(source,method,uuid,'app','same',warp,toggle))
  assert not value.isError(),(label,value.toString())
  result=engine.evaluate(check);assert not result.isError() and result.toBool(),label
  print('PASS: '+label)
 print(f'{len(cases)} scenarios have passed. No real window has been manipulated.')
if __name__=='__main__':main()
