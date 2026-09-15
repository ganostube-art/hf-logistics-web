# -*- coding: utf-8 -*-
"""보수작업 대행 — [T] 전문용어 밀집 페이지. glossary.md 필독"""
import shell
from common import LANGS

PAGE = "repair.html"

M = {
"ko": dict(title="보수작업 대행 — HF 로지스틱스", crumb="BONDED REPAIR", h1="보수작업 원스톱 대행",
  desc="관세법 제158조에 따른 보세 보수작업 대행. 원산지 표시, 한글 표시사항, KC 인증 표기, 라벨 오기, 재포장까지 인천항 보세창고에서 직접 수행합니다.",
  lede="표시사항 하나 때문에 화물을 되돌려 보낼 필요는 없습니다. 보세구역에 둔 상태에서 세관 승인을 받아 보완하면 그대로 통관됩니다. 문제는 그 작업을 한국에서 누가 하느냐입니다.",
  d1=("Definition","보수작업이란"),
  d1p="보세구역에 장치된 물품에 대해 세관장의 승인을 받아 수행하는 작업입니다. 통관을 위한 개장, 분할 · 구분, 합병, 원산지표시 등이 대상이며, 운송 중 파손 · 변질된 물품의 시급한 보수도 포함됩니다.",
  cite=("근거","관세법 제158조 · 보세화물관리에 관한 고시 제20조"),
  d2=("Out of Scope","보수작업으로 해결되지 않는 것"),
  no=[("품목분류가 바뀌는 작업","HSK 10단위가 달라지는 가공은 보수작업 범위를 벗어납니다"),
      ("수입요건 · 인증 자체가 미충족인 경우","표기가 아니라 인증 자체가 없는 경우는 별도 절차가 필요합니다"),
      ("외국물품을 보수 재료로 사용하는 작업","보수에 쓰이는 자재는 내국물품이어야 합니다")],
  nonote="※ 작업 가능 여부는 품목과 세관 판단에 따라 달라질 수 있어, 사전에 확인 후 안내드립니다.",
  s2=("Scope of Work","당사가 수행하는 범위","5 Steps"),
  s2note="원인 파악부터 세관 보고까지 한 창구에서 진행합니다. 수출자는 승인 여부와 비용만 결정하면 됩니다.",
  steps=[("원인 파악","세관 시정 요구 내용을 확인하고 현품과 대조해 무엇을 고쳐야 하는지 특정"),
         ("승인 신청","보수작업승인신청서를 작성해 세관에 제출하고 승인 절차 진행"),
         ("자재 · 라벨 제작","한글 표시사항, 원산지 라벨, 포장재를 국내에서 직접 제작"),
         ("현장 작업","보세창고 내에서 부착 · 재포장 · 분할 등 실작업 수행"),
         ("완료 보고","작업 결과를 세관에 보고하고, 사진과 내역을 수출자에게 전달")],
  s3=("Typical Cases","대표 보수 작업","6 Types"), s3note="실제로 자주 발생하는 유형입니다.",
  cases=[("원산지 표시","표시 누락 또는 기준 미달 시 라벨 제작 후 규정에 맞는 위치 · 방법으로 부착"),
         ("한글 표시사항","제품명 · 수입자 · 제조국 · 주의사항 등 국내 의무 표시를 제작해 부착"),
         ("인증 정보 표기","KC 마크 및 인증번호 등 안전 관련 표기 보완"),
         ("라벨 오기 수정","잘못 인쇄된 라벨 제거 후 정정 라벨 재부착"),
         ("포장 교체 · 재포장","운송 중 파손된 외포장 교체, 내품 확인 후 재포장"),
         ("구분 · 분할 · 합병","세트 구성 변경, 혼재 화물 분할 또는 합병 작업")],
  s4=("Incident Response","돌발상황 대응 프로세스","보류 통보부터 통관 재개까지"),
  inc=[("보류 통보 접수","세관 · 관세사로부터 시정 요구 내용을 즉시 확인합니다."),
       ("현품 확인","보세창고에서 실물을 직접 확인하고 사진으로 상태를 공유합니다."),
       ("수출자 협의","해결 방안과 예상 비용 · 소요 기간을 사전 안내한 뒤 진행에 동의를 받습니다."),
       ("승인 신청 · 작업","세관 승인 후 라벨 제작 및 현장 작업을 수행합니다."),
       ("통관 재개 · 보고","완료 보고 후 통관을 진행하고, 작업 사진과 내역을 수출자에게 전달합니다.")],
  incnote=("참고","수입신고 후 원산지표시 시정 요구에 따른 보수작업은 별도 승인 절차 없이 진행되는 경우가 있어, 사안별로 최단 경로를 안내드립니다."),
  s5=("Work Infrastructure","보수작업은 보세구역 안에서 이루어집니다","Facilities"),
  s5btn="네트워크 상세",
  s5lede="통관 전 상태에서 손을 댈 수 있다는 것이 핵심입니다. 이미 통관된 뒤에 문제를 발견하면 되돌리기 어렵습니다. 보세 상태에서 해결하면 반송 없이 그대로 진행됩니다.",
  cta=("Hold Response","보류 건은 시간이 비용입니다","세관 시정 요구 내용을 그대로 전달해 주시면, 접수 즉시 현품 확인 일정을 잡습니다.","보류 건 접수")),

"en": dict(title="Bonded Reconditioning — HF Logistics", crumb="BONDED REPAIR", h1="Bonded reconditioning, end to end",
  desc="Reconditioning under bond per Article 158 of the Korean Customs Act — country-of-origin marking, Korean-language labelling, KC certification marks, misprinted labels and repacking, carried out at our Incheon Port bonded warehouse.",
  lede="A labelling fault is no reason to send cargo back. Corrected under bond with customs approval, the shipment clears as it stands. The question is who does that work in Korea.",
  d1=("Definition","What reconditioning means here"),
  d1p="Work performed on goods held in a bonded area, with the approval of the head of the customs office. It covers opening, splitting, sorting, combining and country-of-origin marking for the purpose of clearance, and extends to urgent repair of goods damaged or degraded in transit.",
  cite=("Legal basis","Customs Act Article 158 · Bonded Cargo Management Notice Article 20"),
  d2=("Out of Scope","What reconditioning cannot fix"),
  no=[("Work that changes the tariff classification","Processing that shifts the 10-digit HSK code falls outside reconditioning"),
      ("Missing import requirements or certification itself","Where the certification is absent rather than merely unmarked, a separate procedure applies"),
      ("Using foreign goods as reconditioning materials","Materials used in the work must be domestic goods")],
  nonote="Whether a given job is permitted depends on the commodity and on the customs officer's judgement, so we confirm in advance and advise before starting.",
  s2=("Scope of Work","What we carry out","5 Steps"),
  s2note="From diagnosis to the report back to customs, all through one desk. The exporter only decides whether to approve and at what cost.",
  steps=[("Diagnosis","Reading the customs correction notice and comparing it against the actual goods to pin down what must change"),
         ("Approval application","Preparing the reconditioning approval application and filing it with customs"),
         ("Materials and labels","Producing Korean-language labels, country-of-origin marks and packaging in Korea"),
         ("Work on site","Applying labels, repacking and splitting inside the bonded warehouse"),
         ("Completion report","Reporting the result to customs and sending photographs and a breakdown to the exporter")],
  s3=("Typical Cases","Work we do most often","6 Types"), s3note="These are the cases that actually recur.",
  cases=[("Country-of-origin marking","Where marking is missing or falls short, labels are produced and applied in the position and manner the rules require"),
         ("Korean-language particulars","Producing and applying the mandatory Korean markings: product name, importer, country of manufacture and cautions"),
         ("Certification marks","Adding safety-related marks such as the KC mark and certification number"),
         ("Correcting misprinted labels","Removing incorrectly printed labels and applying corrected ones"),
         ("Replacing packaging and repacking","Replacing outer packaging damaged in transit and repacking after checking the contents"),
         ("Sorting, splitting and combining","Changing set composition, and splitting or combining consolidated cargo")],
  s4=("Incident Response","How we respond when cargo is held","From the hold notice to clearance resuming"),
  inc=[("Hold notice received","We confirm the correction required, directly with customs or the customs broker."),
       ("Physical inspection","We inspect the goods at the bonded warehouse and share photographs of their condition."),
       ("Agreeing the plan with you","We set out the remedy, the expected cost and the time needed, and proceed once you agree."),
       ("Approval and work","After customs approval, labels are produced and the work is carried out."),
       ("Clearance resumes","We file the completion report, clearance proceeds, and photographs and a breakdown go to the exporter.")],
  incnote=("Note","Where the correction relates to country-of-origin marking after the import declaration, the work can sometimes proceed without a separate approval step. We advise the shortest route case by case."),
  s5=("Work Infrastructure","Reconditioning happens inside the bonded area","Facilities"),
  s5btn="Network in detail",
  s5lede="Being able to work on the goods before clearance is the whole point. Once cargo has cleared, problems found afterwards are hard to undo. Resolved under bond, the shipment moves on without being returned.",
  cta=("Hold Response","When cargo is held, time is money","Send us the customs correction notice as it stands and we schedule a physical inspection as soon as it arrives.","Report held cargo")),

"zh": dict(title="保税整理作业 — HF物流", crumb="BONDED REPAIR", h1="保税整理作业一站式代理",
  desc="依据韩国《关税法》第158条实施的保税整理作业代理 — 原产地标识、韩文标示事项、KC认证标识、标签印错、重新包装，均在仁川港保税仓库内直接完成。",
  lede="不必因为一处标示问题就把货退回去。在保税区状态下取得海关批准并加以补正，即可照常通关。问题在于，这项作业在韩国由谁来做。",
  d1=("Definition","何谓整理作业"),
  d1p="指对存放于保税区的货物，经海关关长批准后实施的作业。适用范围包括为通关而进行的开箱、分割、分类、合并及原产地标识等，也包括对运输途中破损或变质货物的紧急修整。",
  cite=("法律依据","《关税法》第158条 · 《保税货物管理公告》第20条"),
  d2=("Out of Scope","整理作业无法解决的情形"),
  no=[("导致品目归类变更的作业","使HSK十位编码发生变化的加工，超出整理作业范围"),
      ("进口要件或认证本身未满足","若并非标示缺失、而是认证本身不存在，则需另行办理"),
      ("以外国货物作为整理用材料","整理所用材料必须为韩国国内货物")],
  nonote="※ 能否作业取决于品名及海关判断，我们会事先确认后再行告知。",
  s2=("Scope of Work","我们承担的工作范围","5 Steps"),
  s2note="从查明原因到向海关报告，全部由同一窗口完成。出口商只需决定是否同意及费用。",
  steps=[("查明原因","核对海关整改通知内容并与实物比对，确定究竟需要修正什么"),
         ("申请批准","填写整理作业批准申请书并提交海关，推进审批流程"),
         ("制作材料与标签","在韩国境内自行制作韩文标示、原产地标签与包装材料"),
         ("现场作业","在保税仓库内实施贴标、重新包装、分割等实际作业"),
         ("完成报告","将作业结果报告海关，并把照片与明细交付出口商")],
  s3=("Typical Cases","常见整理作业","6 Types"), s3note="以下为实际高频发生的情形。",
  cases=[("原产地标识","标识缺失或不达标时，制作标签并按规定的位置与方式粘贴"),
         ("韩文标示事项","制作并粘贴产品名称、进口商、原产国、注意事项等韩国法定标示"),
         ("认证信息标识","补充KC标识及认证编号等安全相关标注"),
         ("标签印错修正","去除印制错误的标签，重新粘贴更正后的标签"),
         ("更换包装 · 重新包装","更换运输途中破损的外包装，确认内容物后重新包装"),
         ("分类 · 分割 · 合并","变更套装构成，对拼装货物进行分割或合并")],
  s4=("Incident Response","突发状况应对流程","从扣货通知到恢复通关"),
  inc=[("接到扣货通知","立即向海关或报关师确认整改要求的具体内容。"),
       ("现场查验","在保税仓库直接查看实物，并以照片共享货物状态。"),
       ("与出口商协商","事先说明解决方案、预计费用与所需时间，取得同意后再推进。"),
       ("申请批准 · 实施作业","取得海关批准后制作标签并实施现场作业。"),
       ("恢复通关 · 报告","提交完成报告后继续通关，并将作业照片与明细交付出口商。")],
  incnote=("备注","进口申报后因原产地标识整改要求而进行的整理作业，有时可不经单独审批直接实施。我们会按个案给出最短路径。"),
  s5=("Work Infrastructure","整理作业在保税区内完成","Facilities"),
  s5btn="查看网络详情",
  s5lede="能在通关前动手，正是关键所在。货物一旦通关，事后发现问题就很难挽回。在保税状态下解决，无需退运即可继续推进。",
  cta=("Hold Response","扣货案件，时间就是成本","请将海关整改通知原样转发给我们，受理后立即安排现场查验。","提交扣货案件")),
}

