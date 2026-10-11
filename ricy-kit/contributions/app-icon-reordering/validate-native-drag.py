from pathlib import Path
import json, shlex, subprocess, tempfile, os
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--fonte',type=Path,default=Path(os.environ.get('XDG_CACHE_HOME',Path.home()/'.cache'))/'ricy-noctalia-src-5.2.1')
root=parser.parse_args().fonte;build=root/'build-ricy'
entry=next(x for x in json.loads((build/'compile_commands.json').read_text()) if x['file'].endswith('/taskbar_widget.cpp'))
args=shlex.split(entry['command']);args=args[:args.index('-MD')]
ninja=(build/'build.ninja').read_text().splitlines();index=next(i for i,l in enumerate(ninja) if l.startswith('build noctalia: '))
objects=shlex.split(ninja[index].split('cpp_LINKER_RSP ',1)[1].split(' | ',1)[0]);objects=[x for x in objects if x!='noctalia.p/src_main.cpp.o']
link=shlex.split(ninja[index+1].split(' = ',1)[1])
with tempfile.TemporaryDirectory(prefix='ricy-arraste-native-') as temporary:
 temp=Path(temporary);binary=temp/'test';obj=temp/'test.o'
 subprocess.run(args+['-std=c++23','-c',str(Path(__file__).with_suffix('.cpp')),'-o',str(obj)],cwd=build,check=True)
 subprocess.run(['c++','-o',str(binary),str(obj),*objects,*link],cwd=build,check=True)
 env=os.environ.copy();env['NOCTALIA_CONFIG_HOME']=str(temp/'config');env['NOCTALIA_STATE_HOME']=str(temp/'state');env['NOCTALIA_CACHE_HOME']=str(temp/'cache');env['XDG_CACHE_HOME']=str(temp/'cache');env['XDG_CONFIG_HOME']=str(temp/'config');env['XDG_STATE_HOME']=str(temp/'state');env['XDG_CURRENT_DESKTOP']='unknown';env['WAYLAND_DISPLAY']='ricy-test-unconnected'
 (temp/'config/noctalia').mkdir(parents=True);(temp/'config/noctalia/config.toml').write_text('[shell]\nsetup_wizard_enabled = false\n[widget.taskbar]\napp_order = []\n')
 subprocess.run([str(binary)],env=env,check=True)
