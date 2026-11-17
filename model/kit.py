"""Page components for the Adobe Resource Library (retro-future theme).

Every module's make_pages.py builds its Canvas pages from these functions, so
the look stays consistent and every page passes check_canvas.py. Only CSS that
Canvas keeps is used here: no letter-spacing, text-transform or font-weight.
Bold comes from <strong>; capitals are written in the text.

Text arguments are HTML (so <strong>, <em> and entities work). Titles passed to
page() and h3() are plain text; they're uppercased and escaped here.
"""
import html
import pathlib

FUT = "Futura,'Century Gothic','Trebuchet MS',sans-serif"
MONO = "'Courier New',monospace"
NAVY, INK, PAPER = "#0B1026", "#1B1B2F", "#FFF6E0"
CREAM, YEL, TEAL, AMBER, GREEN = "#F5E9C8", "#FFD54A", "#3DDBD9", "#FFC857", "#7CFFB2"
RED = "#9E1B2A"
CHROME = "4px ridge #C0C7D1"
ACCENTS = {"purple": "#7C3AED", "red": "#E63946", "orange": "#EA580C", "cyan": "#0891B2",
           "green": "#16A34A", "blue": "#2D5B8A"}

THEME = pathlib.Path(__file__).parent / "theme"


def module_badge(slug):
    """Official app logo if it's been dropped into theme/logos/, otherwise the original retro badge."""
    for ext in ("svg", "png"):
        if (THEME / "logos" / f"{slug}.{ext}").exists():
            return f"logos/{slug}.{ext}"
    return f"badge-{slug}.svg" if (THEME / f"badge-{slug}.svg").exists() else None


STRIP = '<img src="../theme/lights-strip.svg" alt="" style="display:block;width:100%;height:auto;">'


def caps(text):
    return html.escape(text.upper(), quote=False)


def page(*, label, banner, banner_alt, kicker, title, body, first=False, kicker_color=TEAL, badge=None):
    if first:
        top = f'<img src="../theme/{banner}" alt="{banner_alt}" style="display:block;width:100%;height:auto;">'
    else:
        top = (f'<div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;'
               f'padding:10px 20px;background:#151A3A;border-bottom:3px ridge #C0C7D1;">'
               f'<span style="font-family:{FUT};color:{YEL};font-size:1.1em;">'
               + (f'<img src="../theme/{badge}" alt="" style="width:38px;height:auto;vertical-align:middle;margin-right:8px;">' if badge else '')
               + f'<strong>&#9733; {caps(label)} &#9733;</strong></span>'
               f'<img src="../theme/lights-strip.svg" alt="" style="display:block;width:100%;max-width:420px;height:auto;"></div>')
    return (f'<div style="background-color:{NAVY};background-image:url(\'../theme/space-bg.svg\');background-repeat:repeat;'
            f'color:{CREAM};border:5px ridge #C0C7D1;border-radius:18px;overflow:hidden;'
            f'font-family:\'Trebuchet MS\',Arial,sans-serif;line-height:1.5;">\n{top}\n'
            f'<div style="padding:4px 20px 20px 20px;">\n'
            f'<p style="margin:12px 0 0 0;font-family:{MONO};font-size:0.85em;color:{kicker_color};">&#9656; {caps(kicker)}</p>\n'
            f'<h2 style="margin:2px 0 8px 0;color:{YEL};font-family:{FUT};">{caps(title)}</h2>\n'
            f'{body}\n</div>\n</div>\n')


def h3(icon, text):
    return (f'<h3 style="margin:20px 0 8px 0;color:{TEAL};font-family:{FUT};font-size:1.15em;">'
            f'{icon} {caps(text)}</h3>\n')


def p(text, color=None, size=None):
    style = "margin:0 0 10px 0;" + (f"color:{color};" if color else "") + (f"font-size:{size};" if size else "")
    return f'<p style="{style}">{text}</p>\n'


