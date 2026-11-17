# Module 2 model: Photoshop

Version 2: a **retro-future flight manual**.  It's built to stay open beside Photoshop while a new teacher works, so it keeps things simple (KISS).  Adapted from Media Tech Fundamentals **Units 2–5**.

## Files

| Path | What it is |
|---|---|
| `pages/*.html` | **The source.** Five Canvas pages, each pasteable into the HTML editor, inline styles only. |
| `preview.html` | All five pages on one page, with the theme art embedded so it opens anywhere.  Generated: run `python model/build_preview.py`. |
| `../theme/*.svg` | The animated art, shared by every module.  Generated: run `python model/make_theme_assets.py`. |

## Pages

1. **Start Here** (Mission Briefing): the First Law of the Lab, a "what do you need right now?" navigation table, the four missions
2. **The Big Five** (Instrument Panel): layers, masks, adjustment layers, blending modes, Smart Objects; for each, what it is, a line to say to students, and what to watch for
3. **Running a Project** (Flight Plan): the two-week cycle, demos, choice with guardrails, and adapting it
4. **The Four Projects** (Mission Files): one card per project with a checkbox list, three demos, and the choice menu
5. **Help! It's Doing a Thing** (Distress Signals): student quotes paired with fixes, ten shortcuts, and the certification gaps

There are **9 Mission Checks**, each a scenario question in a green-screen readout with a hidden "Compute Answer" reveal.  They explain why the wrong answers are wrong, not just which one is right.

## The theme

1950s–60s retro-future: deep-space navy, chrome ridge borders, ray-gun red, atomic teal and yellow.

The animated art is three SVGs:
- **banner-photoshop.svg:** a mainframe with spinning tape reels and blinking diodes, a chrome title, a bobbing rocket, a ringed planet, and a saucer crossing the top
- **lights-strip.svg:** a console strip with blinking diodes, a READY readout and a scrolling oscilloscope.  It heads every Mission Check.
- **space-bg.svg:** a tiling starfield that twinkles behind the content

All the art is original, in the spirit of the era.  Nothing is copied from Star Trek, Batman, Lost in Space or Flash Gordon.  Every animation honors the viewer's reduced-motion setting, and nothing blinks faster than about once a second.

### Why it's built this way (Canvas limits)

Canvas strips `<script>`, `<style>` and CSS animations from pages.  The motion therefore lives *inside* the SVG files, which keep animating when Canvas shows them as images.

**Checked against Canvas's real sanitizer (2026-11-16).** `python model/check_canvas.py` tests every page against the allowlist in [canvas_sanitize.rb](https://github.com/instructure/canvas-lms/blob/master/gems/canvas_sanitize/lib/canvas_sanitize/canvas_sanitize.rb).  What it showed:
- **Survives:** `<details>`/`<summary>` (the answer reveals), `background-image` with https or relative URLs (the starfield), `border-radius`, `overflow`, `font-family`, and `list-style`.
- **Was stripped, now fixed (142 hits):** `letter-spacing`, `text-transform` and `font-weight` aren't on Canvas's list.  Headings are now written in capitals, bold uses `<strong>`, and letter-spacing is gone (the only visual loss).
- **Never works in Canvas:** `data:` URLs in CSS.  That's why the pages point at uploaded files, and only the local preview embeds the art.
- Run the checker after any page edit.  It exits non-zero if anything would be stripped.

**Still needs a real Canvas page:** that uploaded `.svg` files animate when Canvas serves them from course Files.  This is expected to work, but it hasn't been seen yet.

When pasting into Canvas, upload `model/theme/*.svg` to the course Files and swap each `../theme/…` path for the Canvas file URL.

## Fact-check (2026-11-16)

Exam name, shortcuts and troubleshooting were checked against Adobe's documentation; details are in the first fact-check pass.  Carried forward:
- Exam: *Adobe Certified Professional: Visual Design Using Adobe Photoshop* (2025 objectives).  [Adobe exam page](https://certifiedprofessional.adobe.com/photoshop)
- Masks: [disable/enable](https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/disable-or-enable-layer-masks.html), [edit](https://helpx.adobe.com/photoshop/using/editing-layer-masks.html), [clipping masks](https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/create-and-manage-clipping-masks.html)
- [Background layer lock](https://helpx.adobe.com/photoshop/desktop/create-manage-layers/get-started-layers/convert-background-and-regular-layers.html), [selection tools](https://helpx.adobe.com/photoshop/desktop/make-selections/get-started-selections/selection-tools-overview.html)
- The single-key shortcuts still need a 10-minute check in Photoshop itself (Edit > Keyboard Shortcuts).

## Not done yet

- The overview video
- Downloads: project cards, choice menus, a **licensed** starter kit for Project 3, and example sets
- A real Canvas paste test (see the theme section above)
- Module 1 still has the plain look; it needs the same treatment if we keep this theme
