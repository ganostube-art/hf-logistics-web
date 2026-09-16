# -*- coding: utf-8 -*-
"""회사소개 — 개요 · 사업구조 · 사업영역 · 연혁 · 선택 이유"""
import shell
from common import LANGS
import c_index as CI

PAGE = "about.html"

M = {
"ko": dict(title="회사소개 — HF 로지스틱스", crumb="COMPANY", h1="회사소개",
  desc="주식회사 에이치에프로지스틱스 회사 개요, 사업 구조, 사업영역, 연혁. 인천항·인천세관 인접 거점에서 종합물류와 중장비 두 부문을 운영합니다.",
  lede="화물도 중장비도, 인천에서 시작하는 물류. 인천항과 인천세관을 곁에 두고 국제물류주선업과 중장비 운반업을 두 축으로 운영합니다.",
  ov=("Company Overview","회사 개요","Profile"),
  rows=[("상호","주식회사 에이치에프로지스틱스<br>HF LOGISTICS CO., LTD."),("대표이사","안 규 철"),
        ("설립","2024년 7월"),("소재지","인천광역시 중구 서해대로 342, 풍천빌딩 505호"),
        ("연락처","TEL. 032-888-0824 / FAX. 032-888-0825"),("사업자번호","865-86-03145"),
        ("주요 사업","국제물류주선 · 수입통관 대행 · 보세창고 운영 · 보수작업 · 국내 운송")],
  prin="운영 원칙",
  printxt="당사는 인천항과 인천세관 인근에 거점을 두고 수입 화물의 통관과 보관, 국내 운송을 수행합니다. 해외 수출자를 대신해 한국 측에서 직접 움직이는 것이 당사의 역할입니다.",
  princhk=[("수입통관 대행 — 한국 측 창구","수출자를 대신해 신고 · 요건 · 세관 대응"),
           ("보수작업 대행 — 현장 해결","보세 상태에서 표시 · 포장 문제 직접 처리"),
           ("보관 · 국내 운송 — 인천 거점","인천항 · 인천공항 창고에서 현장까지")],
  bs=("Business Structure","두 개의 축, 하나의 운영 체계","Divisions"),
  bsbtn="서비스 상세",
  bslede="일반 화물은 포워딩 · 창고 · 전자상거래 물류로, 중장비는 운반부터 매매 · 수출입까지 이어지는 구조입니다. 인천항과 인천세관을 곁에 두고 양쪽 모두 항만 연계로 처리합니다.",
  sc=("Scope of Business","사업영역","6 Areas"), scnote="정관상 목적사업 기준 · 2026년 개정 반영",
  areas=[("국제물류주선","해상 · 항공 수출입 운송 주선, 선복 확보 및 서류 일괄 관리"),
         ("차량 및 중장비 운반업","건설기계의 해상 운송 주선 및 부두에서 현장까지 육상 운송"),
         ("제3자물류 (3PL)","화주사 물류 기능 전반 위탁 운영, 운송 · 보관 · 재고 · 정산 통합"),
         ("풀필먼트","입고 검수부터 피킹 · 패킹 · 출고, 반품 회수 및 재입고까지"),
         ("중기 · 건설기계 수출입","중국 건설기계 수입 통관 대행 및 장비 매매 · 중개"),
         ("전자상거래 · 통신판매중개","해외 셀러 및 플랫폼 연계 구매대행 · 배송대행 서비스")],
  hs=("History","연혁","Timeline"),
  hist=[("2024.07","주식회사 에이치에프로지스틱스 설립"),("2024.07","국제물류주선업(포워딩) 등록 · 물류창고 운영 개시"),
        ("2026.09","본점 이전 (인천 서해대로) 및 사업목적 확대"),("2026.09","중국 건설기계 수입 운송 개시"),
        ("2026.10","전자상거래 물류 · 풀필먼트 서비스 개시")],
  nx="Next · 다음 단계",
  next=["전자상거래 전담 물류센터 확장","중국 주요 항만 정기 선복 확보","중장비 보관 야드 및 인도장 확보","화주사 전용 물류 관리 시스템 고도화"]),

"en": dict(title="Company — HF Logistics", crumb="COMPANY", h1="About HF Logistics",
  desc="Company profile, business structure, scope and history of HF Logistics, running freight forwarding and heavy cargo transport from a base next to Incheon Port and Incheon Customs.",
  lede="Freight and heavy equipment alike, logistics that starts in Incheon. We run freight forwarding and heavy cargo haulage as two divisions, with Incheon Port and Incheon Customs on our doorstep.",
  ov=("Company Overview","Company overview","Profile"),
  rows=[("Company","HF LOGISTICS CO., LTD."),("CEO","Ahn Gyu-cheol"),
        ("Founded","July 2024"),("Address","#505 Pungcheon Bldg, 342 Seohae-daero, Jung-gu, Incheon, Korea"),
        ("Contact","TEL. +82-32-888-0824 / FAX. +82-32-888-0825"),("Business reg.","865-86-03145"),
        ("Main activities","Freight forwarding · Import customs agency · Bonded warehousing · Reconditioning · Domestic transport")],
  prin="How we work",
  printxt="We operate from a base near Incheon Port and Incheon Customs, handling clearance, storage and domestic transport for imported cargo. Our role is to act on the Korean side on behalf of overseas exporters.",
  princhk=[("Import clearance — your desk in Korea","Declarations, requirement checks and customs correspondence on your behalf"),
           ("Reconditioning — fixed on site","Labelling and packaging faults resolved while cargo is still under bond"),
           ("Storage and domestic transport — Incheon base","From the Incheon Port and Airport warehouses to the final site")],
  bs=("Business Structure","Two divisions, one operation","Divisions"),
  bsbtn="View services",
  bslede="General cargo runs through forwarding, warehousing and e-commerce logistics; heavy equipment runs from haulage through to trading and import/export. Both are handled with direct port connections, with Incheon Port and Customs alongside us.",
  sc=("Scope of Business","What we are licensed to do","6 Areas"), scnote="Per the articles of incorporation, as amended in 2026",
  areas=[("Freight forwarding","Sea and air import/export forwarding, space booking and document control"),
         ("Vehicle and heavy equipment haulage","Ocean forwarding of construction equipment and inland haulage from port to site"),
         ("Third-party logistics (3PL)","Outsourced logistics operations covering transport, storage, inventory and settlement"),
         ("Fulfilment","Inbound inspection through picking, packing, outbound, returns and restocking"),
         ("Equipment import and export","Customs clearance for Chinese construction equipment, plus trading and brokerage"),
         ("E-commerce and marketplace support","Purchasing and delivery agency services for overseas sellers and platforms")],
  hs=("History","History","Timeline"),
  hist=[("2024.07","HF Logistics Co., Ltd. founded"),("2024.07","Registered as a freight forwarder; warehouse operations begin"),
        ("2026.09","Head office relocated to Seohae-daero, Incheon; scope of business expanded"),
        ("2026.09","Construction equipment imports from China begin"),
        ("2026.10","E-commerce logistics and fulfilment services launch")],
  nx="Next · What follows",
  next=["Expanding the dedicated e-commerce fulfilment centre","Securing regular space at major Chinese ports",
        "Adding a storage yard and handover site for heavy equipment","Upgrading the shipper-facing logistics management system"]),

"zh": dict(title="公司介绍 — HF物流", crumb="COMPANY", h1="公司介绍",
  desc="HF物流株式会社的公司概况、业务结构、经营范围与发展历程。以毗邻仁川港与仁川海关的据点，运营综合物流与重型设备两大业务。",
  lede="货物与重型设备，物流始于仁川。我们毗邻仁川港与仁川海关，以国际物流运输代理和重型设备运输为两大支柱。",
  ov=("Company Overview","公司概况","Profile"),
  rows=[("公司名称","HF物流株式会社<br>HF LOGISTICS CO., LTD."),("首席执行官","安 圭 哲"),
        ("成立时间","2024年7月"),("地址","韩国仁川广域市中区西海大路342号 丰川大厦505室"),
        ("联系方式","电话 +82-32-888-0824 / 传真 +82-32-888-0825"),("营业执照号","865-86-03145"),
        ("主营业务","国际物流运输代理 · 进口通关代理 · 保税仓库运营 · 整理作业 · 韩国境内运输")],
  prin="运营理念",
  printxt="我们在仁川港与仁川海关附近设有据点，负责进口货物的通关、仓储与韩国境内运输。代替海外出口商在韩国一侧直接行动，正是我们的职责所在。",
  princhk=[("进口通关代理 — 您在韩国的窗口","代为申报、确认要件、应对海关"),
           ("整理作业代理 — 现场解决","在保税状态下直接处理标签与包装问题"),
           ("仓储 · 境内运输 — 仁川据点","从仁川港与仁川机场仓库直至施工现场")],
  bs=("Business Structure","两大支柱，一套运营体系","Divisions"),
  bsbtn="查看服务详情",
  bslede="普通货物走货运代理、仓储与跨境电商物流；重型设备则从运输延伸至买卖与进出口。两者均依托港口联运处理，仁川港与仁川海关就在身旁。",
  sc=("Scope of Business","经营范围","6 Areas"), scnote="依据公司章程所载经营目的 · 已反映2026年修订",
  areas=[("国际物流运输代理","海运、空运进出口运输代理，舱位预订及单证统一管理"),
         ("车辆及重型设备运输","工程机械海运代理，以及从码头到施工现场的陆运"),
         ("第三方物流 (3PL)","受托运营货主物流全流程，整合运输、仓储、库存与结算"),
         ("履约配送","从入库验货到拣货、包装、出库，以及退货回收与重新入库"),
         ("工程机械进出口","中国工程机械进口通关代理及设备买卖、中介"),
         ("跨境电商 · 网络销售中介","面向海外卖家及平台的代购、代发货服务")],
  hs=("History","发展历程","Timeline"),
  hist=[("2024.07","HF物流株式会社成立"),("2024.07","注册国际物流运输代理业务 · 物流仓库开始运营"),
        ("2026.09","总部迁至仁川西海大路 · 扩大经营范围"),("2026.09","开始中国工程机械进口运输"),
        ("2026.10","跨境电商物流 · 履约配送服务上线")],
  nx="Next · 下一步",
  next=["扩建跨境电商专用物流中心","确保中国主要港口的定期舱位","增设重型设备堆场与交付场地","升级货主专用物流管理系统"]),
}


