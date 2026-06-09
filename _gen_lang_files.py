"""
Generate language-specific HTML files for decodeb64.com.
Creates /en/, /es/, /pt/, /fr/, /de/, /it/, /zh/, /ru/ subfolders
with index.html and base64-to-image.html for each language.
Also updates root index.html and base64-to-image.html to redirect pages.
"""

import os
import re

LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it', 'zh', 'ru']
BASE_DIR = r'D:\Datos\Proyectos\decodeb64'

# ── Read sources ──────────────────────────────────────────────────────────────
with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
    index_src = f.read()

with open(os.path.join(BASE_DIR, 'base64-to-image.html'), 'r', encoding='utf-8') as f:
    b2i_src = f.read()


# ── Helpers ───────────────────────────────────────────────────────────────────
def index_hreflang_block(active_lang):
    lines = []
    for lang in LANGS:
        lines.append(f'  <link rel="alternate" hreflang="{lang}" href="https://decodeb64.com/{lang}/" />')
    lines.append('  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/" />')
    return '\n'.join(lines)


def b2i_hreflang_block(active_lang):
    lines = []
    for lang in LANGS:
        lines.append(f'  <link rel="alternate" hreflang="{lang}" href="https://decodeb64.com/{lang}/base64-to-image.html" />')
    lines.append('  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/base64-to-image" />')
    return '\n'.join(lines)


def assert_replaced(original, old, new, label):
    if old not in original:
        raise ValueError(f"String not found in {label}:\n---\n{old}\n---")
    return original.replace(old, new, 1)


# ── index.html canonical/hreflang currently in source ─────────────────────────
INDEX_OLD_CANONICAL = '  <link rel="canonical" href="https://decodeb64.com/" />'
INDEX_OLD_HREFLANG = (
    '  <link rel="alternate" hreflang="en" href="https://decodeb64.com/" />\n'
    '  <link rel="alternate" hreflang="es" href="https://decodeb64.com/es/" />\n'
    '  <link rel="alternate" hreflang="pt" href="https://decodeb64.com/pt/" />\n'
    '  <link rel="alternate" hreflang="fr" href="https://decodeb64.com/fr/" />\n'
    '  <link rel="alternate" hreflang="de" href="https://decodeb64.com/de/" />\n'
    '  <link rel="alternate" hreflang="it" href="https://decodeb64.com/it/" />\n'
    '  <link rel="alternate" hreflang="zh" href="https://decodeb64.com/zh/" />\n'
    '  <link rel="alternate" hreflang="ru" href="https://decodeb64.com/ru/" />\n'
    '  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/" />'
)

# ── base64-to-image.html canonical/hreflang currently in source ───────────────
B2I_OLD_CANONICAL = '  <link rel="canonical" href="https://decodeb64.com/base64-to-image" />'
B2I_OLD_HREFLANG = (
    '  <link rel="alternate" hreflang="en" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="es" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="pt" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="fr" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="de" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="it" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="zh" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="ru" href="https://decodeb64.com/base64-to-image" />\n'
    '  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/base64-to-image" />'
)

