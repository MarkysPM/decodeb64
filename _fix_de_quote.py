"""Fix unescaped ASCII double-quote inside German faq_q3 JS string."""
import os

LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it', 'zh', 'ru']

# The buggy string: ASCII " closes the JS string early
BAD  = 'faq_q3: "Was bedeutet „Ungültige Base64-Eingabe"?",\n'
# Fixed: use escaped double-quote \" so the string stays valid JS
GOOD = 'faq_q3: "Was bedeutet „Ungültige Base64-Eingabe\\"?",\n'

fixed = 0
for lang in LANGS:
    for fname in ['index.html', 'base64-to-image.html']:
        path = os.path.join(lang, fname)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8') as f:
            content = f.read()
        if BAD in content:
            content = content.replace(BAD, GOOD)
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(content)
            print(f'Fixed: {path}')
            fixed += 1

print(f'\nTotal files fixed: {fixed}')

# Verify fix in en/index.html
with open('en/index.html', encoding='utf-8') as f:
    c = f.read()
de_idx = c.find('  de: {')
q3_idx = c.find('faq_q3', de_idx)
print('\nVerification (de faq_q3 in en/index.html):')
print(repr(c[q3_idx:q3_idx+65]))
