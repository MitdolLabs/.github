"""조직 첫 화면 배너(라이트·다크). 홈페이지 첫 화면의 돌무더기와 같은 값입니다."""
import pathlib, sys
STONES = [(74, 26, 3, 12, False), (108, 30, -5, 14, True), (92, 24, 6, 12, False), (136, 34, -3, 16, True), (118, 28, 4, 14, False)]
THEMES = {
    'light': dict(panel='#f7f7f7', ink='#1f1f1f', body='#ffffff', shade='#e3e3e3', cheek='#c4c4c4', ground='#8c8c8c'),
    'dark': dict(panel='#161616', ink='#ececec', body='#161616', shade='#333333', cheek='#4a4a4a', ground='#6b6b6b'),
}
W, H, GROUND_Y, SCALE = 1280, 320, 276, 1.2

def stone(x, y, w, h, r, fill, ink):
    return f'<rect x="{x:g}" y="{y:g}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{ink}" stroke-width="3"/>'

def banner(theme):
    t = THEMES[theme]
    parts, bottom = [], 0
    for w, h, dx, r, shade in reversed(STONES):
        bottom -= h
        parts.append(stone(-w / 2 + dx, bottom, w, h, r, t['shade'] if shade else t['body'], t['ink']))
    line = f'fill="none" stroke="{t["ink"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
    buddy = f'''<g transform="translate(0 {bottom})"><path {line} d="M-9 -6 V-1 M9 -6 V-1"/><path {line} d="M0 -40 q0 -8 7 -10"/><rect x="-22" y="-40" width="44" height="38" rx="15" fill="{t['body']}" stroke="{t['ink']}" stroke-width="3"/><circle cx="-8" cy="-23" r="3.2" fill="{t['ink']}"/><circle cx="8" cy="-23" r="3.2" fill="{t['ink']}"/><circle cx="-15" cy="-15" r="3.4" fill="{t['cheek']}" opacity=".6"/><circle cx="15" cy="-15" r="3.4" fill="{t['cheek']}" opacity=".6"/><path d="M-6 -17 q6 9 12 0 Z" fill="{t['ink']}" stroke="{t['ink']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>'''
    # 땅에 흩어진 작은 돌 (x, 폭, 높이, 채움)
    loose = [(-470, 46, 16, True), (-405, 30, 12, False), (-250, 38, 14, False), (265, 52, 18, True), (330, 28, 12, False), (480, 40, 14, True)]
    extras = ''.join(stone(x - w / 2, -h, w, h, h / 2, t['shade'] if shade else t['body'], t['ink']) for x, w, h, shade in loose)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Mitdol Labs: a cairn with Mitdori on top">
<!-- make_banner.py 가 만든 파일입니다. 글자는 넣지 않습니다. -->
<rect width="{W}" height="{H}" rx="20" fill="{t['panel']}"/>
<g transform="translate({W / 2:g} {GROUND_Y}) scale({SCALE})">
{extras}
{''.join(parts)}
{buddy}
<line x1="-500" y1="0" x2="500" y2="0" stroke="{t['ground']}" stroke-width="1.5" stroke-linecap="round"/>
</g>
</svg>
'''

out = pathlib.Path(sys.argv[1])
for theme in THEMES:
    (out / f'banner-{theme}.svg').write_text(banner(theme), encoding='utf-8', newline='\n')
