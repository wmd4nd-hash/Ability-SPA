#!/usr/bin/env python3
"""Static page generator for the Ability SPA prototype.

    python3 tools/build.py

- Injects the shared header / footer / cookie bar into index.html (between BUILD markers).
- Builds the sub-pages defined in PAGES (content from the current abilityspa.com texts,
  prices from the spa menus: Burgas Dec 2025, Varna Feb 2026 – see current-site/).
- Writes a noindex "coming soon" page for every address in docs/sitemap-new.md that is not built yet,
  so no link in the prototype is ever broken.

Rules kept on every page: one H1, unique title (< 60 chars) and description (< 155 chars),
canonical + BreadcrumbList JSON-LD, relative links (work in the preview and on the live domain).
"""
import hashlib, html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cache-busting: the stylesheet and script are referenced as styles.css?v=<hash>, so a new page never runs with an
# older cached copy of either (the preview host caches them separately from the HTML).
ASSET_V = hashlib.sha1(b''.join(open(os.path.join(ROOT, f), 'rb').read() for f in ('css/styles.css', 'js/main.js'))).hexdigest()[:8]
SITE = 'https://abilityspa.com'
BOOK_BURGAS = 'https://book.abilityspa.com/reservations/start?site=1'
TEL_BURGAS, TEL_BURGAS_TXT = '+359895635555', '+359 895 635 555'
TEL_BURGAS2, TEL_BURGAS2_TXT = '+35956875260', '056 875 260'
TEL_VARNA, TEL_VARNA_TXT = '+359899994149', '+359 899 994 149'
PDF_B = 'https://abilityspa.com/wp-content/uploads/2026/03/ability_spa_menu_dec_25_bg_online.pdf'
PDF_V = 'https://abilityspa.com/wp-content/uploads/2026/03/ability_spa__wellness_menu_feb_26_bg_online.pdf'
PRICE_SOURCE = 'Цени по СПА менюто: Бургас – декември 2025, Варна – февруари 2026.'

e = html.escape


# ------------------------------------------------------------------------------------------------
# Shared chrome
# ------------------------------------------------------------------------------------------------
EN_MAP = {'': 'en/', 'spa-burgas/': 'en/spa-burgas/', 'spa-varna/': 'en/spa-varna/', 'masazhi-burgas/': 'en/massages/',
          'ceni/': 'en/prices/', 'vaucheri/': 'en/vouchers/', 'promocii/varna/': 'en/promotions/varna/', 'kontakti/': 'en/contact/'}
BG_MAP = {v: k for k, v in EN_MAP.items()}
NAV_MAIN = [('spa-burgas/', 'Бургас'), ('spa-varna/', 'Варна'), ('masazhi-burgas/', 'Масажи'),
            ('terapii/', 'СПА терапии'), ('kozmetika-burgas/', 'Козметика'), ('ceni/', 'Цени'),
            ('kontakti/', 'Контакти')]
NAV_SUB = [('osteopatiya-burgas/', 'Остеопатия'), ('paketi/', 'Пакети'), ('vaucheri/', 'Ваучери'),
           ('promocii/', 'Промоции'), ('parvo-poseshtenie/', 'Първо посещение'), ('za-nas/', 'За нас'),
           ('blog/', 'Блог')]
PHONE_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 '
             '1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 '
             '1l-2.3 2.2Z"/></svg>')


def header(p, current='', path=''):
    nl = '\n          '

    def li(href, label):
        cur = ' aria-current="page"' if href == path else ' aria-current="true"' if href == current else ''
        return f'<li><a href="{p}{href}"{cur}>{e(label)}</a></li>'
    return f'''<header class="site-header">
    <div class="header-inner">
      <div class="header-left">
        <button class="menu-btn" type="button" aria-expanded="false" aria-controls="main-nav">
          <span class="menu-icon" aria-hidden="true"><span></span><span></span><span></span></span>
          <span class="menu-label">Меню</span>
        </button>
        <div class="lang" role="group" aria-label="Език / Language">
          <svg class="lang-ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3Z"/></svg>
          <a href="./" aria-current="true" lang="bg">BG</a>
          <a href="{p}{EN_MAP.get(path, 'en/')}" lang="en" hreflang="en">EN</a>
        </div>
      </div>

      <a class="logo" href="{p or './'}">
        <!-- TODO: swap for SVG once the vector logo is supplied -->
        <img src="{p}images/logo-horizontal.png" alt="Ability SPA" width="618" height="110">
      </a>

      <div class="header-right">
        <a class="header-phone" href="tel:{TEL_BURGAS}">{TEL_BURGAS_TXT}</a>
        <a class="lang-toggle" href="{p}{EN_MAP.get(path, 'en/')}" lang="en" hreflang="en" aria-label="English version">EN</a>
        <a class="btn btn-dark btn-book" href="{BOOK_BURGAS}">Резервирай</a>
      </div>
    </div>

    <nav class="main-nav" id="main-nav" aria-label="Основна навигация">
      <div class="nav-inner">
        <ul class="nav-main">
          {nl.join(li(h, l) for h, l in NAV_MAIN)}
        </ul>
        <div class="nav-side">
          <ul class="nav-sub">
            {nl.join(li(h, l) for h, l in NAV_SUB)}
          </ul>
          <div class="nav-call">
            <p>Обадете се</p>
            <a href="tel:{TEL_BURGAS}"><span>Бургас</span>{TEL_BURGAS_TXT}</a>
            <a href="tel:{TEL_VARNA}"><span>Варна</span>{TEL_VARNA_TXT}</a>
          </div>
        </div>
      </div>
    </nav>
  </header>'''


def footer(p):
    return f'''<footer class="site-footer" id="kontakti">
    <div class="container footer-grid">
      <div>
        <a class="logo logo-footer" href="{p or './'}">
          <img src="{p}images/logo-horizontal-light.png" alt="Ability SPA" width="618" height="110" loading="lazy">
        </a>
        <p class="footer-tag">Градски СПА център в Бургас и Варна.</p>
        <a class="btn btn-light footer-book" href="{BOOK_BURGAS}">Резервирай</a>
      </div>
      <div>
        <h2 class="footer-h">Изживявания</h2>
        <ul class="footer-links">
          <li><a href="{p}masazhi-burgas/">Масажи</a></li>
          <li><a href="{p}terapii/">СПА терапии</a></li>
          <li><a href="{p}kozmetika-burgas/">Козметика</a></li>
          <li><a href="{p}osteopatiya-burgas/">Остеопатия</a></li>
          <li><a href="{p}ceni/">Цени</a></li>
          <li><a href="{p}paketi/">Пакети</a></li>
          <li><a href="{p}parvo-poseshtenie/">Първо посещение</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-h">Бургас</h2>
        <p><a href="https://maps.google.com/?q=ул.+Александровска+21,+Бургас" rel="noopener">ул. „Александровска“ 21<br>хотел „България“</a></p>
        <p>Всеки ден, 07:00 – 22:00</p>
        <ul class="contact-list">
          <li><a href="tel:{TEL_BURGAS}">{TEL_BURGAS_TXT}</a></li>
          <li><a href="tel:{TEL_BURGAS2}">{TEL_BURGAS2_TXT}</a></li>
          <li><a href="mailto:abilityspa@mail.com">abilityspa@mail.com</a></li>
        </ul>
        <ul class="social">
          <li><a href="viber://chat?number=%2B359895635555">Viber</a></li>
          <li><a href="https://wa.me/359895635555" rel="noopener">WhatsApp</a></li>
          <li><a href="https://www.facebook.com/abilityspa" rel="noopener">Facebook</a></li>
          <li><a href="https://www.instagram.com/abilityspa/" rel="noopener">Instagram</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-h">Варна</h2>
        <p><a href="https://maps.google.com/?q=бул.+Сливница+33,+Варна" rel="noopener">бул. „Сливница“ 33<br>хотел „Черно море“</a></p>
        <p>Всеки ден, [07:00 или 09:00] – 21:00</p>
        <ul class="contact-list">
          <li><a href="tel:{TEL_VARNA}">{TEL_VARNA_TXT}</a></li>
          <li><a href="mailto:abilityspawellness@gmail.com">abilityspawellness@gmail.com</a></li>
        </ul>
        <ul class="social">
          <li><a href="viber://chat?number=%2B359899994149">Viber</a></li>
          <li><a href="https://wa.me/359899994149" rel="noopener">WhatsApp</a></li>
          <li><a href="https://www.facebook.com/profile.php?id=61583262998419" rel="noopener">Facebook</a></li>
          <li><a href="https://www.instagram.com/abilityspa.wellness/" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>© <span id="year">2026</span> Ability SPA &amp; Wellness</p>
      <p><a href="{p}vaucheri/">Ваучери</a> · <a href="{p}promocii/">Промоции</a> · <a href="{p}za-nas/">За нас</a> · <a href="{p}blog/">Блог</a> · <a href="{p}obshti-usloviya/">Общи условия</a> · <a href="{p}poveritelnost/">Поверителност</a> · <a href="{p}biskvitki/">Бисквитки</a></p>
    </div>
  </footer>

  <!-- Slim cookie bar: bottom only, never covers the hero text -->
  <div class="cookie-bar" id="cookie-bar" role="region" aria-label="Бисквитки" hidden>
    <p>Сайтът използва бисквитки. <a href="{p}biskvitki/">Научете повече</a></p>
    <button class="btn btn-light btn-sm" type="button" id="cookie-ok">Приемам</button>
  </div>'''


EN_NAV = [('en/spa-burgas/', 'Burgas'), ('en/spa-varna/', 'Varna'), ('en/massages/', 'Massages'), ('en/prices/', 'Prices'),
          ('en/vouchers/', 'Gift vouchers'), ('en/contact/', 'Contact')]


