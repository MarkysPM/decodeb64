import os

BASE = r'D:\Datos\Proyectos\decodeb64'

# ── Shared head scripts (Ezoic + analytics) ─────────────────────────────────
HEAD_SCRIPTS = '''\
  <!-- Ezoic privacy scripts -->
  <script data-cfasync="false" src="https://cmp.gatekeeperconsent.com/min.js"></script>
  <script data-cfasync="false" src="https://the.gatekeeperconsent.com/cmp.min.js"></script>
  <!-- Ezoic main script -->
  <script async src="//www.ezojs.com/ezoic/sa.min.js"></script>
  <script>
    window.ezstandalone = window.ezstandalone || {};
    ezstandalone.cmd = ezstandalone.cmd || [];
  </script>
  <!-- Ezoic analytics -->
  <script src="//ezoicanalytics.com/analytics.js"></script>
  <script>
    (function () {
      var isProd = /decodeb64\\.com$/.test(window.location.hostname);
      window.dataLayer = window.dataLayer || [];
      function gtag() { dataLayer.push(arguments); }
      window.gtag = gtag;
      gtag('consent', 'default', {
        analytics_storage: 'denied', ad_storage: 'denied',
        ad_user_data: 'denied', ad_personalization: 'denied', wait_for_update: 500
      });
      if (!isProd) return;
      var ch = document.createElement('script');
      ch.src = 'https://cdn.cookiehub.eu/c2/37267253.js';
      ch.onload = function () {
        document.addEventListener('DOMContentLoaded', function () {
          window.cookiehub && window.cookiehub.load({});
        });
      };
      document.head.appendChild(ch);
      var ga = document.createElement('script');
      ga.async = true;
      ga.src = 'https://www.googletagmanager.com/gtag/js?id=G-JVDER6MN4Y';
      document.head.appendChild(ga);
      gtag('js', new Date());
      gtag('config', 'G-JVDER6MN4Y');
      var ad = document.createElement('script');
      ad.async = true;
      ad.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7602115974474104';
      ad.crossOrigin = 'anonymous';
      document.head.appendChild(ad);
    })();
  </script>'''

