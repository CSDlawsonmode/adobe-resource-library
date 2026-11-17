"""Build preview.html for every module folder under model/.

Each module's pages/*.html files are the source: page bodies ready to paste
into the Canvas HTML editor. preview.html is only for reading a module in one
place. Edit pages/, then rerun from anywhere:  python model/build_preview.py
"""
import base64
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
CSS = """
  :root { --navy:#070B1E; --panel:#1B1B2F; --chrome:#C0C7D1; --cream:#F5E9C8; --yellow:#FFD54A; --teal:#3DDBD9; --red:#E63946; }
  body { margin:0; font-family:"Trebuchet MS", Arial, sans-serif; color:var(--cream); line-height:1.5;
         background:var(--navy) url("__SPACE__") repeat; }
  header { background:linear-gradient(180deg,#232848 0%,#121633 100%); border-bottom:5px ridge var(--chrome); }
  .head-in { max-width:1600px; margin:0 auto; padding:18px 24px 12px; display:flex; align-items:center; gap:18px; flex-wrap:wrap; }
  .badge { width:54px; height:54px; border-radius:50%; flex:0 0 54px; border:4px ridge var(--chrome);
           background:radial-gradient(circle at 35% 35%,#FFC857,#F26B3A 60%,#8E1F2F); box-shadow:0 0 18px rgba(255,200,87,.45); }
  header h1 { margin:0; font-family:Futura,"Century Gothic","Trebuchet MS",sans-serif; font-size:1.7em; letter-spacing:4px;
              text-transform:uppercase; color:var(--yellow); text-shadow:0 0 12px rgba(255,213,74,.35); }
  header p { margin:2px 0 0 0; color:var(--teal); font-family:"Courier New",monospace; font-size:.9em; letter-spacing:2px; text-transform:uppercase; }
  .strip { display:block; width:100%; max-width:1600px; margin:0 auto; height:auto; padding:0 24px 12px; box-sizing:border-box; }
  .wrap { display:flex; gap:28px; max-width:1600px; margin:0 auto; padding:24px; box-sizing:border-box; }
  nav { flex:0 0 270px; position:sticky; top:18px; align-self:flex-start; background:var(--panel);
        border:5px ridge var(--chrome); border-radius:18px; padding:16px 14px; box-shadow:0 0 30px rgba(61,219,217,.15); }
  nav .log { margin:0 0 12px 4px; font-family:"Courier New",monospace; color:#FFC857; letter-spacing:3px; font-weight:700; }
  nav ol { list-style:none; padding:0; margin:0; counter-reset:m; }
  nav li { counter-increment:m; margin-bottom:10px; }
  nav a { display:flex; gap:10px; align-items:center; text-decoration:none; color:var(--cream); background:#0B1026;
          border:2px solid #34406A; border-radius:12px; padding:10px 12px; font-size:.92em; line-height:1.25; transition:all .15s; }
  nav a::before { content:counter(m, decimal-leading-zero); font-family:"Courier New",monospace; font-weight:700; color:var(--navy);
                  background:var(--yellow); border-radius:6px; padding:2px 6px; flex:0 0 auto; }
  nav a::after { content:""; width:9px; height:9px; border-radius:50%; margin-left:auto; flex:0 0 9px; background:#39FF88;
                 box-shadow:0 0 8px #39FF88; animation:blink 1.6s steps(1) infinite; }
  nav li:nth-child(2) a::after { background:#FFB000; box-shadow:0 0 8px #FFB000; animation-duration:1.1s; }
  nav li:nth-child(3) a::after { background:#FF3B3B; box-shadow:0 0 8px #FF3B3B; animation-duration:2.2s; }
  nav li:nth-child(4) a::after { background:var(--teal); box-shadow:0 0 8px var(--teal); animation-duration:1.4s; }
  nav li:nth-child(5) a::after { background:#FFE66D; box-shadow:0 0 8px #FFE66D; animation-duration:1.8s; }
  nav a:hover, nav a:focus-visible { border-color:var(--teal); background:#14204A; box-shadow:0 0 12px rgba(61,219,217,.5); outline:none; }
  @keyframes blink { 0%,49% {opacity:1} 50%,100% {opacity:.2} }
  main { flex:1; min-width:0; }
  .page { margin-bottom:40px; overflow-x:auto; scroll-margin-top:18px; }
  .page:not(.themed) { background:#FFFFFF; color:#1F2933; border-radius:12px; padding:8px 24px 24px; }
  .file { font-family:"Courier New",monospace; font-size:.78em; color:var(--teal); opacity:.75; margin:0 0 8px 6px; letter-spacing:1px; }
  .file::before { content:"B8  TRANSMISSION: "; }
  code { background:#F3F4F6; color:#1B1B2F; padding:1px 4px; border-radius:3px; }
  footer { text-align:center; padding:10px 0 34px; font-family:"Courier New",monospace; color:var(--teal); letter-spacing:4px; opacity:.8; }
  @media (prefers-reduced-motion: reduce) { * { animation:none !important; transition:none !important; } }
  @media (max-width: 860px) {
    .wrap { flex-direction:column; padding:16px; }
    nav { position:static; flex:none; }
    .head-in { padding:14px 16px 10px; } .strip { padding:0 16px 10px; }
    header h1 { font-size:1.3em; letter-spacing:2px; }
  }
"""