HUBS = {
"ko":[("Sea Cargo","협력사 <b>㈜스카이국제운송</b>","인천항 보세창고","인천광역시 중구 축항대로 202 (항동7가 95-1)",
       ["특허보세구역 · 실내 2,600평 / 야드 1,815평","컨테이너 적입 · 적출 및 보수작업 수행",
        "검역장소 지정 · 특송업체 등록 보유","인천항 부두 인접, 반입 리드타임 단축"]),
      ("Air Cargo","협력사 <b>삼복로지스틱㈜</b>","인천공항 자유무역지역","인천광역시 중구 공항동로 296번길 171, AMB 인천물류센터 F1-1",
       ["자유무역지역 내 보세 상태 보관","보세운송 · 통관 · 하역 일괄 처리",
        "경비 시스템 및 CCTV 상시 운영","정기 재고조사로 수량 차이 관리"])],
"en":[("Sea Cargo","Partner <b>Sky International Transport</b>","Incheon Port bonded warehouse","202 Chukhang-daero, Jung-gu, Incheon",
       ["Licensed bonded area · 8,600 m² indoor / 6,000 m² yard","Container loading, unloading and reconditioning",
        "Designated quarantine site · registered express operator","Adjacent to the quay, shortening inbound lead time"]),
      ("Air Cargo","Partner <b>Sambok Logistic</b>","Incheon Airport Free Trade Zone","F1-1 AMB Incheon Logistics Centre, 171 Gonghangdong-ro 296beon-gil, Jung-gu, Incheon",
       ["Bonded storage inside the Free Trade Zone","Bonded transport, clearance and handling as one service",
        "Security system and CCTV running at all times","Scheduled stock counts to control discrepancies"])],
"zh":[("Sea Cargo","合作方 <b>Sky国际运输</b>","仁川港保税仓库","仁川广域市中区筑港大路202号",
       ["特许保税区 · 室内8,600㎡ / 堆场6,000㎡","集装箱装箱、掏箱及整理作业",
        "指定检疫场所 · 持有快递企业备案","紧邻仁川港码头，缩短入库时效"]),
      ("Air Cargo","合作方 <b>三福物流</b>","仁川机场自由贸易区","仁川广域市中区机场洞路296号街171，AMB仁川物流中心 F1-1",
       ["自由贸易区内保税状态存储","保税运输 · 通关 · 装卸一体化处理",
        "安保系统与摄像头全天运行","定期盘点管控数量差异"])],
}