# ── Shared CSS ────────────────────────────────────────────────────────────────
SHARED_CSS = '''\
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Sora:wght@300;400;500;600;700&display=swap');
    :root {
      --bg: #0d0d14; --bg2: #12121c; --bg3: #1a1a28;
      --amber: #ff8c42; --amber-dim: rgba(255,140,66,0.15);
      --amber-glow: rgba(255,140,66,0.35); --amber-light: #ffb07a;
      --glass-bg: rgba(255,255,255,0.04); --glass-border: rgba(255,255,255,0.09);
      --text: #e8e8f0; --text-muted: #7a7a9a; --text-dim: #4a4a6a;
      --green: #3ecf7e; --red: #ff5a5a; --red-dim: rgba(255,90,90,0.15);
      --radius: 14px; --radius-sm: 8px;
      --mono: 'JetBrains Mono', monospace; --sans: 'Sora', sans-serif;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--sans); background-color: var(--bg); color: var(--text);
      min-height: 100vh; overflow-x: hidden; position: relative;
    }
    body::before {
      content: ''; position: fixed; inset: 0;
      background-image: radial-gradient(circle, rgba(255,140,66,0.12) 1px, transparent 1px);
      background-size: 28px 28px; pointer-events: none; z-index: 0;
    }
    body::after {
      content: ''; position: fixed; top: -20%; left: 50%; transform: translateX(-50%);
      width: 800px; height: 500px;
      background: radial-gradient(ellipse, rgba(255,140,66,0.06) 0%, transparent 70%);
      pointer-events: none; z-index: 0;
    }
    header {
      position: sticky; top: 0; z-index: 100;
      background: rgba(13,13,20,0.85); backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid var(--glass-border);
      padding: 0 24px; height: 62px; display: flex; align-items: center;
      justify-content: space-between; gap: 16px;
    }
    .logo { font-family: var(--mono); font-size: 1.2rem; font-weight: 700;
      letter-spacing: -0.5px; text-decoration: none; flex-shrink: 0; }
    .logo span.decode { color: #ffffff; }
    .logo span.b64 { color: var(--amber); }
    .header-right { display: flex; align-items: center; gap: 10px; }
    .nav-pills { display: flex; gap: 6px; }
    .nav-pill {
      font-family: var(--sans); font-size: 0.78rem; font-weight: 500;
      padding: 5px 14px; border-radius: 20px; text-decoration: none;
      transition: all 0.2s; border: 1px solid transparent;
    }
    .nav-pill.inactive { color: var(--text-muted); border-color: var(--glass-border); background: transparent; }
    .nav-pill.inactive:hover { color: var(--text); border-color: rgba(255,255,255,0.18); }
    .nav-pill.active { color: var(--bg); background: var(--amber); font-weight: 600; }
    .lang-selector { position: relative; }
    .lang-btn {
      display: flex; align-items: center; gap: 6px; padding: 5px 12px;
      background: var(--glass-bg); border: 1px solid var(--glass-border);
      border-radius: 20px; color: var(--text-muted); cursor: pointer;
      font-family: var(--sans); font-size: 0.78rem; transition: all 0.2s; white-space: nowrap;
    }
    .lang-btn:hover { color: var(--text); border-color: rgba(255,255,255,0.18); }
    .lang-btn svg { width: 14px; height: 14px; flex-shrink: 0; }
    .lang-dropdown {
      display: none; position: absolute; top: calc(100% + 8px); right: 0;
      background: #1a1a2e; border: 1px solid var(--glass-border);
      border-radius: var(--radius-sm); overflow: hidden; min-width: 160px;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5); z-index: 200;
    }
    .lang-dropdown.open { display: block; }
    .lang-option {
      display: flex; align-items: center; gap: 8px; padding: 9px 14px;
      cursor: pointer; font-size: 0.82rem; color: var(--text-muted); transition: all 0.15s;
    }
    .lang-option:hover { background: var(--amber-dim); color: var(--text); }
    .lang-option.selected { color: var(--amber); }
    main {
      position: relative; z-index: 1; max-width: 900px;
      margin: 0 auto; padding: 0 20px 80px;
    }
    .page-hero {
      text-align: center; padding: 48px 20px 36px; position: relative;
    }
    .page-hero h1 {
      font-size: clamp(1.8rem, 4vw, 2.8rem); font-weight: 700;
      letter-spacing: -1px; line-height: 1.15; margin-bottom: 12px;
    }
    .breadcrumb {
      font-size: 0.78rem; color: var(--text-dim); margin-bottom: 8px;
    }
    .breadcrumb a { color: var(--text-dim); text-decoration: none; transition: color 0.2s; }
    .breadcrumb a:hover { color: var(--amber); }
    .breadcrumb span { color: var(--text-muted); margin: 0 6px; }
    .glass-card {
      background: var(--glass-bg); border: 1px solid var(--glass-border);
      border-radius: var(--radius); backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px); padding: 32px 36px; margin-bottom: 20px;
    }
    .content-h2 {
      font-size: 1rem; font-weight: 700; color: var(--amber);
      margin: 28px 0 10px; letter-spacing: -0.2px;
    }
    .content-h2:first-child { margin-top: 0; }
    .glass-card p {
      font-size: 0.9rem; color: var(--text-muted); line-height: 1.75; margin-bottom: 12px;
    }
    .glass-card p:last-child { margin-bottom: 0; }
    .glass-card ul {
      list-style: none; padding: 0; margin: 8px 0 12px;
    }
    .glass-card ul li {
      font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;
      padding-left: 18px; position: relative;
    }
    .glass-card ul li::before {
      content: '—'; position: absolute; left: 0; color: var(--amber); font-family: var(--mono);
    }
    .glass-card a { color: var(--amber); text-decoration: none; transition: opacity 0.2s; }
    .glass-card a:hover { opacity: 0.8; text-decoration: underline; }
    .last-updated {
      font-size: 0.75rem; color: var(--text-dim); margin-bottom: 24px;
      font-family: var(--mono);
    }
    footer {
      position: relative; z-index: 1; border-top: 1px solid var(--glass-border);
      padding: 24px 20px; display: flex; flex-wrap: wrap; gap: 16px;
      align-items: center; justify-content: space-between;
      max-width: 900px; margin: 0 auto; font-size: 0.78rem; color: var(--text-dim);
    }
    .footer-links { display: flex; gap: 16px; flex-wrap: wrap; }
    .footer-links a, footer a { color: var(--text-dim); text-decoration: none; transition: color 0.2s; }
    .footer-links a:hover, footer a:hover { color: var(--amber); }
    footer .footer-right { color: var(--text-dim); }
    footer .footer-right a { color: var(--amber); }
    @media (max-width: 640px) {
      header { padding: 0 16px; }
      .logo { font-size: 1rem; }
      .nav-pill { padding: 4px 10px; font-size: 0.73rem; }
      .lang-btn span { display: none; }
      main { padding: 0 16px 60px; }
      .glass-card { padding: 20px 18px; }
      footer { flex-direction: column; align-items: flex-start; gap: 10px; }
    }'''

