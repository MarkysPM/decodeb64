import os, re

BASE = r'D:\Datos\Proyectos\decodeb64'

# Per-file "Developed by" translations
dev_by = {
    'index.html':          'Developed by',
    'es/index.html':       'Desarrollado por',
    'pt/index.html':       'Desenvolvido por',
    'fr/index.html':       'Développé par',
    'de/index.html':       'Entwickelt von',
    'it/index.html':       'Sviluppato da',
    'zh/index.html':       '开发者：',
    'ru/index.html':       'Разработано',
    'ja/index.html':       '開発者：',
    'ko/index.html':       '개발자：',
    'nl/index.html':       'Ontwikkeld door',
    'hi/index.html':       'द्वारा विकसित',
    'base64-to-image.html': 'Developed by',
}

AUTHOR_JSON = ''',
      "author": {
        "@type": "Organization",
        "name": "MpmDigital",
        "url": "https://mpmdigital.es/"
      }'''

for fname, label in dev_by.items():
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Update copyright year 2025 → 2026
    c = c.replace('decodeb64.com &copy; 2025', 'decodeb64.com &copy; 2026')

    # 2. Add "Developed by MpmDigital" span after footer-links div, before </footer>
    dev_span = (
        f'\n  <span class="footer-right" style="font-size:0.72rem;color:var(--text-dim);">\n'
        f'    {label} <a href="https://mpmdigital.es/" rel="noopener noreferrer" target="_blank" '
        f'style="color:var(--amber,#ff8c42);">MpmDigital</a>\n'
        f'  </span>'
    )
    if 'mpmdigital.es' not in c:
        c = c.replace('</footer>', dev_span + '\n</footer>')

    # 3. Add author to WebApplication JSON-LD (after "description" line inside WebApplication block)
    # Pattern: the description field ending inside the WebApplication object
    c = re.sub(
        r'("description":\s*"[^"]*"\s*)\n(\s*\})',
        lambda m: m.group(1) + AUTHOR_JSON + '\n' + m.group(2),
        c,
        count=1
    )

    # 4. Update copyrightYear if present
    c = c.replace('"copyrightYear": "2025"', '"copyrightYear": "2026"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'[OK] {fname}')

print('\nDone.')