def title_of(body, fallback):
    m = re.search(r"<h2[^>]*>(.*?)</h2>", body, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else fallback


def svg_uri(name):
    return "data:image/svg+xml;base64," + base64.b64encode((ROOT / "theme" / name).read_bytes()).decode()


MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif"}


def data_uri(f):
    return f"data:{MIME.get(f.suffix.lower(), 'application/octet-stream')};base64," + base64.b64encode(f.read_bytes()).decode()


def inline_theme(body, module=None):
    """Embed ../theme/* and ../images/* as data URIs so preview.html stands alone."""
    def sub(base):
        def inner(m):
            f = base / m.group(1)
            return data_uri(f) if f.exists() else m.group(0)
        return inner
    body = re.sub(r"\.\./theme/([\w./-]+\.(?:svg|png|jpe?g|gif))", sub(ROOT / "theme"), body)
    if module is not None:
        body = re.sub(r"\.\./images/([\w./-]+\.(?:svg|png|jpe?g|gif))", sub(module / "images"), body)
    return body


def build(module):
    pages = sorted((module / "pages").glob("*.html"))
    if not pages:
        return
    nav, sections, site_sections = [], [], []
    for p in pages:
        body = p.read_text(encoding="utf-8")
        nav.append(f'<li><a href="#{p.stem}">{title_of(body, p.stem)}</a></li>')
        themed = body.lstrip().startswith('<div style="background-color:#0B1026')
        sections.append(
            f'<p class="file">pages/{html.escape(p.name)}</p>'
            f'<section id="{p.stem}" class="page{" themed" if themed else ""}">{inline_theme(body, module)}</section>'
        )
        site_sections.append(
            f'<p class="file">pages/{html.escape(p.name)}</p>'
            f'<section id="{p.stem}" class="page{" themed" if themed else ""}">{body.replace("../images/", "images/")}</section>'
        )
    first = title_of(pages[0].read_text(encoding="utf-8"), module.name)
    heading = first.split(":")[0].strip()
    out = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(heading)} Module Model</title>
