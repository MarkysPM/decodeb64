import os, re

BASE = r'D:\Datos\Proyectos\decodeb64'

files = [
    'index.html',
    'es/index.html', 'pt/index.html', 'fr/index.html', 'de/index.html',
    'it/index.html', 'zh/index.html', 'ru/index.html', 'ja/index.html',
    'ko/index.html', 'nl/index.html', 'hi/index.html',
]

def reorder(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # ── locate all 6 comment anchors ────────────────────────────────
    anchors = {
        'main':       '<!-- MAIN -->',
        'hero':       '  <!-- HERO -->',
        'tool':       '<!-- TOOL CARD -->',
        'accordion':  '  <!-- INFO ACCORDION -->',
        'faq':        '<!-- FAQ -->',
        'h2':         '  <!-- H2-SECTIONS -->',
        'other':      '  <!-- OTHER TOOLS -->',
        'footer':     '<!-- FOOTER -->',
    }
    idx = {k: c.index(v) for k, v in anchors.items()}

    # ── carve blocks ────────────────────────────────────────────────
    # Everything before <main>
    pre = c[:idx['main']] + '<!-- MAIN -->\n<main>\n\n'

    # HERO block: from "  <!-- HERO -->" up to (not including) ezoic-101
    hero_raw = c[idx['hero']:idx['tool']]
    # Strip the trailing ezoic-101 div from hero_raw; it sits just before TOOL CARD
    ezoic101_pat = r'\n  <div id="ezoic-pub-ad-placeholder-101"></div>\n\n'
    m101 = re.search(ezoic101_pat, hero_raw)
    if m101:
        hero_block = hero_raw[:m101.start()].rstrip() + '\n\n'
        ezoic101_block = '\n  <div id="ezoic-pub-ad-placeholder-101"></div>\n\n'
    else:
        hero_block = hero_raw.rstrip() + '\n\n'
        ezoic101_block = ''

    # TOOL CARD block: from "<!-- TOOL CARD -->" to "<!-- INFO ACCORDION -->"
    tool_block = c[idx['tool']:idx['accordion']].rstrip() + '\n\n'

    # ACCORDION block: from "  <!-- INFO ACCORDION -->" to "<!-- FAQ -->"
    acc_raw = c[idx['accordion']:idx['faq']]
    # Remove the ezoic-102 div that lives at the end of this block
    ezoic102_pat = r'\n\n  \n  <div id="ezoic-pub-ad-placeholder-102"></div>\n'
    m102 = re.search(ezoic102_pat, acc_raw)
    if m102:
        acc_block = acc_raw[:m102.start()].rstrip() + '\n\n'
        ezoic102_block = '\n  <div id="ezoic-pub-ad-placeholder-102"></div>\n'
    else:
        acc_block = acc_raw.rstrip() + '\n\n'
        ezoic102_block = ''

    # FAQ block: from "<!-- FAQ -->" to "  <!-- H2-SECTIONS -->"
    faq_block = c[idx['faq']:idx['h2']].rstrip() + '\n'

    # H2 block: from "  <!-- H2-SECTIONS -->" to "  <!-- OTHER TOOLS -->"
    h2_raw = c[idx['h2']:idx['other']]
    # Remove the sentinel comment itself from the start
    h2_content = h2_raw[len('  <!-- H2-SECTIONS -->'):].lstrip('\n')

    # Split 4 individual <section> blocks
    # Each starts with "  <section style=\"margin-top:28px;\">"
    section_starts = [m.start() for m in re.finditer(r'  <section style="margin-top:28px;">', h2_content)]
    if len(section_starts) != 4:
        print(f'  WARNING: found {len(section_starts)} H2 sections in {path}, expected 4')
        return False

    h2_sections = []
    for i, start in enumerate(section_starts):
        end = section_starts[i+1] if i+1 < len(section_starts) else len(h2_content)
        h2_sections.append(h2_content[start:end].rstrip() + '\n')

    # OTHER TOOLS block: from "  <!-- OTHER TOOLS -->" to "</main>"
    main_close = c.index('</main>')
    other_block = c[idx['other']:main_close].rstrip() + '\n\n'

    # Post: "</main>" onwards
    post = c[main_close:]

    # ── reassemble in new order ─────────────────────────────────────
    # 1 Hero | 2 H2-s1 | 3 ezoic101 | 4 Tool | 5 H2-s2 | 6 H2-s3 | 7 H2-s4
    # 8 ezoic102 | 9 FAQ | 10 Accordion | 11 Other Tools
    new_main = (
        hero_block
        + '  <!-- H2-SECTIONS -->\n'
        + h2_sections[0]
        + ezoic101_block
        + tool_block
        + h2_sections[1]
        + h2_sections[2]
        + h2_sections[3]
        + ezoic102_block
        + '\n'
        + faq_block
        + '\n'
        + acc_block
        + other_block
    )

    result = pre + new_main + post

    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)
    return True


for fname in files:
    path = os.path.join(BASE, fname)
    ok = reorder(path)
    status = 'OK' if ok else 'FAIL'
    print(f'[{status}] {fname}')

print('\nDone.')
