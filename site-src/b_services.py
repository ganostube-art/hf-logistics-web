# -*- coding: utf-8 -*-
"""종합물류 부문 서비스"""
import shell
from common import LANGS
import c_index as CI

PAGE = "services.html"

M = {
"ko": dict(title="서비스 — HF 로지스틱스", crumb="SERVICES", h1="종합물류 부문",
  desc="국제물류주선(포워딩), 3PL·풀필먼트, 전자상거래 물류, 통관 대응, 보세창고 보관·보수작업, 국내 배송·반품까지 HF 로지스틱스 종합물류 부문 서비스.",
  lede="수입 화물의 국제 구간부터 국내 수취인까지. 포워딩 · 창고 · 전자상거래 물류를 하나의 운영 체계로 묶어 구간마다 담당이 바뀌지 않게 합니다.",
  ov=("Division 01","종합물류 부문","Overview"), ovbtn="중장비 부문 보기",
  cards=[("#forwarding","국제물류주선","Forwarding","해상 · 항공 수출입 운송 주선, 선복 확보 및 서류 일괄 관리"),
         ("#tpl","3PL · 풀필먼트","Fulfillment","보관 · 포장 · 출고 · 반품 일괄, 재고와 정산까지 통합 운영"),
         ("#ecommerce","전자상거래 물류","E-Commerce","해외 집화부터 전용 통관, 입고 검수, 라스트마일까지"),
         ("#customs","통관 대응","Customs","2026년 개편된 전자상거래 통관 체계에 맞춘 검증 · 알림 운영"),
         ("#bonded","보세창고 보관 · 보수작업","Bonded","인천항 보세창고 · 인천공항 자유무역지역 반입 및 현장 보완"),
         ("#domestic","국내 배송 · 반품","Last Mile","화물 특성별 채널 분리 운영, 전용 반품창고 회수 · 재입고")],
  cta=("품목과 노선만 알려주시면 담당자가 배정됩니다","견적 요청"),
  f=("Service 01","국제물류주선","Freight Forwarding"),
  f1=("해상 · 항공",[("해상 FCL / LCL","선복 확보와 혼재 운영. 위해 집화 창고에서 한국행 화물을 모아 출항합니다"),
                     ("항공 운송","급한 화물은 인천공항 자유무역지역 창고로 받아 리드타임을 줄입니다"),
                     ("선적 서류 일괄 관리","B/L · AWB · 인보이스 · 패킹리스트를 하나의 창구에서 정리합니다"),
                     ("수출입 대행 · 무역업","소싱 · 계약 · 선적 제반 절차를 대행합니다")]),
  f2=("화물 성격별 반입 분리","항공과 해상을 나눠 운영합니다. 급한 화물은 공항 자유무역지역 창고로, 중량 · 대량 화물은 인천항 보세창고로 받습니다. 화물 성격에 따라 리드타임과 비용을 함께 조절할 수 있습니다.",
      [("항공화물","Air","인천공항 자유무역지역 창고","live","보세 보관"),
       ("해상화물","Sea","인천항 보세창고","live","특허보세구역")]),
  t=("Service 02","3PL · 풀필먼트","Third-Party Logistics"),
  t1=("제3자물류 (3PL)","화주사 물류 기능 전반을 위탁 운영합니다. 운송 · 보관 · 재고 · 정산을 하나로 묶어 담당 창구를 단일화합니다.",
      [("운송 · 보관 통합","국제 구간과 국내 구간을 한 계약으로 운영"),("재고 · 정산","재고 현황과 비용을 월 단위로 정리해 제공")]),
  t2=("풀필먼트",[("입고 검수","스캔 기반 입고 처리, 수량 · 상태 확인"),("보관","인천항 · 인천공항 창고에 화물 성격별 배치"),
                  ("피킹 · 패킹 · 출고","주문 단위 집품 및 포장, 운송장 자동 발행"),("반품 회수 · 재입고","전용 반품창고에서 검수 후 재판매 / 폐기 분류")]),
  e=("Service 03","전자상거래 물류","E-Commerce"), enote="해외 셀러부터 국내 수취인까지, 통관을 사이에 두고 끊기지 않게 연결합니다.",
  eflow=[("주문 수집","셀러 · 플랫폼 주문 데이터 연계"),("해외 집화","위해 배대지 수취, 검수 후 혼적 · 출항"),
         ("통관","전자상거래 전용 신고"),("입고 · 검수","스캔 기반 입고 처리"),
         ("라스트마일","CJ · 경동 택배 출고"),("반품 처리","반품창고 회수 · 재입고")],
  elede="주문 · 운송장 · 통관정보를 하나의 플랫폼에서 관리하여, 화주사는 실시간으로 진행 상황을 확인하고 이상 건을 즉시 파악할 수 있습니다. 택배사 API 연동으로 운송장 발행과 배송 추적이 자동 처리됩니다.",
  c=("Service 04","통관 대응 역량","Customs"),
  cnote="2026년 전자상거래 전용 통관플랫폼 시행으로 수입화주 검증과 업체 등록 요건이 대폭 강화되었습니다.",
  chead="제도는 바뀌었습니다.<br>준비된 물류만 멈추지 않습니다.",
  ctext="당사는 제도 변경에 맞춘 검증 · 알림 체계를 갖추고 통관 지연을 최소화합니다. 통관이 멈추면 매출도 멈춥니다. 보류 건을 빨리 찾아내는 것이 곧 리드타임입니다.",
  b=("Service 05","보세창고 보관 · 보수작업","Bonded"), bbtn="보수작업 전체 절차",
  blede="통관 전 상태에서 손을 댈 수 있다는 것이 핵심입니다. 표시사항이나 포장 문제로 화물이 묶이면 보세구역에 둔 상태에서 세관 승인을 받아 보완합니다. 반송 없이 그대로 진행됩니다.",
  d=("Service 06","국내 배송 · 반품 운영","Last Mile &amp; Return"),
  d1=("Last Mile · 국내 배송 네트워크",[("CJ대한통운","전국 소형 화물 기본 채널. API 연동 기반 운송장 자동 발행"),
                                        ("경동택배","중량 · 대형 화물 대응. 일반 택배 규격 초과 품목 커버")],
      "화물 특성에 따라 채널을 분리 운영하여 단가와 파손율을 동시에 관리합니다."),
  d2=("Return · 전용 반품창고 운영",[("회수","반품 전용 주소로 일괄 회수, 송장 단위 추적"),("검수","상태 등급 판정 후 재판매 / 수리 / 폐기 분류"),
                                     ("처리","재입고 또는 폐기 · 반송, 결과 화주사 통보"),("정산","월 단위 반품 리포트 및 비용 정산 제공")],
      "반품은 비용이 아니라 데이터입니다. 사유별 통계를 제공해 재발을 줄입니다.")),

"en": dict(title="Services — HF Logistics", crumb="SERVICES", h1="Logistics division",
  desc="Freight forwarding, 3PL and fulfilment, e-commerce logistics, customs capability, bonded warehousing and reconditioning, domestic delivery and returns.",
  lede="From the international leg to the consignee in Korea. Forwarding, warehousing and e-commerce logistics run as one operation, so the cargo never changes hands between legs.",
  ov=("Division 01","Logistics division","Overview"), ovbtn="View heavy cargo",
  cards=[("#forwarding","Freight forwarding","Forwarding","Sea and air import/export forwarding, space booking and document control"),
         ("#tpl","3PL &amp; fulfilment","Fulfillment","Storage, packing, outbound and returns, with inventory and settlement in one place"),
         ("#ecommerce","E-commerce logistics","E-Commerce","From consolidation abroad through dedicated clearance, inbound checks and last mile"),
         ("#customs","Customs capability","Customs","Verification and alerting built for Korea's 2026 e-commerce clearance regime"),
         ("#bonded","Bonded storage &amp; reconditioning","Bonded","Receipt at Incheon Port and the airport Free Trade Zone, with corrections done on site"),
         ("#domestic","Domestic delivery &amp; returns","Last Mile","Separate channels by cargo type, with a dedicated returns warehouse")],
  cta=("Tell us the commodity and route, and we assign a coordinator","Request a quote"),
  f=("Service 01","Freight forwarding","Freight Forwarding"),
  f1=("Sea and air",[("Sea FCL / LCL","Space booking and consolidation. Korea-bound cargo is gathered at our Weihai warehouse and sails from there"),
                     ("Air freight","Urgent cargo is received at the Incheon Airport Free Trade Zone warehouse to cut lead time"),
                     ("Shipping documents in one place","B/L, AWB, invoices and packing lists handled through a single desk"),
                     ("Trade and sourcing agency","Sourcing, contracting and the shipping formalities handled on your behalf")]),
  f2=("Routing by cargo type","Air and sea run separately. Urgent cargo goes to the airport Free Trade Zone warehouse; heavy or high-volume cargo goes to the bonded warehouse at Incheon Port. Lead time and cost can be tuned together.",
      [("Air cargo","Air","Incheon Airport Free Trade Zone warehouse","live","Bonded storage"),
       ("Sea cargo","Sea","Incheon Port bonded warehouse","live","Licensed bonded area")]),
  t=("Service 02","3PL &amp; fulfilment","Third-Party Logistics"),
  t1=("Third-party logistics","We take over the shipper's logistics function as a whole, bringing transport, storage, inventory and settlement under one contact.",
      [("Transport and storage combined","The international and domestic legs run under one contract"),("Inventory and settlement","Stock position and costs reported monthly")]),
  t2=("Fulfilment",[("Inbound inspection","Scan-based receipt with quantity and condition checks"),("Storage","Allocated across the Incheon Port and airport warehouses by cargo type"),
                    ("Picking, packing, outbound","Order-level picking and packing, with waybills issued automatically"),("Returns and restocking","Inspected at the dedicated returns warehouse and sorted for resale or disposal")]),
  e=("Service 03","E-commerce logistics","E-Commerce"), enote="From the overseas seller to the consignee in Korea, with clearance in the middle and no break in the chain.",
  eflow=[("Order capture","Order data linked from sellers and marketplaces"),("Consolidation abroad","Received at the Weihai depot, inspected, consolidated and shipped"),
         ("Clearance","Dedicated e-commerce declaration"),("Receipt and inspection","Scan-based inbound processing"),
         ("Last mile","Dispatched via CJ Logistics or Kyungdong"),("Returns","Collected at the returns warehouse and restocked")],
  elede="Orders, waybills and clearance data are managed on one platform, so shippers can follow progress live and spot exceptions immediately. Waybill issue and delivery tracking run automatically through the carriers' APIs.",
  c=("Service 04","Customs capability","Customs"),
  cnote="Korea's dedicated e-commerce customs platform, in force from 2026, sharply tightened importer verification and operator registration.",
  chead="The rules changed.<br>Only prepared logistics keeps moving.",
  ctext="We have built the matching verification and alerting workflow to keep clearance delays to a minimum. When clearance stops, revenue stops. Finding held shipments quickly is what lead time really means.",
  b=("Service 05","Bonded storage &amp; reconditioning","Bonded"), bbtn="Full reconditioning procedure",
  blede="Being able to work on the goods before clearance is the whole point. When labelling or packaging holds cargo up, we correct it under bond with customs approval, and the shipment moves on without being returned.",
  d=("Service 06","Domestic delivery &amp; returns","Last Mile &amp; Return"),
  d1=("Last Mile · domestic network",[("CJ Logistics","Default channel for small parcels nationwide, with waybills issued automatically via API"),
                                       ("Kyungdong Parcel","For heavy and oversized items beyond standard parcel dimensions")],
      "Running separate channels by cargo type keeps both unit cost and damage rates under control."),
  d2=("Return · dedicated returns warehouse",[("Collection","Returned to a dedicated address and tracked by waybill"),("Inspection","Graded, then sorted for resale, repair or disposal"),
                                              ("Processing","Restocked or disposed of, with the outcome reported to the shipper"),("Settlement","Monthly returns report and cost reconciliation")],
      "Returns are data, not just cost. We report the reasons so the same problem happens less often.")),

"zh": dict(title="服务 — HF物流", crumb="SERVICES", h1="综合物流业务",
  desc="国际物流运输代理、3PL与履约配送、跨境电商物流、通关应对、保税仓储与整理作业、韩国境内配送与退货。",
  lede="从进口货物的国际段到韩国境内收货人。将货运代理、仓储与跨境电商物流整合为一套运营体系，各区段不更换承运方。",
  ov=("Division 01","综合物流业务","Overview"), ovbtn="查看重型设备业务",
  cards=[("#forwarding","国际物流运输代理","Forwarding","海运、空运进出口运输代理，舱位预订及单证统一管理"),
         ("#tpl","3PL · 履约配送","Fulfillment","仓储、包装、出库、退货一体化，并整合库存与结算"),
         ("#ecommerce","跨境电商物流","E-Commerce","从海外集货到专用通关、入库验货直至末端配送"),
         ("#customs","通关应对","Customs","按2026年改版后的跨境电商通关体系运行验证与提醒机制"),
         ("#bonded","保税仓储 · 整理作业","Bonded","仁川港保税仓库与仁川机场自由贸易区入库及现场补正"),
         ("#domestic","韩国境内配送 · 退货","Last Mile","按货物特性分渠道运营，设专用退货仓库回收与重新入库")],
  cta=("只需告知品名与航线，我们即刻指派负责人","报价咨询"),
  f=("Service 01","国际物流运输代理","Freight Forwarding"),
  f1=("海运 · 空运",[("海运 FCL / LCL","确保舱位并运营拼箱。在威海集货仓库汇集发往韩国的货物后发运"),
                     ("空运","急件由仁川机场自由贸易区仓库接收，缩短时效"),
                     ("装运单证统一管理","提单、空运单、发票与装箱单由同一窗口整理"),
                     ("进出口代理 · 贸易","代办选品、签约与装运的各项手续")]),
  f2=("按货物特性分线入库","空运与海运分线运营。急件送往机场自由贸易区仓库，重货与大批量货物进入仁川港保税仓库。可同时调整时效与成本。",
      [("空运货物","Air","仁川机场自由贸易区仓库","live","保税存储"),
       ("海运货物","Sea","仁川港保税仓库","live","特许保税区")]),
  t=("Service 02","3PL · 履约配送","Third-Party Logistics"),
  t1=("第三方物流 (3PL)","受托运营货主的全部物流职能，将运输、仓储、库存与结算整合为单一对接窗口。",
      [("运输与仓储整合","国际段与境内段以一份合同运营"),("库存 · 结算","按月整理并提供库存状况与费用")]),
  t2=("履约配送",[("入库验货","基于扫描的入库处理，核对数量与状态"),("仓储","按货物特性分配至仁川港与机场仓库"),
                  ("拣货 · 包装 · 出库","按订单集货与包装，自动生成运单"),("退货回收 · 重新入库","在专用退货仓库验货后区分再销售或报废")]),
  e=("Service 03","跨境电商物流","E-Commerce"), enote="从海外卖家到韩国收货人，中间隔着通关，但链条不断。",
  eflow=[("订单采集","对接卖家与平台的订单数据"),("海外集货","威海转运仓收货，验货后拼箱发运"),
         ("通关","跨境电商专用申报"),("入库 · 验货","基于扫描的入库处理"),
         ("末端配送","经CJ大韩通运、庆东快递出库"),("退货处理","退货仓库回收与重新入库")],
  elede="订单、运单与通关信息在同一平台管理，货主可实时查看进度并即刻发现异常件。通过快递公司API对接，运单生成与配送跟踪均自动完成。",
  c=("Service 04","通关应对能力","Customs"),
  cnote="随着2026年跨境电商专用通关平台施行，进口货主验证与企业登记要求大幅收紧。",
  chead="制度已经改变，<br>只有准备好的物流不会停。",
  ctext="我们已建立与新制度匹配的验证与提醒机制，将通关延误降到最低。通关一停，销售也随之停摆。尽快找出被扣件，本身就是时效。",
  b=("Service 05","保税仓储 · 整理作业","Bonded"), bbtn="查看整理作业完整流程",
  blede="能在通关前动手，正是关键所在。若因标示或包装问题导致货物被扣，我们会在保税区状态下取得海关批准并加以补正，无需退运即可继续推进。",
  d=("Service 06","韩国境内配送 · 退货运营","Last Mile &amp; Return"),
  d1=("Last Mile · 韩国境内配送网络",[("CJ大韩通运","全国小件货物的主渠道，通过API对接自动生成运单"),
                                      ("庆东快递","应对重货与大件，覆盖超出普通快递规格的商品")],
      "按货物特性分渠道运营，可同时控制单价与破损率。"),
  d2=("Return · 专用退货仓库运营",[("回收","统一回收至退货专用地址，按运单逐件跟踪"),("验货","判定状态等级后区分再销售、维修或报废"),
                                   ("处理","重新入库或报废、退运，并将结果通知货主"),("结算","按月提供退货报告与费用结算")],
      "退货不是成本，而是数据。我们按原因提供统计，以减少重复发生。")),
}


