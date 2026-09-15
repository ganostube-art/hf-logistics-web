# -*- coding: utf-8 -*-
# 히어로 3분할 블루프린트 아트 — 해상 / 항공 / 중장비
# .art  : 로드 시 선이 그려지는 대상
# .ship .plane .rig : 상시 흔들림
# .wheel .roller    : 회전
# .w1 .w2 .w3       : 수면 · 지면 · 노면 흐름

def grid(uid):
    return (u'<defs><pattern id="g-%s" width="20" height="20" patternUnits="userSpaceOnUse">'
            u'<path d="M20 0H0V20" fill="none" stroke="#7EA0F2" stroke-opacity=".14" stroke-width="1"/>'
            u'</pattern></defs>'
            u'<rect width="400" height="250" fill="#131C34"/>'
            u'<rect width="400" height="250" fill="url(#g-%s)"/>') % (uid, uid)

T = (u'font-family:ui-monospace,SFMono-Regular,Menlo,monospace;'
     u'font-size:8px;letter-spacing:.14em;fill:#7EA0F2')

# 도면 치수 라벨 [T] 전문용어
DIM = {
    "ko": {"h": u"전고 H", "l": u"전장 L"},
    "en": {"h": u"HEIGHT H", "l": u"LENGTH L"},
    "zh": {"h": u"全高 H", "l": u"全长 L"},
}


def sea():
    return u'''<svg viewBox="0 0 400 250" role="img" aria-label="컨테이너선 측면 도면">
%s
<g class="art">
  <g class="ship">
    <g fill="none" stroke="#7EA0F2" stroke-width="1.4" stroke-linejoin="round">
      <path d="M52 152 L372 152 L352 186 L58 186 Z" fill="#1B2745"/>
      <rect x="62" y="110" width="40" height="42" fill="#1B2745"/>
      <rect x="72" y="94" width="17" height="16" fill="#1B2745"/>
      <path d="M67 120h30M67 129h30M67 138h30" stroke-width="1" stroke-opacity=".75"/>
    </g>
    <g stroke="#7EA0F2" stroke-width="1.1" fill="#22305A">
      <rect x="112" y="140" width="28" height="12"/><rect x="142" y="140" width="28" height="12"/>
      <rect x="172" y="140" width="28" height="12"/><rect x="202" y="140" width="28" height="12"/>
      <rect x="232" y="140" width="28" height="12"/><rect x="262" y="140" width="28" height="12"/>
      <rect x="292" y="140" width="28" height="12"/><rect x="322" y="140" width="28" height="12"/>
      <rect x="112" y="126" width="28" height="12"/><rect x="142" y="126" width="28" height="12"/>
      <rect x="172" y="126" width="28" height="12"/><rect x="202" y="126" width="28" height="12"/>
      <rect x="232" y="126" width="28" height="12"/><rect x="262" y="126" width="28" height="12"/>
      <rect x="292" y="126" width="28" height="12"/>
      <g fill="#2C3D70">
        <rect x="112" y="112" width="28" height="12"/><rect x="142" y="112" width="28" height="12"/>
        <rect x="172" y="112" width="28" height="12"/><rect x="202" y="112" width="28" height="12"/>
      </g>
    </g>
    <g stroke="#7EA0F2" stroke-width=".9" stroke-opacity=".8" fill="none">
      <path d="M112 104v-9M140 104v-9M112 100h28"/>
      <path d="M112 100l5 -3M112 100l5 3M140 100l-5 -3M140 100l-5 3"/>
    </g>
    <text x="126" y="92" text-anchor="middle" style="%s">40' HC</text>
  </g>
  <path class="edge" d="M0 186h400" stroke="#7EA0F2" stroke-width="1.1" stroke-opacity=".55" fill="none"/>
  <g stroke="#7EA0F2" stroke-width="1.2" stroke-opacity=".38" stroke-linecap="round" fill="none">
    <path class="w1" d="M-60 197H460" stroke-dasharray="3 10"/>
    <path class="w2" d="M-60 210H460" stroke-dasharray="3 13"/>
    <path class="w3" d="M-60 223H460" stroke-dasharray="3 9"/>
  </g>
  <text x="20" y="40" style="%s">SEA FREIGHT / FCL · LCL</text>
</g>
</svg>''' % (grid('sea'), T, T)