def build(lang):
    m = M[lang]
    h = shell.head(lang, PAGE, m["title"], m["desc"]) + shell.header(lang, PAGE)
    h += shell.phead(lang, m["crumb"], m["h1"], m["lede"])

    rows = "".join('<div class="row"><dt>%s</dt><dd>%s</dd></div>' % r for r in m["rows"])
    chk = "".join('<li><b>%s</b><span>%s</span></li>' % c for c in m["princhk"])
    b = """
<section class="sec flush"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="split">
    <div class="c"><dl class="deflist">%s</dl></div>
    <div class="c"><p class="eyebrow dim">%s</p>
      <p style="font-size:14.5px;line-height:1.84;color:var(--ink-2)">%s</p>
      <ul class="checks">%s</ul></div>
  </div>
</div></section>
""" % (m["ov"][0], m["ov"][1], m["ov"][2], rows, m["prin"], m["printxt"], chk)

    dv = ""
    for d in CI.DIVS[lang]:
        lis = "".join('<li><b>%s</b><span>%s</span></li>' % it for it in d["items"])
        dv += ('<div class="d"><span class="tag2">%s</span><h3>%s</h3><p class="sub">%s</p>'
               '<ul>%s</ul></div>' % (d["tag"], d["h"], d["sub"], lis))
    b += """
<section class="sec panel"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <a class="btn btn-ghost" href="services.html">%s <span class="ar">&rarr;</span></a></div>
  <div class="divs">%s</div>
  <p class="lede" style="margin-top:28px">%s</p>
</div></section>
""" % (m["bs"][0], m["bs"][1], m["bs"][2], m["bsbtn"], dv, m["bslede"])

    ar = "".join('<div class="r"><span class="ix" style="color:var(--indigo)">0%d</span>'
                 '<h3>%s</h3><p>%s</p></div>' % (i + 1, t, d) for i, (t, d) in enumerate(m["areas"]))
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:36ch">%s</p></div>
  <div class="risks cols-3">%s</div>