def en_header(p, path):
    nl = '\n          '
    lis = nl.join(f'<li><a href="{p}{h}"' + (' aria-current="page"' if h == path else '') + f'>{l}</a></li>' for h, l in EN_NAV)
    bg = p + BG_MAP.get(path, '')
    return f'''<header class="site-header">
    <div class="header-inner">
      <div class="header-left">
        <button class="menu-btn" type="button" aria-expanded="false" aria-controls="main-nav">
          <span class="menu-icon" aria-hidden="true"><span></span><span></span><span></span></span>
          <span class="menu-label">Menu</span>
        </button>
        <div class="lang" role="group" aria-label="Language / Език">
          <svg class="lang-ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3Z"/></svg>
          <a href="{bg or './'}" lang="bg" hreflang="bg">BG</a>
          <a href="./" aria-current="true" lang="en">EN</a>
        </div>
      </div>

      <a class="logo" href="{p}en/">
        <img src="{p}images/logo-horizontal.png" alt="Ability SPA" width="618" height="110">
      </a>

      <div class="header-right">
        <a class="header-phone" href="tel:{TEL_BURGAS}">{TEL_BURGAS_TXT}</a>
        <a class="lang-toggle" href="{bg or './'}" lang="bg" hreflang="bg" aria-label="Български сайт">BG</a>
        <a class="btn btn-dark btn-book" href="{BOOK_BURGAS}">Book</a>
      </div>
    </div>

    <nav class="main-nav" id="main-nav" aria-label="Main navigation">
      <div class="nav-inner">
        <ul class="nav-main">
          {lis}
        </ul>
        <div class="nav-side">
          <ul class="nav-sub">
            <li><a href="{p}en/promotions/varna/">Offers in Varna</a></li>
            <li><a href="{bg or './'}" lang="bg">Български сайт</a></li>
          </ul>
          <div class="nav-call">
            <p>Call us</p>
            <a href="tel:{TEL_BURGAS}"><span>Burgas</span>{TEL_BURGAS_TXT}</a>
            <a href="tel:{TEL_VARNA}"><span>Varna</span>{TEL_VARNA_TXT}</a>
          </div>
        </div>
      </div>
    </nav>
  </header>'''


def en_footer(p):
    return f'''<footer class="site-footer" id="contact">
    <div class="container footer-grid">
      <div>
        <a class="logo logo-footer" href="{p}en/">
          <img src="{p}images/logo-horizontal-light.png" alt="Ability SPA" width="618" height="110" loading="lazy">
        </a>
        <p class="footer-tag">City spa in Burgas and Varna, Bulgaria.</p>
        <a class="btn btn-light footer-book" href="{BOOK_BURGAS}">Book in Burgas</a>
      </div>
      <div>
        <h2 class="footer-h">Explore</h2>
        <ul class="footer-links">
          <li><a href="{p}en/massages/">Massages</a></li>
          <li><a href="{p}en/prices/">Prices</a></li>
          <li><a href="{p}en/vouchers/">Gift vouchers</a></li>
          <li><a href="{p}en/promotions/varna/">Offers in Varna</a></li>
          <li><a href="{p}en/contact/">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-h">Burgas</h2>
        <p><a href="https://maps.google.com/?q=ул.+Александровска+21,+Бургас" rel="noopener">21 Aleksandrovska St.<br>Hotel Bulgaria</a></p>
        <p>Daily, 07:00 – 22:00</p>
        <ul class="contact-list">
          <li><a href="tel:{TEL_BURGAS}">{TEL_BURGAS_TXT}</a></li>
          <li><a href="mailto:abilityspa@mail.com">abilityspa@mail.com</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-h">Varna</h2>
        <p><a href="https://maps.google.com/?q=бул.+Сливница+33,+Варна" rel="noopener">33 Slivnitsa Blvd.<br>Hotel Cherno More</a></p>
        <p>Daily, [07:00 or 09:00] – 21:00</p>
        <ul class="contact-list">
          <li><a href="tel:{TEL_VARNA}">{TEL_VARNA_TXT}</a></li>
          <li><a href="mailto:abilityspawellness@gmail.com">abilityspawellness@gmail.com</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>© <span id="year">2026</span> Ability SPA &amp; Wellness</p>
      <p><a href="{p}poveritelnost/" lang="bg">Privacy (BG)</a> · <a href="{p}biskvitki/" lang="bg">Cookies (BG)</a></p>
    </div>
  </footer>

  <div class="cookie-bar" id="cookie-bar" role="region" aria-label="Cookies" hidden>
    <p>This site uses cookies. <a href="{p}biskvitki/" lang="bg">Learn more</a></p>
    <button class="btn btn-light btn-sm" type="button" id="cookie-ok">OK</button>
  </div>'''


def head(path, title, desc, p, jsonld, noindex=False, og_image='images/og-spa-burgas.jpg', lang='bg'):
    assert len(title) <= 60, f'title too long ({len(title)}): {title}'
    assert len(desc) <= 155, f'description too long ({len(desc)}): {desc}'
    robots = '\n  <meta name="robots" content="noindex, follow">' if noindex else ''
    alt = ''
    pair = EN_MAP.get(path) if lang == 'bg' else BG_MAP.get(path)
    if pair is not None and not noindex:
        bg, en = (path, pair) if lang == 'bg' else (pair, path)
        alt = (f'\n  <link rel="alternate" hreflang="bg" href="{SITE}/{bg}">\n  <link rel="alternate" hreflang="en" href="{SITE}/{en}">'
               f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}/{bg}">')
    ld = '\n'.join(f'  <script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">{robots}
  <link rel="canonical" href="{SITE}/{path}">{alt}
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{"en_GB" if lang == "en" else "bg_BG"}">
  <meta property="og:site_name" content="Ability SPA">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{SITE}/{path}">
  <meta property="og:image" content="{SITE}/{og_image}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@400;500;600;700&display=swap&subset=cyrillic" rel="stylesheet">
  <script>(function (d) {{ d.classList.add('js');
    /* PROTOTYPE ONLY: colour palettes to compare (?palette=a…g), see js/main.js */
    try {{ var m = location.search.match(/[?&]palette=([a-g])/), v = m ? m[1] : sessionStorage.getItem('palette');
      if (m) sessionStorage.setItem('palette', v);
      if (v) {{ d.setAttribute('data-palette', v); d.setAttribute('data-palette-ui', ''); }} }} catch (e) {{}}
  }})(document.documentElement);</script>
  <link rel="stylesheet" href="{p}css/styles.css?v={ASSET_V}">
{ld}
</head>'''


def breadcrumb_ld(crumbs):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': f'{SITE}/{u}'}
                                for i, (u, n) in enumerate(crumbs)]}


def page(path, title, desc, body, crumbs, jsonld=(), current='', noindex=False, lang='bg'):
    depth = path.count('/')
    p = '../' * depth
    ld = [breadcrumb_ld(crumbs)] + list(jsonld)
    doc = f'''{head(path, title, desc, p, ld, noindex, lang=lang)}
<body>
  <a class="skip-link" href="#main">{"Skip to content" if lang == "en" else "Към съдържанието"}</a>

  {en_header(p, path) if lang == "en" else header(p, current, path)}

  <main id="main">
{body(p)}
  </main>

  {en_footer(p) if lang == "en" else footer(p)}

  <script src="{p}js/main.js?v={ASSET_V}" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc)
    return path


