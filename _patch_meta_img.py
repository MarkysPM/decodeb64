#!/usr/bin/env python3
"""Patch language-specific meta tags into each lang/base64-to-image.html for decodeb64."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

META = {
    'en': {
        'title':      'Base64 to Image Converter — Free Online Tool | decodeb64.com',
        'desc_full':  'Convert Base64 strings to images instantly in your browser. Paste raw Base64 or a full Data URI and preview, download PNG, JPG, WebP, GIF — 100% private, no uploads.',
        'desc_short': 'Convert Base64 strings to images instantly in your browser. Paste raw Base64 or a Data URI and preview, download PNG, JPG, WebP — 100% private, no uploads.',
        'locale':     'en_US',
        'img_alt':    'Base64 to Image Converter on decodeb64.com',
    },
    'es': {
        'title':      'Conversor Base64 a Imagen — Herramienta Gratuita | decodeb64.com',
        'desc_full':  'Convierte cadenas Base64 a imágenes al instante en tu navegador. Pega Base64 o un Data URI y previsualiza y descarga PNG, JPG o WebP — 100% privado, sin subidas.',
        'desc_short': 'Convierte cadenas Base64 a imágenes al instante. Pega Base64 o un Data URI y descarga PNG, JPG o WebP — 100% privado, sin subidas.',
        'locale':     'es_ES',
        'img_alt':    'Conversor Base64 a Imagen en decodeb64.com',
    },
    'pt': {
        'title':      'Conversor Base64 para Imagem — Ferramenta Gratuita | decodeb64.com',
        'desc_full':  'Converta strings Base64 em imagens instantaneamente no seu navegador. Cole Base64 ou um Data URI e visualize e baixe PNG, JPG ou WebP — 100% privado, sem uploads.',
        'desc_short': 'Converta strings Base64 em imagens instantaneamente. Cole Base64 ou um Data URI e baixe PNG, JPG ou WebP — 100% privado, sem uploads.',
        'locale':     'pt_BR',
        'img_alt':    'Conversor Base64 para Imagem em decodeb64.com',
    },
    'fr': {
        'title':      'Convertisseur Base64 en Image — Outil Gratuit | decodeb64.com',
        'desc_full':  "Convertissez des chaînes Base64 en images instantanément dans votre navigateur. Collez du Base64 ou un Data URI et prévisualisez et téléchargez PNG, JPG ou WebP — 100% privé, sans upload.",
        'desc_short': "Convertissez des chaînes Base64 en images instantanément. Collez du Base64 ou un Data URI et téléchargez PNG, JPG ou WebP — 100% privé, sans upload.",
        'locale':     'fr_FR',
        'img_alt':    'Convertisseur Base64 en Image sur decodeb64.com',
    },
    'de': {
        'title':      'Base64 zu Bild Konverter — Kostenloses Tool | decodeb64.com',
        'desc_full':  'Konvertieren Sie Base64-Strings sofort in Bilder in Ihrem Browser. Fügen Sie Base64 oder eine Data URI ein und laden Sie PNG, JPG oder WebP herunter — 100% privat, kein Upload.',
        'desc_short': 'Konvertieren Sie Base64-Strings sofort in Bilder. Base64 oder Data URI einfügen und PNG, JPG oder WebP herunterladen — 100% privat, kein Upload.',
        'locale':     'de_DE',
        'img_alt':    'Base64 zu Bild Konverter auf decodeb64.com',
    },
    'it': {
        'title':      'Convertitore Base64 in Immagine — Strumento Gratuito | decodeb64.com',
        'desc_full':  'Converti stringhe Base64 in immagini istantaneamente nel browser. Incolla Base64 o un Data URI e scarica PNG, JPG o WebP — 100% privato, senza upload.',
        'desc_short': 'Converti stringhe Base64 in immagini istantaneamente. Incolla Base64 o un Data URI e scarica PNG, JPG o WebP — 100% privato, senza upload.',
        'locale':     'it_IT',
        'img_alt':    'Convertitore Base64 in Immagine su decodeb64.com',
    },
    'zh': {
        'title':      'Base64 转图片转换器 — 免费在线工具 | decodeb64.com',
        'desc_full':  '即时在浏览器中将 Base64 字符串转换为图片。粘贴 Base64 或 Data URI，预览并下载 PNG、JPG 或 WebP — 100% 私密，无上传。',
        'desc_short': '即时将 Base64 字符串转换为图片。粘贴 Base64 或 Data URI，下载 PNG、JPG 或 WebP — 100% 私密，无上传。',
        'locale':     'zh_CN',
        'img_alt':    'decodeb64.com Base64 转图片转换器',
    },
    'ru': {
        'title':      'Конвертер Base64 в изображение — Бесплатный инструмент | decodeb64.com',
        'desc_full':  'Мгновенно конвертируйте строки Base64 в изображения в браузере. Вставьте Base64 или Data URI и скачивайте PNG, JPG или WebP — 100% конфиденциально, без загрузки.',
        'desc_short': 'Мгновенно конвертируйте строки Base64 в изображения. Вставьте Base64 или Data URI и скачивайте PNG, JPG или WebP — 100% конфиденциально, без загрузки.',
        'locale':     'ru_RU',
        'img_alt':    'Конвертер Base64 в изображение на decodeb64.com',
    },
}

EN_TITLE     = 'Base64 to Image Converter — Free Online Tool | decodeb64.com'
EN_DESC_FULL = 'Convert Base64 strings to images instantly in your browser. Paste raw Base64 or a full Data URI and preview, download PNG, JPG, WebP, GIF — 100% private, no uploads.'
EN_DESC_OG   = 'Convert Base64 strings to images instantly in your browser. Paste raw Base64 or a Data URI and preview, download PNG, JPG, WebP — 100% private, no uploads.'


def old_block(lang):
    url = f'https://decodeb64.com/{lang}/base64-to-image.html'
    return (
        f'  <meta property="og:title" content="{EN_TITLE}" />\n'
        f'  <meta property="og:description" content="{EN_DESC_OG}" />\n'
        f'  <meta property="og:url" content="{url}" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:image" content="https://decodeb64.com/og-image.png" />\n'
        f'  <meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta name="twitter:title" content="{EN_TITLE}" />\n'
        f'  <meta name="twitter:description" content="{EN_DESC_OG}" />'
    )


def new_block(lang, m):
    url = f'https://decodeb64.com/{lang}/base64-to-image.html'
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


def patch(s, lang):
    m = META[lang]
    s = s.replace(
        f'<title>{EN_TITLE}</title>',
        f'<title>{m["title"]}</title>',
        1
    )
    s = s.replace(
        f'<meta name="description" content="{EN_DESC_FULL}" />',
        f'<meta name="description" content="{m["desc_full"]}" />',
        1
    )
    old = old_block(lang)
    new = new_block(lang, m)
    if old not in s:
        raise ValueError(f'[{lang}] og/twitter block not found')
    s = s.replace(old, new, 1)
    return s


LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it', 'zh', 'ru']

for lang in LANGS:
    path = os.path.join(BASE, lang, 'base64-to-image.html')
    with open(path, encoding='utf-8') as f:
        src = f.read()
    result = patch(src, lang)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'OK  {lang}/base64-to-image.html')

print('Done.')
