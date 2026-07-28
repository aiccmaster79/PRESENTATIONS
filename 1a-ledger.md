# 1a — Ledger

> An editorial page, not a slide. Hierarchy and white space do the work that cards and
> icons were doing. Answers live in the margin and the tutor opens them one at a time.

## Type

| Role | Family | Weight | Size @1920 | Notes |
| --- | --- | --- | --- | --- |
| Display | Instrument Serif | 400 | 180px title / 96px h2 / 70–82px h3 | `letter-spacing: -0.025em`, `line-height: 0.92–1.02` |
| Body | IBM Plex Sans | 400 / 600 | 33px prose, 27px secondary | `line-height: 1.45–1.6`, `text-wrap: pretty` |
| Label | IBM Plex Mono | 400 | 19–23px | `text-transform: uppercase`, `letter-spacing: 0.14–0.2em` |

Google Fonts: `Instrument+Serif&IBM+Plex+Sans:wght@400;600&IBM+Plex+Mono`

Never set the serif below 32px. Never use it for body copy.

## Tokens

```css
:root {
  --bg: #14131a;  --surface: transparent;
  --ink: #f2efe9; --ink-dim: rgba(242,239,233,.72); --ink-faint: rgba(242,239,233,.45);
  --rule: rgba(242,239,233,.2);
  --you: #F7931E; --provider: #8A2BE2; --accent: #00BDA5;
}
:root[data-scheme="light"] {
  --bg: #f6f3ec; --ink: #17161c; --ink-dim: rgba(23,22,28,.7); --ink-faint: rgba(23,22,28,.45);
  --rule: rgba(23,22,28,.22);
}
```

Brand colours appear **only** as: 4px category rules above a label, mono label colour,
and the convenience→control gradient rule. Never as a fill behind text.

## Grid

- Slide padding `80px 96px`.
- Two zones: **text column** (fluid) + **margin column** (460–560px fixed), `gap: 72–84px`.
- Column dividers are `1px solid var(--rule)`. There are no boxes, no radii, no shadows,
  no `backdrop-filter` anywhere in this direction.
- Section rhythm: mono eyebrow → serif heading → 1px rule → body.
- Three-up comparisons are three grid columns separated by `border-left: 1px solid var(--rule)`
  with `padding: 40px 44px`, each headed by a mono index (`01 — SUBSCRIBE`) in its
  category colour.

## Slide layouts

**Title.** `grid-template-columns: 1fr 460px`. Left: mono meta line (`No. 72 / Level 2–3 / topic`),
serif title at 180px, 1px rule, 35px standfirst, and a bottom row of three category
stubs (`border-top: 4px solid <category>` + mono kicker + serif term). Right: portrait
photo, hard edges, 460×700, with a two-line mono caption beneath.

**Core concept.** Mono eyebrow, 96px serif h2, then the three-column ladder. Footer is a
full-width row: mono `CONVENIENCE` — 1px gradient rule — mono `CONTROL`.

**Prose + margin.** `1fr 560px`. Body copy at 33px with **bold** terms; the margin column
is headed `MARGIN NOTES` and holds one entry per note.

**Plate.** Mono figure line + category tag on a bottom-ruled header, full-width photo
(1728×560), then a two-column footer: 56px serif claim + 29px explanation.

## Widget — Marginalia

Numbered buttons under the prose open the matching margin note. Closed notes show their
category rule, label and the words "Click to open." in `--ink-faint`.

```html
<div class="marginalia">
  <p>… but <strong>data</strong> stays with the school …</p>
  <div class="note-buttons">
    <button type="button" data-note="1" aria-expanded="false" aria-controls="note-1">open note 1</button>
  </div>
</div>
<aside class="margin-notes">
  <div class="note" id="note-1" data-rule="provider">
    <span class="note-label">Data</span>
    <p class="note-body">Retention, sharing links, export rights. Never the provider's call.</p>
  </div>
</aside>
```

Rules: toggling is independent per note (tutors open them out of order); `aria-expanded`
tracks state; closed body text is present in the DOM (dimmed), not removed.

## Imagery

One photograph per slide, maximum. Hard-edged, no radius, no overlay. Portrait in the
margin column; landscape as a full-width plate. Captions are mono, two lines maximum,
and carry a figure number that matches the speaker notes.

## Do not

- Add a card, a border-radius above 0, or any shadow.
- Set the serif in uppercase.
- Use more than one brand colour on a single slide edge.
- Centre body text.