# ── Header HTML ───────────────────────────────────────────────────────────────
HEADER_HTML = '''\
<!-- HEADER -->
<header>
  <a href="/" class="logo">
    <span class="decode">decode</span><span class="b64">B64</span>
  </a>
  <div class="header-right">
    <nav class="nav-pills">
      <a href="https://encodeb64.com" class="nav-pill inactive" rel="noopener noreferrer" target="_blank">Encode</a>
      <a href="/" class="nav-pill inactive">Decode</a>
      <a href="/base64-to-image" class="nav-pill inactive">Base64 to Image</a>
    </nav>
    <div class="lang-selector">
      <button class="lang-btn" id="langBtn" aria-haspopup="listbox" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
        <span id="langLabel">English</span>
        <svg viewBox="0 0 10 6" fill="currentColor" width="10" height="6"><path d="M0 0l5 6 5-6z"/></svg>
      </button>
      <div class="lang-dropdown" id="langDropdown" role="listbox">
        <div class="lang-option selected" data-lang="en" role="option">🇺🇸 English</div>
        <div class="lang-option" data-lang="es" role="option">🇪🇸 Español</div>
        <div class="lang-option" data-lang="pt" role="option">🇧🇷 Português</div>
        <div class="lang-option" data-lang="fr" role="option">🇫🇷 Français</div>
        <div class="lang-option" data-lang="de" role="option">🇩🇪 Deutsch</div>
        <div class="lang-option" data-lang="it" role="option">🇮🇹 Italiano</div>
        <div class="lang-option" data-lang="zh" role="option">🇨🇳 中文</div>
        <div class="lang-option" data-lang="ru" role="option">🇷🇺 Русский</div>
        <div class="lang-option" data-lang="ja" role="option">🇯🇵 日本語</div>
        <div class="lang-option" data-lang="ko" role="option">🇰🇷 한국어</div>
        <div class="lang-option" data-lang="nl" role="option">🇳🇱 Nederlands</div>
        <div class="lang-option" data-lang="hi" role="option">🇮🇳 हिन्दी</div>
      </div>
    </div>
  </div>
</header>'''

# ── Footer HTML ───────────────────────────────────────────────────────────────
def footer_html(dev_label='Developed by'):
    return f'''\
<!-- FOOTER -->
<footer>
  <span>decodeb64.com &copy; 2026</span>
  <div class="footer-links">
    <a href="/about">About</a>
    <a href="/privacy-policy">Privacy Policy</a>
    <a href="/terms-of-use">Terms of Use</a>
    <a href="/contact">Contact</a>
  </div>
  <span class="footer-right"><span>Also try:</span> <a href="https://encodeb64.com" rel="noopener noreferrer" target="_blank">Base64 Encode — encodeb64.com →</a></span>
  <span class="footer-right" style="font-size:0.72rem;color:var(--text-dim);">
    {dev_label} <a href="https://mpmdigital.es/" rel="noopener noreferrer" target="_blank" style="color:var(--amber,#ff8c42);">MpmDigital</a>
  </span>
</footer>'''

