"""Normalize Debian control text before Debtap's line-based parser."""
from pathlib import Path
import re
import subprocess
import sys


def normalize(text):
    folded = {'depends', 'pre-depends', 'recommends', 'suggests', 'conflicts',
              'breaks', 'replaces', 'provides', 'enhances'}
    lines = []
    field = ''
    for line in text.replace('\r\n', '\n').replace('\r', '\n').splitlines():
        if line.startswith((' ', '\t')) and field in folded:
            lines[-1] += ' ' + line.strip()
        else:
            lines.append(line)
            if line and not line.startswith((' ', '\t')):
                field = line.partition(':')[0].lower()
    return '\n'.join(lines) + '\n'


SONAMES = {
    'libc6': 'libc.so.6', 'libgcc1': 'libgcc_s.so.1', 'libgcc-s1': 'libgcc_s.so.1',
    'libstdc++6': 'libstdc++.so.6', 'libudev1': 'libudev.so.1',
    'libssl1.0.0': 'libssl.so.1.0.0', 'libssl1.1': 'libssl.so.1.1',
    'libssl3': 'libssl.so.3', 'libssl3t64': 'libssl.so.3',
    'libx11-6': 'libX11.so.6', 'libxcursor1': 'libXcursor.so.1',
    'libxi6': 'libXi.so.6', 'libsm6': 'libSM.so.6',
    'libgl1-mesa-glx': 'libGL.so.1', 'libgl1': 'libGL.so.1',
    'libasound2': 'libasound.so.2', 'libasound2t64': 'libasound.so.2',
    'libjpeg8': 'libjpeg.so.8', 'libpng16-16': 'libpng16.so.16',
    'libpng16-16t64': 'libpng16.so.16', 'libcurl4': 'libcurl.so.4',
    'libcurl4t64': 'libcurl.so.4',
}


def soname(name):
    if name in SONAMES:
        return SONAMES[name]
    match = re.fullmatch(r'libav(codec|format|util)(\d+)', name)
    return f'libav{match[1]}.so.{match[2]}' if match else None


def provider(library):
    path = Path('/usr/lib') / library
    # Prefer the owner of the actual native ABI, not a file under Wine/Proton or a cross compiler.
    if path.exists():
        proc = subprocess.run(['/usr/bin/pacman', '-Qqo', str(path)],
                              text=True, capture_output=True)
        if not proc.returncode:
            return proc.stdout.strip()
    proc = subprocess.run(['/usr/bin/pkgfile', '-r', '^/usr/lib/' + re.escape(library) + '$'],
                          text=True, capture_output=True)
    choices = {line.split('/', 1)[1] for line in proc.stdout.splitlines() if '/' in line}
    return next(iter(choices)) if len(choices) == 1 else None


def constrained_provider(item, library):
    package = provider(library)
    if not package:
        return None
    constraint = re.search(r'\(\s*(>=|<=|>>|<<|=)\s*([^\s)]+)\s*\)', item)
    if not constraint:
        return package
    operator, version = constraint.groups()
    # Debian epochs/revisions describe Debian packaging, not upstream ABI versions.
    upstream = version.split(':')[-1].split('-')[0]
    if operator not in {'>=', '>>'}:
        raise RuntimeError('Version restriction requires manual adaptation: ' + item.strip())
    local = subprocess.run(['/usr/bin/pacman', '-Q', package], text=True, capture_output=True)
    if not local.returncode:
        native_version = local.stdout.split()[1]
    else:
        repo = subprocess.run(['/usr/bin/pacman', '-Si', package], text=True, capture_output=True)
        match = re.search(r'^Version\s*:\s*(\S+)', repo.stdout, re.MULTILINE)
        if not match:
            return None
        native_version = match[1]
    native_upstream = native_version.split(':')[-1].rsplit('-', 1)[0]
    compared = subprocess.run(['/usr/bin/vercmp', native_upstream, upstream],
                              text=True, capture_output=True)
    if compared.returncode or not compared.stdout.strip():
        return None
    if int(compared.stdout) < (1 if operator == '>>' else 0):
        return None
    return package + ('>' if operator == '>>' else '>=') + upstream


def native_dependencies(text):
    result, dependencies = [], set()
    for line in text.splitlines():
        field, separator, value = line.partition(':')
        if separator and field.lower() in {'depends', 'pre-depends'}:
            remaining = []
            for group in value.split(','):
                alternatives = group.split('|')
                names = [re.split(r'\s|:', item.strip())[0] for item in alternatives]
                libraries = [soname(name) for name in names]
                if all(libraries):
                    candidates = [constrained_provider(item, lib)
                                  for item, lib in zip(alternatives, libraries)]
                    found = next((item for item in candidates if item), None)
                    if not found:
                        raise RuntimeError('No native compatible library was found for ' + group.strip())
                    dependencies.add(found)
                else:
                    remaining.append(group.strip())
            # Keep Debtap's ELF scan active even if all declared libraries were mapped here.
            result.append(field + ': ' + ', '.join(remaining or ['bash']))
        else:
            result.append(line)
    return '\n'.join(result) + '\n', dependencies


if __name__ == '__main__':
    control = Path(sys.argv[1])
    text, dependencies = native_dependencies(normalize(control.read_text()))
    control.write_text(text)
    control.with_name('.native-dependencies').write_text('\n'.join(sorted(dependencies)) + '\n')
