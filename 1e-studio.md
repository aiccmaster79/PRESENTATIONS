# 1e — Studio

> Designed for the person holding the clicker. A permanent left rail carries chapter,
> minutes and what comes next; the content area is photo-led. Section timer and class
> confidence check are built in.

## Type

| Role | Family | Weight | Size @1920 | Notes |
| --- | --- | --- | --- | --- |
| Display | Bricolage Grotesque | 700 | 124px title / 76–88px h2 / 92px numerals | `letter-spacing: -0.03em` |
| Body | IBM Plex Sans | 400 / 600 | 46px lead, 30–34px body | `line-height: 1.35–1.6` |
| Rail / data | IBM Plex Mono | 400 / 500 | 21–24px, 118px clock | uppercase + `0.18em` for labels |

Google Fonts: `Bricolage+Grotesque:opsz,wght@12..96,400..800&IBM+Plex+Sans:wght@400;600&IBM+Plex+Mono`

## Tokens

```css
:root {
  --bg: #101114; --surface: #16181d;
  --ink: #ecedf0; --ink-dim: rgba(236,237,240,.62); --ink-faint: rgba(236,237,240,.4);
  --rule: rgba(255,255,255,.1);
  --accent: #00BDA5;   /* current position, timer, progress */
  --cue: #F7931E;      /* things the tutor should say or do */
  --saas: #8A2BE2; --paas: #00BDA5; --iaas: #F7931E;
}
:root[data-scheme="light"] {
  --bg: #f7f8fa; --surface: #eceef1;
  --ink: #14161a; --ink-dim: rgba(20,22,26,.6); --ink-faint: rgba(20,22,26,.45);
  --rule: rgba(20,22,26,.12);
  --accent: #008574; --cue: #b06a00;   /* darkened for contrast on light */
}
```

Flat fills only — no gradients anywhere except the bottom scrim on full-bleed photos.
Low glare is the point: this is on a projector for 45 minutes.

## Grid

`grid-template-columns: 420px 1fr` on **every** slide. Add `min-width: 0` to the content
cell or a full-bleed image will force the track wide.

### The rail (420px, `--surface`, `border-right: 1px solid var(--rule)`, padding `56px 44px`)

Slide-type variants, in order top to bottom:

- **Title rail** — deck number in `--accent`, deck name at 38px/700, 1px rule, then the
  chapter list: six rows of `NN · name · minutes`, current row in `--ink` with its number
  in `--accent`, others `--ink-faint`. Bottom: `Next up` + the opening question in `--cue`.
- **Content rail** — `CHAPTER 02`, chapter name at 44px, `5 minutes · slide 6 of 18` in
  `--accent`, 1px rule, a 26px delivery note, and a 6-segment progress bar
  (8px tall, filled segments `--accent`) pinned to the bottom.
- **Activity rail** — becomes the HUD (below).

Everything in the rail is for the tutor. Learners read the right-hand 1500px.

### Content area

Either `padding: 72px 80px` with type, or a full-bleed `<figure>` with a bottom scrim
(`linear-gradient(to top, var(--bg) , transparent)` at 94% → 0) carrying the title plate.
Overlay text gets `pointer-events: none`.

Numbered lists use 92px Bricolage numerals in the model colour, a 130px fixed column,
and `border-top: 1px solid var(--rule)` per row.

## Widget — Presenter HUD

Three controls, all in service of delivery.

```html
<div class="hud">
  <p class="hud-label">Presenter HUD</p>
  <p class="clock" aria-live="off">00:00</p>
  <p class="clock-cap">of 8 minutes allowed</p>
  <div class="clock-actions">
    <button type="button" data-action="toggle">Start</button>
    <button type="button" data-action="reset">Reset</button>
  </div>
  <p class="say">Say it out loud<br><span>"Data never moves to the provider."</span></p>
</div>

<div class="confidence">
  <button type="button" data-band="1"><span class="band">1 · lost</span><span class="desc">No idea who patches it</span><span class="count">0</span></button>
  <button type="button" data-band="2">…</button>
  <button type="button" data-band="3">…</button>
</div>
<button type="button" class="reveal-answer" aria-expanded="false">Reveal answer</button>
<p class="answer" hidden>The school does. Renting the machine does not rent the responsibility.</p>
```

- **Timer** — counts up, `setInterval` 1s, mm:ss at 118px in `--accent`. Turns `--cue` at
  the allowed limit and `#ef4444` at 1.5×. Pause/reset. Never auto-advances the slide.
- **Confidence tally** — three tap-to-increment bands with counts at 76px. Tutor taps as
  hands go up. Long-press or right-click decrements. Resets per slide.
- **Reveal answer** — explicit tutor control, `aria-expanded`, answer hidden until pressed.
  Answer copy always states the consequence, not just the fact.
- Timer state persists across slides in the same section (`sessionStorage`), so navigating
  back does not lose the clock.

## Imagery

Photography is the default here, not the exception. Full-bleed 1500×1080 in the content
cell, subject kept out of the bottom 300px where the scrim and title plate sit. Real
photos of real rooms — a school IT suite, a patch panel, staff at laptops. Alt text
describes the scene, not the topic.

## Do not

- Let the rail exceed 420px or drop below 380px.
- Put learner-facing content in the rail.
- Add a gradient outside the photo scrim.
- Auto-advance slides from the timer.