# ── Language switcher JS ──────────────────────────────────────────────────────
def lang_switcher_js(page_slug):
    return f'''\
<script>
  // Language switcher
  (function () {{
    var btn = document.getElementById('langBtn');
    var dd = document.getElementById('langDropdown');
    btn.addEventListener('click', function (e) {{
      e.stopPropagation();
      dd.classList.toggle('open');
      btn.setAttribute('aria-expanded', dd.classList.contains('open'));
    }});
    document.addEventListener('click', function () {{
      dd.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }});
    dd.addEventListener('click', function (e) {{
      var opt = e.target.closest('.lang-option');
      if (!opt) return;
      var sel = opt.dataset.lang;
      var path = sel === 'en' ? '/{page_slug}' : '/' + sel + '/{page_slug}';
      window.location.href = path;
    }});
  }})();
</script>'''

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1: about/index.html
# ══════════════════════════════════════════════════════════════════════════════
ABOUT_HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_SCRIPTS}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About — decodeb64.com</title>
  <meta name="description" content="Learn about decodeb64.com — a free, private Base64 decoder tool built for developers. No servers, no tracking, 100% browser-based." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://decodeb64.com/about" />
  <link rel="alternate" hreflang="en" href="https://decodeb64.com/about" />
  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/about" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="decodeb64.com" />
  <meta property="og:title" content="About — decodeb64.com" />
  <meta property="og:description" content="Learn about decodeb64.com — a free, private Base64 decoder tool built for developers. No servers, no tracking, 100% browser-based." />
  <meta property="og:url" content="https://decodeb64.com/about" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="theme-color" content="#0d0d14" />
  <meta name="color-scheme" content="dark" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

{HEADER_HTML}

<!-- MAIN -->
<main>
  <div class="page-hero">
    <p class="breadcrumb"><a href="/">decodeb64.com</a><span>›</span>About</p>
    <h1>About decodeb64.com</h1>
  </div>

  <div class="glass-card">
    <h2 class="content-h2">What is decodeb64.com?</h2>
    <p>decodeb64.com is a free online tool for decoding Base64 strings and files directly in your browser. It supports text decoding with UTF-8 auto-detection, Base64URL (RFC 4648), per-line decoding, binary file decoding with automatic file type detection, and a Base64 to Image converter supporting JPG, PNG, GIF, WebP, SVG, BMP, ICO, TIFF, and AVIF.</p>

    <h2 class="content-h2">Who built this?</h2>
    <p>decodeb64.com was designed and developed by <strong style="color:var(--text);">MpmDigital</strong>, a digital agency specialising in web development and online tools. You can learn more at <a href="https://mpmdigital.es/" rel="noopener noreferrer" target="_blank">mpmdigital.es</a>.</p>

    <h2 class="content-h2">Our philosophy</h2>
    <p>We believe developer tools should be fast, private, and free. All processing on decodeb64.com happens entirely in your browser — no data is ever sent to a server. No registration required, no usage limits, no ads injected into your decoded content.</p>

    <h2 class="content-h2">Sister tool</h2>
    <p>decodeb64.com is the decoding companion to <a href="https://encodeb64.com" rel="noopener noreferrer" target="_blank">encodeb64.com</a>, which handles Base64 encoding of text, files, and images.</p>

    <h2 class="content-h2">Contact</h2>
    <p>For questions or feedback: <a href="mailto:contacto@mpmdigital.es">contacto@mpmdigital.es</a></p>
  </div>
</main>

{footer_html('Developed by')}