# ------------------------------------------------------------------------------------------------
# Components
# ------------------------------------------------------------------------------------------------
def crumbs_html(p, crumbs):
    items = []
    for i, (u, n) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{e(n)}</li>')
        else:
            items.append(f'<li><a href="{p}{u or "./"}">{e(n)}</a></li>' if u else f'<li><a href="{p or "./"}">{e(n)}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Навигационна пътека"><ol>{"".join(items)}</ol></nav>'


def img(p, src, alt, cls='photo', eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img class="{cls}" src="{p}{src}" alt="{e(alt)}" {load} decoding="async">'


def page_hero(p, crumbs, eyebrow, h1, lead, image=None, actions=None, meta=None):
    act = actions if actions is not None else [('btn-dark', BOOK_BURGAS, 'Резервирай')]
    btns = ''.join(f'<a class="btn {c} btn-arrow" href="{h if h.startswith(("http", "tel:", "viber:", "#")) else p + h}">{e(t)} <span aria-hidden="true">→</span></a>'
                   for c, h, t in act)
    meta_html = ''
    if meta:
        meta_html = '<dl class="svc-meta">' + ''.join(f'<div><dt>{e(k)}</dt><dd>{v}</dd></div>' for k, v in meta) + '</dl>'
    media = f'<div class="page-hero-media">{img(p, image[0], image[1], "photo", eager=True)}</div>' if image else ''
    return f'''    <section class="page-hero{" has-media" if image else ""}">
      <div class="container page-hero-grid">
        <div class="page-hero-text">
          {crumbs_html(p, crumbs)}
          <p class="eyebrow">{e(eyebrow)}</p>
          <h1>{h1}</h1>
          <p class="page-lead">{lead}</p>
          {meta_html}
          <div class="btn-row">{btns}</div>
        </div>
        {media}
      </div>
    </section>
'''


def section(inner, cls='', label=None, sid=None):
    a = f' aria-label="{e(label)}"' if label else ''
    i = f' id="{sid}"' if sid else ''
    return f'''    <section class="section {cls}"{i}{a}>
      <div class="container">
{inner}
      </div>
    </section>
'''


def head_block(eyebrow, h2, hid=None, intro=None):
    i = f' id="{hid}"' if hid else ''
    x = f'<p class="section-intro">{intro}</p>' if intro else ''
    return f'<div class="section-head"><p class="eyebrow">{e(eyebrow)}</p><h2{i}>{h2}</h2>{x}</div>'


def prose(paras):
    return '<div class="prose">' + ''.join(f'<p>{x}</p>' for x in paras) + '</div>'


def checklist(items):
    return '<ul class="checklist">' + ''.join(f'<li>{e(x)}</li>' for x in items) + '</ul>'


def price_rows(rows, note=None):
    """rows: (name, detail or None, price text)"""
    r = ''.join(f'<div><dt>{e(n)}' + (f' <span>{e(d)}</span>' if d else '') + f'</dt><dd>{e(pr)}</dd></div>' for n, d, pr in rows)
    n = f'<p class="price-note">{e(note)}</p>' if note else ''
    return f'{n}<dl class="price-list">{r}</dl>'


def cards(p, items):
    """items: (href, title, price, image or None, alt)"""
    out = []
    for i, (h, t, pr, im, alt) in enumerate(items):
        media = img(p, im, alt, 'exp-img') if im else '<div class="ph ph-massage" aria-hidden="true"></div>'
        out.append(f'''<li><a class="exp-card" href="{p}{h}">{media}<div class="exp-body"><p class="exp-num">{i + 1:02d}</p><h3>{e(t)}</h3><p class="exp-price">{e(pr)}</p><span class="exp-more">Научи повече <span aria-hidden="true">→</span></span></div></a></li>''')
    return f'<ul class="exp-grid">{"".join(out)}</ul>'


CITIES = {
    'bg': [dict(name='Бургас', title='Спа център в Бургас', href='spa-burgas/', hotel='хотел „България“', addr='ул. „Александровска“ 21',
                tel=(TEL_BURGAS, TEL_BURGAS_TXT),
                img='images/spa-burgas-basein-simetrichen', w=(640, 1080), alt='Закритият басейн в Ability Spa Бургас',
                has=['Басейн и джакузи', 'Сауна и парна баня', 'Фитнес', 'Масажи', 'Остеопатия', 'Козметични услуги'],
                hours='Всеки ден 07:00 – 22:00', cta=(BOOK_BURGAS, 'Резервирай онлайн')),
           dict(name='Варна', title='Уелнес във Варна', href='spa-varna/', hotel='хотел „Черно море“', addr='бул. „Сливница“ 33',
                tel=(TEL_VARNA, TEL_VARNA_TXT),
                img='images/library/2026_01_infrachervena_peika_ability-spa_varna', w=None, alt='Инфрачервената пейка в Ability Spa&Wellness Варна',
                has=['Сауна и солна парна баня', 'Инфрачервена пейка', 'Фитнес', 'Групови занимания', 'Масажи', 'Спа терапии'],
                hours='Всеки ден [07:00 или 09:00] – 21:00', cta=(f'tel:{TEL_VARNA}', 'Обадете се'))],
    'en': [dict(name='Burgas', title='Spa centre in Burgas', href='en/spa-burgas/', hotel='Hotel Bulgaria', addr='21 Aleksandrovska St.',
                tel=(TEL_BURGAS, TEL_BURGAS_TXT),
                img='images/spa-burgas-basein-simetrichen', w=(640, 1080), alt='The indoor pool at Ability Spa Burgas',
                has=['Pool & jacuzzi', 'Sauna & steam bath', 'Gym', 'Massages', 'Osteopathy', 'Beauty treatments'],
                hours='Daily 07:00 – 22:00', cta=(BOOK_BURGAS, 'Book online')),
           dict(name='Varna', title='Wellness in Varna', href='en/spa-varna/', hotel='Hotel Cherno More', addr='33 Slivnitsa Blvd.',
                tel=(TEL_VARNA, TEL_VARNA_TXT),
                img='images/library/2026_01_infrachervena_peika_ability-spa_varna', w=None, alt='The infrared bench at Ability Spa&Wellness Varna',
                has=['Sauna & salt steam bath', 'Infrared bench', 'Gym', 'Group classes', 'Massages', 'Spa therapies'],
                hours='Daily [07:00 or 09:00] – 21:00', cta=(f'tel:{TEL_VARNA}', 'Call to book'))],
}


ICON_PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
ICON_CLOCK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 3.5h3l1.5 4-2 1.3a11 11 0 0 0 6.1 6.1l1.3-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.6 5.7a2 2 0 0 1 2-2.2z"/></svg>'


CS_TEXT = {
    'bg': dict(label='Изберете обект', pause='Спри автоматичната смяна', play='Пусни автоматичната смяна',
               more='Повече за {}'),
    'en': dict(label='Choose a location', pause='Stop switching automatically', play='Switch automatically',
               more='More about {}'),
}


def city_switch(p, lang='bg'):
    """Бургас / Варна switch (homepage variant D): per city a title, what it has, address / hours / phone and two actions.
    Changes every 5 s (js/main.js, no visible timer), a pause button,
    pause on hover / focus / off-screen, stops for good once a city is picked, never moves for reduced motion.
    Without JS both cities simply show one under the other."""
    T, cs = CS_TEXT[lang], CITIES[lang]
    slug = lambda c: c['href'].rstrip('/').split('/')[-1].replace('spa-', '')
    tabs = ''.join(
        f'''<button class="cs-tab" type="button" role="tab" id="cs-tab-{slug(c)}" aria-controls="cs-panel-{slug(c)}" aria-selected="{str(i == 0).lower()}"{"" if i == 0 else ' tabindex="-1"'}>{e(c["name"])}<span class="cs-bar" aria-hidden="true"></span></button>'''
        for i, c in enumerate(cs))
    panels = []
    for i, c in enumerate(cs):
        if c['w']:
            src = f'src="{p}{c["img"]}-{c["w"][1]}.webp" srcset="{p}{c["img"]}-{c["w"][0]}.webp {c["w"][0]}w, {p}{c["img"]}-{c["w"][1]}.webp {c["w"][1]}w" sizes="(min-width: 1024px) 58vw, 100vw"'
        else:
            src = f'src="{p}{c["img"]}.webp"'
        has = ''.join(f'<li>{e(x)}</li>' for x in c['has'])
        ext = c['cta'][0].startswith(('http', 'tel:'))
        load = 'fetchpriority="high"' if i == 0 else 'loading="lazy"'
        arrow = ' <span aria-hidden="true">→</span>' if i == 0 else ''
        panels.append(f'''<div class="cs-panel{" is-active" if i == 0 else ""}" id="cs-panel-{slug(c)}" role="tabpanel" aria-labelledby="cs-tab-{slug(c)}">
          <div class="cs-media"><img {src} alt="{e(c["alt"])}" width="1080" height="1080" {load} decoding="async"></div>
          <div class="cs-body">
            <h2 class="cs-title">{e(c["title"])}</h2>
            <ul class="cs-has">{has}</ul>
            <ul class="cs-contact">
              <li>{ICON_PIN}{e(c["addr"])}, {e(c["hotel"])}</li>
              <li>{ICON_CLOCK}{e(c["hours"])}</li>
              <li>{ICON_PHONE}<a href="tel:{c["tel"][0]}">{e(c["tel"][1])}</a></li>
            </ul>
            <div class="btn-row"><a class="btn {"btn-light btn-arrow" if i == 0 else "btn-outline-light"}" href="{c["cta"][0] if ext else p + c["cta"][0]}">{e(c["cta"][1])}{arrow}</a><a class="cs-more" href="{p}{c["href"]}">{e(T["more"].format(c["name"]))} <span aria-hidden="true">→</span></a></div>
          </div>
        </div>''')
    return f'''<div class="city-switch" data-interval="5000">
          <div class="cs-controls">
            <div class="cs-tabs" role="tablist" aria-label="{e(T["label"])}">{tabs}</div>
            <button class="cs-pause" type="button" aria-pressed="false" data-pause="{e(T["pause"])}" data-play="{e(T["play"])}" aria-label="{e(T["pause"])}">
              <svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3v14H7zM14 5h3v14h-3z"/></svg>
              <svg class="i-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
            </button>
          </div>
          <div class="cs-panels">{"".join(panels)}</div>
        </div>'''


def cta_band(p, title='Готови за малко време за себе си?', text='Резервирайте онлайн за Бургас или ни се обадете за Варна.'):
    return f'''    <section class="cta-band" aria-label="Резервация">
      <div class="container"><div class="cta-band-inner">
        <div><h2>{title}</h2><p>{text}</p></div>
        <div class="btn-row">
          <a class="btn btn-dark btn-arrow" href="{BOOK_BURGAS}">Резервирай в Бургас <span aria-hidden="true">→</span></a>
          <a class="btn btn-outline" href="tel:{TEL_VARNA}">Варна: {TEL_VARNA_TXT}</a>
        </div>
      </div></div>
    </section>
'''


def related(p, title, links):
    lis = ''.join(f'<li><a class="tile" href="{p}{h}"><span class="tile-kicker">{e(k)}</span><span class="tile-title">{e(t)}</span><span class="tile-arrow" aria-hidden="true">→</span></a></li>' for h, k, t in links)
    return f'''    <nav class="tiles related" aria-label="{e(title)}">
      <div class="container"><p class="eyebrow">{e(title)}</p></div>
      <ul class="container tiles-list">{lis}</ul>
    </nav>
'''


# ------------------------------------------------------------------------------------------------
# Content: massages (texts from abilityspa.com/massages/*, prices from the spa menus)
# ------------------------------------------------------------------------------------------------
MASSAGES = [
    dict(slug='klasicheski-masazh', name='Класически масаж', title='Класически масаж в Бургас – 60 мин | Ability SPA',
         desc='Класически (шведски) масаж на цяло тяло в Ability SPA Бургас – 60 мин за 45 €, частичен 30 мин за 29 €. Отпуска мускулите и подобрява съня.',
         kw='класически масаж Бургас', img=('images/library/2025_06_masaj_abilityspa.webp', 'Класически масаж на гърба в Ability SPA Бургас'),
         intro=['Класическият масаж, известен още като шведски, е един от най-ефективните методи за профилактика на редица неразположения. Той въздейства комплексно върху мускулите, нормализира състоянието на ставите и сухожилията и ускорява регенерацията на тъканите.',
                'Масажът е цялостна терапия с мека музика, меко осветление и ароматни масла. Използват се различни техники – поглаждане, разтриване, потупване и вибрации.'],
         benefits=['Облекчава стреса и напрежението в мускулите', 'Подобрява циркулацията и лимфния поток', 'Премахва сковаността',
                   'Регенерира и подхранва тъканите', 'Спомага за по-добър сън', 'Успокоява мускулите и намалява болката', 'Стяга и изглажда кожата'],
         forwho=['При натрупана физическа и психическа умора', 'При скованост в определени зони на тялото', 'При ограничена подвижност на ставите',
                 'При главоболие и липса на тонус', 'При дископатия, дискови хернии, плексит, невралгия и мигрена'],
         burgas=[('60 мин', '45 €'), ('частичен, 30 мин', '29 €')], varna=[('60 мин', '45 €'), ('частичен, 30 мин', '29 €')], price_from='от 29 €'),
    dict(slug='dalbokotaken-masazh', name='Дълбокотъканен масаж', title='Дълбокотъканен масаж в Бургас | Ability SPA',
         desc='Дълбокотъканен масаж в Ability SPA Бургас и Варна – 60 мин за 49 €. Намалява мускулните спазми и подобрява обхвата на движение.',
         kw='дълбокотъканен масаж Бургас', img=('images/library/2024_07_ability389.webp', 'Масаж на гърба и раменете в Ability SPA'),
         intro=['Дълбокотъканният масаж работи с по-дълбоките слоеве на мускулите и съединителната тъкан. Подходящ е, когато напрежението е натрупано и не се освобождава с лек, релаксиращ масаж.'],
         benefits=['Намалява мускулните спазми', 'Подобрява обхвата на движение', 'Подобрява гъвкавостта на мускулите'],
         forwho=[], burgas=[('60 мин', '49 €')], varna=[('60 мин', '49 €')], price_from='49 €'),
    dict(slug='antitseluliten-masazh', name='Антицелулитен масаж', title='Антицелулитен масаж в Бургас | Ability SPA',
         desc='Антицелулитен масаж в Ability SPA Бургас – 60 мин за 49 €. Подобрява кръвообращението и лимфния дренаж; препоръчват се 5–10 сесии.',
         kw='антицелулитен масаж Бургас', img=('images/library/2023_07_aspa_014.webp', 'Масаж на тялото в Ability SPA Бургас'),
         intro=['Антицелулитният масаж използва поглаждащи, масажиращи и ритмични движения, за да раздвижи натрупванията от мастни депа и да изглади повърхността на кожата.',
                'Една сесия продължава 60 минути, а за максимален ефект се препоръчват между 5 и 10 сесии.'],
         benefits=['Подобрява кръвообращението', 'Стимулира производството на колаген и еластин', 'Премахва токсините', 'Стяга мускулите',
                   'Подобрява лимфния дренаж', 'Раздвижва сраствания между мускулите и кожата'],
         forwho=['Подходящ е за мъже и жени от всички възрасти, независимо от теглото и физическата им структура.'],
         burgas=[('60 мин', '49 €')], varna=[('60 мин', '49 €')], price_from='49 €'),
    dict(slug='sporten-masazh', name='Спортен масаж', title='Спортен масаж в Бургас | Ability SPA',
         desc='Спортен масаж в Ability SPA Бургас и Варна – 60 мин за 49 €. Подготовка преди натоварване, по-бързо възстановяване и по-малко травми.',
         kw='спортен масаж Бургас', img=('images/library/2024_07_aspa_427.webp', 'Масаж на гърба и раменете в Ability SPA'),
         intro=['Спортният масаж е техника, съсредоточена не върху релаксацията, а върху превенцията и лечението на травми и по-добрите спортни резултати.',
                'Комбинират се различни техники, включително разтягане, което отпуска мускулите и повишава гъвкавостта. Чрез дълбоко въздействие върху мускули, фасции и сухожилия тялото се подготвя за натоварване и се възстановява по-бързо.'],
         benefits=['Увеличава обхвата на движение на ставите', 'Намалява умората', 'Намалява напрежението в мускулите',
                   'Подобрява гъвкавостта на мускулите и сухожилията', 'Премахва дискомфорта и болката'],
         forwho=['За активно спортуващи – преди спортни занимания, за възстановяване след натоварване и за по-добър тренировъчен процес.'],
         burgas=[('60 мин', '49 €')], varna=[('60 мин', '49 €')], price_from='49 €'),
    dict(slug='aromaterapevtichen-masazh', name='Ароматерапевтичен масаж', title='Ароматерапевтичен масаж в Бургас | Ability SPA',
         desc='Ароматерапевтичен масаж с етерични масла в Ability SPA Бургас и Варна – 60 мин за 49 €. Намалява стреса и подобрява съня.',
         kw='ароматерапевтичен масаж Бургас', img=('images/library/2023_07_aspa_001.webp', 'Релаксиращ масаж със свещ в Ability SPA'),
         intro=['Ароматерапевтичният масаж облекчава напрежението в мускулите и стимулира кръвообращението, като към професионалните лосиони се добавят етерични масла.',
                'Ароматите им въздействат на нервната и лимфната система, а масажът подпомага абсорбирането им през кожата.'],
         benefits=['Укрепва организма и имунната система', 'Подобрява качеството на съня', 'Облекчава стреса и умората', 'Подобрява гъвкавостта на белези',
                   'Спомага за детоксикация', 'Намалява болезнеността на мускулите'],
         forwho=['Най-подходящ при повишен стрес или емоционален дисбаланс, при често главоболие, болка в кръста и ставите, безсъние и предменструален синдром.'],
         burgas=[('60 мин', '49 €')], varna=[('60 мин', '49 €')], price_from='49 €'),
    dict(slug='limfodrenazhen-masazh', name='Лимфодренажен масаж', title='Лимфодренажен масаж в Бургас | Ability SPA',
         desc='Лимфодренажен масаж в Ability SPA Бургас и Варна – 30 мин за 29 €. Подпомага детоксикацията и възстановяването.',
         kw='лимфодренаж Бургас', img=('images/library/2023_06_untitled-design-1.webp', 'Масаж със свещ и камъни в Ability SPA'),
         intro=['При ежедневно натоварване тъканите изпадат в спазъм и създават напрежение върху кръвоносната и лимфната система.',
                'С притискащи, изпомпващи и изцеждащи техники лимфодренажният масаж освобождава пътя на течностите, стимулира жлезите и изчистването на организма.'],
         benefits=['Подпомага детоксикацията на тялото', 'Повишава енергията и намалява тревожността', 'Подпомага следоперативното възстановяване', 'Възстановява тонуса при мускулна болка'],
         forwho=['За всеки, който иска детоксикация и по-добър тонус, спазва диета или фитнес режим, или се бори с лошо настроение и тревожност.'],
         burgas=[('30 мин', '29 €')], varna=[('30 мин', '29 €')], price_from='29 €'),
    dict(slug='refleksoterapiya', name='Рефлексотерапия', title='Рефлексотерапия (масаж на ходила) Бургас | Ability SPA',
         desc='Рефлексотерапия – точков масаж на ходилата в Ability SPA Бургас (30 мин, 28 €) и Варна (29 €). Отпуска и повишава енергията.',
         kw='рефлексотерапия Бургас', img=None,
         intro=['Рефлексотерапията (точков масаж или масаж на ходилата) стимулира вътрешните органи и кръвообращението чрез масаж на точки, които в най-голяма степен са съсредоточени в ходилата.',
                'Така се стимулират множество нервни рецептори, движението във вените и лимфната система, а тялото остава с усещане за лекота и бодрост.'],
         benefits=['Отпуска нервната система и повишава енергията', 'Стимулира жлезите с вътрешна секреция', 'Намалява отока при бременни жени', 'Спомага за по-добър сън',
                   'Помага при главоболие, болки в гърба, артрит и спортни травми', 'Помага при храносмилателни проблеми и стрес'],
         forwho=['При мигрена, нарушена функция на щитовидната жлеза, дерматологични проблеми, храносмилателни смущения и възпаление на мускули и сухожилия.'],
         burgas=[('30 мин', '28 €')], varna=[('30 мин', '29 €')], price_from='28 €'),
    dict(slug='terapevtichen-masazh', name='Терапевтичен масаж', title='Терапевтичен масаж в Бургас | Ability SPA',
         desc='Терапевтичен масаж в Ability SPA Бургас и Варна – 60 мин за 49 €. Отпуска мускулите, премахва схващането и облекчава болката.',
         kw='терапевтичен масаж Бургас', img=('images/masazh-goreshti-kamani-burgas-1080.webp', 'Масаж на раменете в Ability SPA Бургас'),
         intro=['Терапевтичният масаж е насочен към конкретни болезнени или схванати зони. Подходящ е, когато тялото има нужда не само от отпускане, а и от облекчаване на болката.'],
         benefits=['Отпуска мускулите', 'Премахва схващането', 'Облекчава болката'],
         forwho=[], burgas=[('60 мин', '49 €')], varna=[('60 мин', '49 €')], price_from='49 €'),
    dict(slug='presoterapiya', name='Пресотерапия', title='Пресотерапия в Бургас | Ability SPA',
         desc='Пресотерапия в Ability SPA Бургас – 30 мин за 23 €, пакет от 10 процедури за 179 €. Подобрява кръвообращението и състоянието на кожата.',
         kw='пресотерапия Бургас', img=None,
         intro=['Пресотерапията е апаратна процедура, която с ритмичен натиск подпомага кръвообращението и лимфния поток.'],
         benefits=['Подобрява кръвообращението', 'Елиминира токсините', 'Подобрява състоянието на кожата'],
         forwho=[], burgas=[('30 мин', '23 €'), ('пакет 10 × 30 мин', '179 €')], varna=[], price_from='23 €'),
]
VOLCANIC = ('terapii/vulkanichni-kamani/', 'Масаж с вулканични камъни', '49 € · 60 мин',
            'images/library/2025_10_masaj_vulkanichni_kamyni_ability.webp', 'Масаж с вулканични камъни в Ability SPA')


def build_massage(m):
    path = f'masazhi-burgas/{m["slug"]}/'
    crumbs = [('', 'Начало'), ('masazhi-burgas/', 'Масажи'), (path, m['name'])]
    b_price = ' · '.join(f'{d} – {pr}' for d, pr in m['burgas'])
    v_price = ' · '.join(f'{d} – {pr}' for d, pr in m['varna']) if m['varna'] else 'не се предлага'
    meta = [('Бургас', e(b_price)), ('Варна', e(v_price))]
    main_price = m['burgas'][0][1].replace(' €', '')

    def body(p):
        s = page_hero(p, crumbs, 'Масажи · Бургас и Варна', e(m['name']), e(m['intro'][0]),
                      image=m['img'], meta=meta,
                      actions=[('btn-dark', BOOK_BURGAS, 'Резервирай в Бургас')] + ([('btn-outline', f'tel:{TEL_VARNA}', 'Варна: обадете се')] if m['varna'] else []))
        blocks = ''
        if len(m['intro']) > 1:
            blocks += head_block('За масажа', 'Какво представлява') + prose(m['intro'][1:])
        cols = f'<div class="two-col"><div><h2 class="h3">Ползи</h2>{checklist(m["benefits"])}</div>'
        if m['forwho']:
            cols += f'<div><h2 class="h3">За кого е подходящ</h2>' + (checklist(m['forwho']) if len(m['forwho']) > 1 else prose(m['forwho'])) + '</div>'
        cols += '</div>'
        s += section(blocks + cols, cls='section-sand' if False else '')
        others = [x for x in MASSAGES if x['slug'] != m['slug']][:3]
        s += related(p, 'Други масажи', [(f'masazhi-burgas/{x["slug"]}/', x['price_from'], x['name']) for x in others])
        s += cta_band(p)
        return s
    service = {'@context': 'https://schema.org', '@type': 'Service', 'name': m['name'], 'serviceType': 'Масаж',
               'provider': {'@id': f'{SITE}/spa-burgas/#spa'}, 'areaServed': ['Бургас', 'Варна'] if m['varna'] else ['Бургас'],
               'offers': {'@type': 'Offer', 'price': main_price, 'priceCurrency': 'EUR'}}
    return page(path, m['title'], m['desc'], body, crumbs, [service], current='masazhi-burgas/')


def build_massages_hub():
    path = 'masazhi-burgas/'
    crumbs = [('', 'Начало'), (path, 'Масажи')]

    def body(p):
        s = page_hero(p, crumbs, 'Масажи · Бургас и Варна', 'Масажи в Бургас',
                      'Професионални масажи в центъра на Бургас, в хотел „България“ – от класически и дълбокотъканен до ароматерапевтичен и спортен. Същите масажи предлагаме и във Варна.',
                      image=('images/masazh-goreshti-kamani-burgas-1080.webp', 'Масаж с горещи камъни и свещ в Ability SPA Бургас'),
                      meta=[('Цени', 'от 28 € (30 мин) до 49 € (60 мин)'), ('Пакет', '5 × 60 мин – 195 €')])
        items = [(f'masazhi-burgas/{m["slug"]}/', m['name'], m['price_from'], m['img'][0] if m['img'] else None, m['img'][1] if m['img'] else '') for m in MASSAGES]
        items.insert(4, (VOLCANIC[0], VOLCANIC[1], VOLCANIC[2], VOLCANIC[3], VOLCANIC[4]))
        s += section(head_block('Изберете масаж', 'Нашите масажи', 'masazhi-title') + cards(p, items), label=None)
        rows = [(m['name'], ' · '.join(d for d, _ in m['burgas']), ' · '.join(pr for _, pr in m['burgas'])) for m in MASSAGES]
        rows.insert(4, ('Масаж с вулканични камъни', '60 мин', '49 €'))
        rows += [('Пакет от 5 масажа', '5 × 60 мин, в рамките на 60 дни', '195 €')]
        vrows = [('Класически частичен / на цяло тяло', '30 / 60 мин', '29 € / 45 €'), ('Ароматерапевтичен, антистрес, дълбокотъканен, терапевтичен, спортен, антицелулитен, с вулканични камъни', '60 мин', '49 €'),
                 ('Лимфодренажен, рефлексотерапия', '30 мин', '29 €'), ('Пакет от 5 масажа', '5 × 30 мин / 5 × 60 мин', '118 € / 195 €')]
        s += section(f'<div class="two-col">{head_block("Цени", "Цени на масажите")}<div>{price_rows(rows, "Ability Spa Бургас")}'
                     f'<div class="spacer"></div>{price_rows(vrows, "Ability Spa&Wellness Варна")}<p class="price-other">{PRICE_SOURCE} <a href="{PDF_B}" rel="noopener">Меню Бургас (PDF)</a> · <a href="{PDF_V}" rel="noopener">Меню Варна (PDF)</a></p></div></div>',
                     cls='section-sand', sid='ceni-masazhi')
        s += related(p, 'Още за вас', [('osteopatiya-burgas/', '59 € · 60 мин', 'Остеопатия'), ('terapii/', 'от 49 €', 'СПА терапии'), ('paketi/', 'от 52 €', 'Пакет „Релакс“')])
        s += cta_band(p)
        return s
    return page(path, 'Масаж в Бургас – цени и видове масажи | Ability SPA',
                'Масажи в центъра на Бургас: класически, дълбокотъканен, спортен, ароматерапевтичен, антицелулитен. От 28 €. Също и във Варна.', body, crumbs, current='masazhi-burgas/')


def build_osteopathy():
    path = 'osteopatiya-burgas/'
    crumbs = [('', 'Начало'), (path, 'Остеопатия')]

    def body(p):
        s = page_hero(p, crumbs, 'Остеопатия · Бургас', 'Остеопатия в Бургас',
                      'Остеопатията е система за диагностика и терапия на проблеми в мускулно-скелетната система, която засилва механизмите за самолечение на тялото.',
                      image=('images/osteopatiya-burgas-petar-damyanov-1080.webp', 'Диплома по остеопатия на Петър Дамянов'),
                      meta=[('Времетраене', '60 мин'), ('Цена', '59 €'), ('Пакет', '5 × 60 мин – 250 €')])
        s += section(head_block('За остеопатията', 'Холистичен подход към болката') + prose([
            'Целта е да се адресира причината за проблема и така да се предотврати повторната поява на болка, а не просто да се намалят симптомите.',
            'Остеопатът оценява състоянието на тъканите, долавя ритъма им на движение и така поставя диагноза и подтиква организма към самооздравяване.']) +
            '<div class="two-col"><div><h2 class="h3">Ползи</h2>' + checklist([
                'Подобрява кръвообращението и биомеханиката на частите на тялото с дисбаланс',
                'Подобрява подвижността и стабилността на опорно-двигателния апарат',
                'Подобрява функционирането на нервната система и лимфообращението']) +
            '</div><div><h2 class="h3">При какви оплаквания</h2>' + prose([
                'Методът е подходящ за широк спектър от проблеми – храносмилателни проблеми, главоболие, бронхиална астма, промени по време на бременност, мигрени, храносмилателни и сърдечно-съдови разстройства.']) + '</div></div>')
        s += section('<div class="two-col">' + head_block('Нашият специалист', 'Петър Дамянов') + prose([
            'Един от малкото остеопати в България. Завършва остеопатия в Санкт Петербург, в Института по остеопатична медицина „Владимир Андриянов“, където се обучава при едни от най-добрите остеопати и преподаватели в Русия и Европа.',
            'Получава диплома и от Френския институт по остеопатия и е практически първият българин, завършил остеопатия в Русия. Самият той казва „завършил“ в кавички – според него обучението е безкрайно.']) + '</div>', cls='section-sand')
        s += related(p, 'Прочетете още', [('blog/petar-damyanov-osteopatia/', 'Блог', 'Петър Дамянов за остеопатията'),
                                          ('blog/osteopatia-kak-pomaga/', 'Блог', 'Що е то остеопатия и как помага?'),
                                          ('masazhi-burgas/', 'от 28 €', 'Масажи')])
        s += cta_band(p)
        return s
    service = {'@context': 'https://schema.org', '@type': 'Service', 'name': 'Остеопатия', 'provider': {'@id': f'{SITE}/spa-burgas/#spa'},
               'areaServed': 'Бургас', 'offers': {'@type': 'Offer', 'price': '59', 'priceCurrency': 'EUR'}}
    return page(path, 'Остеопатия в Бургас – Петър Дамянов | Ability SPA',
                'Остеопатия в Ability SPA Бургас с Петър Дамянов – 60 мин за 59 €, пакет 5 процедури за 250 €. Холистичен подход към болката.', body, crumbs, [service], current='osteopatiya-burgas/')


# ------------------------------------------------------------------------------------------------
# Locations
# ------------------------------------------------------------------------------------------------
def zone_split(p, image, alt, kicker, h3, text, items, link=None, rev=False):
    lk = f'<a class="btn btn-outline btn-arrow" href="{p}{link[0]}">{e(link[1])} <span aria-hidden="true">→</span></a>' if link else ''
    fl = '<ul class="feature-list">' + ''.join(f'<li>{e(x)}</li>' for x in items) + '</ul>' if items else ''
    return f'''<article class="split{" split-rev" if rev else ""}">
          {img(p, image, alt)}
          <div class="split-text"><p class="kicker">{e(kicker)}</p><h3>{h3}</h3><p>{text}</p>{fl}{lk}</div>
        </article>'''


def build_burgas():
    path = 'spa-burgas/'
    crumbs = [('', 'Начало'), (path, 'Бургас')]

    def body(p):
        s = page_hero(p, crumbs, 'Ability Spa · хотел „България“', 'СПА център в&nbsp;Бургас',
                      'В сърцето на Бургас, в обновения хотел „България“ – уютна обстановка, индивидуално подбрани процедури, качествени продукти и висококвалифицирани специалисти.',
                      image=('images/spa-burgas-basein-simetrichen-1080.webp', 'Закритият басейн на Ability Spa Бургас с осветена синя стена'),
                      meta=[('Адрес', 'ул. „Александровска“ 21'), ('Работно време', 'всеки ден, 07:00 – 22:00'), ('Телефон', f'<a href="tel:{TEL_BURGAS}">{TEL_BURGAS_TXT}</a>')],
                      actions=[('btn-dark', BOOK_BURGAS, 'Резервирай'), ('btn-outline', '#zoni', 'Разгледай зоните')])
        z = head_block('Зони', 'Всичко на едно място', 'zoni-h')
        z += zone_split(p, 'images/finlandska-sauna-burgas-1080.webp', 'Финландската сауна в Ability Spa Бургас', 'Термална зона',
                        'Сауни, парна баня и&nbsp;релакс', 'Спокойна и елегантна атмосфера, вдъхновена от топлина и хармония.',
                        ['Билкова сауна', 'Финландска сауна', 'Класическа парна баня', 'Релакс зона'], ('spa-burgas/termalna-zona/', 'Термалната зона'))
        z += zone_split(p, 'images/spa-burgas-dzhakuzi-basein-1080.webp', 'Джакузито и закритият басейн', 'Басейн и джакузи',
                        'Вода за цялото семейство', 'Топъл закрит басейн с релакс зона и джакузи, а за най-малките – детски басейн с температура 32–33&nbsp;°C.',
                        ['Закрит басейн', 'Джакузи', 'Детски басейн 32–33 °C'], ('spa-burgas/basein/', 'Басейнът'), rev=True)
        z += zone_split(p, 'images/library/2026_01_parna_banya_ability_spa.webp', 'Входът на парната баня в Ability Spa', 'Хамам', 'Турска баня',
                        'Парна баня, пилинг с кесе и пенен масаж – вековен ритуал за релакс и пречистване.', ['45 мин – 55 €'], ('spa-burgas/hamam/', 'Хамамът'))
        z += zone_split(p, 'images/spa-burgas-fitnes-technogym-zala-1080.webp', 'Фитнес зала с уреди Technogym', 'Фитнес',
                        'Technogym и протеинов бар', 'Модерна фитнес зала с уреди Technogym; протеиновият бар до басейна предлага хранителни добавки.',
                        ['Еднократна тренировка – 5 €', 'Месечна карта – 35 €', 'Multisport в делнични дни'], ('fitnes-burgas/', 'Фитнесът'), rev=True)
        z += zone_split(p, 'images/spa-burgas-solna-staya-960.webp', 'Солната стая с шезлонги', 'Солна стая', 'Релакс солна зона',
                        'Тиха солна зона за отпускане и незабравимо СПА изживяване.', ['40 мин – 12 €'], ('spa-burgas/solna-staya/', 'Солната стая'))
        z += zone_split(p, 'images/library/2022_11_untitled-design-2.webp', 'Барът до басейна', 'Бар', 'Бар до басейна',
                        'Ароматно кафе, истински билков чай, безалкохолни напитки, фрешове, бира и вино, както и хранителни добавки, сандвичи и торти.', [], None, rev=True)
        s += section(z, cls='facilities', sid='zoni')
        s += section(head_block('Процедури', 'Масажи, терапии и&nbsp;козметика') + cards(p, [
            ('masazhi-burgas/', 'Масажи', 'от 28 €', 'images/masazh-goreshti-kamani-burgas-1080.webp', 'Масаж с горещи камъни'),
            ('terapii/', 'СПА терапии', 'от 49 €', 'images/terapiya-vulkanichni-kamani-1080.webp', 'Терапия с вулканични камъни'),
            ('kozmetika-burgas/', 'Козметика', 'от 8 €', 'images/kozmetika-terapiya-za-litse-burgas-1080.webp', 'Терапия за лице'),
            ('osteopatiya-burgas/', 'Остеопатия', '59 € · 60 мин', 'images/osteopatiya-burgas-petar-damyanov-1080.webp', 'Остеопатия')]), cls='section-sand')
        s += section('<div class="two-col">' + head_block('Цени', 'СПА достъп') + '<div>' + price_rows([
            ('Еднократно посещение', 'термална зона, басейн и джакузи или солна стая', '12 €'), ('Деца 3–14 г.', 'еднократно посещение', '6 €'),
            ('Дневна СПА карта', 'фитнес, басейн, джакузи и термална зона', '19 €'), ('Дневна СПА карта за двама', None, '35 €'),
            ('Месечна СПА карта', 'понеделник – петък / понеделник – неделя', '110 € / 145 €'), ('Хавлия / халат', 'една хавлия е безплатна', '2 € / 3 €')],
            'Ability Spa Бургас') + f'<p class="price-other"><a href="{p}ceni/">Всички цени →</a> · Multisport: делнични дни, 07:00–22:00</p></div></div>')
        s += section('<div class="two-col">' + head_block('Как да ни намерите', 'Хотел „България“, центъра на Бургас') + prose([
            'ул. „Александровска“ 21, гр. Бургас · всеки ден 07:00 – 22:00',
            f'<a href="tel:{TEL_BURGAS}">{TEL_BURGAS_TXT}</a> · <a href="tel:{TEL_BURGAS2}">{TEL_BURGAS2_TXT}</a> · <a href="mailto:abilityspa@mail.com">abilityspa@mail.com</a>',
            '<a href="https://maps.google.com/?q=ул.+Александровска+21,+Бургас" rel="noopener">Отвори в Google Maps →</a>']) + '</div>', cls='section-sand')
        s += cta_band(p)
        return s
    spa = {'@context': 'https://schema.org', '@type': 'DaySpa', '@id': f'{SITE}/spa-burgas/#spa', 'name': 'Ability Spa – Бургас',
           'url': f'{SITE}/spa-burgas/', 'telephone': TEL_BURGAS, 'email': 'abilityspa@mail.com', 'priceRange': '$$', 'currenciesAccepted': 'EUR',
           'address': {'@type': 'PostalAddress', 'streetAddress': 'ул. „Александровска“ 21, хотел „България“', 'addressLocality': 'Бургас', 'addressCountry': 'BG'},
           'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': '07:00', 'closes': '22:00'}],
           'sameAs': ['https://www.facebook.com/abilityspa', 'https://www.instagram.com/abilityspa/']}
    return page(path, 'СПА център в Бургас – хотел България | Ability SPA',
                'СПА център в центъра на Бургас: басейн, джакузи, сауни, хамам, солна стая, фитнес, масажи и козметика. Всеки ден 07:00–22:00.', body, crumbs, [spa], current='spa-burgas/')


