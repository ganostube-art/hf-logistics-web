# -*- coding: utf-8 -*-
"""전체 사이트 생성 — 한국어 / 영어 / 중국어 21개 페이지"""
import b_index, b_services, b_heavy, b_repair, b_network, b_about, b_contact
from common import LANGS

MODULES = [b_index, b_services, b_heavy, b_repair, b_network, b_about, b_contact]

if __name__ == "__main__":
    n = 0
    for mod in MODULES:
        for lang in LANGS:
            mod.build(lang); n += 1
    print("생성 완료: %d개 페이지 (%d페이지 x %d언어)" % (n, len(MODULES), len(LANGS)))