def grid(*items, min=280, align="stretch"):
    return (f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax({min}px,1fr));gap:16px;'
            f'margin:14px 0;align-items:{align};">\n' + "\n".join(items) + '\n</div>\n')


def tip(text, who="COMMANDER SKIP SAYS"):
    return (f'<div style="display:flex;align-items:center;margin:14px 0;">'
            f'<img src="../theme/mascot.svg" alt="Commander Skip, a 1950s spaceman in a glass bubble helmet" '
            f'style="display:block;width:104px;height:auto;flex:0 0 104px;">'
            f'<div style="width:0;height:0;border-top:12px solid transparent;border-bottom:12px solid transparent;'
            f'border-right:16px solid #FFFFFF;flex:0 0 0;"></div>'
            f'<div style="flex:1 1 auto;background:#FFFFFF;color:{INK};border-radius:18px;padding:10px 16px;'
            f'border-bottom:4px solid {YEL};">'
            f'<p style="margin:0 0 2px 0;font-family:{MONO};font-size:0.8em;color:{RED};"><strong>{who}:</strong></p>'
            f'<p style="margin:0;font-size:1.05em;">{text}</p></div></div>\n')


def card(title, inner, accent="purple", icon=""):
    return (f'<div style="background:{PAPER};color:{INK};border:{CHROME};border-left:12px solid {ACCENTS[accent]};'
            f'border-radius:16px;padding:12px 16px;margin:0;">'
            f'<p style="margin:0 0 6px 0;font-size:1.1em;font-family:{FUT};"><strong>{icon} {caps(title)}</strong></p>'
            f'{inner}</div>')


def redbox(label, big, small="", checklist=None):
    items = ""
    if checklist:
        items = ('<ul style="margin:6px 0 0 0;list-style:none;padding-left:2px;color:#FFFFFF;">'
                 + "".join(f"<li>&#9744; {i}</li>" for i in checklist) + "</ul>")
    big_html = f'<p style="margin:0;font-size:1.35em;color:#FFFFFF;font-family:{FUT};"><strong>{big}</strong></p>' if big else ""
    small_html = f'<p style="margin:8px 0 0 0;color:#FFFFFF;">{small}</p>' if small else ""
    return (f'<div style="background:{RED};color:#FFFFFF;border:5px ridge #C0C7D1;border-radius:16px;padding:14px 18px;margin:0;">'
            f'<p style="margin:0 0 6px 0;font-family:{MONO};font-size:0.85em;color:#FFE66D;"><strong>&#9889; {label}</strong></p>'
            f'{big_html}{small_html}{items}</div>')


def checklist(items, color=None):
    c = f"color:{color};" if color else ""
    return (f'<ul style="margin:0 0 8px 0;list-style:none;padding-left:2px;{c}">'
            + "".join(f"<li>&#9744; {i}</li>" for i in items) + "</ul>")


def bullets(items):
    return '<ul style="margin:0 0 6px 0;padding-left:20px;">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def table(headers, rows):
    head = "".join(f'<th scope="col" style="text-align:left;color:{YEL};">{h}</th>' for h in headers)
    body = "".join(
        f'<tr style="border-bottom:1px solid #C9B98F;">' + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<div style="background:{PAPER};color:{INK};border:{CHROME};border-radius:16px;padding:6px;margin:0;">'
            f'<table style="border-collapse:collapse;width:100%;color:{INK};" cellpadding="9">'
            f'<thead><tr style="background:{INK};">{head}</tr></thead><tbody>{body}</tbody></table></div>')


def console_table(headers, rows):
    head = "".join(f'<th scope="col" style="text-align:left;color:{AMBER};">{h}</th>' for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<div style="background:#06140D;border:{CHROME};border-radius:16px;padding:6px;margin:0;">'
            f'<table style="border-collapse:collapse;width:100%;font-family:{MONO};color:{GREEN};" cellpadding="7">'
            f'<thead><tr style="border-bottom:2px solid #2E6B4A;">{head}</tr></thead><tbody>{body}</tbody></table></div>')