def build_varna():
    path = 'spa-varna/'
    crumbs = [('', 'Начало'), (path, 'Варна')]

    def body(p):
        s = page_hero(p, crumbs, 'Ability Spa&Wellness · хотел „Черно море“', 'СПА център във&nbsp;Варна',
                      'Ability SPA&Wellness посреща гостите си в сърцето на Варна – в емблематичния хотел „Черно море“: СПА зона, модерна фитнес зала, групови тренировки, масажи и терапии.',
                      image=('images/hotel-cherno-more-varna-1080.webp', 'Хотел „Черно море“ във Варна'),
                      meta=[('Адрес', 'бул. „Сливница“ 33'), ('Работно време', 'всеки ден, [07:00 или 09:00] – 21:00'), ('Телефон', f'<a href="tel:{TEL_VARNA}">{TEL_VARNA_TXT}</a>'), ('Паркинг', 'платен, към хотела')],
                      actions=[('btn-dark', f'tel:{TEL_VARNA}', 'Обадете се за час'), ('btn-outline', 'viber://chat?number=%2B359899994149', 'Viber')])
        z = head_block('Зони', 'Термална зона, фитнес и&nbsp;релакс')
        z += zone_split(p, 'images/library/2026_01_termalna_zona_abilitwellness_varna.webp', 'Термалната зона на Ability Spa&Wellness Варна', 'Термална зона',
                        'Топлина, тишина и&nbsp;спокойствие', 'Място за истинско възстановяване в елегантна атмосфера, създадена за релакс, детоксикация и презареждане.',
                        ['Финландска (суха) сауна', 'Билкова сауна', 'Парна / солна парна баня', 'Инфрачервена пейка'], ('spa-varna/termalna-zona/', 'Термалната зона'))
        z += zone_split(p, 'images/library/2026_01_fitnes_abilityspawellness_varna.webp', 'Фитнес залата с изглед във Варна', 'Фитнес',
                        'Technogym', 'Висок клас уреди Technogym за силови и кардио упражнения – за интензивни тренировки и за активен, здравословен начин на живот.',
                        ['Еднократна тренировка – 8 €', 'Месечна карта – 50 €'], ('spa-varna/fitnes/', 'Фитнесът'), rev=True)
        z += zone_split(p, 'images/library/2026_01_grupovi_zanimanie_abilityspawellness.webp', 'Групова тренировка по йога', 'Групови тренировки',
                        'Йога, пилатес, kango jumps, табата', 'Под ръководството на опитни инструктори – за различни нива и цели.',
                        ['Еднократна тренировка – 12 €', '10 посещения – 100 €'], ('spa-varna/grupovi-trenirovki/', 'Груповите тренировки'))
        z += zone_split(p, 'images/library/2026_01_relax_zona_abilityspawellness_varna.webp', 'Релакс зоната с шезлонги и камина', 'Релакс зона',
                        'Шезлонги и камина', 'Мека светлина, топлината на огъня и тишина – за почивка след процедура или тренировка.', [], None, rev=True)
        s += section(z, cls='facilities')
        s += section('<div class="two-col">' + head_block('Цени', 'СПА и фитнес във Варна') + '<div>' + price_rows([
            ('СПА – еднократно посещение', None, '15 €'), ('СПА – еднократно посещение за двама', None, '27 €'), ('СПА и фитнес – еднократно посещение', None, '20 €'),
            ('Масажи', '30 / 60 мин', 'от 29 €'), ('СПА терапии', '90 мин', '78 €'), ('СПА пакет за двама „Абилити“', '2 масажа × 60 мин + 2 дневни СПА карти', '100 €')],
            'Ability Spa&Wellness Варна') + f'<p class="price-other"><a href="{p}ceni/#varna">Всички цени →</a> · <a href="{PDF_V}" rel="noopener">Меню Варна (PDF)</a></p></div></div>', cls='section-sand')
        s += section(head_block('Процедури', 'Масажи и&nbsp;терапии във Варна') + cards(p, [
            ('masazhi-varna/', 'Масажи във Варна', 'от 29 €', 'images/library/2023_07_aspa_001.webp', 'Релаксиращ масаж'),
            ('terapii/gold-amber/', 'Gold Amber', '78 € · 90 мин', 'images/library/2026_06_terapia_gold_amber.webp', 'Терапия Gold Amber'),
            ('terapii/bulgarian-rose/', 'Bulgarian Rose', '78 € · 90 мин', 'images/library/2026_06_terapia_bulgarian_rose-1.webp', 'Терапия Bulgarian Rose'),
            ('terapii/lavender-touch/', 'Lavender Touch', '78 € · 90 мин', 'images/library/2026_06_terapia_lavender_touch.webp', 'Терапия Lavender Touch')]))
        s += section('<div class="two-col">' + head_block('Как да ни намерите', 'Хотел „Черно море“, Варна') + prose([
            'бул. „Сливница“ 33, гр. Варна · платен паркинг към хотела',
            f'<a href="tel:{TEL_VARNA}">{TEL_VARNA_TXT}</a> · <a href="mailto:abilityspawellness@gmail.com">abilityspawellness@gmail.com</a>',
            'Засега резервации за Варна се правят по телефона, във Viber или WhatsApp.',
            '<a href="https://maps.google.com/?q=бул.+Сливница+33,+Варна" rel="noopener">Отвори в Google Maps →</a>']) + '</div>', cls='section-sand')
        s += cta_band(p, 'Запазете час във Варна', 'Обадете се или ни пишете във Viber / WhatsApp.')
        return s
    spa = {'@context': 'https://schema.org', '@type': 'DaySpa', '@id': f'{SITE}/spa-varna/#spa', 'name': 'Ability Spa&Wellness – Варна',
           'url': f'{SITE}/spa-varna/', 'telephone': TEL_VARNA, 'email': 'abilityspawellness@gmail.com', 'priceRange': '$$', 'currenciesAccepted': 'EUR',
           'address': {'@type': 'PostalAddress', 'streetAddress': 'бул. „Сливница“ 33, хотел „Черно море“', 'addressLocality': 'Варна', 'addressCountry': 'BG'},
           'sameAs': ['https://www.facebook.com/profile.php?id=61583262998419', 'https://www.instagram.com/abilityspa.wellness/']}
    return page(path, 'СПА център във Варна – хотел Черно море | Ability SPA',
                'СПА център в хотел „Черно море“, Варна: сауни, инфрачервена пейка, фитнес Technogym, йога и пилатес, масажи и СПА терапии.', body, crumbs, [spa], current='spa-varna/')