# ── Generate language files ───────────────────────────────────────────────────
for lang in LANGS:
    lang_dir = os.path.join(BASE_DIR, lang)
    os.makedirs(lang_dir, exist_ok=True)

    # ── index.html ────────────────────────────────────────────────────────────
    c = index_src

    # 1. <html lang>
    c = assert_replaced(c, '<html lang="en">', f'<html lang="{lang}">', f'{lang}/index.html #1')

    # 2. canonical
    c = assert_replaced(c, INDEX_OLD_CANONICAL,
                        f'  <link rel="canonical" href="https://decodeb64.com/{lang}/" />',
                        f'{lang}/index.html #2')

    # 3. hreflang block
    c = assert_replaced(c, INDEX_OLD_HREFLANG, index_hreflang_block(lang), f'{lang}/index.html #3')

    # 4. og:url
    c = assert_replaced(c, '  <meta property="og:url" content="https://decodeb64.com/" />',
                        f'  <meta property="og:url" content="https://decodeb64.com/{lang}/" />',
                        f'{lang}/index.html #4')

    # 5. currentLang init → hardcoded pageLang
    c = assert_replaced(c,
                        "let currentLang = localStorage.getItem('b64_lang') || 'en';",
                        f"const pageLang = '{lang}';\nlet currentLang = pageLang;",
                        f'{lang}/index.html #5')

    # 6. applyLang: add document.documentElement.lang
    c = assert_replaced(c,
                        "function applyLang(lang) {\n  const t = T[lang] || T['en'];\n  currentLang = lang;\n  localStorage.setItem('b64_lang', lang);",
                        "function applyLang(lang) {\n  document.documentElement.lang = lang;\n  const t = T[lang] || T['en'];\n  currentLang = lang;\n  localStorage.setItem('b64_lang', lang);",
                        f'{lang}/index.html #6')

    # 7. langDropdown click: navigate to /<lang>/ instead of applyLang
    c = assert_replaced(c,
                        "langDropdown.addEventListener('click', (e) => {\n  const opt = e.target.closest('.lang-option');\n  if (opt) {\n    applyLang(opt.dataset.lang);\n    langDropdown.classList.remove('open');\n    langBtn.setAttribute('aria-expanded', false);\n  }\n});",
                        "langDropdown.addEventListener('click', (e) => {\n  const opt = e.target.closest('.lang-option');\n  if (opt) {\n    const sel = opt.dataset.lang;\n    localStorage.setItem('b64_lang', sel);\n    window.location.href = '/' + sel + '/';\n  }\n});",
                        f'{lang}/index.html #7')

    # 8. Nav: base64-to-image link → relative
    c = assert_replaced(c,
                        'href="/base64-to-image"',
                        'href="base64-to-image.html"',
                        f'{lang}/index.html #8')

    # 9. Logo link: href="/" → href="./" (stay in language folder)
    c = assert_replaced(c, '<a href="/" class="logo">', '<a href="./" class="logo">', f'{lang}/index.html #9')

    with open(os.path.join(lang_dir, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(c)
    print(f'  OK {lang}/index.html')

    # ── base64-to-image.html ──────────────────────────────────────────────────
    c = b2i_src

    # 1. <html lang>
    c = assert_replaced(c, '<html lang="en">', f'<html lang="{lang}">', f'{lang}/base64-to-image.html #1')

    # 2. canonical
    c = assert_replaced(c, B2I_OLD_CANONICAL,
                        f'  <link rel="canonical" href="https://decodeb64.com/{lang}/base64-to-image.html" />',
                        f'{lang}/base64-to-image.html #2')

    # 3. hreflang block
    c = assert_replaced(c, B2I_OLD_HREFLANG, b2i_hreflang_block(lang), f'{lang}/base64-to-image.html #3')

    # 4. og:url
    c = assert_replaced(c,
                        '  <meta property="og:url" content="https://decodeb64.com/base64-to-image" />',
                        f'  <meta property="og:url" content="https://decodeb64.com/{lang}/base64-to-image.html" />',
                        f'{lang}/base64-to-image.html #4')

    # 5. currentLang init
    c = assert_replaced(c,
                        "let currentLang = localStorage.getItem('b64_lang') || 'en';",
                        f"const pageLang = '{lang}';\nlet currentLang = pageLang;",
                        f'{lang}/base64-to-image.html #5')

    # 6. applyLang: add document.documentElement.lang
    c = assert_replaced(c,
                        "function applyLang(lang) {\n  if (!T[lang]) lang = 'en';\n  currentLang = lang;\n  localStorage.setItem('b64_lang', lang);",
                        "function applyLang(lang) {\n  if (!T[lang]) lang = 'en';\n  document.documentElement.lang = lang;\n  currentLang = lang;\n  localStorage.setItem('b64_lang', lang);",
                        f'{lang}/base64-to-image.html #6')

    # 7. Lang option click: navigate to /<lang>/base64-to-image.html
    c = assert_replaced(c,
                        "    applyLang(opt.dataset.lang);\n    document.getElementById('langDropdown').classList.remove('open');",
                        "    const sel = opt.dataset.lang;\n    localStorage.setItem('b64_lang', sel);\n    window.location.href = '/' + sel + '/base64-to-image.html';\n    document.getElementById('langDropdown').classList.remove('open');",
                        f'{lang}/base64-to-image.html #7')

    # 8. Logo href → relative (stay in language folder)
    c = assert_replaced(c,
                        '<a href="https://decodeb64.com" class="logo">',
                        '<a href="./" class="logo">',
                        f'{lang}/base64-to-image.html #8')

    # 9. Decode nav link → relative
    c = assert_replaced(c,
                        '<a href="https://decodeb64.com" class="nav-pill inactive" data-i18n="nav_decode">Decode</a>',
                        '<a href="./" class="nav-pill inactive" data-i18n="nav_decode">Decode</a>',
                        f'{lang}/base64-to-image.html #9')

    # 10. Breadcrumb link → relative
    c = assert_replaced(c,
                        '<a href="https://decodeb64.com">decodeb64.com</a>',
                        '<a href="./">decodeb64.com</a>',
                        f'{lang}/base64-to-image.html #10')

    with open(os.path.join(lang_dir, 'base64-to-image.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(c)
    print(f'  OK {lang}/base64-to-image.html')

print('\nAll language files generated.')