def build(lang):
    m = M[lang]
    h = shell.head(lang, PAGE, m["title"], m["desc"]) + shell.header(lang, PAGE)
    h += shell.phead(lang, m["crumb"], m["h1"], m["lede"])

    no = "".join('<li><b>%s</b><span>%s</span></li>' % x for x in m["no"])
    b = """
<section class="sec flush"><div class="wrap"><div class="split">
  <div class="c"><p class="eyebrow">%s</p><h2 style="font-size:22px">%s</h2>
    <p style="font-size:14.5px;line-height:1.84;color:var(--ink-2)">%s</p>
    <div class="cite"><b>%s</b>%s</div></div>
  <div class="c"><p class="eyebrow dim">%s</p><h2 style="font-size:22px">%s</h2>
    <ul class="checks no">%s</ul>
    <p class="formnote">%s</p></div>
</div></div></section>
""" % (m["d1"][0], m["d1"][1], m["d1p"], m["cite"][0], m["cite"][1],
       m["d2"][0], m["d2"][1], no, m["nonote"])

    st = "".join('<div class="s%s"><span class="n">0%d</span><b>%s</b><span>%s</span></div>'
                 % (" hot" if i == 3 else "", i + 1, t, d) for i, (t, d) in enumerate(m["steps"]))
    b += """
<section class="sec panel"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:38ch">%s</p></div>
  <div class="flow cols-5">%s</div>
</div></section>
""" % (m["s2"][0], m["s2"][1], m["s2"][2], m["s2note"], st)

    cs = "".join('<div class="r"><span class="ix" style="color:var(--indigo)">0%d</span>'
                 '<h3>%s</h3><p>%s</p></div>' % (i + 1, t, d) for i, (t, d) in enumerate(m["cases"]))
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <p class="note" style="max-width:36ch">%s</p></div>
  <div class="risks cols-3">%s</div>
