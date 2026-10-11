#!/usr/bin/env python3
"""Regressions of validators in temporary copy; does not change session."""
from pathlib import Path
import os,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(label,condition,detail=''):
 if not condition: raise AssertionError(label+'\n'+detail)
 checks.append(label);print('PASS '+label)
with tempfile.TemporaryDirectory(prefix='ricy-foundation-') as tmp:
 dst=Path(tmp)/'fixture'
 shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('work','outputs','assets','archives','__pycache__','.git','*.patch','*.tar.gz','*.zip'))
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
 r=run('shell',env);check('missing Noctalia source returns NOT RUN/exit 2',r.returncode==2 and 'NOT RUN Noctalia actions' in r.stdout,r.stdout+r.stderr)
 p=dst/'ricy-kit/contributions/plasma-noctalia-switching/verify.py';p.write_text('raise RuntimeError("intentional failure")\n')
 r=run('recovery');check('component failure propagates exit 1',r.returncode==1 and 'intentional failure' in r.stdout,r.stdout+r.stderr)
 empty=Path(tmp)/'empty-bin';empty.mkdir()
 env=dict(os.environ,PATH=str(empty));env.pop('XDG_SESSION_TYPE',None)
 r=subprocess.run([sys.executable,'-B',str(dst/'scripts/doctor')],cwd='/',env=env,text=True,capture_output=True)
 check('doctor without tools/environment reports UNKNOWN without PASS',r.returncode==2 and 'UNKNOWN' in r.stdout and 'PASS' not in r.stdout,r.stdout+r.stderr)
print(f'{len(checks)} behavioral checks passed in disposable fixture.')
