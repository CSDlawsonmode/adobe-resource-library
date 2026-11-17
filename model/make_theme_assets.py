"""Generate the retro-future theme art (animated SVGs) into model/theme/.

  python model/make_theme_assets.py

Outputs:
  space-bg.svg          tiling starfield, twinkles (page background)
  lights-strip.svg      console strip: blinking diodes + oscilloscope (divider / Mission Check header)
  banner-<slug>.svg     page banner per module: mainframe, title, rocket, planet, saucer

All motion is CSS inside the SVG, so it still animates when Canvas shows the
SVG as an <img> or a background image. Every file honors
prefers-reduced-motion, and nothing blinks faster than about once a second.
The designs are original; they borrow the era, not any show's props.
"""
import pathlib
import random

OUT = pathlib.Path(__file__).parent / "theme"
OUT.mkdir(exist_ok=True)

FONT = "Futura, 'Century Gothic', 'Avenir Next', 'Trebuchet MS', sans-serif"
MONO = "'Courier New', Courier, monospace"
DIODE_COLORS = ["#FF3B3B", "#FFB000", "#39FF88", "#3DDBD9", "#FFE66D"]

BASE_CSS = """
@keyframes blink { 0%,49% {opacity:1} 50%,100% {opacity:.18} }
@keyframes tw { 0%,100% {opacity:.25} 50% {opacity:1} }
@keyframes spin { to { transform: rotate(360deg) } }
@keyframes bob { 0%,100% {transform: translateY(0)} 50% {transform: translateY(-7px)} }
@keyframes flick { 0% {opacity:1} 100% {opacity:.55} }
@keyframes fly { 0% {transform: translateX(-140px)} 100% {transform: translateX(1140px)} }
@keyframes scope { to { transform: translateX(-60px) } }
.d { animation: blink 1.6s steps(1) infinite }
.tw { animation: tw 3.2s ease-in-out infinite }
.spin { transform-box: view-box; animation: spin 5s linear infinite }
.bob { animation: bob 4s ease-in-out infinite }
.flame { animation: flick .45s ease-in-out infinite alternate }
.fly { animation: fly 22s linear infinite }
.scope { animation: scope 1.8s linear infinite }
@media (prefers-reduced-motion: reduce) { * { animation: none !important } }
"""


def diode(x, y, r, rng):
    c = rng.choice(DIODE_COLORS)
    dur = rng.uniform(0.9, 2.6)
    delay = -rng.uniform(0, 2.6)
    return (
        f'<circle cx="{x}" cy="{y}" r="{r + 2}" fill="#0A0A12"/>'
        f'<circle class="d" cx="{x}" cy="{y}" r="{r}" fill="{c}" '
        f'style="animation-duration:{dur:.2f}s;animation-delay:{delay:.2f}s"/>'
    )


def stars(n, w, h, rng, big=0.12):
    out = []
    for _ in range(n):
        x, y = rng.uniform(0, w), rng.uniform(0, h)
        r = rng.choice([0.6, 0.8, 1.0, 1.2]) if rng.random() > big else 1.8
        cls = ' class="tw"' if rng.random() < 0.55 else ""
        d = -rng.uniform(0, 3.2)
        out.append(
            f'<circle{cls} cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#F5E9C8" '
            f'style="animation-delay:{d:.2f}s"/>'
        )
    return "".join(out)


def sparkle(x, y, s, color="#FFD54A", cls="tw", delay=0.0):
    p = f"M{x},{y - s} L{x + s * .22},{y - s * .22} L{x + s},{y} L{x + s * .22},{y + s * .22} " \
        f"L{x},{y + s} L{x - s * .22},{y + s * .22} L{x - s},{y} L{x - s * .22},{y - s * .22} Z"
    return f'<path class="{cls}" d="{p}" fill="{color}" style="animation-delay:{delay}s"/>'


def space_bg():
    rng = random.Random(7)
    body = stars(26, 320, 320, rng) + sparkle(250, 60, 7, "#F5E9C8", delay=-1.1) \
        + sparkle(70, 240, 5, "#3DDBD9", delay=-2.0)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320">