# ------------------------------------------------------------------------------------------------
# Prices, contacts, vouchers
# ------------------------------------------------------------------------------------------------
def build_prices():
    path = 'ceni/'
    crumbs = [('', 'Начало'), (path, 'Цени')]
    B = {
        'СПА и СПА карти': [
            ('Термална зона', 'сауна, билкова сауна и парна баня · еднократно', '12 €'), ('Басейн и джакузи', 'еднократно', '12 €'), ('Солна стая', 'еднократно, 40 мин', '12 €'),
            ('Деца 3–14 г.', 'еднократно посещение на зона', '6 €'), ('10 / 15 / 20 посещения', 'на зона', '95 € / 120 € / 140 €'),
            ('Дневна СПА карта', 'фитнес, басейн, джакузи и термална зона', '19 €'), ('Дневна СПА карта за двама', None, '35 €'), ('Дневна СПА карта – деца 3–14 г.', None, '11 €'),
            ('Месечна СПА карта', 'понеделник – петък', '110 €'), ('Месечна СПА карта', 'понеделник – неделя', '145 €'), ('Годишна СПА карта', None, '1304 €'),
            ('Пакет 10 / 15 / 20 СПА посещения', 'фитнес, басейн, джакузи, сауни и парна баня · 90 дни', '145 € / 192 € / 235 €'),
            ('Хавлия / халат', 'една хавлия е безплатна', '2 € / 3 €')],
        'Фитнес': [('Еднократна тренировка', None, '5 €'), ('10 тренировки', None, '39 €'), ('Месечна карта', None, '35 €'), ('3 месеца / 6 месеца', None, '90 € / 166 €'), ('Годишна карта', None, '297 €')],
        'Масажи и остеопатия': [(m['name'], ' · '.join(d for d, _ in m['burgas']), ' · '.join(pr for _, pr in m['burgas'])) for m in MASSAGES] +
                               [('Масаж с вулканични камъни', '60 мин', '49 €'), ('Остеопатия', '60 мин', '59 €'), ('Пакет 5 масажа', '5 × 60 мин', '195 €'), ('Пакет 5 × остеопатия', '5 × 60 мин', '250 €')],
        'СПА терапии и ритуали': [('Плодова терапия „Ability Spa“', '60 мин', '55 €'), ('Fitness Nuts · Coffee Time · Chocolate Dream · Sea Kissed', '60 мин', '49 €'),
                                  ('Хамам', 'турска баня, пилинг и пенен масаж · 45 мин', '55 €'), ('Терапия „Поморие“', 'турска баня, кална апликация и лек масаж · 45 мин', '55 €')],
        'Пакети': [('„Фитнес“', 'месечна фитнес карта + 5 посещения термална зона', '72 €'), ('„Здраве“', 'месечна фитнес карта + 5 посещения солна стая', '72 €'),
                   ('„Спорт“', 'месечна фитнес карта + 3 спортни масажа', '150 €'), ('„Релакс“', 'дневна СПА карта + релаксиращ масаж 60 мин', '52 €'),
                   ('„Красота“', 'хамам + ароматерапевтичен масаж + почистване на лице', '120 €'), ('„Абилити Дама“', 'почистване на лице + масаж с вулканични камъни + цял ден СПА', '92 €'),
                   ('„Абилити Джентълмен“', 'масаж на лице + хамам + цял ден СПА', '87 €'), ('СПА пакет за двама „Абилити“', '2 масажа на цяло тяло + цял ден СПА + солна стая + бутилка вино', '120 €')],
    }
    V = {
        'СПА и фитнес': [('Фитнес – еднократно', None, '8 €'), ('Фитнес – 10 тренировки', None, '60 €'), ('Фитнес – месечна / 3 / 6 месеца', None, '50 € / 128 € / 205 €'), ('Фитнес – годишна', None, '358 €'),
                         ('СПА – еднократно', None, '15 €'), ('СПА – еднократно за двама', None, '27 €'), ('СПА – 10 / 15 / 20 посещения', None, '143 € / 195 € / 247 €'),
                         ('Фитнес и СПА – еднократно', None, '20 €'), ('Фитнес и СПА – 10 / 15 / 20 посещения', None, '185 € / 246 € / 287 €'),
                         ('Фитнес и СПА – месечна', 'понеделник – петък / понеделник – неделя', '103 € / 123 €'), ('Фитнес и СПА – годишна', None, '1125 €'),
                         ('Хавлия / халат', 'една хавлия е безплатна', '2 € / 3 €')],
        'Групови занимания': [('Еднократна тренировка', None, '12 €'), ('10 / 15 / 20 посещения', 'в рамките на 30 дни, може от повече от един човек', '100 € / 135 € / 160 €')],
        'Масажи': [('Класически частичен', '30 мин', '29 €'), ('Класически на цяло тяло', '60 мин', '45 €'),
                   ('Ароматерапевтичен · Антистрес · С вулканични камъни · Дълбокотъканен · Терапевтичен · Спортен · Антицелулитен', '60 мин', '49 €'),
                   ('Лимфодренажен · Рефлексотерапия', '30 мин', '29 €'), ('Пакет 5 масажа', '5 × 30 мин / 5 × 60 мин', '118 € / 195 €')],
        'СПА терапии и пакети': [('Gold Amber · Плодова „Ability Spa“ · Chocolate Dream · Lavender Touch · Bulgarian Rose', '90 мин', '78 €'),
                                 ('„Фитнес“', 'месечна фитнес карта + 5 СПА посещения', '110 €'), ('„Спорт“', 'месечна фитнес карта + 3 спортни масажа', '180 €'),
                                 ('„Релакс“', 'дневна СПА карта + релаксиращ масаж 60 мин', '50 €'), ('СПА пакет за двама „Абилити“', '2 масажа × 60 мин + 2 дневни СПА карти', '100 €'),
                                 ('„Абилити Джентълмен“', 'антистрес масаж 60 мин + дневна СПА карта', '60 €'), ('„Абилити Дама“', 'Chocolate Dream 90 мин + дневна СПА карта', '85 €')],
    }

    def body(p):
        s = page_hero(p, crumbs, 'Цени · Бургас и Варна', 'СПА цени в Бургас и Варна',
                      'Всички цени на едно място – СПА достъп, карти, фитнес, масажи, терапии и пакети. Цените са в евро.',
                      actions=[('btn-dark', '#burgas', 'Бургас'), ('btn-outline', '#varna', 'Варна')])
        blocks = ''.join(f'<div class="price-group"><h3>{e(k)}</h3>{price_rows(v)}</div>' for k, v in B.items())
        s += section(head_block('Ability Spa · хотел „България“', 'Цени – Бургас', 'burgas') +
                     f'<p class="price-other">Козметичните процедури и терапиите за лице (от 8 €) са в <a href="{p}kozmetika-burgas/">Козметика</a>. <a href="{PDF_B}" rel="noopener">Пълно меню Бургас (PDF)</a></p>' +
                     f'<div class="price-groups">{blocks}</div>', sid='burgas-sec')
        blocks = ''.join(f'<div class="price-group"><h3>{e(k)}</h3>{price_rows(v)}</div>' for k, v in V.items())
        s += section(head_block('Ability Spa&Wellness · хотел „Черно море“', 'Цени – Варна', 'varna') +
                     f'<p class="price-other"><a href="{PDF_V}" rel="noopener">Пълно меню Варна (PDF)</a></p><div class="price-groups">{blocks}</div>', cls='section-sand', sid='varna-sec')
        s += section(prose([PRICE_SOURCE + ' Промоционалните цени са в <a href="' + p + 'promocii/">Промоции</a>. Карти Multisport се приемат в делнични дни, 07:00–22:00.']))
        s += cta_band(p)
        return s
    return page(path, 'СПА цени в Бургас и Варна | Ability SPA',
                'СПА цени на Ability SPA в Бургас и Варна: дневна СПА карта от 19 €, масажи от 28 €, фитнес, терапии и пакети. Всички цени в евро.', body, crumbs, current='ceni/')


