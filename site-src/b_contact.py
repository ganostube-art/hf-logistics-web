# -*- coding: utf-8 -*-
"""문의처 — 견적 폼 · 오시는 길"""
import shell
from common import LANGS, COMPANY, CONTACT_BLOCK
import c_index as CI

PAGE = "contact.html"
NMAP = "https://map.naver.com/p/search/"

M = {
"ko": dict(title="문의처 — HF 로지스틱스", crumb="CONTACT", h1="문의처 · 견적 요청",
  desc="HF 로지스틱스 견적 요청 및 문의. 인천 본사, 인천항 보세창고, 인천공항 자유무역지역 창고 오시는 길.",
  lede="품목과 노선만 알려주시면 담당자가 배정됩니다. 보류 건은 시간이 비용이므로, 접수 즉시 현품 확인 일정을 잡습니다.",
  q=("Request a Quote","견적 · 상담 요청","Inquiry"),
  qnote="선적 전 검토든, 이미 보류가 걸린 건이든 접수 즉시 대응 경로를 안내드립니다.",
  hours=("운영 시간","평일 09:00 – 18:00<br>보류 건은 접수 즉시 대응"),
  f=dict(company="회사명 Company", name="담당자 Name", phone="연락처 Phone", email="이메일 Email",
         type="문의 유형 Type", cargo="출발지 · 품목 Origin &amp; Cargo", msg="문의 내용 Message",
         submit="문의 보내기",
         ph_cargo="예) 위해 → 인천항 / 주방용품 LCL 12CBM",
         ph_msg="보류 건이라면 세관 시정 요구 내용을 그대로 적어 주십시오.",
         note="보내기를 누르면 메일 작성 창이 열립니다. 서버 접수 기능은 호스팅 연결 후 활성화됩니다.",
         opts=["수입통관 대행","보수작업 · 보류 건 대응","보세창고 보관","국제물류주선 (해상 · 항공)",
               "중장비 · 중량물 수입","이커머스 물류 · 풀필먼트","국내 운송 · 배송","기타 문의"]),
  loc=("Locations","오시는 길","Directions"), mapbtn="지도에서 보기",
  places=[("Head Office","인천 본사","인천광역시 중구 서해대로 342, 풍천빌딩 505호",
           ["인천세관 인접","TEL. 032-888-0824 / FAX. 032-888-0825"],"인천광역시 중구 서해대로 342"),
          ("Sea Cargo","인천항 보세창고","인천광역시 중구 축항대로 202 (항동7가 95-1)<br>협력사 ㈜스카이국제운송",
           ["특허보세구역 · 보수작업 수행","TEL. 032-765-4715~7"],"인천 중구 축항대로 202"),
          ("Air Cargo","인천공항 자유무역지역","인천광역시 중구 공항동로 296번길 171,<br>AMB 인천물류센터 F1-1<br>협력사 삼복로지스틱㈜",
           ["자유무역지역 내 보세 보관","TEL. 070-5066-3352"],"인천 중구 공항동로296번길 171")],
  cta=("24H","한국에서의 문제는, 한국에서 끝내겠습니다","보류 통보를 받으셨다면 내용을 그대로 전달해 주십시오. 당일 현품 확인 일정을 잡습니다.")),

"en": dict(title="Contact — HF Logistics", crumb="CONTACT", h1="Contact &amp; quotes",
  desc="Request a quote from HF Logistics, and find our Incheon head office, Incheon Port bonded warehouse and Incheon Airport Free Trade Zone warehouse.",
  lede="Tell us the commodity and the route and we assign a coordinator. For held cargo, time is money, so we schedule a physical inspection as soon as your enquiry lands.",
  q=("Request a Quote","Request a quote or a call","Inquiry"),
  qnote="Whether you are reviewing a shipment before it sails or dealing with cargo already on hold, we set out the route forward as soon as we hear from you.",
  hours=("Office hours","Weekdays 09:00 – 18:00 KST<br>Held cargo handled on arrival of your enquiry"),
  f=dict(company="Company", name="Contact name", phone="Phone", email="Email",
         type="Enquiry type", cargo="Origin &amp; cargo", msg="Message",
         submit="Send enquiry",
         ph_cargo="e.g. Weihai → Incheon Port / kitchenware, LCL 12 CBM",
         ph_msg="If cargo is on hold, please paste the customs correction notice exactly as received.",
         note="Pressing send opens your email client. Server-side submission will be switched on once hosting is connected.",
         opts=["Import customs clearance","Reconditioning / held cargo","Bonded warehousing","Freight forwarding (sea / air)",
               "Heavy cargo import","E-commerce logistics &amp; fulfilment","Domestic transport &amp; delivery","Other"]),
  loc=("Locations","Where to find us","Directions"), mapbtn="Open in map",
  places=[("Head Office","Incheon head office","#505 Pungcheon Bldg, 342 Seohae-daero, Jung-gu, Incheon",
           ["Next to Incheon Customs","TEL. +82-32-888-0824 / FAX. +82-32-888-0825"],"인천광역시 중구 서해대로 342"),
          ("Sea Cargo","Incheon Port bonded warehouse","202 Chukhang-daero, Jung-gu, Incheon<br>Partner: Sky International Transport",
           ["Licensed bonded area · reconditioning on site","TEL. +82-32-765-4715~7"],"인천 중구 축항대로 202"),
          ("Air Cargo","Incheon Airport Free Trade Zone","F1-1 AMB Incheon Logistics Centre,<br>171 Gonghangdong-ro 296beon-gil, Jung-gu, Incheon<br>Partner: Sambok Logistic",
           ["Bonded storage inside the Free Trade Zone","TEL. +82-70-5066-3352"],"인천 중구 공항동로296번길 171")],
  cta=("24H","Problems in Korea get settled in Korea","If you have received a hold notice, send it to us as it is. We schedule a physical inspection the same day.")),

"zh": dict(title="联系方式 — HF物流", crumb="CONTACT", h1="联系方式 · 报价咨询",
  desc="HF物流报价咨询与联系方式，以及仁川总部、仁川港保税仓库、仁川机场自由贸易区仓库的交通指南。",
  lede="只需告知品名与航线，我们即刻指派负责人。扣货案件时间即成本，受理后立即安排现场查验。",
  q=("Request a Quote","报价 · 咨询申请","Inquiry"),
  qnote="无论是装运前的方案评估，还是已经被扣的货物，受理后我们会立即给出应对路径。",
  hours=("营业时间","工作日 09:00 – 18:00（韩国时间）<br>扣货案件受理后立即处理"),
  f=dict(company="公司名称 Company", name="联系人 Name", phone="联系电话 Phone", email="邮箱 Email",
         type="咨询类型 Type", cargo="起运地 · 品名 Origin &amp; Cargo", msg="咨询内容 Message",
         submit="发送咨询",
         ph_cargo="例）威海 → 仁川港 / 厨房用品 LCL 12CBM",
         ph_msg="若为扣货案件，请原文粘贴海关的整改通知内容。",
         note="点击发送将打开邮件撰写窗口。服务器端接收功能将在主机连接后启用。",
         opts=["进口通关代理","整理作业 · 扣货应对","保税仓储","国际物流运输代理（海运 · 空运）",
               "重型设备进口","跨境电商物流 · 履约配送","韩国境内运输 · 配送","其他咨询"]),
  loc=("Locations","交通指南","Directions"), mapbtn="在地图中查看",
  places=[("Head Office","仁川总部","韩国仁川广域市中区西海大路342号 丰川大厦505室",
           ["毗邻仁川海关","电话 +82-32-888-0824 / 传真 +82-32-888-0825"],"인천광역시 중구 서해대로 342"),
          ("Sea Cargo","仁川港保税仓库","仁川广域市中区筑港大路202号<br>合作方 Sky国际运输",
           ["特许保税区 · 可实施整理作业","电话 +82-32-765-4715~7"],"인천 중구 축항대로 202"),
          ("Air Cargo","仁川机场自由贸易区","仁川广域市中区机场洞路296号街171<br>AMB仁川物流中心 F1-1<br>合作方 三福物流",
           ["自由贸易区内保税存储","电话 +82-70-5066-3352"],"인천 중구 공항동로296번길 171")],
  cta=("24H","在韩国发生的问题，在韩国解决","若已收到扣货通知，请原样转发给我们。我们当天就安排现场查验。")),
}