def air():
    return u'''<svg viewBox="0 0 400 250" role="img" aria-label="화물 항공기 측면 도면">
%s
<g class="art">
  <g class="plane">
    <path d="M330 118 L376 108 L378 115 L334 125 Z" fill="#22305A" stroke="#7EA0F2" stroke-width="1.2" stroke-linejoin="round"/>
    <path d="M316 130 L344 70 L357 70 L350 130 Z" fill="#1B2745" stroke="#7EA0F2" stroke-width="1.3" stroke-linejoin="round"/>
    <path d="M64 128 L300 126 Q332 124 352 104 L363 110 Q346 142 330 162 L64 162 Q44 162 44 145 Q44 128 64 128 Z"
          fill="#1B2745" stroke="#7EA0F2" stroke-width="1.5" stroke-linejoin="round"/>
    <path d="M176 160 L248 160 L276 180 L206 180 Z" fill="#22305A" stroke="#7EA0F2" stroke-width="1.3" stroke-linejoin="round"/>
    <rect x="216" y="172" width="38" height="15" rx="7" fill="#2C3D70" stroke="#7EA0F2" stroke-width="1.2"/>
    <rect x="182" y="166" width="36" height="14" rx="7" fill="#22305A" stroke="#7EA0F2" stroke-width="1.1" stroke-opacity=".7"/>
    <rect x="104" y="133" width="52" height="22" rx="2" fill="none" stroke="#7EA0F2" stroke-width="1.1" stroke-opacity=".85"/>
    <path d="M70 150h226" stroke="#7EA0F2" stroke-width=".9" stroke-opacity=".35" fill="none"/>
    <path d="M58 136 L74 133 L74 140 L58 143 Z" fill="#2C3D70" stroke="#7EA0F2" stroke-width="1"/>
    <g stroke="#7EA0F2" stroke-width="1.3" fill="#1B2745">
      <path d="M76 162v26"/>
      <g class="wheel"><circle cx="76" cy="193" r="6"/><path d="M76 187v12M70 193h12" stroke-width=".9" stroke-opacity=".6"/></g>
      <path d="M228 180v8"/>
      <g class="wheel"><circle cx="221" cy="193" r="6"/><path d="M221 187v12M215 193h12" stroke-width=".9" stroke-opacity=".6"/></g>
      <g class="wheel"><circle cx="236" cy="193" r="6"/><path d="M236 187v12M230 193h12" stroke-width=".9" stroke-opacity=".6"/></g>
    </g>
  </g>
  <g stroke="#7EA0F2" stroke-width="1.2" fill="#22305A">
    <path d="M300 176 L340 176 L346 184 L346 200 L300 200 Z"/>
    <path d="M300 176 L300 200" stroke-opacity=".6"/>
  </g>
  <text x="323" y="213" text-anchor="middle" style="%s">ULD</text>
  <path class="edge" d="M0 200h400" stroke="#7EA0F2" stroke-opacity=".45" stroke-width="1.1" fill="none"/>
  <g stroke="#7EA0F2" stroke-opacity=".34" stroke-width="1.2" stroke-linecap="round" fill="none">
    <path class="w1" d="M-60 214H460" stroke-dasharray="4 11"/>
    <path class="w2" d="M-60 228H460" stroke-dasharray="4 9"/>
  </g>
  <text x="20" y="40" style="%s">AIR FREIGHT / INCHEON FTZ</text>
</g>
</svg>''' % (grid('air'), T, T)


