# -*- coding: utf-8 -*-
"""페이지 뼈대 — 언어별로 head / 헤더 / 푸터를 생성합니다."""

import io, os, hashlib
from common import META, UTILITY, NAV, QUOTE_BTN, MENU_BTN, NAV_ARIA, LANG_ARIA, COMPANY, FOOT, LANGS

# 이 스크립트의 상위 폴더가 사이트 루트입니다.
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_URL = "https://hflogis.com"


def asset_ver():
    """CSS/JS 내용 해시 — 파일이 바뀌면 URL이 바뀌어 캐시가 무효화됩니다."""
    h = hashlib.sha1()
    for rel in ("assets/css/site.css", "assets/js/site.js"):
        p = os.path.join(OUT, rel)
        if os.path.exists(p):
            h.update(open(p, "rb").read())
    return h.hexdigest()[:8]


def up(lang):
    """언어 폴더에서 사이트 루트까지의 상대경로."""
    return "" if lang == "ko" else "../"


def to_lang(cur, target, page):
    """cur 언어의 page 에서 target 언어의 같은 page 로 가는 상대경로."""
    return up(cur) + ("" if target == "ko" else target + "/") + page


def head(lang, page, title, desc):
    m = META[lang]
    u = up(lang)
    v = asset_ver()
    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s/%s%s">' %
        (META[l]["htmllang"], SITE_URL, META[l]["dir"], page) for l in LANGS)
    return """<!doctype html>
<html lang="%(hl)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(site)s/%(dir)s%(page)s">
%(alts)s
<link rel="alternate" hreflang="x-default" href="%(site)s/%(page)s">
<link rel="icon" href="%(u)sassets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="%(u)sassets/img/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=%(font)s&family=JetBrains+Mono:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="%(u)sassets/css/site.css?v=%(v)s">
<style>:root{--ff-sans:%(family)s}body{word-break:%(wb)s}</style>
</head>
<body>
""" % dict(hl=m["htmllang"], title=title, desc=desc, site=SITE_URL, dir=m["dir"], page=page,
           alts=alts, u=u, font=m["font"], family=m["family"], wb=m["wordbreak"], v=v)


def brand(lang):
    u = up(lang)
    return ('<a class="brand" href="index.html" aria-label="%s">\n'
            '      <img class="dark" src="%sassets/img/logo-dark.png" alt="%s" width="360" height="96">\n'
            '      <img class="light" src="%sassets/img/logo-light.png" alt="" aria-hidden="true" width="360" height="96">\n'
            '    </a>') % (COMPANY[lang]["short"], u, COMPANY[lang]["short"], u)


def lang_switch(lang, page):
    """상단 바 언어 전환. 현재 언어는 강조하고 링크를 걸지 않습니다."""
    out = []
    for l in LANGS:
        if l == lang:
            out.append('<span class="cur">%s</span>' % META[l]["label"])
        else:
            out.append('<a href="%s" hreflang="%s">%s</a>' % (to_lang(lang, l, page), META[l]["htmllang"], META[l]["label"]))
    return ('<span class="langs" role="group" aria-label="%s">%s</span>'
            % (LANG_ARIA[lang], '<i aria-hidden="true">/</i>'.join(out)))


def header(lang, page):
    items = "\n      ".join('<a href="%s">%s</a>' % (h, t) for h, t in NAV[lang])
    return """<div class="utility">
  <div class="wrap">
    <span>%(util)s</span>
    <span class="right">
      <a href="tel:032-888-0824">T. 032-888-0824</a>
      %(langs)s
    </span>
  </div>
</div>

<header class="masthead">
  <div class="wrap">
    %(brand)s
    <button class="navtoggle" type="button" aria-expanded="false" aria-controls="nav">%(menu)s</button>
    <nav class="nav" id="nav" aria-label="%(aria)s">
      %(items)s
      <a class="btn btn-indigo" href="contact.html#quote">%(quote)s</a>
    </nav>
  </div>
</header>
""" % dict(util=UTILITY[lang], langs=lang_switch(lang, page), brand=brand(lang),
           menu=MENU_BTN[lang], aria=NAV_ARIA[lang], items=items, quote=QUOTE_BTN[lang])


def footer(lang):
    c, f = COMPANY[lang], FOOT[lang]
    col = lambda h, items: ('<div>\n        <h4>%s</h4>\n        <ul>\n%s\n        </ul>\n      </div>'
                            % (h, "\n".join('          <li><a href="%s">%s</a></li>' % (a, t) for a, t in items)))
    return """
<footer class="foot">
  <div class="wrap">
    <div class="top">
      <div class="co">
        %(brand)s
        <p>
          %(addr)s<br>
          TEL. 032-888-0824 &nbsp;|&nbsp; FAX. 032-888-0825<br>
          %(biz)s &nbsp;|&nbsp; %(ceo)s
        </p>
      </div>
      %(c1)s
      %(c2)s
      %(c3)s
    </div>
    <div class="bottom">
      <span>&copy; <span data-year></span> HF Logistics Co., Ltd.</span>
      <span>%(tag)s</span>
    </div>
  </div>
</footer>

<script src="%(u)sassets/js/site.js?v=%(v)s"></script>
</body>
</html>
""" % dict(brand=brand(lang), addr=c["addr"], biz=c["biz"], ceo=c["ceo"],
           c1=col(f["c1"], f["c1items"]), c2=col(f["c2"], f["c2items"]), c3=col(f["c3"], f["c3items"]),
           tag=f["tag"], u=up(lang), v=asset_ver())


def phead(lang, crumb, h1, lede):
    from common import HOME
    return """
<section class="phead">
  <div class="wrap">
    <p class="crumb"><a href="index.html">%s</a> &nbsp;/&nbsp; %s</p>
    <h1>%s</h1>
    <p class="lede">%s</p>
  </div>
</section>
""" % (HOME[lang], crumb, h1, lede)


def write(lang, page, html):
    d = os.path.join(OUT, META[lang]["dir"].rstrip("/"))
    if d and not os.path.isdir(d):
        os.makedirs(d)
    path = os.path.join(OUT, META[lang]["dir"], page)
    io.open(path, "w", encoding="utf-8").write(html)
    return path