def build(lang):
    import urllib.parse as up
    m, co, cb = M[lang], COMPANY[lang], CONTACT_BLOCK[lang]
    h = shell.head(lang, PAGE, m["title"], m["desc"]) + shell.header(lang, PAGE)
    h += shell.phead(lang, m["crumb"], m["h1"], m["lede"])
    f = m["f"]
    opts = "".join("<option>%s</option>" % o for o in f["opts"])
    asks = "".join('<li><b>%s</b><span>%s</span></li>' % a for a in CI.ASK[lang])

    b = """
<section class="sec flush" id="quote"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:40ch">%s</p></div>
  <div class="contact">
    <div>
      <p class="eyebrow dim">HF Logistics Co., Ltd.</p>
      <dl class="deflist">
        <div class="row"><dt>%s</dt><dd>%s</dd></div>
        <div class="row"><dt>%s</dt><dd class="mono"><a href="tel:032-888-0824" style="text-decoration:none">032-888-0824</a></dd></div>
        <div class="row"><dt>%s</dt><dd class="mono">032-888-0825</dd></div>
        <div class="row"><dt>%s</dt><dd>%s<br><span class="mono"><a href="tel:010-5248-0066" style="text-decoration:none">010-5248-0066</a></span></dd></div>
        <div class="row"><dt>%s</dt><dd>%s</dd></div>
      </dl>
      <p class="eyebrow dim">%s</p>
      <ul class="checks">%s</ul>
    </div>
    <div>
      <form class="form" id="quote-form" novalidate>
        <div class="row2">
          <div class="field"><label for="f-company">%s</label><input id="f-company" name="company" type="text" autocomplete="organization" required></div>
          <div class="field"><label for="f-name">%s</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
        </div>
        <div class="row2">
          <div class="field"><label for="f-phone">%s</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="f-email">%s</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="f-type">%s</label><select id="f-type" name="type">%s</select></div>
        <div class="field"><label for="f-cargo">%s</label><input id="f-cargo" name="cargo" type="text" placeholder="%s"></div>
        <div class="field"><label for="f-message">%s</label><textarea id="f-message" name="message" rows="5" placeholder="%s"></textarea></div>
        <button class="btn btn-primary" type="submit" style="align-self:flex-start">%s <span class="ar">&rarr;</span></button>
        <p class="formnote" id="quote-status" role="status" aria-live="polite">%s</p>
      </form>
    </div>
  </div>
</div></section>
""" % (m["q"][0], m["q"][1], m["q"][2], m["qnote"],
       cb["addr"], co["addr"], cb["tel"], cb["fax"], cb["mgr"], cb["mgrname"],
       m["hours"][0], m["hours"][1], cb["ask"], asks,
       f["company"], f["name"], f["phone"], f["email"], f["type"], opts,
       f["cargo"], f["ph_cargo"], f["msg"], f["ph_msg"], f["submit"], f["note"])

    hubs = ""
    for en, name, addr, bullets, query in m["places"]:
        lis = "".join("<li>%s</li>" % x for x in bullets)
        hubs += ('<div class="hub"><div class="kind"><span class="en">%s</span></div>'
                 '<h3>%s</h3><p class="addr">%s</p><ul>%s</ul>'
                 '<a class="btn btn-ghost" href="%s%s" target="_blank" rel="noopener" '
                 'style="align-self:flex-start">%s <span class="ar">&rarr;</span></a></div>'
                 % (en, name, addr, lis, NMAP, up.quote(query), m["mapbtn"]))
    b += """
<section class="sec panel"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="hubs cols-3">%s</div>
</div></section>

<section class="slab"><div class="wrap" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:24px">
  <div style="display:flex;flex-direction:column;gap:10px;max-width:52ch">
    <p class="eyebrow">%s</p><h2>%s</h2><p class="lede">%s</p></div>
  <a class="btn btn-indigo" href="tel:032-888-0824">032-888-0824</a>
</div></section>
""" % (m["loc"][0], m["loc"][1], m["loc"][2], hubs, m["cta"][0], m["cta"][1], m["cta"][2])

    return shell.write(lang, PAGE, h + b + shell.footer(lang))


if __name__ == "__main__":
    for l in LANGS:
        print(build(l))
