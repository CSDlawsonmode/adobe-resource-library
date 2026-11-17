"""Check every module page against Canvas LMS's HTML sanitizer allowlist.

  python model/check_canvas.py

Lists anything Canvas would silently strip when the page is pasted into the
Rich Content Editor: elements, attributes, inline CSS properties, and URL
schemes. Exit code 1 if anything would be stripped.

The allowlists below are copied from instructure/canvas-lms,
gems/canvas_sanitize/lib/canvas_sanitize/canvas_sanitize.rb (master, checked
2026-11-16). Re-check that file if Canvas behavior seems to change.
"""
import pathlib
import re
import sys
from html.parser import HTMLParser

ELEMENTS = set("""a b blockquote br caption cite code col hr h1 h2 h3 h4 h5 h6 del ins iframe font
colgroup dd div dl dt em figure figcaption i img li ol p pre q small source span strike strong
sub sup abbr table tbody td tfoot th thead tr u ul object embed param video track audio address
acronym map area bdo dfn kbd legend samp tt var big article aside details footer header nav
section summary time picture ruby rt rp mark""".split())

GLOBAL_ATTRS = {"style", "class", "id", "title", "role", "lang", "dir"}
ELEMENT_ATTRS = {
    "img": {"align", "alt", "height", "src", "usemap", "width", "longdesc"},
    "table": {"summary", "width", "border", "cellpadding", "cellspacing", "center", "frame", "rules"},
    "td": {"abbr", "axis", "colspan", "rowspan", "width", "align", "valign", "dir"},
    "th": {"abbr", "axis", "colspan", "rowspan", "width", "align", "valign", "dir", "scope"},
    "ol": {"start", "type"},
    "ul": {"type"},
    "a": {"href", "target", "name"},
}

CSS = set("""align-content align-items align-self background border border-radius clear clip color
column-gap cursor direction display flex flex-basis flex-direction flex-flow flex-grow flex-shrink
flex-wrap float font gap grid height justify-content justify-items justify-self left line-height
list-style margin max-height max-width min-height min-width order overflow overflow-x overflow-y
padding position place-content place-items place-self right row-gap text-align table-layout
text-decoration text-indent top user-select vertical-align visibility white-space width z-index
zoom""".split())
CSS |= {f"grid-{i}" for i in "area auto-columns auto-flow auto-rows column gap row template".split()}
CSS |= {f"grid-template-{i}" for i in "areas columns rows".split()}
CSS |= {f"grid-column-{i}" for i in "end gap start".split()}
CSS |= {f"grid-row-{i}" for i in "end gap start".split()}
CSS |= {f"background-{i}" for i in "attachment color image position repeat".split()}
CSS |= {f"background-position-{i}" for i in "x y".split()}
CSS |= {f"border-{i}" for i in "bottom collapse color left right spacing style top width".split()}
CSS |= {f"border-{i}-{j}" for i in "bottom left right top".split() for j in "color style width".split()}
CSS |= {f"font-{i}" for i in "family size stretch style variant width".split()}
CSS |= {f"list-style-{i}" for i in "image position type".split()}
CSS |= {f"margin-{i}" for i in "bottom left right top offset".split()}
CSS |= {f"padding-{i}" for i in "bottom left right top".split()}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.problems = []

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        if tag not in ELEMENTS:
            self.problems.append((line, f"element <{tag}> is stripped"))
            return
        allowed = GLOBAL_ATTRS | ELEMENT_ATTRS.get(tag, set())
        for name, value in attrs:
            if name.startswith(("data-", "aria-")):
                continue
            if name not in allowed:
                self.problems.append((line, f"<{tag} {name}=...> attribute is stripped"))
            if name == "style" and value:
                for decl in value.split(";"):
                    if ":" not in decl:
                        continue
                    prop, val = (s.strip() for s in decl.split(":", 1))
                    if prop.lower() not in CSS:
                        self.problems.append((line, f"CSS '{prop}' is stripped"))
                    for url in re.findall(r"url\(\s*['\"]?([^'\")]+)", val):
                        if url.startswith("data:"):
                            self.problems.append((line, f"CSS data: URL is stripped"))
            if name == "src" and value and value.startswith("data:") and tag == "img":
                self.problems.append((line, "img data: URL is stripped"))


def main():
    root = pathlib.Path(__file__).parent
    total = 0
    for page in sorted(root.glob("module-*/pages/*.html")):
        c = Checker()
        c.feed(page.read_text(encoding="utf-8"))
        if c.problems:
            print(f"\n{page.relative_to(root)}")
            seen = {}
            for line, msg in c.problems:
                seen.setdefault(msg, []).append(line)
            for msg, lines in seen.items():
                print(f"  {msg}  (lines {', '.join(map(str, lines[:6]))}{'...' if len(lines) > 6 else ''})")
            total += len(c.problems)
    print(f"\n{total} thing(s) Canvas would strip." if total else "Clean: Canvas would keep everything.")
    sys.exit(1 if total else 0)


main()