def build_contacts():
    path = 'kontakti/'
    crumbs = [('', 'Начало'), (path, 'Контакти')]

    def loc(cid, name, hotel, addr, hours, phones, email, maps, book, social):
        ph = ''.join(f'<li><a href="tel:{t}">{e(x)}</a></li>' for t, x in phones)
        so = ''.join(f'<li><a href="{h}" rel="noopener">{e(n)}</a></li>' for h, n in social)
        return f'''<article class="contact-card" id="{cid}">
          <h2 class="h3">{e(name)}</h2><p class="kicker">{e(hotel)}</p>
          <dl class="svc-meta"><div><dt>Адрес</dt><dd><a href="{maps}" rel="noopener">{e(addr)}</a></dd></div><div><dt>Работно време</dt><dd>{e(hours)}</dd></div>
          <div><dt>Телефон</dt><dd><ul class="contact-list">{ph}</ul></dd></div><div><dt>Имейл</dt><dd><a href="mailto:{email}">{email}</a></dd></div></dl>
          <ul class="social">{so}</ul>
          <div class="btn-row">{book}</div>
        </article>'''

    def body(p):
        s = page_hero(p, crumbs, 'Контакти', 'Контакти – Бургас и Варна',
                      'Два обекта в центъра на двата града. Резервирайте онлайн за Бургас или се свържете с нас по телефона, във Viber или WhatsApp.', actions=[])
        b = loc('burgas', 'Ability Spa – Бургас', 'хотел „България“', 'ул. „Александровска“ 21, Бургас', 'всеки ден, 07:00 – 22:00',
                [(TEL_BURGAS, TEL_BURGAS_TXT), (TEL_BURGAS2, TEL_BURGAS2_TXT)], 'abilityspa@mail.com', 'https://maps.google.com/?q=ул.+Александровска+21,+Бургас',
                f'<a class="btn btn-dark btn-arrow" href="{BOOK_BURGAS}">Резервирай онлайн <span aria-hidden="true">→</span></a>',
                [('viber://chat?number=%2B359895635555', 'Viber'), ('https://wa.me/359895635555', 'WhatsApp'), ('https://www.facebook.com/abilityspa', 'Facebook'), ('https://www.instagram.com/abilityspa/', 'Instagram')])
        v = loc('varna', 'Ability Spa&Wellness – Варна', 'хотел „Черно море“', 'бул. „Сливница“ 33, Варна', 'всеки ден, [07:00 или 09:00] – 21:00',
                [(TEL_VARNA, TEL_VARNA_TXT)], 'abilityspawellness@gmail.com', 'https://maps.google.com/?q=бул.+Сливница+33,+Варна',
                f'<a class="btn btn-dark" href="tel:{TEL_VARNA}">Обадете се за час</a>',
                [('viber://chat?number=%2B359899994149', 'Viber'), ('https://wa.me/359899994149', 'WhatsApp'), ('https://www.facebook.com/profile.php?id=61583262998419', 'Facebook'), ('https://www.instagram.com/abilityspa.wellness/', 'Instagram')])
        s += section(f'<div class="contact-grid-2">{b}{v}</div>')
        s += related(p, 'Полезно', [('parvo-poseshtenie/', 'Преди да дойдете', 'Първо посещение'), ('ceni/', 'от 12 €', 'Цени'), ('vaucheri/', 'Подарете', 'Ваучери')])
        return s
    return page(path, 'Контакти – Ability SPA Бургас и Варна',
                'Контакти на Ability SPA: Бургас, ул. Александровска 21 (хотел България) и Варна, бул. Сливница 33 (хотел Черно море). Телефони и часове.', body, crumbs, current='kontakti/')


