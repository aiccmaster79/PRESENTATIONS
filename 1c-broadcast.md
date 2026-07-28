# 1c — Broadcast

> One idea per slide, at the size the back row can read. Full-bleed brand colour fields
> keyed permanently to each model. Roughly double the slide count, ~8 seconds each.

## Type

| Role | Family | Weight | Size @1920 | Notes |
| --- | --- | --- | --- | --- |
| Display | Archivo Black | 400 | 252px title / 104–132px h2 / 76–104px cards | uppercase, `letter-spacing: -0.035em`, `line-height: 0.84–1.02` |
| Statement | Archivo | 600 | 38–44px | sentence case |
| Body / meta | Archivo | 400 / 600 | 26–36px | `letter-spacing: 0.2–0.24em` uppercase for meta |

Google Fonts: `Archivo:wght@400;600&Archivo+Black`

Two weights only. If a slide needs a third size, it needs to be two slides.

## Tokens

Colour **is** the taxonomy — it never varies by slide, only by model.

```css
:root {
  --saas: #8A2BE2;  --saas-ink: #ffffff;
  --paas: #00BDA5;  --paas-ink: #04231f;
  --iaas: #F7931E;  --iaas-ink: #2a1400;
  --bg: #0e0e10;    --ink: #ffffff;   /* neutral slides */
}
:root[data-scheme="light"] { --bg: #ffffff; --ink: #0e0e10; }
```

Field slides use `background: var(--saas)` etc. with the paired ink token. Never put
purple type on a teal field. Never gradient two brand colours together.

## Grid

- Slide padding `72–80px`; fields bleed to all four edges.
- Title slides: meta line top, headline pushed to the optical centre with `margin: auto 0 0`,
  footer row separated by `border-top: 6px solid rgba(255,255,255,.35)`.
- Comparison slides are **horizontal bands**, one per model, each `flex: 1` of the full
  1080px height: model name at 132px in a fixed 520px column, statement at 44px beside it.
- Split slides are `1fr 860px` — type on one side, full-bleed photo on the other. The
  photo bleeds; the type never sits over it except on the title.
- No cards, no panels, no rules. Fields, bands, type.

## Slide layouts

**Title.** Solid `--saas` field. 28px uppercase meta, 252px three-line headline, footer of
`SaaS / PaaS / IaaS` at 44px plus a duration note.

**Core concept.** Three bands (purple / teal / orange), `flex: 1` each: name + two-line
statement (second line at 400 weight, 0.72–0.78 opacity).

**Reveal cards.** `--bg` slide, 104px heading, three cards `flex: 1; height: 600px`, each a
solid model field.

**Photo split (light).** White field, 124px black headline, orange kicker; photo bleeds
the right 860px with a solid `--iaas` caption block anchored bottom-left.

## Widget — Tap to reveal

```html
<div class="reveal-cards">
  <button type="button" class="reveal-card" data-model="saas" aria-pressed="false">
    <span class="kicker">Gmail</span>
    <span class="face">SaaS or IaaS?</span>
    <span class="hint">Tap to reveal</span>
  </button>
</div>
```

- The whole card is the button: minimum 500×600px. Nothing smaller — this is designed to
  be hit from the front of the room without aiming.
- Question at 76px, answer at 104px, so the answer visibly lands.
- Independent toggles, both directions (`Tap to hide`), `aria-pressed` tracked.
- No flip animation beyond a `120ms` opacity/scale on the face; the room needs the answer
  instantly, not a transition.
- Rule for the tutor, printed in the notes: **call it out as a class before tapping.**

## Imagery

Full-bleed or absent. One photo per slide, no captions floating over faces, caption in a
solid model-colour block. Duotone treatment is allowed via
`filter: grayscale(1)` plus a `mix-blend-mode: multiply` field — never a gradient scrim.

## Do not

- Add a fourth colour.
- Put more than one idea on a field slide.
- Drop below 38px for any text.
- Use Archivo Black in sentence case or below 76px.
