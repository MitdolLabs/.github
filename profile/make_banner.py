"""조직 첫 화면 배너(라이트·다크). 홈페이지 첫 화면의 돌무더기와 같은 값입니다."""
import pathlib, sys
STONES = [(74, 26, 3, 12, False), (108, 30, -5, 14, True), (92, 24, 6, 12, False), (136, 34, -3, 16, True), (118, 28, 4, 14, False)]
THEMES = {
    'light': dict(panel='#f7f7f7', ink='#1f1f1f', body='#ffffff', shade='#e3e3e3', cheek='#c4c4c4', ground='#8c8c8c',
                  far='#eeeeee', near='#e6e6e6', cloud='#ffffff', soft='#c9c9c9'),
    'dark': dict(panel='#161616', ink='#ececec', body='#161616', shade='#333333', cheek='#4a4a4a', ground='#6b6b6b',
                 far='#1d1d1d', near='#252525', cloud='#1f1f1f', soft='#484848'),
}
W, H, GROUND_Y, SCALE = 1280, 320, 276, 1.2

def stone(x, y, w, h, r, fill, ink):
    return f'<rect x="{x:g}" y="{y:g}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{ink}" stroke-width="3"/>'

def pill(x, y, w, h, fill, line):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2:g}" fill="{fill}" stroke="{line}" stroke-width="2"/>'

def backdrop(theme, t):
    """돌무더기 뒤의 배경: 먼 산, 가까운 언덕, 구름, 해(다크는 달과 별), 새, 풀. 먹색 한 가지의 옅은 단계만 씁니다."""
    g = GROUND_Y
    hills = (
        f'<path fill="{t["far"]}" d="M60 {g} C200 {g} 260 150 400 150 C520 150 560 230 660 230 C760 230 800 120 940 120 C1090 120 1120 {g} 1230 {g} Z"/>'
        f'<path fill="{t["near"]}" d="M40 {g} C120 {g} 150 215 250 215 C350 215 380 {g} 470 {g} Z"/>'
        f'<path fill="{t["near"]}" d="M790 {g} C890 {g} 920 205 1040 205 C1150 205 1180 {g} 1240 {g} Z"/>'
    )
    clouds = ''.join(pill(x, y, w, h, t['cloud'], t['soft']) for x, y, w, h in [
        (182, 62, 70, 24), (150, 80, 132, 26), (432, 46, 66, 18), (846, 40, 48, 20), (816, 55, 104, 22)])
    if theme == 'dark':
        sky = f'<circle cx="1096" cy="76" r="24" fill="{t["shade"]}" stroke="{t["ink"]}" stroke-width="3"/><circle cx="1088" cy="68" r="4" fill="{t["soft"]}"/><circle cx="1104" cy="84" r="6" fill="{t["soft"]}"/>'
        sky += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{t["ground"]}"/>' for x, y, r in [
            (90, 44, 2), (330, 34, 1.6), (372, 96, 2), (548, 58, 2), (604, 112, 1.6), (716, 36, 1.6), (742, 92, 2), (980, 44, 1.6), (1190, 52, 2), (1168, 128, 1.6)])
    else:
        sky = f'<circle cx="1096" cy="76" r="24" fill="{t["body"]}" stroke="{t["ink"]}" stroke-width="3"/>'
        sky += f'<path fill="none" stroke="{t["ground"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M520 104 q8 -8 16 0 q8 -8 16 0 M566 84 q6 -6 12 0 q6 -6 12 0"/>'
    grass = ''.join(f'M{x} {g} l-5 -10 M{x} {g} v-13 M{x} {g} l5 -9 ' for x in (250, 520, 866, 1120))
    grass = f'<path fill="none" stroke="{t["ground"]}" stroke-width="2" stroke-linecap="round" d="{grass.strip()}"/>'
    return hills + sky + clouds + grass

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
{backdrop(theme, t)}
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
