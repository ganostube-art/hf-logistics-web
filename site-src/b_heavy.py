# -*- coding: utf-8 -*-
"""중장비 부문"""
import shell
from common import LANGS

PAGE = "heavy.html"

M = {
"ko": dict(title="중장비 부문 — HF 로지스틱스", crumb="HEAVY CARGO", h1="중장비 부문",
  desc="중국 건설기계 수입 운송 — 공장 상차부터 해상 운송, 중량물 하역, 수입통관, 국내 현장 하차까지 단일 창구로 관리합니다.",
  lede="중국 공장에서 국내 현장까지, 장비 전용 물류. 굴착기·지게차·고소작업차 등 장비 규격에 맞춰 선종과 선복을 정하고, 부두에서 현장 하차까지 이어서 처리합니다.",
  s1=("Transport Flow","중국 공장에서 국내 현장까지","6 Stages"),
  s1note="화주사는 장비만 고르면 됩니다. 전 구간을 단일 창구로 관리합니다.",
  flow=[("현지 집화","중국 공장 상차, 선적항까지 내륙 운송"),("선적","선종 선정 및 선복 확보, 결박 · 고박 관리"),
        ("해상 운송","RO-RO · 벌크 · 플랫랙 / 오픈탑"),("입항 · 하역","인천항 · 평택항 중량물 하역"),
        ("수입통관","요건 확인 · HS 분류, 한중 FTA 적용"),("현장 반입","저상 트레일러로 국내 현장 하차")],
  hot=4,
  s1lede="중국 공장 앞에서 국내 현장 하차까지 전 구간을 단일 창구로 관리합니다. 구간마다 업체가 바뀌지 않으므로 지연이 생겨도 책임 소재를 찾을 필요가 없고, 진행 상황을 한 곳에서 확인할 수 있습니다.",
  s2=("Equipment","장비별 운송 관리","By Type"), s2note="화물마다 답이 다릅니다.",
  eq=[("굴착기 · 로더 등 토공장비","중량과 전고가 관건입니다. 붐 · 암을 분리해 전고를 낮추고, 규격에 따라 RO-RO 또는 벌크 · 플랫랙으로 나눠 선적합니다."),
      ("지게차 · 하역장비","소형은 마스트를 분리하면 컨테이너 적입이 가능해 운임을 크게 낮출 수 있습니다. 중대형은 자주 이동으로 RO-RO 선적합니다."),
      ("고소작업차 · 크레인","자력 주행이 가능한 차량형이라 RO-RO가 유리합니다. 붐 길이와 전장에 따라 선복을 사전에 확보해야 합니다.")],
  s3=("Import Requirements","건설기계 수입은 세율보다 요건에서 막힙니다",""),
  req=[("제조사 인증 서류 사전 검증","배출가스 · 형식 관련 서류가 해당 모델 및 엔진과 일치하는지 선적 전에 확인합니다."),
       ("인증 기준 시점 관리","수입 건설기계는 통관 시점이 기준이 됩니다. 기준 변경 일정을 역산해 선적을 조정합니다."),
       ("HS 분류 및 한중 FTA","품목 분류에 따라 세율이 갈립니다. 원산지증명서 사전 확보로 관세를 절감합니다."),
       ("건설기계 등록 지원","통관 후 등록에 필요한 서류를 정리해 전달하고, 현장 투입까지 공백을 최소화합니다.")],
  reqnote=("참고","인증은 중국 제조사가 보유하며, 당사는 해당 서류가 통관 요건에 맞게 제출되도록 관리합니다."),
  s4=("Scope","중장비 부문 사업 범위","Division 02"),
  sc1=("운송 · 통관",[("중기 · 건설기계 수입 운송","중국 → 한국 해상 운송 주선"),
                      ("중량물 통관 · 요건 관리","건설기계 수입 요건 확인 및 서류 관리"),
                      ("차량 및 중장비 운송","부두에서 현장까지 국내 육상 운송")]),
  sc2=("거래 · 중개",[("중기 및 건설기계 매매업","장비 거래 및 중개"),
                      ("중량물 하역 수배","인천항(신항) · 평택항 중량물 하역 조율")]),
  sc2note="다음 단계로 중장비 보관 야드 및 인도장 확보를 준비하고 있습니다.",
  cta=("Get a Quote","장비 모델과 인도 현장만 알려주시면 됩니다","규격과 중량을 확인해 선종 · 선복과 국내 운송 경로까지 함께 제안드립니다.","중장비 견적 요청")),

"en": dict(title="Heavy Cargo — HF Logistics", crumb="HEAVY CARGO", h1="Heavy cargo division",
  desc="Importing construction equipment from China — factory loading, ocean transport, heavy-lift discharge, customs clearance and final delivery, managed through one desk.",
  lede="Dedicated logistics for equipment, from the Chinese factory to the Korean site. We match vessel type and space to the machine — excavators, forklifts, aerial platforms — and stay with it through to drop-off.",
  s1=("Transport Flow","From the Chinese factory to the Korean site","6 Stages"),
  s1note="You pick the machine. We manage every leg through a single desk.",
  flow=[("Loading at origin","Loaded at the Chinese factory and hauled inland to the load port"),
        ("Shipment","Vessel selection, space booking, lashing and securing"),
        ("Ocean transport","RO-RO, bulk, flat rack or open top"),
        ("Arrival and discharge","Heavy-lift discharge at Incheon or Pyeongtaek Port"),
        ("Import clearance","Requirement checks, HS classification and Korea–China FTA treatment"),
        ("Delivery to site","Final drop-off by low-bed trailer")],
  hot=4,
  s1lede="Every leg from the factory gate in China to the drop-off in Korea runs through one desk. Because vendors do not change between legs, there is no question of who is responsible when something slips, and progress can be checked in one place.",
  s2=("Equipment","Handling by equipment type","By Type"), s2note="Every machine needs a different answer.",
  eq=[("Excavators, loaders and earthmoving machines","Weight and overall height decide the method. We detach the boom and arm to bring the height down, then ship by RO-RO or on bulk and flat rack depending on the dimensions."),
      ("Forklifts and handling equipment","On smaller units, removing the mast allows container stuffing and cuts freight cost sharply. Larger units are driven on board for RO-RO."),
      ("Aerial platforms and cranes","These are self-driving vehicle types, so RO-RO works best. Space has to be booked in advance according to boom length and overall length.")],
  s3=("Import Requirements","Equipment imports stall on requirements, not on duty rates",""),
  req=[("Manufacturer certification checked in advance","We confirm before shipment that emissions and type-approval documents match the exact model and engine."),
       ("Managing the effective date of standards","For imported construction equipment, the clearance date is what counts. We work back from any change in standards and adjust the sailing."),
       ("HS classification and the Korea–China FTA","Classification decides the duty rate. Securing the certificate of origin in advance reduces duty."),
       ("Support for equipment registration","We compile and hand over the documents needed for registration after clearance, so there is no gap before the machine goes to work.")],
  reqnote=("Note","Certification is held by the Chinese manufacturer; our role is to ensure those documents are submitted in the form clearance requires."),
  s4=("Scope","What the heavy cargo division covers","Division 02"),
  sc1=("Transport and clearance",[("Construction equipment import transport","Ocean forwarding from China to Korea"),
                                  ("Heavy-lift clearance and compliance","Import requirement checks and document control"),
                                  ("Vehicle and equipment haulage","Inland transport from the quay to the site")]),
  sc2=("Trading and brokerage",[("Equipment trading","Sales and brokerage of construction machinery"),
                                ("Heavy-lift handling","Coordinating heavy-lift discharge at Incheon and Pyeongtaek Port")]),
  sc2note="A storage yard and handover site for heavy equipment are being prepared as the next step.",
  cta=("Get a Quote","Just tell us the model and the delivery site","We check the dimensions and weight, then propose the vessel type, the space and the inland route together.","Request a heavy cargo quote")),

"zh": dict(title="重型设备业务 — HF物流", crumb="HEAVY CARGO", h1="重型设备业务",
  desc="中国工程机械进口运输 — 从工厂装车、海运、重件卸货、进口通关到韩国境内现场卸车，由单一窗口统一管理。",
  lede="从中国工厂到韩国工地的设备专用物流。按挖掘机、叉车、高空作业车等设备规格确定船型与舱位，并一路负责到码头至现场卸车。",
  s1=("Transport Flow","从中国工厂到韩国工地","6 Stages"),
  s1note="货主只需选定设备，全程由我们以单一窗口管理。",
  flow=[("产地集货","在中国工厂装车，内陆运至装货港"),("装运","选定船型、确保舱位，管理绑扎与固定"),
        ("海上运输","滚装 · 散货 · 框架箱／开顶箱"),("到港 · 卸货","仁川港、平泽港重件卸货"),
        ("进口通关","要件确认 · HS归类，适用中韩FTA"),("现场交付","由低平板拖车送抵工地卸车")],
  hot=4,
  s1lede="从中国工厂门口到韩国现场卸车的全部区段由单一窗口管理。各区段不更换承运方，即便出现延误也无需追究责任归属，进度可在一处查询。",
  s2=("Equipment","按设备类型运输管理","By Type"), s2note="每台设备的答案都不一样。",
  eq=[("挖掘机 · 装载机等土方机械","重量与全高是关键。拆下动臂与斗杆降低全高，再按规格分别以滚装或散货、框架箱装运。"),
      ("叉车 · 装卸设备","小型机拆下门架即可装箱，可大幅降低运费。中大型则自行驶上船，采用滚装。"),
      ("高空作业车 · 起重机","属可自行行驶的车辆型，滚装更有利。需根据臂长与全长提前确保舱位。")],
  s3=("Import Requirements","工程机械进口卡在要件，而不是税率",""),
  req=[("事前核验制造商认证文件","装运前确认排放与型式相关文件是否与该型号及发动机一致。"),
       ("认证基准时点管理","进口工程机械以通关时点为准。倒推基准变更时间表，相应调整装运安排。"),
       ("HS归类与中韩FTA","品目归类决定税率。提前取得原产地证书可降低关税。"),
       ("协助工程机械登记","通关后整理并交付登记所需文件，尽量缩短投入现场前的空档。")],
  reqnote=("备注","认证由中国制造商持有，我们的职责是确保这些文件按通关要件的格式提交。"),
  s4=("Scope","重型设备业务范围","Division 02"),
  sc1=("运输 · 通关",[("工程机械进口运输","中国 → 韩国海运代理"),
                      ("重件通关 · 要件管理","工程机械进口要件确认及单证管理"),
                      ("车辆及重型设备运输","从码头到现场的韩国境内陆运")]),
  sc2=("交易 · 中介",[("工程机械买卖","设备交易及中介"),
                      ("重件装卸安排","协调仁川港、平泽港的重件装卸")]),
  sc2note="下一步正在筹备重型设备堆场与交付场地。",
  cta=("Get a Quote","只需告知设备型号与交货现场","我们会核对规格与重量，连同船型、舱位及韩国境内运输路线一并提出方案。","重型设备报价咨询")),
}


