# -*- coding: utf-8 -*-
"""협력사 시설 사진을 웹용으로 가공합니다.

원본은 저장소 밖 `ref/photos/` 에 있습니다. 협력사 소유 자료라 공개 저장소에
넣지 않습니다. 이 스크립트는 한 번 돌려 `assets/img/fac-*.jpg` 를 만들고,
결과물만 커밋합니다. 빌드가 ref/ 에 의존하지 않도록 build_all.py 와 분리했습니다.

    python3 photos.py

출처
    sky-*     ㈜스카이국제운송 — https://www.skylogis.co.kr/kr/warehouse/
    sambok-*  삼복로지스틱㈜ — 회사소개서 V3.3
"""

import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.abspath(os.path.join(OUT, "..", "ref", "photos"))
DST = os.path.join(OUT, "assets", "img")

# 카드 상단에 들어가는 16:9 배너. 레티나 대비 2배 폭입니다.
W, H = 1280, 720

JOBS = [
    ("sky_warehouse_aerial.jpg", "fac-sky.jpg", 0.50),
    ("sambok_exterior.png",      "fac-sambok.jpg", 0.52),
]


def fit(im, w, h, focus=0.5):
    """가로세로비를 맞춰 잘라냅니다. focus 는 세로 기준점(0=위, 1=아래)."""
    sr, dr = im.width / im.height, w / h
    if sr > dr:                      # 원본이 더 넓다 — 좌우를 자릅니다
        nw = round(im.height * dr)
        x = (im.width - nw) // 2
        im = im.crop((x, 0, x + nw, im.height))
    else:                            # 원본이 더 높다 — 위아래를 자릅니다
        nh = round(im.width / dr)
        y = round((im.height - nh) * focus)
        im = im.crop((0, y, im.width, y + nh))
    return im.resize((w, h), Image.LANCZOS)


if __name__ == "__main__":
    if not os.path.isdir(SRC):
        raise SystemExit("원본이 없습니다: %s" % SRC)
    for src, dst, focus in JOBS:
        im = Image.open(os.path.join(SRC, src)).convert("RGB")
        fit(im, W, H, focus).save(os.path.join(DST, dst), "JPEG",
                                  quality=82, optimize=True, progressive=True)
        p = os.path.join(DST, dst)
        print("%-16s %dx%d  %d KB" % (dst, W, H, os.path.getsize(p) // 1024))