{lang_switcher_js('about')}
</body>
</html>'''

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2: privacy-policy/index.html
# ══════════════════════════════════════════════════════════════════════════════
PRIVACY_HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_SCRIPTS}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Privacy Policy — decodeb64.com</title>
  <meta name="description" content="Privacy Policy for decodeb64.com. We process no personal data — all Base64 decoding happens locally in your browser." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://decodeb64.com/privacy-policy" />
  <link rel="alternate" hreflang="en" href="https://decodeb64.com/privacy-policy" />
  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/privacy-policy" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="decodeb64.com" />
  <meta property="og:title" content="Privacy Policy — decodeb64.com" />
  <meta property="og:description" content="Privacy Policy for decodeb64.com. We process no personal data — all Base64 decoding happens locally in your browser." />
  <meta property="og:url" content="https://decodeb64.com/privacy-policy" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="theme-color" content="#0d0d14" />
  <meta name="color-scheme" content="dark" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

{HEADER_HTML}

<!-- MAIN -->
<main>
  <div class="page-hero">
    <p class="breadcrumb"><a href="/">decodeb64.com</a><span>›</span>Privacy Policy</p>
    <h1>Privacy Policy</h1>
  </div>

  <div class="glass-card">
    <p class="last-updated">Last updated: August 2026</p>

    <h2 class="content-h2">1. Overview</h2>
    <p>decodeb64.com is operated by MpmDigital (<a href="https://mpmdigital.es/" rel="noopener noreferrer" target="_blank">https://mpmdigital.es/</a>). This Privacy Policy explains how we handle information when you use our website.</p>

    <h2 class="content-h2">2. Data we do NOT collect</h2>
    <p>We do not collect, store, or transmit any of the following:</p>
    <ul>
      <li>The text, files, or Base64 strings you encode or decode</li>
      <li>Your IP address (beyond standard server logs retained by our hosting provider, Cloudflare)</li>
      <li>Personal identifiable information of any kind</li>
      <li>Cookies for tracking or advertising purposes</li>
    </ul>
    <p>All encoding and decoding operations happen entirely in your browser using standard JavaScript APIs. Nothing is uploaded to our servers.</p>

    <h2 class="content-h2">3. Analytics</h2>
    <p>We use Google Analytics 4 to collect anonymous usage statistics (page views, session duration, general geographic region). This data is anonymised and does not identify individual users. You can opt out via your browser's privacy settings or by using an ad blocker.</p>
    <p>We use Google AdSense to display advertisements. Google may use cookies to serve ads based on your prior visits to this or other websites. You can opt out of personalised advertising at <a href="https://adssettings.google.com/" rel="noopener noreferrer" target="_blank">Google's Ad Settings</a>.</p>

    <h2 class="content-h2">4. Cookies</h2>
    <p>We use CookieHub to manage cookie consent in compliance with GDPR. Only strictly necessary cookies are set by default. You may update your preferences at any time via the cookie banner.</p>

    <h2 class="content-h2">5. Third-party services</h2>
    <p>Our website is hosted on Cloudflare Pages. Cloudflare may retain standard server access logs. Please refer to <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener noreferrer" target="_blank">Cloudflare's Privacy Policy</a> for details.</p>

    <h2 class="content-h2">6. Your rights (GDPR)</h2>
    <p>If you are located in the European Union, you have rights under the GDPR including the right to access, rectify, and erase personal data. Since we collect no personal data, there is nothing to access or erase. For any privacy-related questions, contact us at: <a href="mailto:contacto@mpmdigital.es">contacto@mpmdigital.es</a></p>

    <h2 class="content-h2">7. Changes to this policy</h2>
    <p>We may update this policy from time to time. The "Last updated" date at the top of this page will reflect any changes.</p>

    <h2 class="content-h2">8. Contact</h2>
    <p>MpmDigital<br>
    Website: <a href="https://mpmdigital.es/" rel="noopener noreferrer" target="_blank">https://mpmdigital.es/</a><br>
    Email: <a href="mailto:contacto@mpmdigital.es">contacto@mpmdigital.es</a></p>
  </div>
</main>

{footer_html('Developed by')}

{lang_switcher_js('privacy-policy')}
</body>
</html>'''

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3: terms-of-use/index.html
# ══════════════════════════════════════════════════════════════════════════════
TERMS_HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_SCRIPTS}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Terms of Use — decodeb64.com</title>
  <meta name="description" content="Terms of Use for decodeb64.com. Free to use, no registration required. All processing happens in your browser." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://decodeb64.com/terms-of-use" />
  <link rel="alternate" hreflang="en" href="https://decodeb64.com/terms-of-use" />
  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/terms-of-use" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="decodeb64.com" />
  <meta property="og:title" content="Terms of Use — decodeb64.com" />
  <meta property="og:description" content="Terms of Use for decodeb64.com. Free to use, no registration required. All processing happens in your browser." />
  <meta property="og:url" content="https://decodeb64.com/terms-of-use" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="theme-color" content="#0d0d14" />
  <meta name="color-scheme" content="dark" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <style>
{SHARED_CSS}
  </style>