<style>{CSS.replace("__SPACE__", svg_uri("space-bg.svg"))}</style></head>
<body>
<header><div class="head-in"><div class="badge" aria-hidden="true"></div><div>
<h1>Module Model: {html.escape(heading)}</h1>
<p>Adobe Resource Library (IDE) &middot; {len(pages)} Canvas pages &middot; preview only</p></div></div>
<img class="strip" src="{svg_uri("lights-strip.svg")}" alt=""></header>
<div class="wrap"><nav aria-label="Pages"><p class="log">&#9656; MISSION LOG</p><ol>{''.join(nav)}</ol></nav>
<main>{''.join(sections)}</main></div>
<footer>&#9733; END OF TRANSMISSION &#9733;</footer>
</body></html>
"""
    (module / "preview.html").write_text(out, encoding="utf-8")
    print(f"{module.name}: preview.html built from {len(pages)} pages")
    site = (out.replace(''.join(sections), ''.join(site_sections))
               .replace(svg_uri("space-bg.svg"), "../theme/space-bg.svg")
               .replace(svg_uri("lights-strip.svg"), "../theme/lights-strip.svg"))
    return {"slug": module.name.split("-", 2)[-1], "heading": heading, "html": site, "pages": len(pages),
            "images": module / "images",
            "titles": [title_of(p.read_text(encoding="utf-8"), p.stem) for p in pages]}


# ------------------------------------------------------------------ public site (GitHub Pages)
SITE = ROOT.parent / "docs"
HOME_LINK = ('<a class="home" href="../" aria-label="All modules">&#9664; ALL MODULES</a>')
SITE_CSS = """
  .home { font-family:"Courier New",monospace; color:#0B1026; background:#FFD54A; text-decoration:none;
          border-radius:999px; padding:6px 14px; font-weight:700; letter-spacing:1px; border:3px ridge #C0C7D1; }
  .home:hover, .home:focus-visible { background:#3DDBD9; outline:none; }
  .hero { max-width:1600px; margin:0 auto; padding:24px; box-sizing:border-box; }
  .skip { display:flex; align-items:center; gap:0; max-width:980px; margin:8px auto 28px; }
  .skip img { width:150px; flex:0 0 150px; }
  .tail { width:0; height:0; border-top:14px solid transparent; border-bottom:14px solid transparent; border-right:20px solid #FFF; }
  .bubble { background:#FFF; color:#1B1B2F; border-radius:22px; padding:16px 22px; border-bottom:5px solid #FFD54A; font-size:1.15em; }
  .bubble b { display:block; font-family:"Courier New",monospace; color:#9E1B2A; font-size:.75em; letter-spacing:2px; }
  .tiles { display:grid; grid-template-columns:repeat(auto-fit,minmax(360px,1fr)); gap:24px; }
  .tile { display:block; text-decoration:none; color:#F5E9C8; background:#1B1B2F; border:5px ridge #C0C7D1; border-radius:20px;
          overflow:hidden; transition:transform .15s, box-shadow .15s; }
  .tile:hover, .tile:focus-visible { transform:translateY(-4px); box-shadow:0 0 28px rgba(61,219,217,.55); outline:none; }
  .tile img { display:block; width:100%; height:auto; }
  .tile .in { padding:14px 18px 18px; }
  .tile h2 { margin:0 0 6px; font-family:Futura,"Century Gothic","Trebuchet MS",sans-serif; color:#FFD54A; letter-spacing:2px; }
  .tile p { margin:0 0 8px; }
  .tile .go { font-family:"Courier New",monospace; color:#3DDBD9; letter-spacing:2px; }
  .soon { display:flex; flex-direction:column; justify-content:center; min-height:180px; border-style:dashed; opacity:.75; cursor:default; }
  .soon:hover { transform:none; box-shadow:none; }
  .soon .in { text-align:center; }
  @media (max-width: 860px) { .tiles { grid-template-columns:1fr; } .skip img { width:96px; flex-basis:96px; } .hero { padding:16px; } }
"""
PLANNED = [("&#127912;", "Illustrator", "Shapes, color, and the Pen tool."),
           ("&#127909;", "Premiere Pro", "Cutting, sound, titles, export."),
           ("&#11088;", "Best Practices", "The two-week cycle, choice, feedback, AI."),
           ("&#127891;", "Certification Prep", "Adobe Certified Professional, mapped to the missions."),
           ("&#128301;", "Extended Resources", "Graphic design, media arts, digital literacy.")]
BLURBS = {"getting-started": "Day one and day two: every kid signed in, organized, sharing files, and emailing like a pro.",
          "photoshop": "Five ideas, one rule, four missions, and a help desk for when it's doing a thing."}


def badge_img(slug):
    for name in (f"logos/{slug}.svg", f"logos/{slug}.png", f"badge-{slug}.svg"):
        if (ROOT / "theme" / name).exists():
            return (f'<img src="theme/{name}" alt="" style="width:44px;height:auto;vertical-align:middle;'
                    f'margin-right:10px;display:inline;">')
    return ""


def build_site(mods):
    import shutil
    SITE.mkdir(exist_ok=True)
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copytree(ROOT / "theme", SITE / "theme", dirs_exist_ok=True)
    tiles = []
    for m in mods:
        page = (m["html"].replace("</style>", SITE_CSS + "</style>", 1)
                .replace('<div class="head-in">', f'<div class="head-in">{HOME_LINK}', 1)
                .replace("&middot; preview only", "&middot; Canvas-ready", 1))
        (SITE / m["slug"]).mkdir(exist_ok=True)
        (SITE / m["slug"] / "index.html").write_text(page, encoding="utf-8")
        if m["images"].exists():
            shutil.copytree(m["images"], SITE / m["slug"] / "images", dirs_exist_ok=True)
        tiles.append(f'<a class="tile" href="{m["slug"]}/"><img src="theme/banner-{m["slug"]}.svg" alt="">'
                     f'<div class="in"><h2>{badge_img(m["slug"])}{html.escape(m["heading"])}</h2><p>{BLURBS.get(m["slug"], "")}</p>'
                     f'<p class="go">&#9656; {m["pages"]} PAGES &middot; LAUNCH</p></div></a>')
    for icon, name, blurb in PLANNED:
        tiles.append(f'<div class="tile soon"><div class="in"><h2>{icon} {name.upper()}</h2><p>{blurb}</p>'
                     f'<p class="go">COMING SOON</p></div></div>')
    index = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Adobe Resource Library</title>
<meta name="description" content="A retro-future flight manual for teachers new to Adobe Creative Cloud.">
<link rel="icon" href="theme/mascot.svg" type="image/svg+xml">
<style>{CSS.replace('url("__SPACE__")', 'url("theme/space-bg.svg")')}{SITE_CSS}</style></head>
<body>
<header><div class="head-in"><div class="badge" aria-hidden="true"></div><div>
<h1>Adobe Resource Library</h1>
<p>A flight manual for teachers new to Adobe Creative Cloud</p></div></div>
<img class="strip" src="theme/lights-strip.svg" alt=""></header>
<div class="hero">
<div class="skip"><img src="theme/mascot.svg" alt="Commander Skip, a 1950s spaceman in a glass bubble helmet">
<div class="tail"></div><div class="bubble"><b>COMMANDER SKIP SAYS:</b>Hey there, sport!  Brand new to Adobe, or just need a hand
mid-lesson?  Pick a module and blast off.  Every page has Mission Checks to make sure it stuck.</div></div>
<div class="tiles">{''.join(tiles)}</div>
</div>
<footer>&#9733; BUILT BY A TEACHER, FOR TEACHERS &#9733;<br><span style="font-size:.75em;letter-spacing:0;opacity:.8;">Adobe, Creative Cloud, Photoshop, Illustrator and Premiere Pro are trademarks of Adobe Inc.  This resource is not affiliated with or endorsed by Adobe.</span></footer>
</body></html>
"""
    (SITE / "index.html").write_text(index, encoding="utf-8")
    print(f"site: docs/ built with {len(mods)} modules")


mods = [m for m in (build(d) for d in sorted(d for d in ROOT.iterdir() if d.is_dir() and d.name.startswith("module-"))) if m]
build_site(mods)
