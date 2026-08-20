# OCN NI deck design directions — shared spec

Source repo: `aiccmaster79/PRESENTATIONS` · reference deck: `saas-paas-iaas-comparison-ocn-level2-presentation.html` (#72)
Live exploration: `Deck Design Directions.dc.html` (ids `1a`–`1e`)

## Purpose

Five candidate visual systems for the ~140-deck teaching library. Each keeps the brand
triad and the OCN NI content model, and each replaces the current "glass card + Font
Awesome icon + auto-fit grid" treatment with a system that has an actual point of view.

## What is fixed across all five

| Constraint | Value |
| --- | --- |
| Brand orange | `#F7931E` |
| Brand purple | `#8A2BE2` |
| Brand teal | `#00BDA5` |
| Deck size | reveal.js `width: 1920, height: 1080`, `margin: 0.04` |
| Engine | reveal.js 4.6.0, no build step, no new CDN dependencies beyond fonts |
| Chrome | `.back-to-index` pill, `.site-credit` line, `aside.notes` on every slide |
| Filenames | never renamed — `index.html` links are hand-maintained |
| Min type size | 24px at 1920×1080. Nothing smaller, ever. |
| Schemes | every direction ships dark **and** light (see "Theme toggle" below) |
| Photos | author-supplied images, never generated SVG illustration |

## What every direction must drop

- `.animated-gradient` clipped-text headings (8s infinite animation on every h2).
- `backdrop-filter` glass cards used as the default container for all content.
- Decorative Font Awesome icons that repeat the adjacent word ("Objectives 🎯").
- `font-size` in `em` relative to reveal's root scale — use absolute px at 1920×1080.
- `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` as the universal layout.
- The 5-slide filler tail (Career Pathways / stats-bar / Next Steps / Thank You) unless
  the content is genuinely per-topic.

## Proposed teaching structure (replaces the current 22-slide recipe)

The current sequence front-loads meta ("How to use this deck") and back-loads filler.
Recommended 18-slide spine, same for all five directions:

1. Title
2. The hook — one real consequence of getting this wrong
3. Objectives (max 4, verb-led)
4. Core concept (the single diagram or ladder the whole deck hangs on)
5–7. One slide per part of the concept
8. **Activity 1** — the direction's signature widget
9. Worked example
10. Trade-offs
11. **Activity 2** — applied, scenario-based
12–13. Case study (real, named, two slides max)
14. Common faults table
15. **Activity 3** — quiz, 4–6 questions, scored
16. Results + what a wrong answer means
17. Key takeaways (max 4)
18. Close: one instruction for what to do next

Cut: "How to use this deck", keyboard hints slide, glossary slide (make it a `?` overlay),
deck map, career pathways, stats-bar, "Thank You".

## Theme toggle

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

## Widget conventions (unchanged from PRESENTATION-UPGRADE-PLAN.md)

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
