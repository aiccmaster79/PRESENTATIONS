# AGENTS.md

## Cursor Cloud specific instructions

This repo is a **static site** — a searchable catalog (`index.html`) plus ~140+ self-contained
reveal.js teaching decks (`*.html`). There is no backend, package manager, build step, or test suite,
and the maintainers explicitly want to keep it that way (see the "Do not… add build tooling, add new
CDN dependencies" rule in [`PRESENTATION-UPGRADE-PLAN.md`](PRESENTATION-UPGRADE-PLAN.md) §5).

### Running it
- Serve the folder over HTTP and open in a browser, e.g. `python3 -m http.server 8080` then
  `http://localhost:8080/index.html`. Use HTTP (not `file://`) so relative deck links and the
  Mermaid ES module in `network-diagram-ocn-level2-presentation.html` behave correctly.
- There is nothing to install or build; editing a `.html` file and refreshing the browser is the
  whole dev loop.

### Gotchas
- **Outbound HTTPS is required at runtime.** Decks pull reveal.js, highlight.js, Font Awesome,
  Google Fonts, and Mermaid from CDNs (jsdelivr / cdnjs / googleapis). With no network the decks
  render unstyled and interactive widgets that rely on reveal.js lifecycle hooks won't initialise.
- Deck files must never be renamed — `index.html` links are hand-maintained.
- Widget conventions (state handling, keyboard/touch a11y, `Reveal.on('ready')` init) and the
  per-deck "definition of done" live in [`PRESENTATION-UPGRADE-PLAN.md`](PRESENTATION-UPGRADE-PLAN.md);
  read it before upgrading a deck.

### Verifying a change
Open the affected deck over HTTP, check the browser console is clean, exercise any widget you
touched, run the quiz through to the results slide, and press **S** for speaker view (per the
upgrade plan's verification checklist).

### Related repo
The sibling `INTRO-TO-WORLDSKILLS` repo will be built out using **this repo's decks as the visual
and structural model**. Reuse the brand palette, chrome (`.back-to-index`, `.site-credit`,
particle canvas), and widget patterns from here when working on that repo.
