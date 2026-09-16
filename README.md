# HF 로지스틱스 홈페이지

주식회사 에이치에프로지스틱스(HF LOGISTICS CO., LTD.) 공식 홈페이지.
빌드 도구 없이 동작하는 정적 사이트입니다.

## 다국어

한국어 · 영어 · 중국어(간체) 3개 언어로 제공합니다.

| 언어 | 주소 | 폴더 |
|---|---|---|
| 한국어 | `hflogis.com/` | 루트 |
| English | `hflogis.com/en/` | `en/` |
| 中文 | `hflogis.com/zh/` | `zh/` |

**HTML을 직접 고치지 마세요.** 21개 페이지는 `site-src/` 의 파이썬 스크립트가 생성합니다.

```bash
cd site-src
python3 build_all.py    # 21개 페이지 재생성
```

문구 위치는 `GLOSSARY.md` 하단을 참고하세요.
전문용어 검수 목록도 `GLOSSARY.md` 에 있습니다.

## 협력사 시설 사진

`network.html` 의 "한국 반입 창고" 카드에 협력사 창고 사진이 들어갑니다.

| 파일 | 시설 | 출처 |
|---|---|---|
| `assets/img/fac-sky.jpg` | 인천항 보세창고 | ㈜스카이국제운송 |
| `assets/img/fac-sambok.jpg` | 인천공항 자유무역지역 창고 | 삼복로지스틱㈜ |

**저작권은 각 협력사에 있습니다.** 페이지에 "사진 제공 · 〇〇" 출처를 달아두었으니
지우지 마세요. 게재 동의 여부는 실무팀에서 확인이 필요합니다.

원본은 저장소 밖 `ref/photos/` 에 있고, 가공은 아래로 합니다.

```bash
cd site-src
python3 photos.py       # 16:9 크롭 · 1280x720 · JPEG
```

사진을 바꾸시려면 `photos.py` 의 `JOBS` 에서 파일명과 세로 기준점만 고치면 됩니다.

## 공유 카드 (OG)

카톡·슬랙·페이스북에 주소를 붙이면 뜨는 미리보기 카드입니다.
`assets/img/og-{ko,en,zh}.png` (1200×630) 를 씁니다.

```bash
cd site-src
python3 ogimage.py      # 카드 이미지 3장 재생성
python3 build_all.py    # 이미지 해시가 바뀌므로 HTML도 같이
```

카드 문구는 `ogimage.py` 의 `CARD` 에 있습니다. macOS 시스템 폰트를
쓰므로 다른 환경에서 돌리려면 `FONTS` 경로를 바꿔야 합니다.

로고 원본이 360×96 저해상도라 카드에는 HF 심볼만 잘라 쓰고 회사명은
글자로 조판했습니다. 고해상도 로고를 받으면 `ogimage.py` 의 `symbol()`
을 손보면 됩니다.

> 카드를 바꾼 뒤에는 각 플랫폼 캐시를 비워야 새 이미지가 보입니다.
> 카카오 [디버거](https://developers.kakao.com/tool/debugger/sharing) ·
> 페이스북 [Sharing Debugger](https://developers.facebook.com/tools/debug/)

## 구성

| 파일 | 내용 |
|---|---|
| `index.html` | 메인 — 히어로 슬라이더(3슬라이드), 사업 2축, 주간 스케줄 보드, 사업영역 |
| `services.html` | 종합물류 부문 — 포워딩 · 3PL/풀필먼트 · 이커머스 · 통관 · 보세 · 국내배송 |
| `heavy.html` | 중장비 부문 — 수입 운송 6단계, 장비별 관리, 통관 요건 |
| `repair.html` | 보수작업 대행 — 근거, 수행 범위, 대표 작업, 돌발상황 대응 |
| `network.html` | 중국 집화 거점 · 인천항/인천공항 창고 · 차량 운용 |
| `about.html` | 회사 개요 · 사업 구조 · 사업영역 · 연혁 |
| `contact.html` | 견적 요청 폼 · 오시는 길 |
| `assets/css/site.css` | 전체 스타일 (디자인 토큰 · 라이트/다크 대응) |
| `assets/js/site.js` | 모바일 메뉴 · 현재 페이지 표시 · 견적 폼 |
| `assets/img/` | 로고(라이트/다크) · 파비콘 · 공유 카드 · 협력사 시설 사진 |

## 디자인 기준

홈페이지 디자인 시안 **2A — Blueprint** 기준, 회사소개서 **r3**(종합물류 + 중장비 2축) 내용 반영.
흰 배경 + 인디고 액센트, 괘선 기반 데이터 조판, 모노스페이스 숫자, 한·영 병기 라벨.

색상·여백·타이포는 모두 `assets/css/site.css` 상단의 `:root` 변수에서 관리합니다.

### 히어로 슬라이더

메인 히어로는 **해상 · 항공 · 중장비 3개 슬라이드**가 6.5초마다 전환됩니다.
마우스를 올리거나 탭에 포커스가 가면 멈추고, 하단 탭을 눌러 바로 이동할 수 있습니다.
전환 주기는 `assets/js/site.js`의 `HOLD` 값으로 조정합니다.

슬라이드 문구는 `index.html`의 `<article class="slide">` 안에서 직접 고치면 됩니다.

### 히어로 이미지 교체 방법

각 슬라이드의 시각물은 현재 **블루프린트 도면(인라인 SVG)** 입니다.
실사진으로 바꾸려면 `index.html`에서 각 `<div class="hp-art">` 안의 `<svg>…</svg>`를 통째로 아래로 교체하면 됩니다.

```html
<div class="hp-art">
  <img src="assets/img/hero-sea.jpg" alt="인천항 컨테이너 선적">
</div>
```

`object-fit: cover`가 걸려 있어 사진 비율이 달라도 잘립니다. 권장 크기는 가로 1600px 이상,
가로:세로 = 16:10 입니다.

### 로고

`assets/img/logo-dark.png`(밝은 배경용) / `logo-light.png`(어두운 배경용) 두 벌을 쓰며,
테마에 따라 CSS가 자동으로 바꿉니다. 원본은 `../ref/HF_LOGO.png` 한 벌에서 색만 바꿔 생성했습니다.

## 로컬에서 보기

파일을 직접 열거나,

```bash
python3 -m http.server 8000
```

실행 후 <http://localhost:8000> 접속.

## 배포

`main` 브랜치에 푸시하면 GitHub Pages에 자동 반영됩니다.

## 연결 전 확인 필요

- **견적 폼** — 담당자 메일(`dydw0625@nate.com`)로 메일 클라이언트를 여는 방식입니다.
  회사 도메인 메일(`info@hflogis.com` 등)로 옮길지 실무팀 협의 중입니다.
- **로고** — 워드마크가 `HF LOGISTIS` 로 되어 있습니다. `LOGISTICS` 의 C 누락으로 보이며,
  수정된 원본을 받으면 교체합니다. 고해상도 파일이면 공유 카드도 같이 개선됩니다.
- **주간 스케줄** — `index.html` 히어로의 일정은 화면 구성용 예시입니다. 운영팀 주간 갱신 값으로 교체해야 합니다.
- **히어로 사진** — 현재 블루프린트 도면(SVG)입니다. HF 자체 사진이 없어 촬영 또는 구매가 필요합니다.
- **협력사 사진 게재 동의** — 스카이 · 삼복 사진의 서면 동의 확인이 필요합니다.
