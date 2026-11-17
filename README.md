# Adobe Resource Library

A retro-future "flight manual" for teachers who are new to Adobe Creative Cloud.  Commander Skip gives the tips, and every page has Mission Checks to make sure it stuck.

**View it on the web:** https://csdlawsonmode.github.io/adobe-resource-library/

| Module | Status |
|---|---|
| [Getting Started: The First Two Days](https://csdlawsonmode.github.io/adobe-resource-library/getting-started/) | Model |
| [Photoshop](https://csdlawsonmode.github.io/adobe-resource-library/photoshop/) | Model |
| Illustrator, Premiere Pro, Best Practices, Certification Prep, Extended Resources | Coming soon |

These are working models for a Canvas-based professional learning library.  Each page in `model/module-*/pages/` is built to paste into the Canvas HTML editor.

## How it's built

Everything is generated; see [model/README.md](model/README.md).  The short version:

```bash
python model/make_theme_assets.py
python model/module-1-getting-started/make_pages.py
python model/module-2-photoshop/make_pages.py
python model/check_canvas.py
python model/build_preview.py
```

`build_preview.py` also rebuilds `docs/`, which GitHub Pages serves.

---

Adapted from Media Tech Fundamentals at Caldwell High School by Chad Lawson.  Adobe, Creative Cloud, Photoshop, Illustrator and Premiere Pro are trademarks of Adobe Inc.; this resource is not affiliated with or endorsed by Adobe.