<style>{BASE_CSS}</style>{body}</svg>"""
    (OUT / "space-bg.svg").write_text(svg, encoding="utf-8")


def lights_strip():
    rng = random.Random(11)
    diodes = "".join(diode(36 + i * 22, 20, 5, rng) for i in range(26))
    wave = " ".join(
        f"{'M' if i == 0 else 'L'}{730 + i * 5},{20 + (8 if (i // 3) % 4 == 0 else -8 if (i // 3) % 4 == 2 else 0)}"
        for i in range(60)
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 40" width="1000" height="40" role="img" aria-label="Decorative console lights">
<style>{BASE_CSS}</style>
<defs><linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#F4F6F8"/><stop offset=".5" stop-color="#9AA4B1"/><stop offset="1" stop-color="#E3E7EC"/></linearGradient>
<clipPath id="scr"><rect x="740" y="8" width="160" height="24" rx="4"/></clipPath></defs>
<rect x="2" y="2" width="996" height="36" rx="10" fill="#1B1B2F" stroke="url(#chrome)" stroke-width="3"/>
{diodes}
<rect x="616" y="10" width="104" height="20" rx="3" fill="#120C00" stroke="#5A4A1A"/>
<text x="668" y="25" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="#FFC857" class="tw" style="animation-duration:2.4s">READY</text>
<rect x="740" y="8" width="160" height="24" rx="4" fill="#06140D" stroke="#2E6B4A"/>
<g clip-path="url(#scr)"><path class="scope" d="{wave}" fill="none" stroke="#39FF88" stroke-width="2"/></g>
<circle cx="926" cy="20" r="8" fill="#2A2A3A" stroke="url(#chrome)" stroke-width="2"/>
<line x1="926" y1="20" x2="931" y2="14" stroke="#F5E9C8" stroke-width="2"/>
<circle cx="958" cy="20" r="8" fill="#2A2A3A" stroke="url(#chrome)" stroke-width="2"/>
<line x1="958" y1="20" x2="952" y2="15" stroke="#F5E9C8" stroke-width="2"/>
</svg>"""
    (OUT / "lights-strip.svg").write_text(svg, encoding="utf-8")


def reel(cx, cy, dur):
    spokes = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - 26}" stroke="#C0C7D1" stroke-width="4" '
        f'transform="rotate({a} {cx} {cy})"/>' for a in (0, 120, 240)
    )
    return (
        f'<circle cx="{cx}" cy="{cy}" r="32" fill="#2A2A3A" stroke="#C0C7D1" stroke-width="3"/>'
        f'<circle cx="{cx}" cy="{cy}" r="22" fill="#4A3A2A"/>'
        f'<g class="spin" style="transform-origin:{cx}px {cy}px;animation-duration:{dur}s">{spokes}</g>'
        f'<circle cx="{cx}" cy="{cy}" r="6" fill="#E3E7EC"/>'
    )