</div></section>
""" % (m["sc"][0], m["sc"][1], m["sc"][2], m["scnote"], ar)

    hi = "".join('<div class="h"><time>%s</time><p>%s</p></div>' % x for x in m["hist"])
    nx = "".join('<li><span>%s</span></li>' % x for x in m["next"])
    b += """
<section class="sec panel" id="history"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="split" style="border:0;background:transparent;gap:clamp(28px,4vw,48px)">
    <div class="c" style="padding:0;background:transparent"><div class="hist">%s</div></div>
    <div class="c" style="padding:0;background:transparent"><p class="eyebrow dim">%s</p>
      <ul class="checks">%s</ul></div>
  </div>
</div></section>
""" % (m["hs"][0], m["hs"][1], m["hs"][2], hi, m["nx"], nx)

    S = CI.SEC[lang]
    rr = "".join('<div class="rr"><span class="n">0%d</span><h3>%s</h3><p>%s</p></div>'
                 % (i + 1, t, d) for i, (t, d) in enumerate(CI.WHY[lang]))
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p><h2>%s</h2></div></div>
  <div class="reasons">%s</div>
</div></section>
""" % (S["why"][2], S["why"][0], rr)

    return shell.write(lang, PAGE, h + b + shell.footer(lang))


if __name__ == "__main__":
    for l in LANGS:
        print(build(l))
