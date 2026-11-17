"""Build the Photoshop module's Canvas pages.   python model/module-2-photoshop/make_pages.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from kit import (bullets, card, check, checklist, console_table, credit, grid, h3, mission, p, page,
                 redbox, shot, table, tip, video, write, module_badge)

HERE = pathlib.Path(__file__).parent
BASE = dict(label="Photoshop", banner="banner-photoshop.svg", badge=module_badge("photoshop"),
            banner_alt="Photoshop: flight manual for new teachers")
DARK_CODE = 'style="background:#1B1B2F;color:#FFD54A;padding:1px 6px;border-radius:4px;border:1px solid #3DDBD9;"'


def code(t):
    return f"<code {DARK_CODE}>{t}</code>"


# ---------------------------------------------------------------- 1. Start Here
start = page(**BASE, first=True, kicker="Mission Briefing", title="Photoshop: Start Here", body="".join([
    tip("Hey there, sport!  Never opened Photoshop?  Swell... you don't need to be a wizard to teach it.  "
        "Five ideas, one rule, and this page open while you work.  That's the whole trick."),
    grid(
        redbox("THE FIRST LAW OF THE LAB", "Never destroy a pixel you might want back.",
               "Masks, not the Eraser.  Adjustment layers, not menus that bake changes in.  If students leave "
               "knowing only this, they work the way professionals do."),
        table(["I need to&hellip;", "Go to"], [
            ["Understand Photoshop first", "<strong>The Big Five</strong>"],
            ["Plan two weeks of class", "<strong>Running a Project</strong>"],
            ["Pick a project; see &ldquo;done&rdquo;", "<strong>The Four Projects</strong>"],
            ["Fix what a student is waving about", "<strong>Help! It's Doing a Thing</strong>"],
        ]), min=340),
    grid(
        card("Four missions, in order",
             p("<strong>Masking</strong> &#9656; <strong>Color</strong> &#9656; <strong>Light &amp; Glow</strong> "
               "&#9656; <strong>Capstone</strong>.  Two weeks each; about eight weeks for all four.  Only time "
               "for one?  Run Masking."), accent="orange", icon="&#128640;"),
        check("A student cut a dog out of a photo with the Eraser.  It looks great.  Problem?",
              "<strong>B.</strong>  It looks fine today... and on Thursday they'll want the tail back.  A mask "
              "hides the same pixels without deleting them.  Saving (C) doesn't help; a saved deletion is still "
              "a deletion.",
              ["No.  It looks great.", "Yes.  Those pixels are gone for good.", "Only if they forgot to save."]),
        min=340),
    credit(),
]))

# ---------------------------------------------------------------- 2. The Big Five
def five(n, icon, name, what, say, watch, accent):
    return card(f"{n} ▸ {name}", p(what) + p(f"<strong>Say it:</strong> {say}") +
                f'<p style="margin:0;"><strong>Watch for:</strong> {watch}</p>', accent=accent, icon=icon)


big5 = page(**BASE, kicker="Instrument Panel", title="The Big Five", body="".join([
    tip("Photoshop's got about a million menus, champ.  You need five ideas.  "
        "The kids'll find the menus faster than you anyway... let 'em!"),
    video("Watch first: Photoshop in 6 minutes"),
    grid(
        five(1, "&#129374;", "Layers", "A stack of see-through sheets.  Every image, effect and word gets its own.",
             "&ldquo;One thing per layer, and give it a name.&rdquo;",
             "&ldquo;Layer 1 copy 3.&rdquo;  Default names mean they're lost in their own file.", "purple"),
        five(2, "&#127917;", "Layer masks", "A stencil on a layer.  <strong>Black hides.  White shows.</strong>  "
             "Nothing gets deleted.", "&ldquo;Black hides, white shows.&rdquo;  (Until they groan.  Then again.)",
             "missing pixels and no mask thumbnail.  That's the Eraser.", "red"),
        five(3, "&#127898;", "Adjustment layers", "A color or light change on its own layer.  Tweak it, mask it, "
             "switch it off any time.", "&ldquo;Use the half-black circle at the bottom of the Layers panel.&rdquo;",
             "color changes with no matching layer.  Image &gt; Adjustments baked it in.", "orange"),
        five(4, "&#10024;", "Blending modes", "How a layer mixes with what's under it.  <strong>Screen</strong> only "
             "lightens, and black vanishes; that's your glow button.", "&ldquo;Light is a blend mode, not white "
             "paint.&rdquo;", "a glow that looks like a white sticker.", "cyan"),
        five(5, "&#128230;", "Smart Objects", "A protective bubble.  Resize it all day and it never gets blurry.",
             "&ldquo;Convert to Smart Object, <em>then</em> resize.&rdquo;",
             "an image shrunk, enlarged, and now looks underwater.", "green"),
        card("Save, export, share", bullets([
            f"<strong>Save</strong> makes a <code>.psd</code>: the working file, every layer.  Keep it forever.",
            "<strong>Save As</strong> with <code>_V2</code> is a checkpoint before a big change.",
            "<strong>Export As</strong> makes a <code>.png</code> or <code>.jpg</code> for showing it off.",
            "<strong>Share the .psd with you</strong> to turn it in.  You open it and see every layer.  "
            "(Saved in the class folder they shared on day two?  It already is.)",
        ]), accent="blue", icon="&#128190;"),
        min=290),
    grid(
        check("On a layer mask, you paint with BLACK.  What happens?",
              "<strong>B.</strong>  You're painting on the stencil, not the picture, so nothing turns black (A), and "
              "nothing is deleted (C); paint white and it comes right back.",
              ["That part turns black.", "That part of the layer gets hidden.", "That part gets deleted."], " #1"),
        check("Whole photo warmer, but NOT the person's face.  Best move?",
              "<strong>B.</strong>  An adjustment layer plus a mask to keep it off the face.  A breaks the First "
              "Law twice in one move, which is honestly impressive.  C just fades the photo.",
              ["Image &gt; Adjustments &gt; Color Balance, then erase the face.",
               "Color Balance adjustment layer; paint black on its mask over the face.",
               "Duplicate the layer and lower its opacity."], " #2"),
        min=340),
]))

# ---------------------------------------------------------------- 3. Running a Project
running = page(**BASE, kicker="Flight Plan", title="Running a Project", body="".join([
    tip("Same two weeks, every project.  By project two, nobody asks &ldquo;what are we doing today?&rdquo;  "
        "Gee whiz, imagine that!"),
    grid(
        card("Week 1 ▸ Learn it", bullets([
            "<strong>Mon:</strong> 3 finished examples (great, okay, rough); students score them.  Demo #1, practice.",
            "<strong>Tue:</strong> Practice.  You walk the room reading Layers panels.",
            "<strong>Wed:</strong> A little design theory the project will use.",
            "<strong>Thu:</strong> Demo #2, practice.",
            "<strong>Fri:</strong> Demo #3, practice.  Students name the option they picked.",
        ]), accent="blue", icon="&#128216;"),
        card("Week 2 ▸ Prove it", bullets([
            "<strong>Mon&ndash;Tue:</strong> Build.  Tuesday, check every file against two checklist items.",
            "<strong>Wed:</strong> Quick status: <em>Done / Next / Stuck</em>.",
            "<strong>Thu:</strong> Share the file with a partner; show one decision and why.  Partner opens it, "
            "gives one compliment, one suggestion.",
            "<strong>Fri:</strong> Fix one thing.  Share the project file with you to turn it in.",
        ]), accent="green", icon="&#128215;"),
        min=340),
    grid(
        card("Demos: 3 ways, 15 min", p("Teach the <em>same</em> skill three ways across the week; whoever missed "
             "Monday gets two more shots.  Practice in a throwaway file... never the real project."),
             accent="purple", icon="&#127908;"),
        card("Choice, with guardrails", bullets([
            "6+ options, plus bring-your-own.",
            "<strong>Options change what they make, never the bar.</strong>",
            "Can't decide?  Hand them a category, not an option.",
            "Not a choice: the checklist, the due date, showing their work."]), accent="orange", icon="&#127922;"),
        card("Bending it to fit", bullets([
            "<strong>Under 5 days a week?</strong> Same order, over three weeks.",
            "<strong>Holiday in Week 2?</strong> Due date moves <em>earlier</em>.",
            "<strong>Already knows Photoshop?</strong> Same bar, harder option."]), accent="red", icon="&#128295;"),
        min=260),
    grid(
        check("Why do students score three examples on Monday, BEFORE you teach?",
              "<strong>B.</strong>  If they can see great vs. rough on Monday, they can aim for great by Friday.  "
              "(A is tempting on a slow-login day... I get it.)",
              ["Fills time while computers boot.", "So they know what &ldquo;good&rdquo; looks like first.",
               "So there's an early grade in the book."], " #1"),
        check("A student picks an option because it &ldquo;looks easiest.&rdquo;  What needs fixing?",
              "<strong>B.</strong>  Every option should clear the same bar.  If one looks easier, it's broken; "
              "adjust it.", ["The student.", "The option.", "Nothing.  Choice is choice."], " #2"),
        min=340),
]))

# ---------------------------------------------------------------- 4. The Four Projects
def proj(num, accent, icon, title, tagline, done, demos, menu, q, a):
    inner = (p(f"<em>{tagline}</em>") + p("<strong>Done means:</strong>") + checklist(done) +
             p(f"<strong>Your three demos:</strong> {demos}") + p(f"<strong>The menu:</strong> {menu}") +
             check(q, a))
    return mission(f"MISSION {num}", title, inner, accent=accent, icon=icon)


projects = page(**BASE, kicker="Mission Files", title="The Four Projects", body="".join([
    tip("Pick a mission, sport!  Click a card to open it: the checklist, your three demos, and the menu kids "
        "choose from.  Every project, every time: <strong>file shared with you, layers named, a _V2 saved, "
        "and outside images credited.</strong>"),
    grid(
        proj("01", "purple", "&#127917;", "Masking: put things where they don't belong",
             "Combine images so cleanly nobody can tell... and keep every edit reversible.",
             ["3 to 5 images combined", "At least 4 layer masks", "The Eraser used ZERO times",
              "Clean edges at 100% zoom (no halo)", "At least 1 Smart Object"],
             "selection &rarr; mask &middot; refine the mask with a brush &middot; Smart Objects and <code>_V2</code>",
             "a place you've never been &middot; swap a sky &middot; a product on a new background &middot; an "
             "animal made of two animals &middot; a band poster &middot; erase a photobomber &middot; <em>bring your own</em>",
             "At 100% zoom there's a thin white outline around the cutout.  Bar met?",
             "Not yet.  That halo is leftover background.  Paint the mask edge with a small, soft black brush, or "
             "use <strong>Select and Mask</strong>.  Close... but the bar says clean at 100%."),
        proj("02", "orange", "&#127912;", "Color: make it FEEL like something",
             "Same photo, new mood... and they named the mood before they started.",
             ["3+ adjustment layers: one light (Curves/Levels), one color (Hue/Sat or Color Balance)",
              "At least 2 of them masked", "Nothing baked into pixels", "Reads as the exact mood they named",
              "No crushed shadows or blown highlights"],
             "light first (Curves, histogram) &middot; shift color without orange skin &middot; mood in one move "
             "(Gradient Map, masked adjustment)",
             "morning AND midnight &middot; make it the 80s &middot; fake golden hour &middot; horror, then comedy "
             "&middot; two posters, one movie &middot; an album cover &middot; <em>bring your own</em>",
             "The histogram is piled against the far RIGHT side.  What's that tell you?",
             "Blown highlights: those areas are pure white, no detail.  Pull the top of the Curve down a little.  "
             "(Piled LEFT means crushed shadows.)"),
        proj("03", "cyan", "&#10024;", "Light &amp; Glow: make it belong",
             "Light tells the viewer where to look.  Light that ignores its source... just looks fake.",
             ["3+ light layers using blend modes, each on its own layer",
              "2+ glows masked, each traceable to a source", "The scene picks up the light's color",
              "ONE light is the boss; the rest are half as bright or less"],
             "guided glow on a starter image &middot; glow from nothing (brush, blur, Screen, mask) &middot; make "
             "the scene react, plus a rim light",
             "a neon sign &middot; phone glow in the dark &middot; a magic effect &middot; headlights or a campfire "
             "&middot; relight as sunset &middot; a rim-lit product &middot; <em>bring your own</em>",
             "Lamp on the LEFT.  The glow lights the RIGHT side of the face.  Your one question?",
             "&ldquo;Where's that light coming from?&rdquo;  Then stop talking.  They'll find it."),
        proj("04", "green", "&#127942;", "Capstone: everything, one message",
             "A brand-new design with type, masking, color AND light.  Pitched first: what, why it's new, who "
             "it's for, the look, the skills.  You reply <em>Approved</em> or <em>Revise</em>.",
             ["Brand-new file (not last project with a hat on)", "Tracking and leading changed from defaults",
              "2 typefaces, max", "4+ masks, 3+ adjustment layers, 2+ light layers",
              "They can say what a viewer sees 1st, 2nd, 3rd"],
             "type that behaves (tracking, kerning, leading) &middot; subtle layer styles, image clipped into text "
             "&middot; building a reading order",
             "a poster of someone they admire &middot; album cover &middot; trading card &middot; coloring sheet "
             "&middot; sticker sheet &middot; book or game cover &middot; event poster &middot; <em>bring your own</em>",
             "Four different fonts, and it &ldquo;looks cool.&rdquo;  Bar met?",
             "No.  Two, max.  Keep the font doing the most work plus one partner.  (It hurts.  It always hurts.)"),
        min=420, align="start"),
    p("&#128229; <strong>Supply drop</strong> <em>[coming]</em>: student project cards &middot; choice menus "
      "&middot; a licensed starter kit for Mission 03 &middot; great / okay / rough example sets", size="0.95em"),
]))

# ---------------------------------------------------------------- 5. Help
help_page = page(**BASE, kicker="Distress Signals", kicker_color="#FF6B6B", title="Help!  It's Doing a Thing",
                 body="".join([
    tip("A hand goes up: &ldquo;It's doing a thing.&rdquo;  First move, every time: <strong>check which layer is "
        "highlighted.</strong>  That's the answer about half the time, sport!"),
    grid(
        table(["The student says&hellip;", "Do this"], [
            ["&ldquo;My whole layer vanished when I added a mask!&rdquo;",
             "Mask is all black.  Click it, press <strong>Ctrl + I</strong> (Cmd + I) to flip it."],
            ["&ldquo;It's painting COLOR on my mask.&rdquo;", "They're on the picture.  Undo, click the mask thumbnail, paint again."],
            ["&ldquo;Nothing happens.&rdquo;", "Wrong layer, or hidden, or locked.  Check highlight, eye, lock."],
            ["&ldquo;It says the layer is locked.&rdquo;", "Background starts locked.  Click the little lock."],
            ["&ldquo;My adjustment changed EVERYTHING.&rdquo;",
             "Hold <strong>Alt</strong> (Option), hover the line between layers, click.  Now it hits one layer."],
            ["&ldquo;My picture got blurry.&rdquo;", "Re-place the original, Smart Object it, <em>then</em> resize."],
            ["&ldquo;My panels are gone.&rdquo;", "<strong>Window &gt; Workspace &gt; Reset Essentials.</strong>"],
        ]),
        console_table(["PRESS", "TO"], [
            ["<strong>B</strong> / <strong>V</strong>", "Brush / Move"],
            ["<strong>W</strong> (Shift+W cycles)", "Selection tools"],
            ["<strong>D</strong>, then <strong>X</strong>", "Black/white, then swap"],
            ["<strong>[</strong> <strong>]</strong>", "Smaller / bigger brush"],
            ["<strong>Ctrl+J</strong>", "Duplicate layer"],
            ["<strong>Ctrl+T</strong>", "Resize / rotate"],
            ["<strong>Ctrl+Z</strong> / <strong>+Shift</strong>", "Undo (keep going) / Redo"],
            ["<strong>Ctrl+I</strong> on mask", "Flip the mask"],
            ["<strong>Alt-click</strong> mask", "See just the mask"],
            ["<strong>Shift-click</strong> mask", "Mask off/on (red X)"],
            ["<em>Mac:</em>", "Ctrl&rarr;Cmd, Alt&rarr;Option"],
        ]),
        min=380, align="start"),
    grid(
        check("Last day.  &ldquo;Which file do I turn in?&rdquo;",
              "<strong>B.</strong>  The .psd is the real work; you open it and see every layer and mask.  A .png "
              "(A) is a photo of the work, not the work.  And sharing is a skill they'll use with every partner "
              "and client.  (C happens... gently redirect.)",
              ["Just an exported .png.", "Share the .psd project file with you.", "A screenshot of the screen."]),
        card("Heading toward certification?",
             p("The exam: <strong>Adobe Certified Professional: Visual Design Using Adobe Photoshop</strong>.  "
               "50 minutes; part questions, part live tasks.") +
             p("These missions cover layers, masks and adjustments well.  Gaps to fill: <strong>retouching</strong> "
               "(Spot Healing, Content-Aware Fill), <strong>vector shapes</strong>, <strong>document setup</strong>, "
               "<strong>file formats</strong>.  The Certification Prep module covers them."),
             accent="purple", icon="&#127891;"),
        min=340),
    p("Shortcuts are Photoshop's defaults; a school can customize them (Edit &gt; Keyboard Shortcuts).",
      color="#B8C2CC", size="0.85em"),
]))

write(HERE, [("01-start-here.html", start), ("02-the-big-five.html", big5),
             ("03-running-a-project.html", running), ("04-the-four-projects.html", projects),
             ("05-help.html", help_page)])