def heavy(lang="ko"):
    return u'''<svg viewBox="0 0 400 250" role="img" aria-label="저상 트레일러에 적재된 굴착기 도면">
%(grid)s
<g class="art">
  <g class="rig">
    <path d="M34 158 L66 158 L74 176 L300 176 L308 164 L360 164 L360 188 L74 188 L34 188 Z"
          stroke="#7EA0F2" stroke-width="1.4" fill="#1B2745" stroke-linejoin="round"/>
    <g stroke="#7EA0F2" stroke-width="1.3" fill="#22305A">
      <g class="wheel"><circle cx="52" cy="196" r="11"/><circle cx="52" cy="196" r="4" fill="#131C34"/><path d="M52 185v22M41 196h22" stroke-width=".9" stroke-opacity=".55"/></g>
      <g class="wheel"><circle cx="316" cy="196" r="11"/><circle cx="316" cy="196" r="4" fill="#131C34"/><path d="M316 185v22M305 196h22" stroke-width=".9" stroke-opacity=".55"/></g>
      <g class="wheel"><circle cx="342" cy="196" r="11"/><circle cx="342" cy="196" r="4" fill="#131C34"/><path d="M342 185v22M331 196h22" stroke-width=".9" stroke-opacity=".55"/></g>
    </g>
    <rect x="122" y="150" width="122" height="26" rx="13" stroke="#7EA0F2" stroke-width="1.4" fill="#22305A"/>
    <g stroke="#7EA0F2" stroke-width="1" stroke-opacity=".6" fill="none">
      <g class="roller"><circle cx="136" cy="163" r="7"/><path d="M136 156v14M129 163h14" stroke-opacity=".5"/></g>
      <g class="roller"><circle cx="230" cy="163" r="7"/><path d="M230 156v14M223 163h14" stroke-opacity=".5"/></g>
      <circle cx="166" cy="168" r="4"/><circle cx="196" cy="168" r="4"/>
    </g>
    <path d="M148 150 L148 122 L232 122 L244 132 L244 150 Z" fill="#1B2745" stroke="#7EA0F2" stroke-width="1.4" stroke-linejoin="round"/>
    <rect x="228" y="126" width="18" height="24" rx="3" fill="#2C3D70" stroke="#7EA0F2" stroke-width="1.2"/>
    <path d="M152 122 L152 100 L184 100 L188 122 Z" fill="#22305A" stroke="#7EA0F2" stroke-width="1.3" stroke-linejoin="round"/>
    <path d="M157 105 L180 105 L182 117 L157 117 Z" fill="#2C3D70" stroke="#7EA0F2" stroke-width="1"/>
    <g class="boom" stroke="#7EA0F2" stroke-width="1.5" fill="#22305A" stroke-linejoin="round">
      <path d="M152 134 L118 100 L126 92 L162 126 Z"/>
      <path d="M118 100 L126 92 L146 122 L138 129 Z"/>
      <path d="M138 129 L148 124 L156 140 L142 144 Z"/>
      <circle cx="122" cy="96" r="3" fill="#131C34" stroke-width="1"/>
    </g>
  </g>
  <g class="dim" stroke="#7EA0F2" stroke-width=".9" stroke-opacity=".8" fill="none">
    <path d="M92 92v116" stroke-dasharray="4 4"/>
    <path d="M86 92h12M86 208h12"/>
    <path d="M92 92l-3 6M92 92l3 6M92 208l-3 -6M92 208l3 -6"/>
    <path d="M34 224h326"/>
    <path d="M34 218v12M360 218v12"/>
    <path d="M34 224l6 -3M34 224l6 3M360 224l-6 -3M360 224l-6 3"/>
  </g>
  <text x="80" y="152" text-anchor="middle" transform="rotate(-90 80 152)" style="%(t)s">%(dh)s</text>
  <text x="197" y="220" text-anchor="middle" style="%(t)s">%(dl)s</text>
  <path class="edge" d="M0 208h400" stroke="#7EA0F2" stroke-opacity=".45" stroke-width="1.1" fill="none"/>
  <g stroke="#7EA0F2" stroke-opacity=".32" stroke-width="1.3" stroke-linecap="round" fill="none">
    <path class="w1" d="M-60 236H460" stroke-dasharray="6 12"/>
    <path class="w2" d="M-60 246H460" stroke-dasharray="6 16"/>
  </g>
  <text x="20" y="40" style="%(t)s">HEAVY CARGO / RO-RO · FLAT RACK</text>
</g>
</svg>''' % dict(grid=grid('hvy'), t=T, dh=DIM[lang]["h"], dl=DIM[lang]["l"])