</div></section>
""" % (m["s3"][0], m["s3"][1], m["s3"][2], m["s3note"], cs)

    inc = "".join('<li style="border-color:rgba(255,255,255,.14)"><b style="color:#fff">%s</b>'
                  '<span style="color:#A9B8D6">%s</span></li>' % x for x in m["inc"])
    b += """
<section class="slab"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p><h2>%s</h2>
    <p class="lede">%s</p></div></div>
  <ol class="steps" style="border-color:rgba(255,255,255,.14)">%s</ol>
  <div class="cite" style="background:rgba(125,160,242,.12);border-left-color:#7EA0F2;color:#C3D0EA;margin-top:24px">
    <b style="color:#7EA0F2">%s</b>%s</div>
</div></section>
""" % (m["s4"][0], m["s4"][1], m["s4"][2], inc, m["incnote"][0], m["incnote"][1])

    hubs = "".join('<div class="hub"><div class="kind"><span class="en">%s</span>'
                   '<span class="partner">%s</span></div><h3>%s</h3><p class="addr">%s</p>'
                   '<ul>%s</ul></div>' % (a, p, t, ad, "".join("<li>%s</li>" % x for x in li))
                   for a, p, t, ad, li in HUBS[lang])
    b += """
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="t"><p class="eyebrow">%s</p>
    <h2>%s<span class="en">%s</span></h2></div>
    <a class="btn btn-ghost" href="network.html">%s <span class="ar">&rarr;</span></a></div>
  <div class="hubs">%s</div>
  <p class="lede" style="margin-top:28px">%s</p>
</div></section>

<section class="sec panel"><div class="wrap" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:24px">
  <div style="display:flex;flex-direction:column;gap:10px;max-width:52ch">
    <p class="eyebrow">%s</p><h2>%s</h2><p class="lede">%s</p></div>
  <div style="display:flex;flex-wrap:wrap;gap:10px">
    <a class="btn btn-primary" href="contact.html#quote">%s <span class="ar">&rarr;</span></a>
    <a class="btn btn-ghost" href="tel:032-888-0824">032-888-0824</a></div>
</div></section>
""" % (m["s5"][0], m["s5"][1], m["s5"][2], m["s5btn"], hubs, m["s5lede"],
       m["cta"][0], m["cta"][1], m["cta"][2], m["cta"][3])

    return shell.write(lang, PAGE, h + b + shell.footer(lang))


if __name__ == "__main__":
    for l in LANGS:
        print(build(l))
