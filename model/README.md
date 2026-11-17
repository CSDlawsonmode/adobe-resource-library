# Adobe Resource Library: module models

Retro-future "flight manual" pages for the IDE Canvas library.  **Every page is generated.**  Edit the generator and rebuild; a hand edit to `pages/*.html` is overwritten the next time anything rebuilds.

## Rebuild everything

```bash
python model/make_theme_assets.py
python model/module-1-getting-started/make_pages.py
python model/module-2-photoshop/make_pages.py
python model/check_canvas.py
python model/build_preview.py
```

| File | Job |
|---|---|
| `make_theme_assets.py` | Draws the animated SVGs in `theme/`: banners, starfield, console strip, and **Commander Skip** (the mascot) |
| `kit.py` | Page components: `page`, `tip` (Skip's speech bubble), `grid`, `card`, `mission` (click-to-open card), `check` (Mission Check), `redbox`, `table`, `console_table`, `student_box`, and others |
| `module-*/make_pages.py` | Each module's content, built from the kit |
| `check_canvas.py` | Fails if Canvas's sanitizer would strip anything |
| `build_preview.py` | One self-contained `preview.html` per module, with the art embedded |

## Commander Skip

An original 1950s spaceman: dark pompadour, big grin, red flight suit with a lightning-bolt emblem, fishbowl glass helmet with a blinking antenna, wagging a "here's a tip" finger.  His line is "Hey there, sport!"  He was deliberately designed not to resemble existing retro mascots: no wink, no thumbs-up, not blond.  He appears once per page, carrying the page's intro or most important tip.

## Less scrolling (v3)

- The full banner appears only on each module's Start Here page.  Other pages get a slim console header.
- Cards sit in responsive grids (`repeat(auto-fit, minmax(...))`): 2–3 across on a wide screen, 1 on a phone.
- Missions and lesson kits are click-to-open `<details>` cards.
- At 1700px wide, each page is now about 400–1250px tall.
