# AGENTS.md

## Cursor Cloud specific instructions

This repo is a **static site** — a searchable catalog (`index.html`) plus ~140+
self-contained reveal.js teaching decks (`*.html`). There is no backend, package
manager, build step, or test suite. Do not add build tooling or new CDN
libraries (fonts named by a chosen visual direction are allowed). See
[`00-shared-spec.md`](00-shared-spec.md).

**Default delivery is an explainer-style tutorial**, not a widget-heavy workshop.
Do not add interactives, activities, a quiz, speaker notes, or a colour system
until the author has answered the questions in [Ask before you build](#ask-before-you-build).

### Running it

- Serve the folder over HTTP and open in a browser, e.g. `python3 -m http.server 8080`
  then `http://localhost:8080/index.html`. Use HTTP (not `file://`) so relative
  deck links and the Mermaid ES module in
  `network-diagram-ocn-level2-presentation.html` behave correctly.
- There is nothing to install or build; editing a `.html` file and refreshing
  the browser is the whole dev loop.

### Gotchas

- **Outbound HTTPS is required at runtime.** Decks pull reveal.js, highlight.js,
  Font Awesome, Google Fonts, and Mermaid from CDNs (jsdelivr / cdnjs /
  googleapis). With no network the decks render unstyled.
- Deck files must never be renamed — `index.html` links are hand-maintained.

### Read these first

1. This file (defaults and questions).
2. [`00-shared-spec.md`](00-shared-spec.md) — constraints, explainer spine,
   optional activity/quiz slots, photos.
3. Any **course specs** in this repo or a sibling workspace repo (see
   [Course specs](#course-specs)).
4. A visual direction file (`1a-ledger.md` … `1e-studio.md`) only after colour
   and layout are agreed.
5. [`PRESENTATION-UPGRADE-PLAN.md`](PRESENTATION-UPGRADE-PLAN.md) is **legacy
   inventory** (deck list, widget recipes, claim checkboxes). It is not the
   slide recipe and not a reason to add widgets.

---

## Ask before you build

Ask these questions **before** creating or rebuilding a tutorial presentation.
If the author has not answered, ask — do not assume “yes” because older decks
or the upgrade plan include them.

1. **Widgets?** Default **no**. “Do you want interactive widgets (drag-and-drop,
   simulators, click-to-reveal boards, and so on) in this tutorial? Default is
   an explainer with no widgets.”
2. **Activities and quiz?** Default **no**. “Do you need in-deck activities
   (tasks on a slide) and/or a scored quiz? Default is explainer only: concept,
   example, takeaways, close.”
3. **Colour?** No default until they pick. “Should this use **white text on a
   black background**, or **college brand colours** (orange `#F7931E`, purple
   `#8A2BE2`, teal `#00BDA5`)?”
4. **Speaker notes?** Default **no**. “Do you need `aside.notes` on slides for
   presenter view (S key)?”

Do not invent a third colour system unless they name one. If they want both a
dark classroom look and brand accents, confirm that explicitly (for example
white-on-black with brand used only for rules, labels, and highlights).

---

## Course specs

Content must be **relatable to any course spec provided in the repo** (this
workspace, including sibling folders such as `tutorials`).

Before writing slides:

1. Search for spec files: unit outlines, assessment criteria, learning outcomes,
   schemes of work, `instructions/`, `*spec*`, qualification markdown, PDFs,
   and [`PRESENTATION-IDEAS.md`](PRESENTATION-IDEAS.md) “Assessment fit” notes.
2. Map each teaching slide to a named outcome, assessment criterion, or unit
   heading from those files. Use the spec’s wording where it helps learners and
   assessors recognise the work.
3. Prefer classroom and workplace examples that match the spec’s level and
   context (for this library that is often OCN NI Level 2 IT, but **the files
   in the repo win** if they describe a different course).
4. If no spec is present, say so, then write an explainer that still uses
   concrete, checkable language (what the learner can do, not a slogan). Do not
   pad with career-pathways or generic “Thank You” slides.

---

## Teaching structure

### Default — explainer tutorial

Use this spine unless the author asked for activities or a quiz.

| # | Slide |
| --- | --- |
| 1 | Title — topic, level/unit from the spec if known |
| 2 | The hook — one real consequence of getting this wrong |
| 3 | Objectives — max 4, verb-led, mapped to the spec |
| 4 | Core concept — the diagram or ladder the deck hangs on |
| 5–7 | One slide per part of the concept |
| 8 | Worked example — named, relatable to the spec’s setting |
| 9 | Trade-offs or limits |
| 10 | Common faults — symptom → likely cause → fix (table, not a widget) |
| 11 | Key takeaways — max 4 |
| 12 | Close — one instruction for what to do next |

Cut unless the topic truly needs them: “How to use this deck”, keyboard hints,
glossary slide, deck map, career pathways, stats-bar, “Thank You”.

Searchable jargon, if needed, is a `?` overlay, not a slide.

### If they asked for activities

Insert after the concept parts: **Activity 1** (signature task), keep the
worked example, then **Activity 2** (applied scenario). Keep activities as
plain steps and success criteria unless they also asked for widgets.

### If they asked for a quiz

Add a short scored quiz (4–6 questions) and a results slide that says what a
wrong answer means. Skip quiz and results when they said no.

### If they asked for widgets

Follow widget conventions in [`00-shared-spec.md`](00-shared-spec.md):
`Reveal.on('ready')`, click/tap/keyboard, `aria-live="polite"` on scores, wrong
answers explain **why**. Do not copy widgets from the upgrade-plan library
“because other decks have them”.

Broadcast direction (`1c`) may use more slides (one idea per slide). Other
directions stay on the explainer spine or the agreed activity/quiz extras.

---

## Must / must not

**Must**

- Never rename a deck file.
- Min type size **24px** at 1920×1080; reveal.js `width: 1920, height: 1080`,
  `margin: 0.04`.
- `.back-to-index` pill and `.site-credit` line.
- Absolute `px` type, not `em` relative to reveal’s root.
- Tie examples and objectives to provided course specs.
- Apply the colour choice they confirmed (white-on-black **or** brand triad).

**Must not**

- Add widgets, activities, quiz, or speaker notes unless they asked.
- `.animated-gradient` headings.
- `backdrop-filter` glass cards as the default container.
- Decorative Font Awesome that repeats the heading word.
- `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` as the universal layout.
- Generated SVG illustration; photos are author-supplied plates when used.
- Treat particle canvas or a 26–34 slide count as required.
- Add new CDNs except fonts the chosen direction already names.

---

## Verifying a change

Open the affected deck over HTTP, check the browser console is clean, and
confirm the explainer spine (or the extras they requested) with no cut-list
slides.

Also check, **when they asked for them**:

- widgets: exercise each one
- quiz: run through to results
- speaker notes: press **S**
- colour: white-on-black **or** brand, matching the answer (and scheme toggle
  only if they asked for both)

### Related repo

The sibling `INTRO-TO-WORLDSKILLS` repo can reuse this library’s chrome
(`.back-to-index`, `.site-credit`) and, when requested, brand colours and
widget patterns. Do not assume that repo wants widgets, a quiz, or speaker
notes either — ask the same questions.