</head>
<body>

{HEADER_HTML}

<!-- MAIN -->
<main>
  <div class="page-hero">
    <p class="breadcrumb"><a href="/">decodeb64.com</a><span>›</span>Terms of Use</p>
    <h1>Terms of Use</h1>
  </div>

  <div class="glass-card">
    <p class="last-updated">Last updated: August 2026</p>

    <h2 class="content-h2">1. Acceptance of terms</h2>
    <p>By accessing and using decodeb64.com, you agree to be bound by these Terms of Use. If you do not agree, please do not use the site.</p>

    <h2 class="content-h2">2. Description of service</h2>
    <p>decodeb64.com provides a free, browser-based Base64 decoding tool. All processing is performed locally in your browser. We do not store or process any of the data you input.</p>

    <h2 class="content-h2">3. Permitted use</h2>
    <p>You may use decodeb64.com for any lawful purpose, including personal, commercial, and educational use. The tool is provided free of charge with no registration required.</p>

    <h2 class="content-h2">4. Prohibited use</h2>
    <p>You may not:</p>
    <ul>
      <li>Use the site in any way that violates applicable laws or regulations</li>
      <li>Attempt to interfere with, disrupt, or gain unauthorised access to the site or its infrastructure</li>
      <li>Use automated tools to scrape or overload the site in a way that degrades service for other users</li>
    </ul>

    <h2 class="content-h2">5. Intellectual property</h2>
    <p>The design, code, and content of decodeb64.com are the property of MpmDigital. You may not copy, reproduce, or redistribute the site's design or code without prior written permission.</p>

    <h2 class="content-h2">6. Disclaimer of warranties</h2>
    <p>decodeb64.com is provided "as is" without warranties of any kind. We do not guarantee that the service will be uninterrupted, error-free, or suitable for any particular purpose.</p>

    <h2 class="content-h2">7. Limitation of liability</h2>
    <p>MpmDigital shall not be liable for any direct, indirect, incidental, or consequential damages arising from your use of decodeb64.com or the inability to use it.</p>

    <h2 class="content-h2">8. Security notice</h2>
    <p>Base64 is an encoding scheme, not encryption. Do not use Base64 as a security measure for sensitive data. Do not execute decoded files from untrusted sources.</p>

    <h2 class="content-h2">9. Changes to terms</h2>
    <p>We reserve the right to modify these terms at any time. Continued use of the site after changes constitutes acceptance of the new terms.</p>

    <h2 class="content-h2">10. Governing law</h2>
    <p>These terms are governed by the laws of Spain. Any disputes shall be subject to the exclusive jurisdiction of the courts of Spain.</p>

    <h2 class="content-h2">11. Contact</h2>
    <p>MpmDigital<br>
    Website: <a href="https://mpmdigital.es/" rel="noopener noreferrer" target="_blank">https://mpmdigital.es/</a><br>
    Email: <a href="mailto:contacto@mpmdigital.es">contacto@mpmdigital.es</a></p>
  </div>
</main>

{footer_html('Developed by')}

