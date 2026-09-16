# -*- coding: utf-8 -*-
"""메인 페이지 조립 — 언어별로 같은 구조에 문구만 바꿔 끼웁니다."""
import shell, svgart, c_index as C
from common import COMPANY, CONTACT_BLOCK, QUOTE_BTN, LANGS, MGR, mgr_phone

PAGE = "index.html"


def build(lang):
    h = shell.head(lang, PAGE, C.TITLE[lang], C.DESC[lang])
    h += shell.header(lang, PAGE)
    art = [svgart.sea(), svgart.air(), svgart.heavy(lang)]
    S, cb = C.SEC[lang], CONTACT_BLOCK[lang]

    # 히어로 슬라이더
    slides = ""
    for i, s in enumerate(C.HERO[lang]):
        slides += """
    <article class="slide" role="group" aria-roledescription="slide" aria-label="%d / 3">
      <div class="wrap"><div class="sgrid">
        <div class="stext">
          <p class="eyebrow">%s</p>
          <h1>%s</h1>
          <p class="lede">%s</p>
          <div class="cta">
            <a class="btn btn-primary" href="contact.html#quote">%s <span class="ar">&rarr;</span></a>
            <a class="btn btn-ghost" href="%s">%s</a>
          </div>
        </div>
        <div class="hp-art">%s</div>
      </div></div>
    </article>
""" % (i + 1, s["eb"], s["h"], s["p"], s["a1"], s["l2"], s["a2"], art[i])
    tabs = "".join(
        '<button class="hdot" type="button" role="tab" aria-selected="%s" tabindex="%s">'
        '<span class="n">0%d</span><span class="t">%s</span><i class="bar"></i></button>'
        % ("true" if i == 0 else "false", "0" if i == 0 else "-1", i + 1, s["tab"])
        for i, s in enumerate(C.HERO[lang]))

    b = """
<section class="hero3" aria-roledescription="carousel">
  <div class="slides" id="slides">%s</div>
  <div class="wrap"><div class="hnav" role="tablist">%s</div></div>
</section>

<section class="facts"><div class="wrap"><div class="grid">%s</div></div></section>
""" % (slides, tabs,
       "".join('<div class="cell"><p class="v">%s<small>%s</small></p><p class="k">%s<br>%s</p></div>'
               % f for f in C.FACTS[lang]))

    # 사업 2축
    dv = ""
    for d in C.DIVS[lang]:
        lis = "".join('<li><b>%s</b><span>%s</span></li>' % it for it in d["items"])
        dv += ('<div class="d"><span class="tag2">%s</span><h3>%s</h3><p class="sub">%s</p>'
               '<ul>%s</ul><a class="btn btn-ghost" href="%s" style="align-self:flex-start">%s '
               '<span class="ar">&rarr;</span></a></div>'
               % (d["tag"], d["h"], d["sub"], lis, d["link"], d["btn"]))
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <a class="btn btn-ghost" href="about.html">%s <span class="ar">&rarr;</span></a></div>
  <div class="divs">%s</div>
</div></section>
""" % (S["div"][2], S["div"][0], S["div"][1], C.DIVS[lang][0]["btn"].replace("서비스 상세", "회사소개") if lang == "ko" else ("About us" if lang == "en" else "公司介绍"), dv)

    # 주간 스케줄
    sc = C.SCHED[lang]
    rows = "".join('<tr><td>%s</td><td class="num">%s</td><td class="num">%s</td>'
                   '<td class="num">%s</td><td><span class="tag %s">%s</span></td></tr>' % r
                   for r in sc["rows"])
    b += """
<section class="sec panel"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <a class="btn btn-ghost" href="contact.html#quote">%s <span class="ar">&rarr;</span></a></div>
  <div class="board-scroll"><table class="data"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>
  <p class="note" style="margin-top:16px">%s</p>
