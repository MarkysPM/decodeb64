#!/usr/bin/env python3
"""Patch language-specific meta tags into each lang/index.html for decodeb64."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

META = {
    'en': {
        'title':      'Base64 Decoder Online — Free Tool | decodeb64.com',
        'desc_full':  'Free online Base64 decoder. Decode Base64 strings and files back to text, images, and binary instantly — UTF-8 auto-detect, URL-safe support, 100% private.',
        'desc_short': 'Free online Base64 decoder. Decode Base64 strings and files back to text, images, and binary instantly. UTF-8 auto-detect, URL-safe, 100% private.',
        'locale':     'en_US',
        'img_alt':    'Base64 Decoder Online on decodeb64.com',
    },
    'es': {
        'title':      'Decodificador Base64 Online — Herramienta Gratuita | decodeb64.com',
        'desc_full':  'Decodificador Base64 online gratis. Decodifica cadenas y archivos Base64 a texto, imágenes y binario al instante — detección UTF-8, soporte URL-safe, 100% privado.',
        'desc_short': 'Decodificador Base64 online gratis. Decodifica cadenas y archivos Base64 al instante. Detección UTF-8, URL-safe, 100% privado.',
        'locale':     'es_ES',
        'img_alt':    'Decodificador Base64 Online en decodeb64.com',
    },
    'pt': {
        'title':      'Decodificador Base64 Online — Ferramenta Gratuita | decodeb64.com',
        'desc_full':  'Decodificador Base64 online gratuito. Decodifique strings e arquivos Base64 para texto, imagens e binário instantaneamente — detecção UTF-8, suporte URL-safe, 100% privado.',
        'desc_short': 'Decodificador Base64 online gratuito. Decodifique strings Base64 instantaneamente. Detecção UTF-8, URL-safe, 100% privado.',
        'locale':     'pt_BR',
        'img_alt':    'Decodificador Base64 Online em decodeb64.com',
    },
    'fr': {
        'title':      'Décodeur Base64 en Ligne — Outil Gratuit | decodeb64.com',
        'desc_full':  "Décodeur Base64 en ligne gratuit. Décodez des chaînes et fichiers Base64 en texte, images et binaire instantanément — détection UTF-8, support URL-safe, 100% privé.",
        'desc_short': "Décodeur Base64 en ligne gratuit. Décodez des chaînes Base64 instantanément. Détection UTF-8, URL-safe, 100% privé.",
        'locale':     'fr_FR',
        'img_alt':    'Décodeur Base64 en Ligne sur decodeb64.com',
    },
    'de': {
        'title':      'Base64 Decoder Online — Kostenloses Tool | decodeb64.com',
        'desc_full':  'Kostenloser Online-Base64-Decoder. Base64-Strings und Dateien sofort in Text, Bilder und Binärdaten dekodieren — automatische UTF-8-Erkennung, URL-safe, 100% privat.',
        'desc_short': 'Kostenloser Online-Base64-Decoder. Base64-Strings sofort dekodieren. Automatische UTF-8-Erkennung, URL-safe, 100% privat.',
        'locale':     'de_DE',
        'img_alt':    'Base64 Decoder Online auf decodeb64.com',
    },
    'it': {
        'title':      'Decodificatore Base64 Online — Strumento Gratuito | decodeb64.com',
        'desc_full':  'Decodificatore Base64 online gratuito. Decodifica stringhe e file Base64 in testo, immagini e dati binari istantaneamente — rilevamento UTF-8, supporto URL-safe, 100% privato.',
        'desc_short': 'Decodificatore Base64 online gratuito. Decodifica stringhe Base64 istantaneamente. Rilevamento UTF-8, URL-safe, 100% privato.',
        'locale':     'it_IT',
        'img_alt':    'Decodificatore Base64 Online su decodeb64.com',
    },
    'zh': {
        'title':      'Base64 在线解码器 — 免费工具 | decodeb64.com',
        'desc_full':  '免费在线 Base64 解码器。即时将 Base64 字符串和文件解码为文本、图片和二进制数据 — 自动 UTF-8 检测，支持 URL-safe，100% 私密。',
        'desc_short': '免费在线 Base64 解码器。即时解码 Base64 字符串。自动 UTF-8 检测，URL-safe，100% 私密。',
        'locale':     'zh_CN',
        'img_alt':    'decodeb64.com Base64 在线解码器',
    },
    'ru': {
        'title':      'Декодировщик Base64 Онлайн — Бесплатный Инструмент | decodeb64.com',
        'desc_full':  'Бесплатный онлайн-декодировщик Base64. Мгновенно декодируйте строки и файлы Base64 в текст, изображения и бинарные данные — автоопределение UTF-8, URL-safe, 100% конфиденциально.',
        'desc_short': 'Бесплатный онлайн-декодировщик Base64. Мгновенно декодируйте строки Base64. Автоопределение UTF-8, URL-safe, 100% конфиденциально.',
        'locale':     'ru_RU',
        'img_alt':    'Декодировщик Base64 Онлайн на decodeb64.com',
    },
}

EN_TITLE     = 'Base64 Decoder Online — Free Tool | decodeb64.com'
EN_DESC_FULL = 'Free online Base64 decoder. Decode Base64 strings and files back to text, images, and binary instantly — UTF-8 auto-detect, URL-safe support, 100% private.'
EN_DESC_TW   = 'Free online Base64 decoder. Decode Base64 strings and files back to text, images, and binary instantly. UTF-8 auto-detect, URL-safe, 100% private.'


def build_new_block(lang, m):
    url = f'https://decodeb64.com/{lang}/'
    return (
        f'  <meta property="og:locale" content="{m["locale"]}" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:site_name" content="decodeb64.com" />\n'
        f'  <meta property="og:title" content="{m["title"]}" />\n'
        f'  <meta property="og:description" content="{m["desc_short"]}" />\n'
        f'  <meta property="og:url" content="{url}" />\n'
        f'  <meta property="og:image" content="https://decodeb64.com/og-image.png" />\n'
        f'  <meta property="og:image:secure_url" content="https://decodeb64.com/og-image.png" />\n'
        f'  <meta property="og:image:alt" content="{m["img_alt"]}" />\n'
        f'  <meta property="og:image:width" content="1200" />\n'
        f'  <meta property="og:image:height" content="630" />\n'
        f'  <meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta name="twitter:title" content="{m["title"]}" />\n'
        f'  <meta name="twitter:description" content="{m["desc_short"]}" />\n'
        f'  <meta name="twitter:image" content="https://decodeb64.com/og-image.png" />\n'
        f'  <meta name="twitter:image:alt" content="{m["img_alt"]}" />'
    )


def old_block(lang):
    url = f'https://decodeb64.com/{lang}/'
    return (
        f'  <meta property="og:title" content="{EN_TITLE}" />\n'
        f'  <meta property="og:description" content="{EN_DESC_FULL}" />\n'
        f'  <meta property="og:url" content="{url}" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:image" content="https://decodeb64.com/og-image.png" />\n'
        f'  <meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta name="twitter:title" content="{EN_TITLE}" />\n'
        f'  <meta name="twitter:description" content="{EN_DESC_TW}" />'
    )


def patch(s, lang):
    m = META[lang]

    # <title>
    s = s.replace(
        f'<title>{EN_TITLE}</title>',
        f'<title>{m["title"]}</title>',
        1
    )
    # <meta name="description">
    s = s.replace(
        f'<meta name="description" content="{EN_DESC_FULL}" />',
        f'<meta name="description" content="{m["desc_full"]}" />',
        1
    )
    # Replace the entire og+twitter block
    old = old_block(lang)
    new = build_new_block(lang, m)
    if old not in s:
        raise ValueError(f'[{lang}] og/twitter block not found — check the source strings')
    s = s.replace(old, new, 1)

    return s


LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it', 'zh', 'ru']

for lang in LANGS:
    path = os.path.join(BASE, lang, 'index.html')
    with open(path, encoding='utf-8') as f:
        src = f.read()
    result = patch(src, lang)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'OK  {lang}/index.html')

print('Done.')