def console(lines):
    return (f'<div style="background:#06140D;border:{CHROME};border-radius:16px;padding:12px 16px;margin:0;'
            f'font-family:{MONO};color:{GREEN};">'
            + "".join(f'<p style="margin:0 0 6px 0;">{l}</p>' for l in lines) + "</div>")


def check(question, answer, options=None, label=""):
    opts = ""
    if options:
        opts = ('<ol type="A" style="margin:0 0 6px 0;padding-left:24px;">'
                + "".join(f"<li>{o}</li>" for o in options) + "</ol>")
    return (f'<div style="border:{CHROME};border-radius:16px;overflow:hidden;background:#06140D;margin:0;">{STRIP}'
            f'<div style="padding:10px 16px 14px 16px;font-family:{MONO};color:{GREEN};">'
            f'<p style="margin:0 0 6px 0;color:{AMBER};"><strong>&#128640; MISSION CHECK{label}</strong></p>'
            f'<p style="margin:0 0 6px 0;">{question}</p>{opts}'
            f'<details><summary style="cursor:pointer;color:{AMBER};"><strong>COMPUTE ANSWER</strong></summary>'
            f'<p style="margin:8px 0 0 0;color:{CREAM};">{answer}</p></details></div></div>')


def mission(tag, title, inner, accent="purple", icon=""):
    """A click-to-open card. Closed, it's one line; open, it holds everything."""
    return (f'<details style="background:{PAPER};color:{INK};border:{CHROME};border-top:10px solid {ACCENTS[accent]};'
            f'border-radius:16px;padding:12px 16px;margin:0;">'
            f'<summary style="cursor:pointer;font-family:{FUT};font-size:1.1em;">'
            f'<span style="background:{INK};color:{YEL};font-family:{MONO};padding:2px 10px;border-radius:999px;font-size:0.8em;">'
            f'<strong>{tag}</strong></span> <strong>{icon} {title}</strong></summary>'
            f'<div style="margin-top:10px;">{inner}</div></details>')


def student_box(title, inner):
    return (f'<div style="background:#FFFFFF;border:2px solid {INK};border-radius:12px;padding:10px 14px;margin:8px 0;">'
            f'<p style="margin:0 0 6px 0;font-family:{MONO};font-size:0.85em;color:{RED};"><strong>&#128203; {title}</strong></p>'
            f'{inner}</div>')


def shot(src, alt, caption=""):
    """A framed screenshot. Put the file in the module's images/ folder; src is just the file name."""
    cap = f'<p style="margin:6px 4px 0 4px;font-size:0.9em;color:{INK};"><em>{caption}</em></p>' if caption else ""
    return (f'<div style="background:{PAPER};border:{CHROME};border-radius:16px;padding:8px;margin:0;">'
            f'<img src="../images/{src}" alt="{html.escape(alt)}" style="display:block;width:100%;height:auto;'
            f'border-radius:10px;border:2px solid {INK};">{cap}</div>')


def video(text):
    return (f'<div style="border:3px dashed {TEAL};border-radius:16px;padding:12px;text-align:center;margin:0;background:#141A3A;">'
            f'<p style="margin:0;color:{CREAM};"><strong>&#127909; {text}</strong> <em>[video goes here]</em></p></div>')


def credit():
    return (f'<p style="color:#B8C2CC;font-size:0.9em;margin:18px 0 0 0;">Built from my own Media Tech classroom at '
            f'Caldwell High School.  Steal what works for your room and leave the rest. &nbsp;~ Chad Lawson</p>')


def write(module_dir, pages):
    out = pathlib.Path(module_dir) / "pages"
    out.mkdir(exist_ok=True)
    for old in out.glob("*.html"):
        old.unlink()
    for name, html_text in pages:
        (out / name).write_text(html_text, encoding="utf-8")
    print(f"{pathlib.Path(module_dir).name}: wrote {len(pages)} pages")
