#!/usr/bin/env python3
"""Regressions of validators in temporary copy; does not change session."""
from pathlib import Path
import json,os,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(label,condition,detail=''):
 if not condition: raise AssertionError(label+'\n'+detail)
 checks.append(label);print('PASS '+label)
with tempfile.TemporaryDirectory(prefix='ricy-foundation-') as tmp:
 dst=Path(tmp)/'fixture'
 shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('work','outputs','assets','archives','__pycache__','.git','*.tar.gz','*.zip'))
 # Link validation needs the archive path, never its private contents.
 if (ROOT/'archives/ricy.zip').is_file():
  (dst/'archives').mkdir();(dst/'archives/ricy.zip').touch()
 def run(scope='architecture',env=None):
  return subprocess.run([sys.executable,'-B',str(dst/'scripts/verify'),scope],cwd='/',env=env,text=True,capture_output=True)
 result=run();check('root resolved outside the project working directory',result.returncode==0,result.stdout+result.stderr)
 for rel in ['AGENTS.md','docs/ARCHITECTURE.md','docs/adr/0001-single-workspace.md','.agents/skills/testing/SKILL.md','shell/AGENTS.md']:
  p=dst/rel;data=p.read_bytes();p.unlink();result=run();p.write_bytes(data)
  check('mandatory file missing: '+rel,result.returncode==1 and rel in result.stdout,result.stdout)
 p=dst/'shell/AGENTS.md';data=p.read_text()
 p.write_text(data+'\n[broken](../docs/does-not-exist.md)\n');r=run();p.write_text(data)
 check('broken relative link detected',r.returncode==1 and 'broken link' in r.stdout,r.stdout)
 p.write_text('# Shell\n\nRead [root](../AGENTS.md).\n');r=run();p.write_text(data)
 check('local AGENTS without a documentation reference rejected',r.returncode==1 and 'missing reference' in r.stdout,r.stdout)
 p.write_text(data+'\n[no destination reference][missing]\n');r=run();p.write_text(data)
 check('Markdown undefined reference detected',r.returncode==1 and 'undefined reference' in r.stdout,r.stdout)
 p.write_text(data+'\n```md\n[example](../does-not-exist.md)\n```\n');r=run();p.write_text(data)
 check('example links in ignored code block',r.returncode==0,r.stdout)
 p=dst/'.agents/skills/testing/SKILL.md';data=p.read_text();p.write_text(data.replace('name: testing','name: wrong'));r=run();p.write_text(data)
 check('inconsistent frontmatter detected',r.returncode==1 and 'frontmatter' in r.stdout,r.stdout)
 p=dst/'scripts/doctor';data=p.read_text();p.write_text(data+'\nsyntax broken !\n');r=run();p.write_text(data)
 check('invalid syntax in detected script',r.returncode==1 and 'doctor' in r.stdout,r.stdout)
 p=dst/'scripts/doctor';p.chmod(0o644);r=run();p.chmod(0o755)
 check('script without executable permission rejected',r.returncode==1 and 'not executable' in r.stdout,r.stdout)
 r=run('invalid');check('invalid target returns usage/exit 2',r.returncode==2 and 'Usage:' in r.stderr,r.stdout+r.stderr)
 env=dict(os.environ,XDG_CACHE_HOME=str(Path(tmp)/'empty-cache'))
 env.pop('RICY_NOCTALIA_SOURCE',None)
 r=run('shell',env);check('missing Noctalia source returns NOT RUN/exit 2',r.returncode==2 and 'NOT RUN Noctalia actions' in r.stdout,r.stdout+r.stderr)
 selection=subprocess.run([sys.executable,'-B','-c',
  'import json,runpy; m=runpy.run_path('+repr(str(dst/'scripts/verify'))+'); '
  'print(json.dumps([str(p.relative_to(m["ROOT"])) for p in m["source_files"]()]))'],
  text=True,capture_output=True,check=True)
 selected=set(json.loads(selection.stdout))
 historical=('notification-continuity','taskbar-menu-composition','tray-menu-composition',
  'app-icon-interactions','taskbar-app-actions','app-indicator-animations','app-icon-states')
 retained=['notification-continuity/enable.py','notification-continuity/sync-wallpaper.py',
  'app-icon-reordering/build.sh','plasma-noctalia-switching/ricy','blur-continuity/start.py']
 check('normal source selection retains mixed-role, recovery and UNKNOWN consumers',
  all('ricy-kit/contributions/'+p in selected for p in retained))
 check('normal source selection excludes historical builders, effect installer and root generators',
  not any('ricy-kit/contributions/'+name+'/build.sh' in selected for name in historical)
  and 'ricy-kit/contributions/app-icon-reordering/apply-animations.py' not in selected
  and 'ricy-kit/prepare-environment.py' not in selected
  and 'ricy-kit/generate-kvantum-variant.py' not in selected)
 for name in historical[1:]:
  check('historical folder excluded: '+name,
   not any(p.startswith('ricy-kit/contributions/'+name+'/') for p in selected))
 # Replace only the build body in the disposable fixture with a sentinel. Even a
 # broken guard cannot clone, patch, build, or touch the real installation here.
 build_env=dict(os.environ,XDG_CACHE_HOME=str(Path(tmp)/'cache'))
 build_env.pop('RICY_NOCTALIA_SOURCE',None);build_env.pop('RICY_BUILD_HISTORICAL',None)
 cache=Path(build_env['XDG_CACHE_HOME'])/'ricy-noctalia-src-5.2.1'
 alias=Path(tmp)/'cache-alias';alias.symlink_to(cache,target_is_directory=True)
 repo_alias=Path(tmp)/'repository-alias';repo_alias.symlink_to(dst,target_is_directory=True)
 isolated=Path(tmp)/'isolated-history'
 for name in historical:
  p=dst/'ricy-kit/contributions'/name/'build.sh';data=p.read_text()
  p.write_text(data.split('commit=',1)[0]+'echo isolated-build-body\nexit 73\n')
  trials=[{}, {'RICY_NOCTALIA_SOURCE':str(isolated)}, {'RICY_BUILD_HISTORICAL':'1'},
   {'RICY_BUILD_HISTORICAL':'1','RICY_NOCTALIA_SOURCE':'relative-source'}]
  trials += [dict(RICY_BUILD_HISTORICAL='1',RICY_NOCTALIA_SOURCE=str(source))
   for source in (dst/'ricy-kit/work/history',repo_alias/'history',cache,cache/'nested',alias,
    Path.home()/'.cache/ricy-noctalia-src-5.2.1')]
  for extra in trials:
   r=subprocess.run(['bash',str(p)],env=dict(build_env,**extra),text=True,capture_output=True)
   assert r.returncode==2 and 'HISTORICAL' in r.stderr and 'isolated-build-body' not in r.stdout, (name,extra,r.stdout,r.stderr)
  r=subprocess.run(['bash',str(p)],env=dict(build_env,RICY_BUILD_HISTORICAL='1',
   RICY_NOCTALIA_SOURCE=str(isolated)),text=True,capture_output=True)
  check(name+': opt-in/isolation guards reject unsafe paths and admit isolated reproduction',
   r.returncode==73 and r.stdout.strip()=='isolated-build-body',r.stdout+r.stderr)
  p.write_text(data)
 check('historical guard tests create no source/cache checkout',not isolated.exists() and not cache.exists())
 p=dst/'ricy-kit/contributions/plasma-noctalia-switching/verify.py';p.write_text('raise RuntimeError("intentional failure")\n')
 r=run('recovery');check('component failure propagates exit 1',r.returncode==1 and 'intentional failure' in r.stdout,r.stdout+r.stderr)
 empty=Path(tmp)/'empty-bin';empty.mkdir()
 env=dict(os.environ,PATH=str(empty));env.pop('XDG_SESSION_TYPE',None)
 r=subprocess.run([sys.executable,'-B',str(dst/'scripts/doctor')],cwd='/',env=env,text=True,capture_output=True)
 check('doctor without tools/environment reports UNKNOWN without PASS',r.returncode==2 and 'UNKNOWN' in r.stdout and 'PASS' not in r.stdout,r.stdout+r.stderr)
print(f'{len(checks)} behavioral checks passed in disposable fixture.')
