"""Preserva grupos KConfig dos painéis sem restaurar desktops ou wallpaper."""
import re

HEADER = re.compile(r'^((?:\[[^\]\n]+\])+)[ \t]*$', re.M)
ROOT = re.compile(r'^\[Containments\]\[(\d+)\]$')
IDS = re.compile(r'\[(?:Containments|Applets)\]\[(\d+)\]')


def sections(text):
    matches = list(HEADER.finditer(text))
    return [(m.group(1), text[m.start():matches[i + 1].start() if i + 1 < len(matches) else len(text)])
            for i, m in enumerate(matches)]


def panel_groups(text):
    groups = sections(text)
    roots = {m.group(1) for header, body in groups
             if (m := ROOT.match(header)) and re.search(r'^plugin=org\.kde\.panel$', body, re.M)}
    owned = set(roots)
    # Algumas versões armazenam o containment do tray fora da árvore do painel.
    while True:
        old = set(owned)
        for header, body in groups:
            if any(header == f'[Containments][{i}]' or header.startswith(f'[Containments][{i}][') for i in owned):
                owned.update(re.findall(r'^SystrayContainmentId=(\d+)$', body, re.M))
        if owned == old:
            break
    selected = [(h, b) for h, b in groups if any(h == f'[Containments][{i}]' or h.startswith(f'[Containments][{i}][') for i in owned)]
    return roots, selected


def capture(applets, views):
    roots, groups = panel_groups(applets)
    view_groups = [(h, b) for h, b in sections(views)
                   if any(h == f'[PlasmaViews][Panel {i}]' or h.startswith(f'[PlasmaViews][Panel {i}][') for i in roots)]
    return {'panels': sorted(roots), 'applets': ''.join(b for _, b in groups),
            'views': ''.join(b for _, b in view_groups)}


def merge(applets, views, saved):
    # Se já existem painéis, conservar o layout vivo: retorno repetido é inócuo.
    if panel_groups(applets)[0]:
        return applets, views
    if not saved['panels']:
        raise ValueError('Nenhum painel salvo; o layout atual foi preservado.')
    used = {int(i) for i in IDS.findall(applets)}
    incoming = {int(i) for i in IDS.findall(saved['applets'])}
    next_id = max(used | incoming | {0}) + 1
    mapping = {}
    for i in sorted(used & incoming):
        mapping[str(i)] = str(next_id)
        next_id += 1

    def translate(body):
        body = IDS.sub(lambda m: m.group(0).rsplit('[', 1)[0] + '[' + mapping.get(m.group(1), m.group(1)) + ']', body)
        body = re.sub(r'\[Panel (\d+)\]', lambda m: '[Panel ' + mapping.get(m.group(1), m.group(1)) + ']', body)
        body = re.sub(r'^(AppletOrder|SystrayContainmentId)=(.*)$',
                      lambda m: m.group(1) + '=' + re.sub(r'\d+', lambda n: mapping.get(n.group(), n.group()), m.group(2)), body, flags=re.M)
        return body

    restored_views = translate(saved['views'])
    replaced = {h for h, _ in sections(restored_views)}
    first = HEADER.search(views)
    preamble = views[:first.start()] if first else views
    kept_views = preamble + ''.join(b for h, b in sections(views) if h not in replaced)
    return applets.rstrip() + '\n\n' + translate(saved['applets']), kept_views.rstrip() + '\n\n' + restored_views