def build(lang):
    m = M[lang]
    h = shell.head(lang, PAGE, m["title"], m["desc"]) + shell.header(lang, PAGE)
    h += shell.phead(lang, m["crumb"], m["h1"], m["lede"])

    fl = "".join('<div class="s%s"><span class="n">0%d</span><b>%s</b><span>%s</span></div>'
                 % (" hot" if i + 1 == m["hot"] + 1 else "", i + 1, t, d)
                 for i, (t, d) in enumerate(m["flow"]))
    b = """
<section class="sec flush"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:40ch">%s</p></div>
  <div class="flow">%s</div>
  <p class="lede" style="margin-top:26px">%s</p>
</div></section>
""" % (m["s1"][0], m["s1"][1], m["s1"][2], m["s1note"], fl, m["s1lede"])

    eq = "".join('<div class="r"><span class="ix" style="color:var(--indigo)">0%d</span>'
                 '<h3>%s</h3><p>%s</p></div>' % (i + 1, t, d) for i, (t, d) in enumerate(m["eq"]))
    b += """
<section class="sec panel" id="equipment"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:36ch">%s</p></div>
  <div class="risks cols-3">%s</div>
</div></section>
""" % (m["s2"][0], m["s2"][1], m["s2"][2], m["s2note"], eq)

    rq = "".join('<li style="border-color:rgba(255,255,255,.14)"><b style="color:#fff">%s</b>'
                 '<span style="color:#A9B8D6">%s</span></li>' % r for r in m["req"])
    b += """
<section class="slab" id="requirements"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p><h2>%s</h2></div></div>
  <ol class="steps" style="border-color:rgba(255,255,255,.14)">%s</ol>
  <div class="cite" style="background:rgba(125,160,242,.12);border-left-color:#7EA0F2;color:#C3D0EA;margin-top:24px">
    <b style="color:#7EA0F2">%s</b>%s</div>
</div></section>
""" % (m["s3"][0], m["s3"][1], rq, m["reqnote"][0], m["reqnote"][1])

    mk = lambda blk, extra="": ('<div class="c"><p class="eyebrow dim">%s</p><ul class="checks">%s</ul>%s</div>'
                                % (blk[0], "".join('<li><b>%s</b><span>%s</span></li>' % x for x in blk[1]), extra))
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div></div>
  <div class="split">%s%s</div>
</div></section>

<section class="sec panel"><div class="wrap" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:24px">
  <div style="display:flex;flex-direction:column;gap:10px;max-width:52ch">
    <p class="eyebrow">%s</p><h2>%s</h2><p class="lede">%s</p></div>
  <a class="btn btn-primary" href="contact.html#quote">%s <span class="ar">&rarr;</span></a>
</div></section>
""" % (m["s4"][0], m["s4"][1], m["s4"][2], mk(m["sc1"]),
       mk(m["sc2"], '<p class="formnote">%s</p>' % m["sc2note"]),
       m["cta"][0], m["cta"][1], m["cta"][2], m["cta"][3])

    return shell.write(lang, PAGE, h + b + shell.footer(lang))


if __name__ == "__main__":
    for l in LANGS:
        print(build(l))
