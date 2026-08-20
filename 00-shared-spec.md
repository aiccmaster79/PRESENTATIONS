# OCN NI deck design directions — shared spec

Source repo: `aiccmaster79/PRESENTATIONS` · reference deck: `saas-paas-iaas-comparison-ocn-level2-presentation.html` (#72)
Live exploration: `Deck Design Directions.dc.html` (ids `1a`–`1e`)

Agents: read [`AGENTS.md`](AGENTS.md) first. Default is an **explainer-style
tutorial**. Ask before adding widgets, activities, a quiz, speaker notes, or a
colour system. Map content to any course spec files in the repo.

## Purpose

Five candidate visual systems for the teaching library. Each can use college
brand colours when that is the chosen palette, keeps a spec-led content model,
and replaces the current "glass card + Font Awesome icon + auto-fit grid"
treatment with a system that has an actual point of view.

This spine **supersedes** section 2 of `PRESENTATION-UPGRADE-PLAN.md` (the
26–34 slide blueprint) and that file’s scale “definition of done”. The upgrade
plan remains inventory: deck list, widget recipes, claim workflow.

## What is fixed across all five

| Constraint | Value |
| --- | --- |
| Brand orange (when brand palette is chosen) | `#F7931E` |
| Brand purple (when brand palette is chosen) | `#8A2BE2` |
| Brand teal (when brand palette is chosen) | `#00BDA5` |
| White-on-black (when that palette is chosen) | ink `#ffffff` / near-white on `#000000` or `#0e0e10` |
| Deck size | reveal.js `width: 1920, height: 1080`, `margin: 0.04` |
| Engine | reveal.js 4.6.0, no build step, no new CDN dependencies beyond fonts |
| Chrome | `.back-to-index` pill, `.site-credit` line |
| Speaker notes | only if the author asked — then `aside.notes` on every slide |
| Filenames | never renamed — `index.html` links are hand-maintained |
| Min type size | 24px at 1920×1080. Nothing smaller, ever. |
| Schemes | ship a toggle only if they asked for both looks; otherwise one palette |
| Photos | author-supplied images, never generated SVG illustration |
| Content | examples and objectives relatable to course specs found in the repo |

## What every direction must drop

- `.animated-gradient` clipped-text headings (8s infinite animation on every h2).
- `backdrop-filter` glass cards used as the default container for all content.
- Decorative Font Awesome icons that repeat the adjacent word ("Objectives 🎯").
- `font-size` in `em` relative to reveal's root scale — use absolute px at 1920×1080.
- `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` as the universal layout.
- The 5-slide filler tail (Career Pathways / stats-bar / Next Steps / Thank You) unless
  the content is genuinely per-topic.

## Canonical teaching structure

The old sequence front-loads meta ("How to use this deck") and back-loads filler.
**Default is explainer-style** — no widgets, activities, or quiz until the author
asks for them ([`AGENTS.md`](AGENTS.md)).

### Explainer spine (default)

| # | Slide |
| --- | --- |
| 1 | Title — topic, level/unit from the spec if known |
| 2 | The hook — one real consequence of getting this wrong |
| 3 | Objectives — max 4, verb-led, mapped to the course spec |
| 4 | Core concept — the diagram or ladder the deck hangs on |
| 5–7 | One slide per part of the concept |
| 8 | Worked example — named, relatable to the spec’s setting |
| 9 | Trade-offs or limits |
| 10 | Common faults — symptom → likely cause → fix |
| 11 | Key takeaways — max 4 |
| 12 | Close — one instruction for what to do next |

### Optional extras (only if asked)

- **Activities:** after concept parts, Activity 1 (signature task) and Activity 2
  (applied scenario). Use plain steps unless they also asked for widgets.
- **Quiz:** 4–6 scored questions plus a results slide that says what a wrong
  answer means.
- **Case study:** real, named, two slides max — add when the spec or the author
  wants a workplace story; otherwise the worked example is enough.
- **Widgets:** the direction’s signature widget on an activity slide. Never the
  default.
- **Speaker notes:** `aside.notes` on every slide only if requested.

Broadcast (`1c`) may exceed this count (one idea per slide). Other directions
stay on the explainer spine plus agreed extras.

Cut: "How to use this deck", keyboard hints slide, glossary slide (make it a `?`
overlay), deck map, career pathways, stats-bar, "Thank You".

### Applying this to an existing deck

Map old slides onto the explainer spine, delete cut-list slides, keep topic
content that still teaches the spec. Do not add widgets, quiz, or notes unless
asked. Do not rename the file. Bump `index.html` `data-updated` only when a
deck is actually rebuilt.

## Course specs

Search this repo and sibling workspace repos for unit outlines, assessment
criteria, learning outcomes, and related markdown/PDFs. Map objectives and
examples to those headings. Files in the repo override any assumed OCN NI
Level 2 default. If none are found, say so and keep language concrete and
checkable.

## Colour

Ask: **white text on black** or **college brand colours** (see [`AGENTS.md`](AGENTS.md)).
Do not ship both until they ask for a toggle.

College mark files: [`logos/src_logo.svg`](logos/src_logo.svg) (light grounds),
[`logos/src_logo_on_black.svg`](logos/src_logo_on_black.svg) (dark grounds),
[`logos/src_logo.png`](logos/src_logo.png), [`logos/src_logo_mobile.svg`](logos/src_logo_mobile.svg).

### Theme toggle (only if they asked for both looks)

One `data-scheme` attribute on `<html>`; every colour in the deck reads from CSS custom
properties defined twice. No per-element overrides.

```html
<button class="scheme-toggle" type="button" aria-pressed="false">Light</button>
```

```css
:root { /* dark tokens */ }
:root[data-scheme="light"] { /* light tokens */ }
```

```js
const t = document.querySelector('.scheme-toggle');
const set = v => {
  document.documentElement.dataset.scheme = v;
  t.setAttribute('aria-pressed', v === 'light');
  t.textContent = v === 'light' ? 'Dark' : 'Light';
  localStorage.setItem('ocn-scheme', v);
};
set(localStorage.getItem('ocn-scheme') || 'dark');
t.addEventListener('click', () => set(document.documentElement.dataset.scheme === 'light' ? 'dark' : 'light'));
```

Token names used by all five specs:

`--bg` `--surface` `--ink` `--ink-dim` `--ink-faint` `--rule` `--you` `--provider` `--accent`

## Photo slots

Every direction has named image regions. Author them as a plain wrapper with a fixed
aspect and `object-fit: cover`:

```html
<figure class="plate">
  <img src="img/72-comms-room.jpg" alt="Rack of network switches in a school comms room">
  <figcaption>Fig. 4 — legacy exam VM, campus comms room</figcaption>
</figure>
```

Store images at `img/<deck-number>-<slug>.jpg`, max 1920px wide, ≤300KB. Every image gets
a real `alt`. No stock-photo abstractions (no glowing padlocks, no server-room render).

## Widget conventions (only if they asked for widgets)

Do not add widgets by default. When they are requested:

- Initialise inside `Reveal.on('ready')`.
- Click, tap and keyboard (`Enter`/`Space`) all work.
- `aria-live="polite"` on every score or feedback readout.
- State resets per slide; best score may persist in `localStorage`.
- Wrong answers explain **why**, never just show a cross.

## Choosing between them

| Direction | Strongest when | Weakest when |
| --- | --- | --- |
| 1a Ledger | text-heavy, discussion-led topics | diagram-first topics |
| 1b Terminal | networking, cyber, dev, CLI topics | employability / soft-skills topics |
| 1c Broadcast | large rooms, low-literacy groups, revision | dense reference content |
| 1d Blueprint | anything with layers, flows or hardware | pure discussion topics |
| 1e Studio | tutor-paced delivery across a whole scheme of work | self-paced revision |

A hybrid is legitimate: **1d's persistent diagram inside 1e's presenter rail** is the
most useful pairing, and both are token-compatible.