</div></section>
""" % (S["sch"][2], S["sch"][0], S["sch"][1], sc["btn"],
       "".join('<th scope="col">%s</th>' % c for c in sc["cols"]), rows, sc["note"])

    # 사업영역
    cards = "".join(
        '<a class="s" href="%s"><span class="n">0%d</span><span class="b">'
        '<h3>%s<span class="en">%s</span></h3><p>%s</p></span></a>'
        % (l, i + 1, t, en, d) for i, (l, t, en, d) in enumerate(C.SVCS[lang]))
    cta = C.SVCS_CTA[lang]
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="svcs">%s<a class="cta" href="contact.html#quote"><b>%s</b><span>%s &rarr;</span></a></div>
  <p class="formnote" style="margin-top:18px">%s</p>
</div></section>
""" % (S["svc"][2], S["svc"][0], S["svc"][1], cards, cta[0], cta[1], C.SVCS_NOTE[lang])

    # 네트워크
    N = C.NODES[lang]
    nd = lambda rows: "".join(
        '<div class="nd"><span class="city">%s <i>%s</i></span><span class="desc">%s</span>'
        '<span class="st %s">%s</span></div>' % r for r in rows)
    b += """
<section class="sec panel"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <a class="btn btn-ghost" href="network.html">%s <span class="ar">&rarr;</span></a></div>
  <div class="split" style="border:0;background:transparent;gap:clamp(28px,4vw,48px)">
    <div class="c" style="padding:0;background:transparent"><p class="eyebrow dim">%s</p><div class="nodes">%s</div></div>
    <div class="c" style="padding:0;background:transparent"><p class="eyebrow dim">%s</p><div class="nodes">%s</div></div>
  </div>
  <p class="lede" style="margin-top:30px">%s</p>
</div></section>
""" % (S["net"][2], S["net"][0], S["net"][1], N["btn"], N["cn"], nd(N["cnrows"]), N["kr"], nd(N["krrows"]), N["lede"])

    # 통관 대응
    K = C.CUSTOMS[lang]
    st = "".join('<li style="border-color:rgba(255,255,255,.14)"><b style="color:#fff">%s</b>'
                 '<span style="color:#A9B8D6">%s</span></li>' % s for s in K["steps"])
    b += """
<section class="slab"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p><h2>%s</h2>
    <p class="lede">%s</p></div>
    <a class="btn btn-indigo" href="services.html#customs">%s <span class="ar">&rarr;</span></a></div>
  <ol class="steps" style="border-color:rgba(255,255,255,.14)">%s</ol>
</div></section>
""" % (K["eb"], K["h"], K["lede"], K["btn"], st)

    # 선택 이유
    rr = "".join('<div class="rr"><span class="n">0%d</span><h3>%s</h3><p>%s</p></div>'
                 % (i + 1, t, d) for i, (t, d) in enumerate(C.WHY[lang]))
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p><h2>%s</h2></div></div>
  <div class="reasons">%s</div>
</div></section>
""" % (S["why"][2], S["why"][0], rr)

    # 문의
    co = COMPANY[lang]
    asks = "".join('<li><b>%s</b><span>%s</span></li>' % a for a in C.ASK[lang])
    b += """
<section class="sec panel"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p><h2>%s</h2></div></div>
  <div class="contact">
    <div>
      <p class="eyebrow dim">HF Logistics Co., Ltd.</p>
      <dl class="deflist">
        <div class="row"><dt>%s</dt><dd>%s</dd></div>
        <div class="row"><dt>%s</dt><dd class="mono">032-888-0824</dd></div>
        <div class="row"><dt>%s</dt><dd class="mono">032-888-0825</dd></div>
        <div class="row"><dt>%s</dt><dd>%s<br><span class="mono">%s</span></dd></div>
        <div class="row"><dt>%s</dt><dd class="mono"><a href="mailto:%s">%s</a></dd></div>
      </dl>
      <a class="btn btn-primary" href="contact.html#quote" style="align-self:flex-start">%s <span class="ar">&rarr;</span></a>
    </div>
    <div>
      <p class="eyebrow dim">%s</p>
      <ul class="checks">%s</ul>
      <p class="formnote">%s</p>
    </div>
  </div>
</div></section>
""" % (S["con"][2], S["con"][0], cb["addr"], co["addr"], cb["tel"], cb["fax"],
       cb["mgr"], cb["mgrname"], mgr_phone(lang),
       cb["email"], MGR["email"], MGR["email"],
       cb["toform"], cb["ask"], asks, C.ASK_NOTE[lang])

    return shell.write(lang, PAGE, h + b + shell.footer(lang))


if __name__ == "__main__":
    for l in LANGS:
        print(build(l))
