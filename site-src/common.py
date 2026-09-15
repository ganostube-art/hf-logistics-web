# -*- coding: utf-8 -*-
"""공통 문구 — 상단 바 · 내비게이션 · 푸터 · 회사 정보

용어 검수 표시
  [T] 표시가 붙은 항목은 통관·물류 전문용어라 실무 검수가 필요합니다.
  glossary.md 에 전체 목록이 정리되어 있습니다.
"""

LANGS = ["ko", "en", "zh"]

# 언어별 표기 · 폰트 · 줄바꿈 규칙
META = {
    "ko": {"label": "KOR", "htmllang": "ko", "dir": "",
           "font": "Noto+Sans+KR:wght@400;500;700;800",
           "family": '"Noto Sans KR","Pretendard",-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo",sans-serif',
           "wordbreak": "keep-all"},
    "en": {"label": "ENG", "htmllang": "en", "dir": "en/",
           "font": "Inter:wght@400;500;600;700;800",
           "family": '"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif',
           "wordbreak": "normal"},
    "zh": {"label": "中文", "htmllang": "zh-Hans", "dir": "zh/",
           "font": "Noto+Sans+SC:wght@400;500;700;900",
           "family": '"Noto Sans SC","PingFang SC","Microsoft YaHei",-apple-system,sans-serif',
           "wordbreak": "normal"},
}

# 상단 유틸리티 바
UTILITY = {
    "ko": "국제물류주선 · 중장비 운반<span class=\"dot\">·</span>인천항 · 인천세관 인접",
    "en": "Freight Forwarding &amp; Heavy Cargo<span class=\"dot\">·</span>Next to Incheon Port &amp; Customs",
    "zh": "国际物流运输 · 重型设备运输<span class=\"dot\">·</span>毗邻仁川港与仁川海关",
}

# 주 메뉴
NAV = {
    "ko": [("services.html", "서비스"), ("heavy.html", "중장비"), ("network.html", "네트워크"),
           ("about.html", "회사소개"), ("contact.html", "문의처")],
    "en": [("services.html", "Services"), ("heavy.html", "Heavy Cargo"), ("network.html", "Network"),
           ("about.html", "Company"), ("contact.html", "Contact")],
    "zh": [("services.html", "服务"), ("heavy.html", "重型设备"), ("network.html", "网络"),
           ("about.html", "公司介绍"), ("contact.html", "联系方式")],
}

QUOTE_BTN = {"ko": "견적 요청", "en": "Request a Quote", "zh": "报价咨询"}
MENU_BTN = {"ko": "MENU", "en": "MENU", "zh": "菜单"}
NAV_ARIA = {"ko": "주 메뉴", "en": "Main menu", "zh": "主菜单"}
LANG_ARIA = {"ko": "언어 선택", "en": "Language", "zh": "语言选择"}
HOME = {"ko": "HOME", "en": "HOME", "zh": "首页"}

# 회사 정보 (주소는 언어별 표기)
COMPANY = {
    "ko": {"name": "주식회사 에이치에프로지스틱스", "short": "HF 로지스틱스",
           "addr": "인천광역시 중구 서해대로 342, 풍천빌딩 505호",
           "biz": "사업자등록번호 865-86-03145", "ceo": "대표이사 안규철"},
    "en": {"name": "HF LOGISTICS CO., LTD.", "short": "HF Logistics",
           "addr": "#505 Pungcheon Bldg, 342 Seohae-daero, Jung-gu, Incheon, Korea",
           "biz": "Business Reg. No. 865-86-03145", "ceo": "CEO Ahn Gyu-cheol"},
    "zh": {"name": "HF物流株式会社", "short": "HF物流",
           "addr": "韩国仁川广域市中区西海大路342号 丰川大厦505室",
           "biz": "营业执照号 865-86-03145", "ceo": "首席执行官 安圭哲"},
}

