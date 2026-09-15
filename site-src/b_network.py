# -*- coding: utf-8 -*-
"""네트워크 — 중국 집화 거점 · 한국 반입 창고 · 차량 운용"""
import shell
from common import LANGS
import c_index as CI

PAGE = "network.html"

M = {
"ko": dict(title="네트워크 · 인프라 — HF 로지스틱스", crumb="NETWORK", h1="물류 네트워크",
  desc="중국 위해 집화 거점부터 인천항 보세창고, 인천공항 자유무역지역 창고, 국내 배송망까지. 협력사 ㈜스카이국제운송 · 삼복로지스틱㈜와 함께 운영합니다.",
  lede="현지 집화부터 국내 반입까지. 중국 위해 집화 창고, 인천항 보세창고, 인천공항 자유무역지역 창고를 잇는 구간을 한 창구에서 관리합니다.",
  s1=("China","중국 집화 거점","Consolidation Hubs"),
  s1note="현지에서 실어 한국에서 끝냅니다. 구간마다 담당이 바뀌지 않습니다.",
  cn=[("위해","威海 / Weihai","泛杰产业园 내 2개 동 운영 — LCL 혼재 창고(HF LOGIS, B3-5) · 전자상거래 배대지(NOVA HF, B3-1)<br>海埠路56号 泛杰产业园","live","운영 중"),
      ("심천","深圳 / Shenzhen","화남 지역 집화 거점","plan","확보 예정"),
      ("항저우","杭州 / Hangzhou","화동 지역 집화 거점","plan","확보 예정")],
  wh=[("HF LOGIS · LCL 혼재 창고","한국행 일반 화물 집화 · 혼재","海埠路56号 泛杰产业园 B3-5",
       "여러 수출자의 화물을 모아 한 컨테이너로 혼재해 출항합니다. 소량 화물도 정기 스케줄에 실을 수 있습니다."),
      ("NOVA HF · 전자상거래 배대지","구매 물품 수취 · 검수 · 발송","海埠路56号 泛杰产业园 B3-1",
       "셀러 · 플랫폼 주문을 현지에서 수취해 검수한 뒤 혼적 · 출항합니다. 전자상거래 전용 통관으로 이어집니다.")],
  s2=("Korea","한국 반입 창고","Bonded Facilities"),
  s2note="급한 화물은 공항 자유무역지역 창고로, 중량 · 대량 화물은 인천항 보세창고로 받습니다. 화물 성격에 따라 리드타임과 비용을 함께 조절할 수 있습니다.",
  hubs=[("Sea Cargo · 협력사","㈜스카이국제운송","인천항 보세창고",
         "인천광역시 중구 축항대로 202 (항동7가 95-1)<br>T. 032-765-4715~7",
         ["특허보세구역 · 실내 2,600평 / 야드 1,815평","컨테이너 STUFFING · 적입 · 적출 작업","보수작업 수행 가능",
          "검역장소 지정 · 특송업체 등록 보유","국제물류주선업 · 3PL · 통관 · 보험 연계",
          "25년간 축적된 중국 네트워크 — 현지 지사 및 협력사 10개소","인천항 부두 인접, 반입 리드타임 단축"]),
        ("Air Cargo · 협력사","삼복로지스틱㈜","인천공항 자유무역지역",
         "인천광역시 중구 공항동로 296번길 171, AMB 인천물류센터 F1-1<br>T. 070-5066-3352",
         ["2002년 설립 · 임직원 45명 (본사 기준)","자유무역지역 내 보세 상태 보관","보세운송 · 통관 · 하역 일괄 처리",
          "특수화물 운송 · 보수작업 · 3PL &amp; 4PL","ADT캡스 경비 시스템 · CCTV 70대 이상 상시 운영",
          "매주 수요일 정기 재고조사로 수량 차이 관리","화물 반출입 · 보세운송 신청 · 적하 조회 프로그램 운영"])],
  s3=("Fleet","국내 운송 차량 운용","Vehicles"),
  s3note="협력사 삼복로지스틱㈜ 보유 기준. 냉장 · 냉동 및 무진동 차량을 포함해 화물 특성에 맞춰 배차합니다.",
  vcols=["Class 톤급","일반","냉장 · 냉동","리프트","무진동","합계"],
  last=("Last Mile · 택배 채널",[("CJ대한통운","전국 소형 화물 기본 채널. API 연동 기반 운송장 자동 발행"),
                                ("경동택배","중량 · 대형 화물 대응. 일반 택배 규격 초과 품목 커버")]),
  hvy=("Heavy Cargo · 중량물",[("저상 트레일러","부두에서 국내 현장까지 건설기계 직접 반입"),
                               ("인천항 · 평택항 하역","RO-RO · 벌크 · 플랫랙 / 오픈탑 화물의 중량물 하역 수배")]),
  cta=("One Operator","구간마다 담당이 바뀌지 않습니다","중국 현지 집화부터 한국 반입 · 통관 · 보수작업 · 국내 배송까지 한 회사가 이어서 처리합니다.","노선 상담")),

"en": dict(title="Network &amp; Facilities — HF Logistics", crumb="NETWORK", h1="Logistics network",
  desc="From the Weihai consolidation hub in China to the Incheon Port bonded warehouse, the Incheon Airport Free Trade Zone warehouse and domestic delivery, run with partners Sky International Transport and Sambok Logistic.",
  lede="From consolidation at origin to receipt in Korea. The stretch linking our Weihai warehouse, the Incheon Port bonded warehouse and the Incheon Airport Free Trade Zone warehouse is managed through a single desk.",
  s1=("China","Consolidation hubs in China","Consolidation Hubs"),
  s1note="Loaded at origin, finished in Korea. The same operator stays with the cargo throughout.",
  cn=[("Weihai","威海","Two units in the Fanjie Industrial Park — LCL consolidation warehouse (HF LOGIS, B3-5) and e-commerce forwarding depot (NOVA HF, B3-1)<br>Fanjie Industrial Park, 56 Haibu Road","live","Live"),
      ("Shenzhen","深圳","Hub for southern China","plan","Planned"),
      ("Hangzhou","杭州","Hub for eastern China","plan","Planned")],
  wh=[("HF LOGIS · LCL consolidation","Consolidating general cargo bound for Korea","Fanjie Industrial Park B3-5, 56 Haibu Road",
       "Cargo from several exporters is consolidated into one container before sailing, so even small shipments make the regular schedule."),
      ("NOVA HF · e-commerce depot","Receiving, checking and dispatching purchased goods","Fanjie Industrial Park B3-1, 56 Haibu Road",
       "Seller and marketplace orders are received locally, inspected, consolidated and shipped, feeding straight into dedicated e-commerce clearance.")],
  s2=("Korea","Receiving warehouses in Korea","Bonded Facilities"),
  s2note="Urgent cargo goes to the airport Free Trade Zone warehouse; heavy or high-volume cargo goes to the bonded warehouse at Incheon Port. Lead time and cost can be tuned to the shipment.",
  hubs=[("Sea Cargo · Partner","Sky International Transport","Incheon Port bonded warehouse",
         "202 Chukhang-daero, Jung-gu, Incheon<br>T. +82-32-765-4715~7",
         ["Licensed bonded area · 8,600 m² indoor / 6,000 m² yard","Container stuffing, loading and unloading","Reconditioning carried out on site",
          "Designated quarantine site · registered express operator","Forwarding, 3PL, clearance and insurance in one place",
          "25 years of China coverage — 10 branches and partner offices","Adjacent to the Incheon Port quay, shortening inbound lead time"]),
        ("Air Cargo · Partner","Sambok Logistic","Incheon Airport Free Trade Zone",
         "F1-1 AMB Incheon Logistics Centre, 171 Gonghangdong-ro 296beon-gil, Jung-gu, Incheon<br>T. +82-70-5066-3352",
         ["Founded 2002 · 45 staff at head office","Bonded storage inside the Free Trade Zone","Bonded transport, clearance and handling as one service",
          "Special cargo transport · reconditioning · 3PL &amp; 4PL","ADT Caps security system · more than 70 CCTV cameras",
          "Scheduled stock count every Wednesday to control discrepancies","In-house systems for cargo movements, bonded transport filing and manifest lookup"])],
  s3=("Fleet","Domestic transport fleet","Vehicles"),
  s3note="Held by our partner Sambok Logistic. Refrigerated, frozen and air-ride vehicles are assigned according to the nature of the cargo.",
  vcols=["Class","Standard","Refrigerated","Lift-gate","Air-ride","Total"],
  last=("Last Mile · parcel channels",[("CJ Logistics","Default channel for small parcels nationwide, with waybills issued automatically via API"),
                                       ("Kyungdong Parcel","For heavy and oversized items beyond standard parcel dimensions")]),
  hvy=("Heavy Cargo",[("Low-bed trailers","Construction equipment delivered from the quay to the site"),
                      ("Incheon and Pyeongtaek Port handling","Heavy-lift discharge arranged for RO-RO, bulk, flat-rack and open-top cargo")]),
  cta=("One Operator","The same operator, end to end","From consolidation in China through receipt in Korea, clearance, reconditioning and domestic delivery, one company carries the cargo through.","Discuss a route")),

"zh": dict(title="网络 · 基础设施 — HF物流", crumb="NETWORK", h1="物流网络",
  desc="从中国威海集货据点到仁川港保税仓库、仁川机场自由贸易区仓库及韩国境内配送网络，由合作方Sky国际运输与三福物流共同运营。",
  lede="从产地集货到韩国入库。连接威海集货仓库、仁川港保税仓库与仁川机场自由贸易区仓库的全段，由同一窗口统一管理。",
  s1=("China","中国集货据点","Consolidation Hubs"),
  s1note="在中国装货，在韩国收尾。全程不更换承运方。",
  cn=[("威海","威海 / Weihai","泛杰产业园内运营2栋 — LCL拼箱仓库（HF LOGIS，B3-5）· 跨境电商转运仓（NOVA HF，B3-1）<br>海埠路56号 泛杰产业园","live","运营中"),
      ("深圳","深圳 / Shenzhen","华南地区集货据点","plan","筹备中"),
      ("杭州","杭州 / Hangzhou","华东地区集货据点","plan","筹备中")],
  wh=[("HF LOGIS · LCL拼箱仓库","发往韩国的普通货物集货 · 拼箱","海埠路56号 泛杰产业园 B3-5",
       "将多家出口商的货物拼装入同一集装箱后发运，小批量货物同样能赶上定期班期。"),
      ("NOVA HF · 跨境电商转运仓","采购商品的收货 · 验货 · 发运","海埠路56号 泛杰产业园 B3-1",
       "在当地接收卖家与平台订单，验货后拼箱发运，并直接对接跨境电商专用通关。")],
  s2=("Korea","韩国入库仓库","Bonded Facilities"),
  s2note="急件送往机场自由贸易区仓库，重货与大批量货物进入仁川港保税仓库。可根据货物性质同时调整时效与成本。",
  hubs=[("Sea Cargo · 合作方","Sky国际运输","仁川港保税仓库",
         "仁川广域市中区筑港大路202号<br>电话 +82-32-765-4715~7",
         ["特许保税区 · 室内8,600㎡ / 堆场6,000㎡","集装箱装箱、装货与掏箱作业","可实施整理作业",
          "指定检疫场所 · 持有快递企业备案","货运代理 · 3PL · 通关 · 保险一体衔接",
          "积累25年的中国网络 — 当地分公司及合作方共10处","紧邻仁川港码头，缩短入库时效"]),
        ("Air Cargo · 合作方","三福物流","仁川机场自由贸易区",
         "仁川广域市中区机场洞路296号街171，AMB仁川物流中心 F1-1<br>电话 +82-70-5066-3352",
         ["2002年成立 · 总部员工45名","自由贸易区内保税状态存储","保税运输 · 通关 · 装卸一体化处理",
          "特种货物运输 · 整理作业 · 3PL与4PL","ADT Caps安保系统 · 70台以上摄像头全天运行",
          "每周三定期盘点，管控数量差异","自有货物进出库、保税运输申报与舱单查询系统"])],
  s3=("Fleet","韩国境内运输车辆","Vehicles"),
  s3note="以合作方三福物流的保有量为准。包含冷藏冷冻车与无振动车，按货物特性调配。",
  vcols=["吨位 Class","普通","冷藏 · 冷冻","尾板","无振动","合计"],
  last=("Last Mile · 快递渠道",[("CJ大韩通运","全国小件货物的主渠道，通过API对接自动生成运单"),
                                ("庆东快递","应对重货与大件，覆盖超出普通快递规格的商品")]),
  hvy=("Heavy Cargo · 重件",[("低平板拖车","将工程机械从码头直接送抵韩国境内工地"),
                             ("仁川港 · 平泽港装卸","为滚装、散货、框架箱／开顶箱货物安排重件装卸")]),
  cta=("One Operator","全程不更换承运方","从中国集货到韩国入库、通关、整理作业及境内配送，由一家公司连贯处理。","航线咨询")),
}

