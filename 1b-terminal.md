# 1b — Terminal

> The deck as an inspectable system. Near-black, monospace-forward, 1px panels that read
> as code blocks. Brand colours become syntax tokens. The quiz becomes a console.

## Type

| Role | Family | Weight | Size @1920 | Notes |
| --- | --- | --- | --- | --- |
| Display | JetBrains Mono | 700 | 132px title / 56–60px h2 | `letter-spacing: -0.045em` |
| UI / data | JetBrains Mono | 400 / 500 | 23–28px | `line-height: 1.85–1.95` |
| Prose | IBM Plex Sans | 400 | 30px | only for explanatory paragraphs |

Google Fonts: `JetBrains+Mono:wght@400;500;700&IBM+Plex+Sans:wght@400;600`

Headings are lowercase and read as commands: `> classify(service)`, `> describe --all`.

## Tokens

```css
:root {
  --bg: #07080b; --surface: #0d0f14;
  --ink: #dbe0e8; --ink-dim: #8c95a3; --ink-faint: #4c5563;
  --rule: rgba(255,255,255,.11);
  --key: #F7931E;      /* field names */
  --type: #8A2BE2;     /* function / model names */
  --value: #00BDA5;    /* strings, examples, cursor */
  --pass: #22c55e; --fail: #ef4444;
}
:root[data-scheme="light"] {
  --bg: #f1f2f4; --surface: #ffffff;
  --ink: #0a0b0e; --ink-dim: #5b6472; --ink-faint: #8b93a0;
  --rule: rgba(10,11,14,.24);
}
```

Colour has one job: syntax role. `--key` for field names, `--type` for model names,
`--value` for strings and examples. Never decorative.

## Grid

- Slide padding `64px 80px`.
- **Status bar** on every slide: `display:flex; justify-content:space-between`,
  `border-bottom: 1px solid var(--rule)`, 23px mono, `--ink-dim`. Left: a 14px
  `--value` dot + breadcrumb `ocnni/level-2 ▸ deck-72 ▸ cloud-models`. Right: `sheet 01 / 18`.
- Panels: `background: var(--surface); border: 1px solid var(--rule)`, radius 0, no shadow.
  Each panel has a header bar tinted at 16% of its category colour with a mono name
  (`saas.model`) and a `1px` bottom rule.
- Panel bodies are key/value lines, not prose: `you:`, `provider:`, `buy:`, `risk:`,
  `examples:` — the same five fields on every panel so the class compares by scanning.
- Blockquote pattern for objectives/notes: `border-left: 3px solid var(--value); padding-left: 34px`.
- Footer line, 23px `--ink-faint`: `press S for notes · ← → to move · ? for the glossary`.

## Slide layouts

**Title.** Status bar, then a `// module:` comment line in `--type`, then the 132px
lowercase title with a 56×104px `--value` cursor block (`animation: blink 1.1s steps(1) infinite`,
suppressed under `prefers-reduced-motion`). Below: the objectives block as `- item` lines
with the dash in `--key`.

**Core concept.** Three equal panels, `gap: 30px`, one per model, five identical fields each.

**Console.** Prompt heading, progress line, then a panel containing the current call
(`classify("Azure App Service") → ?`) and the answer buttons; output lines print beneath.

**Plate (light).** `1fr 520px`. Photo inside a `1px` bordered viewport with `12px` padding
and a filename/dimensions line under it; right column is a `symptom / cause / fix` list
with the labels in `--type`.

## Widget — REPL classifier

```html
<section class="repl">
  <p class="repl-progress" aria-live="polite">card 1 of 9 · pick a model</p>
  <div class="repl-call"><span class="fn">classify</span>(<span class="str">"Azure App Service"</span>) → ?</div>
  <div class="repl-actions">
    <button type="button" data-choice="saas">saas</button>
    <button type="button" data-choice="paas">paas</button>
    <button type="button" data-choice="iaas">iaas</button>
    <button type="button" data-action="reset">reset</button>
  </div>
  <ol class="repl-out" aria-live="polite"></ol>
  <p class="repl-score">score <span>0 / 0</span></p>
</section>
```

Output line format — the reason is mandatory:

```
PASS  Azure App Service → PAAS  // you push code, the platform patches the runtime
FAIL  Microsoft 365 is SAAS, not IAAS  // a finished application — you only own data and accounts
```

Keep the last 4 lines visible; older lines scroll out. `PASS` in `--pass`, `FAIL` in
`--fail`, the `//` reason in `--ink-dim`. Best score in `localStorage` under
`deck-72-classifier-best`.

## Imagery

Screenshots beat photographs in this direction — patch reports, portal blades, consoles.
Every image sits in a 1px bordered viewport with a filename caption. No rounding, no
drop shadow, no browser-chrome mockup.

## Do not

- Use title case in headings.
- Add a second accent outside the three syntax roles.
- Let mono body copy exceed ~70 characters per line.
- Animate anything except the cursor.
