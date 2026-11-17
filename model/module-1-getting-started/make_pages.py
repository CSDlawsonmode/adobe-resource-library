"""Build the Getting Started module's Canvas pages.   python model/module-1-getting-started/make_pages.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from kit import (bullets, card, check, checklist, console, console_table, credit, grid, h3, mission, p, page,
                 redbox, student_box, table, tip, video, write)

HERE = pathlib.Path(__file__).parent
BASE = dict(label="Liftoff: The First Two Days", banner="banner-getting-started.svg",
            banner_alt="Liftoff: the first two days")

# ---------------------------------------------------------------- 1. Start Here
start = page(**BASE, first=True, kicker="Mission Briefing", title="Getting Started: Start Here", body="".join([
    tip("Hey there, sport!  The first two days aren't about Photoshop.  Get every kid signed in, organized, and "
        "emailing you like a pro... and the rest of the semester runs on rails."),
    grid(
        redbox("THE FIRST LAW OF DAY ONE", "Every student signed in before the bell.",
               "Culture first, then logins.  But the logins aren't optional; a kid who can't sign in today "
               "loses tomorrow."),
        table(["I need to&hellip;", "Go to"], [
            ["Know what students sign into", "<strong>Creative Cloud in 5 Minutes</strong>"],
            ["Plan day one and day two", "<strong>The First Two Days</strong>"],
            ["Grab lessons to paste in", "<strong>Lesson Kits</strong>"],
            ["Fix a kid who can't get in", "<strong>Help! I Can't Get In</strong>"],
        ]), min=340),
    grid(
        card("The two-day mission",
             p("<strong>Day 1:</strong> the room, then the sign-in.") +
             p("<strong>Day 2:</strong> a folder system they'll use all year, shared with you, and their first "
               "professional email.") +
             p("Two class periods.  No Adobe experience needed."), accent="orange", icon="&#128640;"),
        check("Minute 35 of day one, and you're behind.  What do you cut?",
              "<strong>B.</strong>  Procedures reteach themselves through repetition; nobody remembers the "
              "pencil-sharpener speech anyway.  The sign-in (A) can't wait; tomorrow needs working accounts.  And "
              "the welcome (C) IS day one... it's the part they'll remember.",
              ["The sign-in check.", "Some of your procedures talk.", "The welcome and expectations."]),
        min=340),
    credit(),
]))

# ---------------------------------------------------------------- 2. Creative Cloud in 5 Minutes
cc = page(**BASE, kicker="Instrument Panel", title="Creative Cloud in 5 Minutes", body="".join([
    tip("You don't need to know Photoshop yet, champ.  Just three things: what they sign into, which app does "
        "what, and where the files go."),
    video("Watch: Day One in an Adobe Lab (5 minutes)"),
    grid(
        card("What they sign into", p("<strong>Creative Cloud</strong> is the account, plus a little launcher that "
             "opens everything else.  Usually the district assigns licenses, and students sign in with their "
             "<strong>school</strong> Google or Microsoft account.  No personal Adobe accounts."),
             accent="purple", icon="&#128273;"),
        redbox("BEFORE DAY ONE, FIND OUT", "", checklist=[
            "Who manages Adobe licenses (get their email)", "Google or Microsoft sign-in?",
            "Apps installed and updated in your lab?", "Can YOU sign in on a student machine?"]),
        card("Which app does what", bullets([
            "<strong>Photoshop:</strong> photos and pixels.", "<strong>Illustrator:</strong> logos and anything "
            "that has to scale.", "<strong>Premiere Pro:</strong> video."]), accent="orange", icon="&#129520;"),
        card("Where the files go", p("School cloud storage (Google Drive or OneDrive), never a lab computer's "
             "desktop.  Lab machines get wiped.  Kids change seats.  The cloud doesn't care."),
             accent="green", icon="&#9729;"),
        min=260),
    grid(
        console_table(["FILE", "WHAT IT IS"], [
            ["<strong>.psd</strong>", "Photoshop working file.  Keeps layers."],
            ["<strong>.ai</strong>", "Illustrator working file."],
            ["<strong>.prproj</strong>", "Premiere project.  POINTS to clips; doesn't hold them."],
            ["<strong>.jpg/.png</strong>", "Finished images.  .png can be see-through."],
            ["<strong>.mp4</strong>", "Finished video."],
        ]),
        check("Friday a student saves to the desktop of computer 14.  Monday they sit at computer 9.  Where's the "
              "project?",
              "<strong>B.</strong>  The desktop belongs to the machine, not the kid.  That's why day two builds "
              "folders in cloud storage.",
              ["On computer 9; it follows their login.", "Stuck on 14... if the weekend wipe missed it.",
               "In the cloud; it syncs on its own."], " #1"),
        check("Clips moved to a new folder; now Premiere shows red &ldquo;media offline.&rdquo;  Which file type "
              "explains it?",
              "<strong>.prproj.</strong>  It only points to where the clips were.  Pick the folder BEFORE "
              "importing, and never move the clips afterward.", label=" #2"),
        min=300),
]))

# ---------------------------------------------------------------- 3. The First Two Days
days = page(**BASE, kicker="Flight Plan", title="The First Two Days", body="".join([
    tip("Times are for a 50-minute class.  Stretch 'em or squeeze 'em to fit yours, sport!"),
    grid(
        card("Pre-flight checklist", checklist([
            "Sign in to Creative Cloud yourself on a student machine",
            "Leave ONE machine signed out, for the demo",
            "Draft your course email; don't send it yet",
            "Something to write names on: every kid who can't sign in"]), accent="blue", icon="&#128203;"),
        card("Day 1 ▸ The room, then the sign-in", bullets([
            "<strong>0&ndash;8:</strong> Welcome, seats, roll.",
            "<strong>8&ndash;18:</strong> Expectations both ways.  <em>You go first.</em>",
            "<strong>18&ndash;30:</strong> What we'll make (say the app names), grading, how the room runs.",
            "<strong>30&ndash;42:</strong> <strong>Sign-in check, everyone.</strong>  Demo on the signed-out "
            "machine; write down every name that fails.",
            "<strong>42&ndash;50:</strong> Send your course email live.  &ldquo;Tomorrow: your first "
            "professional email.&rdquo;"]), accent="purple", icon="&#128216;"),
        card("Day 2 ▸ Folders, sharing, first email", bullets([
            "<strong>0&ndash;5:</strong> Fix yesterday's sign-in failures.",
            "<strong>5&ndash;25:</strong> <strong>Lesson 1:</strong> folders together, screens visible, then "
            "share the class folder with you.",
            "<strong>25&ndash;35:</strong> <strong>Lesson 2:</strong> bad email first, deadpan; then type a good "
            "one live.",
            "<strong>35&ndash;48:</strong> Students send Getting To Know You.",
            "<strong>48&ndash;50:</strong> Confirm arrivals; fix stragglers."]), accent="green", icon="&#128215;"),
        min=280),
    grid(
        card("Bending it to fit", bullets([
            "<strong>Block schedule?</strong> Both days, one block.",
            "<strong>Licenses not ready?</strong> Run Day 2 first.",
            "<strong>No student email?</strong> LMS messages, same format.",
            "<strong>Joins in week three?</strong> Folders, sign-in, email."]), accent="red", icon="&#128295;"),
        check("Day 2 writing time.  When do you check subject lines?",
              "<strong>B.</strong>  One lap before send saves a week of mislabeled email.  A means 30 correction "
              "replies; C means the bad habit got a week of practice.",
              ["After they send.", "Before they hit send.", "Friday, when grading."], " #1"),
        check("Why do YOU go first with expectations?",
              "Because a deal where the adult commits first feels like a deal, not a rule list.  Keep your "
              "promises specific enough that they can hold you to them in week three.  They will.", label=" #2"),
        min=280),
]))

# ---------------------------------------------------------------- 4. Lesson Kits
lesson1 = (
    p("<em>&ldquo;I lost my file&rdquo; is the most expensive sentence in media production.  This lesson "
      "retires it.</em>") +
    p("<strong>Done means:</strong>") +
    checklist(["Archive folder, plus a folder for this school year", "Four project folders, spelled exactly",
               "Three theme images, renamed", "Class folder shared with you",
               "A file shared with a partner, and theirs opened"]) +
    student_box("COPY TO STUDENTS", '<ol style="margin:0;padding-left:22px;">' + "".join(f"<li>{s}</li>" for s in [
        "At the top of your school Drive, make a folder named <code>-- Archive --</code>.  Move everything "
        "already there into it.  Nothing gets deleted.",
        "Make a folder for this school year, like <code>2026-27</code>.",
        "Inside it, a folder for each class.  Real names: &ldquo;Media Design,&rdquo; not &ldquo;3rd hr.&rdquo;",
        "Inside this class's folder: <code>01_Photoshop</code> <code>02_Illustrator</code> <code>03_Video</code> "
        "<code>04_Resources</code>",
        "Pick a semester theme: a game, team, band, animal... something you like.",
        "Save three theme images into <code>04_Resources</code>, named like <code>Wolves_01.jpg</code>.",
        "Share your class folder with your teacher.  Every project in it is now turned in automatically.",
        "Share one image with a partner.  Open the one they shared with you.",
    ]) + "</ol>") +
    p("<strong>Why share on day two?</strong> Students turn in the real project file, so you can open it and see "
      "the layers.  And partner sharing is practice for peer review... and every job they'll ever have.") +
    check("Which name follows the convention?",
          "<strong>C.</strong>  A is a file nobody finds again.  B is close, but spaces break things in some apps "
          "and links.", ["download (3).jpg", "Wolves 01.jpg", "Wolves_01.jpg"])
)

lesson2 = (
    p("<em>A professional email answers the reader's questions before they have to ask.</em>") +
    p("<strong>Done means:</strong> exact subject line, a greeting, a body that answers everything, a sign-off "
      "with name and class period.") +
    grid(
        student_box("EMAIL 1 (SHOW FIRST)", '<p style="margin:0;font-family:\'Courier New\',monospace;">Subject: '
                    'hey<br><br>yo so my thing isnt working idk what happened it just wont do the thing<br>can u '
                    'help</p>'),
        student_box("EMAIL 2", '<p style="margin:0;font-family:\'Courier New\',monospace;">Subject: [P3 Media '
                    'Design] - Unit 3 Status<br><br>Hello, Ms. Rivera,<br><br>Done: three adjustment layers.<br>'
                    'Next: mask the grade off the face.<br>Stuck: the mask hides the whole layer.  Could you look '
                    'tomorrow?<br><br>Thanks,<br>First Last, Period 3</p>'),
        min=220) +
    p("<strong>Ask:</strong> 40 emails today... which gets answered first?  Email 2 isn't fancy; it's useful.  "
      "<strong>Subject format:</strong> <code>[P# Course Name] - Task Name</code>") +
    student_box("COPY TO STUDENTS: GETTING TO KNOW YOU",
                p("Subject: <code>[P# Course Name] - Getting To Know You</code>.  Number your answers.  Write in "
                  "whatever language you're most comfortable in.") +
                '<ol style="margin:0;padding-left:22px;">' + "".join(f"<li>{q}</li>" for q in [
                    "What language do you prefer?", "Rate yourself 1&ndash;3: I keep my files organized.",
                    "Rate yourself 1&ndash;3: I can figure out new software on my own.",
                    "Creative apps you've used?  &ldquo;None yet&rdquo; is fine.",
                    "Computer at home?  (yes / sometimes / no)", "What would you be excited to make?",
                    "An artist, brand, game or creator whose style you like?",
                    "Anything that would help you succeed here?"]) + "</ol>") +
    p("<strong>Tip:</strong> the 1&ndash;3 ratings are your baseline; ask again at the end.  Questions 6 and 7 "
      "hand you project ideas all semester.") +
    check("A student writes the whole email in Spanish, with the right subject, greeting and sign-off.  Count it?",
          "Yes, every word.  The format is the skill; the language is theirs.  Reply on the same thread with a "
          "translation tool.")
)

kits = page(**BASE, kicker="Mission Files", title="Lesson Kits", body="".join([
    tip("Two lessons, ready to launch!  Click one open.  The white boxes talk to students... copy 'em straight "
        "into your LMS."),
    grid(
        mission("LESSON 01", "Set Up Your Workspace", lesson1, accent="purple", icon="&#128193;"),
        mission("LESSON 02", "The Professional Email", lesson2, accent="orange", icon="&#9993;"),
        min=420, align="start"),
    p("&#128229; <strong>Supply drop</strong> <em>[coming]</em>: workspace handout &middot; Two Emails handout "
      "&middot; subject-line wall poster &middot; Day 1 welcome slides", size="0.95em"),
]))

# ---------------------------------------------------------------- 5. Help
help_page = page(**BASE, kicker="Distress Signals", kicker_color="#FF6B6B", title="Help!  I Can't Get In",
                 body="".join([
    tip("Sign-in trouble on day one is as normal as rain, sport.  First question, every time: are they using "
        "their <strong>SCHOOL</strong> account?"),
    grid(
        table(["The student says&hellip;", "Do this"], [
            ["&ldquo;It's asking which account.&rdquo;", "They made a personal Adobe account once.  Pick "
             "<strong>school</strong>.  Every time."],
            ["&ldquo;It says trial,&rdquo; or won't open.", "No license yet.  Send the name to your Adobe admin; "
             "they do folders and email meanwhile."],
            ["&ldquo;Sign-in keeps looping.&rdquo;", "Sign out of every browser account; retry with only the "
             "school one.  Still looping?  IT."],
            ["&ldquo;But I signed in yesterday!&rdquo;", "Normal on lab machines.  Sign in again; cloud files are "
             "fine."],
            ["&ldquo;I forgot my password.&rdquo;", "It's the school password, not Adobe's.  District reset "
             "process."],
        ]),
        "<div>" + console([
            '<span style="color:#FFC857;"><strong>FILE NAMING, IN FOUR RULES</strong></span>',
            '<span style="color:#FFC857;">01</span> NO SPACES.  Wolves_01.jpg',
            '<span style="color:#FFC857;">02</span> LEADING ZEROS: 01, 02... 10',
            '<span style="color:#FFC857;">03</span> NAME IT SO A STRANGER COULD FIND IT',
            '<span style="color:#FFC857;">04</span> SHARE THE PROJECT FILE, NOT A PICTURE OF IT']) +
        '<div style="height:14px;"></div>' +
        card("Multilingual learners", bullets([
            "They can write in their most comfortable language; reply with a translation tool.",
            "Same format in every language: subject, greeting, body, sign-off.",
            "Write the arrangement down so it carries all course."]), accent="cyan", icon="&#127760;") + "</div>",
        min=380, align="start"),
    check("Minute 38 of day one.  Six students still can't get in.  Your move?",
          "<strong>B.</strong>  One list gets fixed faster than six tickets, and nobody sits idle.  C sends the "
          "problem home, where nobody can see it... and some kids don't have a computer there.",
          ["Six separate IT tickets, right now.",
           "Write down names and errors, start them on folders, send IT one email with the list.",
           "Tell them to try again at home tonight."]),
]))

write(HERE, [("01-start-here.html", start), ("02-creative-cloud.html", cc),
             ("03-the-first-two-days.html", days), ("04-lesson-kits.html", kits), ("05-help.html", help_page)])
