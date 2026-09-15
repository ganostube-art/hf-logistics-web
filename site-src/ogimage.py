# -*- coding: utf-8 -*-
"""OG 공유 카드(1200x630)를 언어별로 생성합니다.

로고 원본이 360x96 저해상도라 확대하면 뭉개집니다. 그래서 HF 심볼만 잘라 쓰고
회사명·문구는 시스템 폰트로 조판합니다. 덤으로 로고에 박힌 'LOGISTIS' 오타가
공유 카드마다 퍼지는 것도 피할 수 있습니다.

    python3 ogimage.py

macOS 전용(Apple SD Gothic Neo / Hiragino Sans GB)입니다. 다른 환경에서 돌릴 일이
생기면 FONTS 경로만 바꾸면 됩니다.
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG = os.path.join(OUT, "assets", "img")

W, H = 1200, 630
PAD = 88                       # 좌우 여백
INNER = W - PAD * 2            # 본문 폭 1024

# site.css 토큰과 같은 값입니다.
NAVY = (19, 28, 52)
INDIGO = (29, 78, 216)
WHITE = (255, 255, 255)
SKY = (143, 176, 245)          # eyebrow — indigo 계열 밝은 톤
MUTED = (150, 163, 186)
RULE = (44, 56, 84)

SD = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
HG = "/System/Library/Fonts/Hiragino Sans GB.ttc"

# (경로, ttc 인덱스) — 언어별 [굵게, 보통]
FONTS = {
    "ko": {"bold": (SD, 6), "med": (SD, 4), "reg": (SD, 2)},
    "en": {"bold": (SD, 6), "med": (SD, 4), "reg": (SD, 2)},
    "zh": {"bold": (HG, 2), "med": (HG, 2), "reg": (HG, 0)},
}

CARD = {
    "ko": {
        "eyebrow": "국제물류주선 · 중장비 운반",
        "head": ["컨테이너 한 박스부터", "40톤 중장비까지"],
        "sub": "인천에서 시작하는 국제물류 · 주식회사 에이치에프로지스틱스",
        "tel": "T. 032-888-0824",
    },
    "en": {
        "eyebrow": "FREIGHT FORWARDING · HEAVY CARGO",
        "head": ["From one container", "to 40-tonne cargo"],
        "sub": "International logistics from Incheon, Korea · HF Logistics Co., Ltd.",
        "tel": "T. +82-32-888-0824",
    },
    "zh": {
        "eyebrow": "国际物流运输 · 重型设备运输",
        "head": ["从一个集装箱", "到40吨重型设备"],
        "sub": "物流始于仁川 · HF物流株式会社",
        "tel": "T. +82-32-888-0824",
    },
}


def font(lang, weight, size):
    path, idx = FONTS[lang][weight]
    return ImageFont.truetype(path, size, index=idx)


def tracked(draw, xy, text, ft, fill, track=0):
    """자간을 준 한 줄. PIL에는 letter-spacing이 없어 글자마다 그립니다."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=ft, fill=fill)
        x += draw.textlength(ch, font=ft) + track
    return x


def symbol(height):
    """로고에서 HF 심볼만 잘라냅니다. 좌표는 logo-light.png 알파 분석으로 구했습니다."""
    src = Image.open(os.path.join(IMG, "logo-light.png")).convert("RGBA")
    mark = src.crop((14, 6, 94, 88))
    # 원본이 JPEG에서 온 탓에 RGB에 얼룩이 남아 있습니다. 색은 버리고 알파만
    # 마스크로 써서 순백 실루엣으로 다시 칠합니다.
    a = mark.split()[3].point(lambda v: 0 if v < 70 else 255 if v > 190 else v)
    w = round(mark.width * height / mark.height)
    a = a.resize((w, height), Image.LANCZOS)
    out = Image.new("RGBA", (w, height), WHITE + (0,))
    out.putalpha(a)
    return out


def ground():
    """네이비 바탕 + 우하단 인디고 광. 카드에 깊이만 주고 시선은 뺏지 않습니다."""
    im = Image.new("RGB", (W, H), NAVY)
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    cx, cy = W - 120, H + 40
    for i in range(34, 0, -1):
        r = i * 26
        gd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=int(52 * (1 - i / 34.0)))
    im.paste(Image.new("RGB", (W, H), INDIGO), (0, 0), glow)
    return im


def build(lang):
    c = CARD[lang]
    im = ground()
    d = ImageDraw.Draw(im)

    # 상단 인디고 밴드 — 브랜드 색을 한 번만 강하게 씁니다.
    d.rectangle((0, 0, W, 7), fill=INDIGO)

    mark = symbol(96)
    im.paste(mark, (PAD, 92), mark)

    y = 246
    tracked(d, (PAD, y), c["eyebrow"], font(lang, "med", 25), SKY, track=1.6)

    y = 300
    fh = font(lang, "bold", 66)
    for line in c["head"]:
        d.text((PAD, y), line, font=fh, fill=WHITE)
        y += 84

    d.text((PAD, 486), c["sub"], font=font(lang, "reg", 27), fill=MUTED)

    d.line((PAD, 552, W - PAD, 552), fill=RULE, width=1)

    fu = font(lang, "bold", 28)
    d.text((PAD, 574), "hflogis.com", font=fu, fill=WHITE)
    ft = font(lang, "reg", 25)
    d.text((W - PAD - d.textlength(c["tel"], font=ft), 577), c["tel"], font=ft, fill=MUTED)

    path = os.path.join(IMG, "og-%s.png" % lang)
    im.save(path, optimize=True)
    return path


if __name__ == "__main__":
    for lang in ("ko", "en", "zh"):
        p = build(lang)
        print("%s  %d KB" % (os.path.relpath(p, OUT), os.path.getsize(p) // 1024))