def build_vouchers():
    path = 'vaucheri/'
    crumbs = [('', 'Начало'), (path, 'Ваучери')]

    def body(p):
        s = page_hero(p, crumbs, 'Подаръчни ваучери', 'СПА ваучер за подарък',
                      'Зарадвайте любимите хора с подаръчен ваучер от Ability SPA – за конкретна услуга, пакет или просто заредена сума. Валиден е една година от датата на покупката.',
                      actions=[('btn-dark', f'tel:{TEL_BURGAS}', 'Поръчайте: Бургас'), ('btn-outline', f'tel:{TEL_VARNA}', 'Поръчайте: Варна')])
        s += section(f'''<div class="voucher">
          <div class="voucher-card" aria-hidden="true"><img class="vc-logo" src="{p}images/ability-spa-logo-light.png" alt="" loading="lazy"><p class="vc-title">Подаръчен ваучер</p></div>
          <div class="voucher-text">{head_block("Как работи", "Три вида ваучери")}{checklist(["Услуга – масаж, терапия, хамам или процедура за лице",
            "Пакет – напр. „Релакс“ (52 €) или „СПА пакет за двама“ (120 € в Бургас, 100 € във Варна)", "Сума по избор – получателят сам избира как да я използва"])}
          <p class="price-other">Валидност: 1 година от датата на покупката. [НАЧИН НА ПОКУПКА – на място, по телефона, онлайн?]</p></div></div>''')
        s += section(head_block('Идеи за подарък', 'Популярни пакети') + '<div class="two-col"><div>' + price_rows([
            ('„Релакс“', 'дневна СПА карта + релаксиращ масаж 60 мин', '52 €'), ('„Абилити Дама“', 'почистване на лице + масаж с вулканични камъни + цял ден СПА', '92 €'),
            ('„Абилити Джентълмен“', 'масаж на лице + хамам + цял ден СПА', '87 €'), ('СПА пакет за двама „Абилити“', '2 масажа, цял ден СПА, солна стая и бутилка вино', '120 €')],
            'Бургас') + '</div><div>' + price_rows([('„Релакс“', 'дневна СПА карта + релаксиращ масаж 60 мин', '50 €'), ('„Абилити Дама“', 'Chocolate Dream 90 мин + дневна СПА карта', '85 €'),
            ('„Абилити Джентълмен“', 'антистрес масаж 60 мин + дневна СПА карта', '60 €'), ('СПА пакет за двама „Абилити“', '2 масажа × 60 мин + 2 дневни СПА карти', '100 €')], 'Варна') + '</div></div>',
            cls='section-sand')
        s += cta_band(p, 'Искате ваучер?', 'Обадете ни се – ще подготвим ваучера за вас.')
        return s
    return page(path, 'СПА ваучер за подарък – Бургас и Варна | Ability SPA',
                'Подаръчни ваучери от Ability SPA за услуга, пакет или сума по избор – валидни 1 година. СПА пакет за двама от 100 €.', body, crumbs, current='vaucheri/')