# 푸터 메뉴
FOOT = {
    "ko": {
        "c1": "종합물류",
        "c1items": [("services.html#forwarding", "국제물류주선 (포워딩)"), ("services.html#tpl", "3PL · 풀필먼트"),
                    ("services.html#ecommerce", "전자상거래 물류"), ("services.html#bonded", "보세창고 보관"),
                    ("repair.html", "보수작업 대행"), ("services.html#domestic", "국내 배송 · 반품")],
        "c2": "중장비",
        "c2items": [("heavy.html", "중국 건설기계 수입 운송"), ("heavy.html#equipment", "장비별 운송 관리"),
                    ("heavy.html#requirements", "통관 요건 관리")],
        "c3": "회사",
        "c3items": [("about.html", "회사소개"), ("about.html#history", "연혁"),
                    ("network.html", "네트워크 · 인프라"), ("contact.html", "문의처 · 오시는 길"),
                    ("contact.html#quote", "견적 요청")],
        "tag": "국제물류주선 · 중량물 운송 · 인천",
    },
    "en": {
        "c1": "Logistics",
        "c1items": [("services.html#forwarding", "Freight Forwarding"), ("services.html#tpl", "3PL &amp; Fulfillment"),
                    ("services.html#ecommerce", "E-Commerce Logistics"), ("services.html#bonded", "Bonded Warehousing"),
                    ("repair.html", "Bonded Reconditioning"), ("services.html#domestic", "Delivery &amp; Returns")],
        "c2": "Heavy Cargo",
        "c2items": [("heavy.html", "Construction Equipment Import"), ("heavy.html#equipment", "Handling by Equipment Type"),
                    ("heavy.html#requirements", "Import Requirements")],
        "c3": "Company",
        "c3items": [("about.html", "About Us"), ("about.html#history", "History"),
                    ("network.html", "Network &amp; Facilities"), ("contact.html", "Contact &amp; Directions"),
                    ("contact.html#quote", "Request a Quote")],
        "tag": "Freight Forwarding · Heavy Cargo · Incheon, Korea",
    },
    "zh": {
        "c1": "综合物流",
        "c1items": [("services.html#forwarding", "国际物流运输代理"), ("services.html#tpl", "3PL · 履约配送"),
                    ("services.html#ecommerce", "跨境电商物流"), ("services.html#bonded", "保税仓储"),
                    ("repair.html", "保税整理作业"), ("services.html#domestic", "韩国境内配送 · 退货")],
        "c2": "重型设备",
        "c2items": [("heavy.html", "中国工程机械进口运输"), ("heavy.html#equipment", "按设备类型运输管理"),
                    ("heavy.html#requirements", "通关要件管理")],
        "c3": "公司",
        "c3items": [("about.html", "公司介绍"), ("about.html#history", "发展历程"),
                    ("network.html", "网络 · 基础设施"), ("contact.html", "联系方式 · 交通指南"),
                    ("contact.html#quote", "报价咨询")],
        "tag": "国际物流运输 · 重型货物运输 · 韩国仁川",
    },
}

# 담당자 — 이 한 곳만 고치면 전 페이지에 반영됩니다
MGR = {"phone": "010-3178-8330", "email": "dydw0625@nate.com"}

# 공통 CTA · 문의 블록
CONTACT_BLOCK = {
    "ko": {"addr": "주소", "tel": "대표전화", "fax": "팩스", "mgr": "담당", "mgrname": "임민지 부장", "email": "이메일",
           "toform": "견적 요청 폼으로", "ask": "문의 시 알려주시면 빠릅니다"},
    "en": {"addr": "Address", "tel": "Tel", "fax": "Fax", "mgr": "Contact", "mgrname": "Lim Min-ji, General Manager", "email": "Email",
           "toform": "Go to quote form", "ask": "Tell us this and we can move faster"},
    "zh": {"addr": "地址", "tel": "电话", "fax": "传真", "mgr": "负责人", "mgrname": "Lim Min-ji 部长", "email": "邮箱",
           "toform": "前往报价表单", "ask": "告知以下信息可加快处理"},
}
