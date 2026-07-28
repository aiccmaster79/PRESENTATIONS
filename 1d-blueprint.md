# 1d — Blueprint

> The diagram *is* the slide. A drawing sheet: warm paper, technical strokes, a title
> block. One six-layer stack persists across the whole deck and recolours as ownership
> moves — replacing three separate drag-and-drop games with a single mental model.

## Type

| Role | Family | Weight | Size @1920 | Notes |
| --- | --- | --- | --- | --- |
| Display | Space Grotesk | 700 | 136px title / 72–76px h2 / 38px layer labels | `letter-spacing: -0.035em` |
| Body | Space Grotesk | 400 | 29–31px | `line-height: 1.45–1.5` |
| Annotation | Space Mono | 400 | 22–30px | uppercase + `letter-spacing: 0.14–0.18em` for labels |

Google Fonts: `Space+Grotesk:wght@400;500;700&Space+Mono:wght@400;700`

Every dimension, figure number, scale note and owner tag is Space Mono. Prose is Grotesk.

## Tokens

Light is the **default** scheme here; dark is the inversion.

```css
:root {
  --bg: #f3f0e8; --surface: rgba(255,255,255,.45);
  --ink: #1b1a17; --ink-dim: #4a463d; --ink-faint: #6b665a;
  --stroke: #1b1a17; --stroke-w: 2px;
  --grid-dot: rgba(27,26,23,.16);
  --you: #F7931E; --you-ink: #2a1400;
  --provider: #8A2BE2; --provider-ink: #ffffff;
  --annotate: #00BDA5;
}
:root[data-scheme="dark"] {
  --bg: #14171b; --surface: rgba(255,255,255,.05);
  --ink: #e8e6df; --ink-dim: rgba(232,230,223,.72); --ink-faint: rgba(232,230,223,.5);
  --stroke: rgba(232,230,223,.6); --grid-dot: rgba(255,255,255,.12);
}
```

Two-colour semantics, applied everywhere without exception: **orange = you manage,
purple = provider manages.** Teal is annotation only.

## Sheet furniture

```css
.reveal .slides section {
  background-image: radial-gradient(var(--grid-dot) 1.5px, transparent 1.5px);
  background-size: 48px 48px;
}
```

- **Frame** (title/section slides only): `border: 2px solid var(--stroke)` inset 44px.
- **Title block**, bottom-right, borders on left and top only, three rows in a
  `auto auto` grid: `DRAWING / No. 72`, `SCALE / 1:1 · 45 min`, `SHEET / 01 of 18`.
  Labels in `--ink-faint`, values in `--ink`, all Space Mono 22px.
- Content slides: header row with 72px h2 left and a mono `FIG. 2.1 · CAPTION` right,
  divided by `border-bottom: 2px solid var(--stroke)`.
- Footer: mono 26px forward-reference line above a `2px` top rule.

## The stack (the deck's one diagram)

Top to bottom, always these six, always this order:

`Application` · `Data` · `Runtime` · `Operating system` · `Virtualisation` · `Hardware`

Each layer is a bar: `border: 2px solid var(--stroke); padding: 20px 30px;` with the name
at 38px/700 left and a mono note or owner tag right. `gap: 12–14px` between bars.

Ownership by model — hard-coded, no ambiguity:

| Model | Yours |
| --- | --- |
| On-prem (baseline) | all six |
| SaaS | Data |
| PaaS | Application, Data |
| IaaS | Application, Data, Runtime, Operating system |

Right-hand column (300–340px) carries the bracket, the legend and the annotation note.

## Widget — Ownership slider

One control replaces the current deck's three drag-and-drop activities.

```html
<div class="stack-widget">
  <ol class="stack" aria-live="polite"><!-- six .layer bars --></ol>
  <div class="stack-controls">
    <label for="model-range">Service model</label>
    <input id="model-range" type="range" min="0" max="2" step="1" value="1">
    <div class="range-ticks"><span>SaaS</span><span>PaaS</span><span>IaaS</span></div>
    <p class="legend"><span class="sw you"></span> you manage</p>
    <p class="legend"><span class="sw provider"></span> provider manages</p>
    <p class="stack-note"></p>
  </div>
</div>
```

- `input` + `change` both bound, so keyboard arrows work with no extra code.
- Readout in the slide header: `PAAS · YOU MANAGE 2 OF 6`.
- Note text per position:
  - SaaS — "one layer is yours, and it is the one that matters most."
  - PaaS — "you own the code and the data. Runtime drift is the classic bug."
  - IaaS — "four layers of duty. This is where unpatched machines come from."
- Bar recolour transition `160ms`; `prefers-reduced-motion` removes it.
- `accent-color: var(--you)` on the range; track height ≥34px so it is draggable on a
  touchscreen at the front of the room.

## Imagery

Photos are **plates**: `border: 2px solid var(--stroke)` with `14px` padding, a mono
`PLATE 3 · RACK ELEVATION` label above and a scale/provenance line below
(`Scale 1:20 · campus comms room B · surveyed 2026`). Landscape, never full-bleed.

## Do not

- Break the orange/purple ownership semantics for emphasis.
- Reorder or rename the six layers between slides.
- Add a third stroke weight.
- Use a radius anywhere.