# ------------------------------------------------------------------------------------------------
# Stubs + homepage injection
# ------------------------------------------------------------------------------------------------
def build_stub(path, name):
    en = path.startswith('en/')
    if len(name) > 40 and ':' in name:
        name = name.split(':')[0]
    crumbs = [('', 'Home' if en else 'Начало'), (path, name)]

    def body(p):
        if en:
            return page_hero(p, crumbs, 'Coming soon', e(name),
                             'The English version of the site is being prepared. In the meantime you can book online or visit the Bulgarian pages.',
                             actions=[('btn-dark', BOOK_BURGAS, 'Book'), ('btn-outline', '', 'Bulgarian homepage')])
        return page_hero(p, crumbs, 'Скоро', e(name),
                         'Тази страница се подготвя за новия сайт. Междувременно можете да резервирате онлайн или да разгледате готовите страници.',
                         actions=[('btn-dark', BOOK_BURGAS, 'Резервирай'), ('btn-outline', '', 'Към началната страница')])
    t = f'{name} – Ability SPA'
    t = t if len(t) <= 60 else name[:45] + ' – Ability SPA'
    d = f'{name} – coming soon.' if en else f'{name} – страницата се подготвя.'
    return page(path, t, d[:150], body, crumbs, noindex=True, lang='en' if en else 'bg')


def build_blog_stub(slug, name):
    """Existing posts keep their address; until they are moved over, the preview links to the live article."""
    path = f'blog/{slug}/'
    crumbs = [('', 'Начало'), ('blog/', 'Блог'), (path, name)]

    def body(p):
        return page_hero(p, crumbs, 'Блог', e(name),
                         'Статията запазва адреса си и ще бъде пренесена в новия сайт. Дотогава можете да я прочетете на сегашния сайт.',
                         actions=[('btn-dark', f'{SITE}/{path}', 'Прочети статията'), ('btn-outline', 'blog/', 'Към блога')])
    t = name if len(name) <= 44 else name[:42].rstrip(' ,–-') + '…'
    return page(path, f'{t} | Ability SPA', f'{name} – статия от блога на Ability SPA.'[:150], body, crumbs, noindex=True, current='blog/')


def blog_posts():
    """(slug, title) of the live posts (current-site/blog-titles.tsv). /blog/spa-voucher/ moves to /vaucheri/."""
    rows = open(os.path.join(ROOT, 'current-site', 'blog-titles.tsv'), encoding='utf-8').read().splitlines()[1:]
    return [tuple(r.split('\t')) for r in rows if r and not r.startswith('spa-voucher\t')]


def sitemap_paths():
    rows = re.findall(r'^\| `(/[^`]*)` \| ([^|]+) \|', open(os.path.join(ROOT, 'docs', 'sitemap-new.md'), encoding='utf-8').read(), re.M)
    return [(u.strip('/') + '/' if u != '/' else '', n.strip()) for u, n in rows]


def inject_homepage():
    f = os.path.join(ROOT, 'index.html')
    t = open(f, encoding='utf-8').read()
    t = re.sub(r'<header class="site-header">.*?</header>', header('').replace('\n  ', '\n  ', 1), t, count=1, flags=re.S)
    t = re.sub(r'<footer class="site-footer".*?</footer>\s*<!-- Slim cookie bar.*?</div>', footer(''), t, count=1, flags=re.S)
    t = t.replace('href="./spa-burgas/"', 'href="spa-burgas/"')
    t = re.sub(r'css/styles\.css(\?v=\w+)?"', f'css/styles.css?v={ASSET_V}"', t)
    t = re.sub(r'js/main\.js(\?v=\w+)?"', f'js/main.js?v={ASSET_V}"', t)
    t = re.sub(r'<!-- CITY-CARDS -->.*?<!-- /CITY-CARDS -->', lambda m: '<!-- CITY-CARDS -->' + city_switch('') + '<!-- /CITY-CARDS -->', t, count=1, flags=re.S)
    open(f, 'w', encoding='utf-8').write(t)


if __name__ == '__main__':
    built = [build_burgas(), build_varna(), build_massages_hub(), build_osteopathy(), build_prices(), build_contacts(), build_vouchers()]
    built += [build_massage(m) for m in MASSAGES]
    import pages2
    built += pages2.build_all()
    stubs = []
    for path, name in sitemap_paths():
        if not path or path in built or path.startswith('blog/') and path != 'blog/':
            continue
        stubs.append(build_stub(path, re.sub(r'\s*\(.*?\)\s*$', '', name)))
    stubs += [build_blog_stub(s, n) for s, n in blog_posts()]
    inject_homepage()
    print(f'built {len(built)} pages, {len(stubs)} coming-soon pages')
