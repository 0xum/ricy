#!/usr/bin/env python3
"""Regressões dos validadores em cópia temporária; não altera a sessão."""
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
 result=run();check('raiz resolvida fora do cwd do projeto',result.returncode==0,result.stdout+result.stderr)
 for rel in ['AGENTS.md','docs/ARCHITECTURE.md','docs/adr/0001-single-workspace.md','.agents/skills/testing/SKILL.md','shell/AGENTS.md']:
  p=dst/rel;data=p.read_bytes();p.unlink();result=run();p.write_bytes(data)
  check('arquivo obrigatório ausente: '+rel,result.returncode==1 and rel in result.stdout,result.stdout)
 p=dst/'shell/AGENTS.md';data=p.read_text()
 p.write_text(data+'\n[quebrado](../docs/nao-existe.md)\n');r=run();p.write_text(data)
 check('link relativo quebrado detectado',r.returncode==1 and 'link quebrado' in r.stdout,r.stdout)
 p.write_text('# Shell\n\nLeia [raiz](../AGENTS.md).\n');r=run();p.write_text(data)
 check('AGENTS local sem referência a docs rejeitado',r.returncode==1 and 'falta referência' in r.stdout,r.stdout)
 p.write_text(data+'\n[referência sem destino][missing]\n');r=run();p.write_text(data)
 check('referência Markdown indefinida detectada',r.returncode==1 and 'referência indefinida' in r.stdout,r.stdout)
 p.write_text(data+'\n```md\n[exemplo](../nao-existe.md)\n```\n');r=run();p.write_text(data)
 check('links de exemplo em bloco de código ignorados',r.returncode==0,r.stdout)
 p=dst/'.agents/skills/testing/SKILL.md';data=p.read_text();p.write_text(data.replace('name: testing','name: wrong'));r=run();p.write_text(data)
 check('frontmatter inconsistente detectado',r.returncode==1 and 'frontmatter' in r.stdout,r.stdout)
 p=dst/'scripts/doctor';data=p.read_text();p.write_text(data+'\nsyntax broken !\n');r=run();p.write_text(data)
 check('sintaxe inválida em script detectada',r.returncode==1 and 'doctor' in r.stdout,r.stdout)
 p=dst/'scripts/doctor';p.chmod(0o644);r=run();p.chmod(0o755)
 check('script sem permissão executável rejeitado',r.returncode==1 and 'não executável' in r.stdout,r.stdout)
 r=run('invalid');check('alvo inválido retorna uso/exit 2',r.returncode==2 and 'Uso:' in r.stderr,r.stdout+r.stderr)
 env=dict(os.environ,XDG_CACHE_HOME=str(Path(tmp)/'empty-cache'))
 r=run('shell',env);check('fonte Noctalia ausente retorna NOT RUN/exit 2',r.returncode==2 and 'NOT RUN ações Noctalia' in r.stdout,r.stdout+r.stderr)
 p=dst/'ricy-kit/contributions/plasma-noctalia-switching/verificar.py';p.write_text('raise RuntimeError("intentional failure")\n')
 r=run('recovery');check('falha de componente propaga exit 1',r.returncode==1 and 'intentional failure' in r.stdout,r.stdout+r.stderr)
 empty=Path(tmp)/'empty-bin';empty.mkdir()
 env=dict(os.environ,PATH=str(empty));env.pop('XDG_SESSION_TYPE',None)
 r=subprocess.run([sys.executable,'-B',str(dst/'scripts/doctor')],cwd='/',env=env,text=True,capture_output=True)
 check('doctor sem ferramentas/ambiente informa UNKNOWN sem PASS',r.returncode==2 and 'UNKNOWN' in r.stdout and 'PASS' not in r.stdout,r.stdout+r.stderr)
print(f'{len(checks)} verificações comportamentais passaram em fixture descartável.')