VROWS = [("1t", "11", "8", "5", "—", "24"), ("3.5t", "—", "3", "3", "—", "6"),
         ("5t", "6", "10", "—", "2", "18"), ("11t", "15", "9", "—", "5", "29")]


def build(lang):
    m = M[lang]
    h = shell.head(lang, PAGE, m["title"], m["desc"]) + shell.header(lang, PAGE)
    h += shell.phead(lang, m["crumb"], m["h1"], m["lede"])

    nd = "".join('<div class="nd"><span class="city">%s <i>%s</i></span><span class="desc">%s</span>'
                 '<span class="st %s">%s</span></div>' % r for r in m["cn"])
    wh = "".join('<div class="c"><p class="eyebrow dim">%s</p><h3>%s</h3>'
                 '<p class="addr" style="font-size:13px;color:var(--muted)">%s</p>'
                 '<p style="font-size:13.5px;color:var(--ink-2);line-height:1.74">%s</p></div>' % w for w in m["wh"])
    b = """
<section class="sec flush"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:40ch">%s</p></div>
  <div class="nodes">%s</div>
  <div class="split" style="margin-top:32px">%s</div>
</div></section>
""" % (m["s1"][0], m["s1"][1], m["s1"][2], m["s1note"], nd, wh)

    hubs = "".join('<div class="hub"><div class="kind"><span class="en">%s</span>'
                   '<span class="partner"><b>%s</b></span></div><h3>%s</h3>'
                   '<p class="addr">%s</p><ul>%s</ul></div>'
                   % (a, b_, c, d, "".join("<li>%s</li>" % x for x in e)) for a, b_, c, d, e in m["hubs"])
    b += """
<section class="sec panel"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:42ch">%s</p></div>
  <div class="hubs">%s</div>
</div></section>
""" % (m["s2"][0], m["s2"][1], m["s2"][2], m["s2note"], hubs)

    vr = "".join("<tr><td>%s</td>" % r[0] + "".join('<td class="num">%s</td>' % c for c in r[1:]) + "</tr>"
                 for r in VROWS)
    mk = lambda blk: ('<div class="c"><p class="eyebrow dim">%s</p><ul class="checks">%s</ul></div>'
                      % (blk[0], "".join('<li><b>%s</b><span>%s</span></li>' % x for x in blk[1])))
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:40ch">%s</p></div>
  <div class="board-scroll"><table class="data"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>
  <div class="split" style="margin-top:34px">%s%s</div>
</div></section>

<section class="slab"><div class="wrap" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:24px">
  <div style="display:flex;flex-direction:column;gap:10px;max-width:54ch">
    <p class="eyebrow">%s</p><h2>%s</h2><p class="lede">%s</p></div>
  <a class="btn btn-indigo" href="contact.html#quote">%s <span class="ar">&rarr;</span></a>
</div></section>
""" % (m["s3"][0], m["s3"][1], m["s3"][2], m["s3note"],
       "".join('<th scope="col">%s</th>' % c for c in m["vcols"]), vr,
       mk(m["last"]), mk(m["hvy"]),
       m["cta"][0], m["cta"][1], m["cta"][2], m["cta"][3])

    return shell.write(lang, PAGE, h + b + shell.footer(lang))


if __name__ == "__main__":
    for l in LANGS:
        print(build(l))