def banner(slug, title, subtitle):
    rng = random.Random(slug)
    grid = "".join(
        diode(52 + c * 26, 150 + r * 18, 5, rng) for r in range(4) for c in range(7)
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 260" width="1000" height="260" role="img" aria-label="{title}: {subtitle}">
<style>{BASE_CSS}</style>
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070B1E"/><stop offset=".65" stop-color="#1C1F4A"/><stop offset="1" stop-color="#3B1E54"/></linearGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#C0C7D1"/><stop offset=".55" stop-color="#6E7886"/><stop offset="1" stop-color="#E8ECF1"/></linearGradient>
<radialGradient id="planet" cx=".35" cy=".35" r=".75"><stop offset="0" stop-color="#FFC857"/><stop offset=".6" stop-color="#F26B3A"/><stop offset="1" stop-color="#8E1F2F"/></radialGradient>
<linearGradient id="cab" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2B3550"/><stop offset=".5" stop-color="#3B4A6B"/><stop offset="1" stop-color="#2B3550"/></linearGradient>
</defs>
<rect width="1000" height="260" fill="url(#sky)"/>
{stars(70, 1000, 230, rng)}
{sparkle(300, 42, 10, delay=-0.6)}{sparkle(690, 210, 8, "#3DDBD9", delay=-1.8)}{sparkle(960, 40, 7, "#F5E9C8", delay=-2.4)}

<g transform="translate(0,26)"><g class="fly">
  <ellipse cx="0" cy="0" rx="26" ry="6" fill="url(#chrome)"/>
  <path d="M-11,-2 A11,10 0 0 1 11,-2 Z" fill="#3DDBD9" opacity=".85"/>
  <circle class="d" cx="-14" cy="2" r="2" fill="#FF3B3B" style="animation-duration:1.2s"/>
  <circle class="d" cx="0" cy="3" r="2" fill="#FFE66D" style="animation-duration:1.2s;animation-delay:-.4s"/>
  <circle class="d" cx="14" cy="2" r="2" fill="#39FF88" style="animation-duration:1.2s;animation-delay:-.8s"/>
</g></g>

<!-- mainframe -->
<rect x="22" y="34" width="222" height="216" rx="14" fill="url(#cab)" stroke="url(#chrome)" stroke-width="4"/>
<rect x="34" y="46" width="198" height="78" rx="8" fill="#151A2C" stroke="#56627A"/>
{reel(82, 85, 4.5)}{reel(184, 85, 6)}
<path d="M82,117 L184,117" stroke="#4A3A2A" stroke-width="3"/>
<rect x="34" y="134" width="198" height="78" rx="8" fill="#151A2C" stroke="#56627A"/>
{grid}
<rect x="60" y="220" width="146" height="22" rx="4" fill="#120C00" stroke="#5A4A1A"/>
<text x="133" y="236" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="#FFC857" letter-spacing="2">COMPUTING&#8230;</text>

<!-- title -->
<text x="535" y="126" text-anchor="middle" font-family="{FONT}" font-size="64" font-weight="700" letter-spacing="5" fill="url(#chrome)" stroke="#0B1026" stroke-width="2">{title}</text>
<text x="535" y="170" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="700" letter-spacing="5" fill="#FFD54A">&#9733; {subtitle} &#9733;</text>
<path d="M320,190 L750,190" stroke="#E63946" stroke-width="3"/>
<path d="M360,197 L710,197" stroke="#3DDBD9" stroke-width="2"/>

<!-- planet -->
<ellipse cx="912" cy="172" rx="78" ry="16" fill="none" stroke="#F5E9C8" stroke-width="4" opacity=".55" transform="rotate(-14 912 172)"/>
<circle cx="912" cy="172" r="44" fill="url(#planet)"/>
<path d="M836,184 A78,16 -14 0 0 988,152" fill="none" stroke="#F5E9C8" stroke-width="4" transform="rotate(0)"/>

<!-- rocket -->
<g transform="translate(838,78) rotate(35)"><g class="bob">
  <path class="flame" d="M-8,30 L0,56 L8,30 Z" fill="#FFB000"/>
  <path class="flame" d="M-4,30 L0,46 L4,30 Z" fill="#FFE66D" style="animation-delay:-.2s"/>
  <path d="M0,-44 C15,-28 15,14 10,30 L-10,30 C-15,14 -15,-28 0,-44 Z" fill="url(#chrome)" stroke="#0B1026" stroke-width="1.5"/>
  <path d="M-10,8 L-26,36 L-10,30 Z" fill="#E63946"/><path d="M10,8 L26,36 L10,30 Z" fill="#E63946"/>
  <circle cx="0" cy="-10" r="6" fill="#3DDBD9" stroke="#0B1026" stroke-width="1.5"/>
  <path d="M-12,-26 L12,-26" stroke="#E63946" stroke-width="3"/>
</g></g>

<path d="M0,252 L1000,252" stroke="#E63946" stroke-width="3"/>
<path d="M0,257 L1000,257" stroke="#FFD54A" stroke-width="2"/>
</svg>"""
    (OUT / f"banner-{slug}.svg").write_text(svg, encoding="utf-8")


def mascot():
    """Commander Skip: an original 1950s spaceman in a fishbowl helmet, wagging a tip finger."""
    css = BASE_CSS + """
@keyframes wag { 0%,100% {transform: rotate(-5deg)} 50% {transform: rotate(7deg)} }
@keyframes glint { 0%,62%,100% {opacity:.35} 74% {opacity:1} }
.wag { transform-box: view-box; transform-origin: 52px 204px; animation: wag 1.8s ease-in-out infinite }
.glint { animation: glint 4.5s ease-in-out infinite }
"""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 260" width="220" height="260" role="img" aria-label="Commander Skip, a grinning 1950s spaceman in a glass bubble helmet, raising one finger to give a tip">
<style>{css}</style>
<defs>
<linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#9AA4B1"/><stop offset="1" stop-color="#E3E7EC"/></linearGradient>
<linearGradient id="suit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E63946"/><stop offset="1" stop-color="#9E1B2A"/></linearGradient>
<radialGradient id="glass" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#E6F7FF" stop-opacity=".35"/><stop offset=".7" stop-color="#9FDDF5" stop-opacity=".12"/><stop offset="1" stop-color="#5BC0EB" stop-opacity=".3"/></radialGradient>
</defs>
<g class="bob">
  <path d="M38,262 L50,204 Q110,180 170,204 L182,262 Z" fill="url(#suit)" stroke="#0B1026" stroke-width="2.5"/>
  <path d="M104,212 L120,212 L111,228 L124,228 L100,256 L106,234 L95,234 Z" fill="#FFD54A" stroke="#0B1026" stroke-width="1.8"/>
  <path d="M168,206 Q186,226 180,262" fill="none" stroke="#9E1B2A" stroke-width="3"/>
  <rect x="98" y="158" width="24" height="26" fill="#E8B48C" stroke="#0B1026" stroke-width="2"/>
  <ellipse cx="72" cy="120" rx="7" ry="11" fill="#F2C29A" stroke="#0B1026" stroke-width="2"/>
  <ellipse cx="148" cy="120" rx="7" ry="11" fill="#F2C29A" stroke="#0B1026" stroke-width="2"/>
  <path d="M74,110 C74,150 88,166 110,166 C132,166 146,150 146,110 C146,92 132,84 110,84 C88,84 74,92 74,110 Z" fill="#F2C29A" stroke="#0B1026" stroke-width="2.5"/>
  <path d="M72,112 C66,74 96,52 122,60 C146,56 160,78 150,110 C146,94 134,88 118,90 C112,80 90,84 84,96 C80,100 76,104 72,112 Z" fill="#3B2416" stroke="#0B1026" stroke-width="2"/>
  <path d="M100,64 C110,52 130,52 136,62" fill="none" stroke="#6B4A33" stroke-width="3" stroke-linecap="round"/>
  <path d="M87,104 Q95,97 104,102" fill="none" stroke="#3B2416" stroke-width="3.5" stroke-linecap="round"/>
  <path d="M116,102 Q125,97 133,104" fill="none" stroke="#3B2416" stroke-width="3.5" stroke-linecap="round"/>
  <ellipse cx="96" cy="114" rx="4.2" ry="5.6" fill="#0B1026"/><circle cx="97.5" cy="112" r="1.4" fill="#FFFFFF"/>
  <ellipse cx="124" cy="114" rx="4.2" ry="5.6" fill="#0B1026"/><circle cx="125.5" cy="112" r="1.4" fill="#FFFFFF"/>
  <path d="M110,116 Q105,128 112,130" fill="none" stroke="#B5754F" stroke-width="2.2" stroke-linecap="round"/>
  <circle cx="85" cy="132" r="6" fill="#E98A7A" opacity=".45"/><circle cx="135" cy="132" r="6" fill="#E98A7A" opacity=".45"/>
  <path d="M90,137 Q110,160 130,137 Q110,145 90,137 Z" fill="#FFFFFF" stroke="#0B1026" stroke-width="2.2" stroke-linejoin="round"/>
  <path d="M106,158 Q110,161 114,158" fill="none" stroke="#B5754F" stroke-width="1.6"/>
  <circle cx="110" cy="112" r="74" fill="url(#glass)" stroke="#E3F4FF" stroke-width="4"/>
  <path class="glint" d="M56,84 A62,62 0 0 1 92,46" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/>
  <circle class="glint" cx="160" cy="70" r="4" fill="#FFFFFF" style="animation-delay:-1.2s"/>
  <line x1="110" y1="38" x2="110" y2="14" stroke="#C0C7D1" stroke-width="4"/>
  <circle class="d" cx="110" cy="11" r="6.5" fill="#FF3B3B" stroke="#0B1026" stroke-width="1.5" style="animation-duration:1.4s"/>
  <ellipse cx="110" cy="186" rx="58" ry="12" fill="url(#chrome)" stroke="#0B1026" stroke-width="2.5"/>
  <circle class="d" cx="80" cy="186" r="3" fill="#39FF88" style="animation-duration:1.1s"/>
  <circle class="d" cx="140" cy="186" r="3" fill="#FFB000" style="animation-duration:1.7s;animation-delay:-.5s"/>
  <g class="wag">
    <path d="M54,206 L24,152" stroke="url(#suit)" stroke-width="19" stroke-linecap="round"/>
    <path d="M54,206 L24,152" stroke="#0B1026" stroke-width="2" stroke-linecap="round" opacity=".25"/>
    <ellipse cx="22" cy="146" rx="12" ry="11" fill="#F5F5F5" stroke="#0B1026" stroke-width="2.2"/>
    <rect x="16.5" y="118" width="8" height="26" rx="4" fill="#F5F5F5" stroke="#0B1026" stroke-width="2.2"/>
    <path d="M12,152 L32,152" stroke="#C9CDD3" stroke-width="3"/>
  </g>
</g>
</svg>"""
    (OUT / "mascot.svg").write_text(svg, encoding="utf-8")


def badge_photoshop():
    """Original retro badge for the Photoshop module: three stacked layers in a chrome ring (not Adobe's logo)."""
    css = BASE_CSS + "@keyframes lift { 0%,100% {transform:translateY(0)} 50% {transform:translateY(-4px)} } .lift { animation: lift 3s ease-in-out infinite }"
    sheet = lambda y, fill: (f'<path d="M30,{y} L66,{y - 14} L94,{y} L58,{y + 14} Z" fill="{fill}" stroke="#0B1026" '
                             f'stroke-width="3" stroke-linejoin="round"/>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 124 124" width="124" height="124" role="img" aria-label="Photoshop module badge: three stacked layers">
<style>{css}</style>
<defs><linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".5" stop-color="#9AA4B1"/><stop offset="1" stop-color="#E3E7EC"/></linearGradient></defs>
<circle cx="62" cy="62" r="56" fill="#0B1026" stroke="url(#chrome)" stroke-width="8"/>
<circle cx="62" cy="62" r="45" fill="none" stroke="#3DDBD9" stroke-width="2" stroke-dasharray="4 5"/>
{sheet(80, "#E63946")}{sheet(66, "#FFD54A")}<g class="lift">{sheet(52, "#3DDBD9")}</g>
<circle class="d" cx="62" cy="14" r="3.5" fill="#39FF88" style="animation-duration:1.5s"/>
</svg>"""
    (OUT / "badge-photoshop.svg").write_text(svg, encoding="utf-8")


space_bg()
badge_photoshop()
mascot()
lights_strip()
banner("photoshop", "PHOTOSHOP", "FLIGHT MANUAL FOR NEW TEACHERS")
banner("getting-started", "LIFTOFF", "THE FIRST TWO DAYS")
print("theme assets written to", OUT)
