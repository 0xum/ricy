"""Local package conversion. Never installs a foreign package with dpkg/rpm."""
import fcntl
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import tarfile
import tempfile

CACHE = Path.home() / '.cache/cachyos-package-installer'


def command_env():
    return {**os.environ, 'LC_ALL': 'C', 'SHELL': '/usr/bin/bash', 'TERM': 'dumb'}


def run(args, cwd, log, capture=False):
    log('Executando: ' + Path(args[0]).name)
    if capture:
        proc = subprocess.run(args, cwd=cwd, stdin=subprocess.DEVNULL,
                              capture_output=True, text=True, errors='replace',
                              env=command_env())
        for line in (proc.stdout + proc.stderr).splitlines():
            log(line)
        if proc.returncode:
            raise RuntimeError('Falha em ' + Path(args[0]).name + '. Consulte os detalhes abaixo.')
        return proc.stdout
    with subprocess.Popen(args, cwd=cwd, stdin=subprocess.DEVNULL,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True, errors='replace', env=command_env()) as proc:
        output = []
        for line in proc.stdout:
            output.append(line)
            log(re.sub(r'\x1b(?:\[[0-?]*[ -/]*[@-~]|\([A-Z])', '', line).rstrip())
        if proc.wait():
            raise RuntimeError('Falha em ' + Path(args[0]).name + '. Consulte os detalhes abaixo.')
    return ''.join(output) if capture else None


def rpm_to_deb(source, work, log):
    database = work / 'rpmdb'
    database.mkdir()
    run(['/usr/bin/rpm', '--dbpath', str(database), '--initdb'], work, log)
    rpm = ['/usr/bin/rpm', '--dbpath', str(database)]
    query = lambda fmt: run(rpm + ['-qp', '--qf', fmt, str(source)], work, log, True)
    name, version, release, arch = query('%{NAME}\n%{VERSION}\n%{RELEASE}\n%{ARCH}').splitlines()
    if arch not in {platform.machine(), 'noarch'}:
        raise RuntimeError(f'Arquitetura RPM incompatível: {arch}.')
    if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9+._-]*', name):
        raise RuntimeError('Nome de pacote RPM inválido.')
    scripts = run(rpm + ['-qp', '--scripts', str(source)], work, log, True)
    triggers = run(rpm + ['-qp', '--triggers', str(source)], work, log, True)
    filetriggers = run(rpm + ['-qp', '--filetriggers', str(source)], work, log, True)
    if scripts.strip() or triggers.strip() or filetriggers.strip():
        raise RuntimeError('Este RPM contém scripts de instalação ou gatilhos que precisam de '
                           'adaptação para o CachyOS. A conversão automática não os ignora. '
                           'Procure a versão deste programa nos repositórios/AUR ou use um .deb.')
    payload = work / 'payload.tar.gz'
    log('Extraindo conteúdo do RPM…')
    with payload.open('wb') as stream:
        proc = subprocess.run(['/usr/bin/rpm2archive', str(source)], cwd=work,
                              stdout=stream, stderr=subprocess.PIPE)
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode(errors='replace'))
    root = work / 'deb-root'
    root.mkdir()
    with tarfile.open(payload) as archive:
        # Python's data filter blocks traversal, devices and escaping links.
        archive.extractall(root, filter='data')
    if (root / 'DEBIAN').exists():
        raise RuntimeError('O RPM contém um diretório de controle inesperado.')
    control = root / 'DEBIAN'
    control.mkdir()
    summary = query('%{SUMMARY}').replace('\n', ' ').strip()
    homepage = query('%{URL}').replace('\n', '').strip()
    requires = query('[%{REQUIRENAME}\n]').splitlines()
    deps = set()
    for dep in requires:
        if dep.startswith(('rpmlib(', 'config(')):
            continue
        if '.so' in dep:
            # Debtap also scans ELF objects and resolves shared-library providers.
            continue
        if dep.startswith('/'):
            owners = subprocess.run(['/usr/bin/pkgfile', '-b', Path(dep).name],
                                    text=True, capture_output=True).stdout.splitlines()
            choices = {line.rsplit('/', 1)[-1] for line in owners if '/' in line}
            installed = [p for p in sorted(choices) if subprocess.run(
                ['/usr/bin/pacman', '-Q', p], stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL).returncode == 0]
            if len(installed) == 1:
                deps.add(installed[0])
            elif len(choices) == 1:
                deps.update(choices)
            else:
                raise RuntimeError(f'Não foi possível identificar a dependência RPM {dep}.')
        elif re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9+._-]*', dep):
            deps.add(dep.lower())
        else:
            raise RuntimeError(f'A dependência RPM {dep} exige adaptação manual.')
    deb_arch = {'x86_64': 'amd64', 'aarch64': 'arm64', 'noarch': 'all'}[arch]
    deb_version = re.sub(r'[^a-zA-Z0-9.+~]', '.', version + '-' + release)
    if not deb_version[0].isdigit():
        deb_version = '0.' + deb_version
    content = (f'Package: {name.lower().replace("_", "-")}\nVersion: {deb_version}\n'
               f'Architecture: {deb_arch}\nMaintainer: Local conversion <local@localhost>\n'
               f'Description: {summary or name}\n')
    if homepage and homepage != '(none)':
        content += f'Homepage: {homepage}\n'
    if deps:
        content += 'Depends: ' + ', '.join(sorted(deps)) + '\n'
    (control / 'control').write_text(content)
    result = work / 'input.deb'
    run(['/usr/bin/dpkg-deb', '--root-owner-group', '--build', str(root), str(result)], work, log)
    return result


def prepare(filename, log=print):
    source = Path(filename).resolve(strict=True)
    if not source.is_file() or source.suffix.lower() not in {'.deb', '.rpm'}:
        raise RuntimeError('Selecione um arquivo .deb ou .rpm local.')
    CACHE.mkdir(parents=True, exist_ok=True, mode=0o700)
    with (CACHE / 'conversion.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('Outro pacote está sendo convertido. Aguarde a conclusão.')
        work = Path(tempfile.mkdtemp(prefix='conversion-', dir=CACHE))
        log('Arquivos e registro da conversão: ' + str(work))
        copied = work / ('input' + source.suffix.lower())
        shutil.copyfile(source, copied)
        deb = rpm_to_deb(copied, work, log) if copied.suffix == '.rpm' else copied
        run(['/usr/bin/dpkg-deb', '--info', str(deb)], work, log)
        output = work / 'output'
        output.mkdir()
        converter = str(Path(__file__).with_name('debtap'))
        run([converter, '-Q', '-o', str(output), str(deb)], work, log)
        packages = list(output.glob('*.pkg.tar.*'))
        if len(packages) != 1:
            raise RuntimeError('O conversor não gerou um único pacote válido.')
        package = packages[0]
        info = run(['/usr/bin/pacman', '-Qip', str(package)], work, log, True)
        # Fail before the Install button if pacman cannot resolve the transaction.
        run(['/usr/bin/pacman', '-Up', '--print-format', '%n %v', str(package)], work, log)
        return str(package), info


def install(package, log):
    run(['/usr/bin/pkexec', '/usr/bin/pacman', '-U', '--noconfirm', package], Path(package).parent, log)