def build(lang):
    m = M[lang]
    h = shell.head(lang, PAGE, m["title"], m["desc"]) + shell.header(lang, PAGE)
    h += shell.phead(lang, m["crumb"], m["h1"], m["lede"])
    chk = lambda items: "".join('<li><b>%s</b><span>%s</span></li>' % x for x in items)
    stp = lambda items: "".join('<li><b>%s</b><span>%s</span></li>' % x for x in items)

    cards = "".join('<a class="s" href="%s"><span class="n">0%d</span><span class="b">'
                    '<h3>%s<span class="en">%s</span></h3><p>%s</p></span></a>'
                    % (l, i + 1, t, en, d) for i, (l, t, en, d) in enumerate(m["cards"]))
    b = """
<section class="sec flush"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <a class="btn btn-ghost" href="heavy.html">%s <span class="ar">&rarr;</span></a></div>
  <div class="svcs">%s<a class="cta wide" href="contact.html#quote"><b>%s</b><span>%s &rarr;</span></a></div>
</div></section>
""" % (m["ov"][0], m["ov"][1], m["ov"][2], m["ovbtn"], cards, m["cta"][0], m["cta"][1])

    nd = "".join('<div class="nd"><span class="city">%s <i>%s</i></span><span class="desc">%s</span>'
                 '<span class="st %s">%s</span></div>' % r for r in m["f2"][2])
    b += """
<section class="sec" id="forwarding"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="split">
    <div class="c"><p class="eyebrow dim">%s</p><ul class="checks">%s</ul></div>
    <div class="c"><p class="eyebrow dim">%s</p>
      <p style="font-size:14px;line-height:1.82;color:var(--ink-2)">%s</p>
      <div class="nodes">%s</div></div>
  </div>
</div></section>
""" % (m["f"][0], m["f"][1], m["f"][2], m["f1"][0], chk(m["f1"][1]), m["f2"][0], m["f2"][1], nd)

    b += """
<section class="sec panel" id="tpl"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="split">
    <div class="c"><p class="eyebrow dim">%s</p>
      <p style="font-size:14px;line-height:1.82;color:var(--ink-2)">%s</p>
      <ul class="checks">%s</ul></div>
    <div class="c"><p class="eyebrow dim">%s</p><ol class="steps">%s</ol></div>
  </div>
</div></section>
""" % (m["t"][0], m["t"][1], m["t"][2], m["t1"][0], m["t1"][1], chk(m["t1"][2]), m["t2"][0], stp(m["t2"][1]))

    fl = "".join('<div class="s%s"><span class="n">0%d</span><b>%s</b><span>%s</span></div>'
                 % (" hot" if i == 2 else "", i + 1, t, d) for i, (t, d) in enumerate(m["eflow"]))
    b += """
<section class="sec" id="ecommerce"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:40ch">%s</p></div>
  <div class="flow">%s</div>
  <p class="lede" style="margin-top:26px">%s</p>
</div></section>
""" % (m["e"][0], m["e"][1], m["e"][2], m["enote"], fl, m["elede"])

    b += """
<section class="sec panel" id="customs"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:42ch">%s</p></div>
  <div class="split">
    <div class="c"><h3 style="font-size:20px">%s</h3>
      <p style="font-size:14px;line-height:1.82;color:var(--ink-2)">%s</p></div>
    <div class="c"><ul class="checks">%s</ul></div>
  </div>
</div></section>
""" % (m["c"][0], m["c"][1], m["c"][2], m["cnote"], m["chead"], m["ctext"],
       chk([(t, d) for t, d in CI.CUSTOMS[lang]["steps"]]))

    import b_repair
    hubs = "".join('<div class="hub"><div class="kind"><span class="en">%s</span>'
                   '<span class="partner">%s</span></div><h3>%s</h3><p class="addr">%s</p>'
                   '<ul>%s</ul></div>' % (a, p, t, ad, "".join("<li>%s</li>" % x for x in li))
                   for a, p, t, ad, li in b_repair.HUBS[lang])
    b += """
<section class="sec" id="bonded"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <a class="btn btn-ghost" href="repair.html">%s <span class="ar">&rarr;</span></a></div>
  <p class="lede" style="margin-bottom:28px">%s</p>
  <div class="hubs">%s</div>
</div></section>
""" % (m["b"][0], m["b"][1], m["b"][2], m["bbtn"], m["blede"], hubs)

    b += """
<section class="sec panel" id="domestic"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="split">
    <div class="c"><p class="eyebrow dim">%s</p><ol class="steps">%s</ol>
      <p class="formnote">%s</p></div>
    <div class="c"><p class="eyebrow dim">%s</p><ol class="steps">%s</ol>
      <p class="formnote">%s</p></div>
  </div>
</div></section>
""" % (m["d"][0], m["d"][1], m["d"][2],
       m["d1"][0], stp(m["d1"][1]), m["d1"][2], m["d2"][0], stp(m["d2"][1]), m["d2"][2])

    return shell.write(lang, PAGE, h + b + shell.footer(lang))


if __name__ == "__main__":
    for l in LANGS:
        print(build(l))