{lang_switcher_js('terms-of-use')}
</body>
</html>'''

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4: contact/index.html
# ══════════════════════════════════════════════════════════════════════════════
CONTACT_HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_SCRIPTS}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Contact — decodeb64.com</title>
  <meta name="description" content="Contact the decodeb64.com team. Questions, feedback, or partnership enquiries — we'd love to hear from you." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://decodeb64.com/contact" />
  <link rel="alternate" hreflang="en" href="https://decodeb64.com/contact" />
  <link rel="alternate" hreflang="x-default" href="https://decodeb64.com/contact" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="decodeb64.com" />
  <meta property="og:title" content="Contact — decodeb64.com" />
  <meta property="og:description" content="Contact the decodeb64.com team. Questions, feedback, or partnership enquiries — we'd love to hear from you." />
  <meta property="og:url" content="https://decodeb64.com/contact" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="theme-color" content="#0d0d14" />
  <meta name="color-scheme" content="dark" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <style>
{SHARED_CSS}
    .contact-email {{
      display: inline-block;
      font-family: var(--mono);
      font-size: 1rem;
      font-weight: 600;
      color: var(--amber);
      text-decoration: none;
      padding: 10px 20px;
      border: 1px solid rgba(255,140,66,0.35);
      border-radius: var(--radius-sm);
      background: rgba(255,140,66,0.07);
      margin: 8px 0 16px;
      transition: all 0.2s;
    }}
    .contact-email:hover {{
      background: rgba(255,140,66,0.15);
      box-shadow: 0 0 20px rgba(255,140,66,0.2);
      text-decoration: none !important;
      opacity: 1 !important;
    }}
  </style>
</head>
<body>

{HEADER_HTML}

<!-- MAIN -->
<main>
  <div class="page-hero">
    <p class="breadcrumb"><a href="/">decodeb64.com</a><span>›</span>Contact</p>
    <h1>Contact</h1>
  </div>

  <div class="glass-card">
    <h2 class="content-h2">Get in touch</h2>
    <p>Have a question, found a bug, or want to suggest a feature? We'd love to hear from you.</p>

    <p style="margin-top:16px;"><strong style="color:var(--text);font-size:0.8rem;text-transform:uppercase;letter-spacing:0.8px;">Email</strong></p>
    <a href="mailto:contacto@mpmdigital.es" class="contact-email">contacto@mpmdigital.es</a>

    <p><strong style="color:var(--text);font-size:0.8rem;text-transform:uppercase;letter-spacing:0.8px;">Website</strong></p>
    <p><a href="https://mpmdigital.es/" rel="noopener noreferrer" target="_blank">mpmdigital.es</a></p>

    <h2 class="content-h2">Response time</h2>
    <p>We typically respond within 1–2 business days.</p>

    <h2 class="content-h2">Other tools</h2>
    <p>Looking for the encoder? Visit <a href="https://encodeb64.com" rel="noopener noreferrer" target="_blank">encodeb64.com</a>.</p>
  </div>
</main>

{footer_html('Developed by')}

{lang_switcher_js('contact')}
</body>
</html>'''

# ══════════════════════════════════════════════════════════════════════════════
# Write new pages
# ══════════════════════════════════════════════════════════════════════════════
pages = [
    ('about/index.html', ABOUT_HTML),
    ('privacy-policy/index.html', PRIVACY_HTML),
    ('terms-of-use/index.html', TERMS_HTML),
    ('contact/index.html', CONTACT_HTML),
]

for rel_path, content in pages:
    full_path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'[CREATED] {rel_path}')

# ══════════════════════════════════════════════════════════════════════════════
# Update footer links in all existing pages
# ══════════════════════════════════════════════════════════════════════════════
existing_files = [
    'index.html',
    'es/index.html', 'pt/index.html', 'fr/index.html', 'de/index.html',
    'it/index.html', 'zh/index.html', 'ru/index.html', 'ja/index.html',
    'ko/index.html', 'nl/index.html', 'hi/index.html',
    'base64-to-image/index.html',
]

replacements = [
    ('<a href="#" data-i18n="footer_about">',   '<a href="/about" data-i18n="footer_about">'),
    ('<a href="#" data-i18n="footer_privacy">', '<a href="/privacy-policy" data-i18n="footer_privacy">'),
    ('<a href="#" data-i18n="footer_terms">',   '<a href="/terms-of-use" data-i18n="footer_terms">'),
    ('<a href="#" data-i18n="footer_contact">', '<a href="/contact" data-i18n="footer_contact">'),
]

for fname in existing_files:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    changed = False
    for old, new in replacements:
        if old in c:
            c = c.replace(old, new)
            changed = True
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'[UPDATED] {fname}')
    else:
        print(f'[SKIP]    {fname} (no # links found)')

print('\nDone.')
