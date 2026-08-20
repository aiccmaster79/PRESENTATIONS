# Presentation Upgrade Plan — Tracker

**Progress: 33 / 145 presentations complete**

Every Reveal.js deck in this repo is being rebuilt to the same "feature rich and
engaging" standard set by
[`inside-the-pc-components-ocn-level2-presentation.html`](inside-the-pc-components-ocn-level2-presentation.html)
(deck #94) — 33 slides, seven interactive features, speaker notes throughout.

This file is the shared worklist. Each agent claims decks, upgrades them, and
ticks the boxes in [section 7](#7-deck-checklist).

**Contents**

1. [Definition of done](#1-definition-of-done)
2. [Canonical slide blueprint](#2-canonical-slide-blueprint)
3. [Interactive widget library](#3-interactive-widget-library)
4. [Tier recipes](#4-tier-recipes)
5. [Agent workflow](#5-agent-workflow)
6. [Priority order](#6-priority-order)
7. [Deck checklist](#7-deck-checklist)

---

## 1. Definition of done

A deck is only ticked when **all** of the following are true.

**Scale**

- 26–34 slides. Small-tier decks grow the most, large-tier decks the least.

**Interactivity**

- 3–5 topic-specific interactive widgets from [the library](#3-interactive-widget-library),
  chosen because they fit the topic — not bolted on because they were easy to copy.
- At least one must be a *doing* widget (build, sort, simulate, calculate), not
  just a click-to-reveal.
- A 6-question scored quiz with progress pill, score bar, a results slide with a
  letter grade, and a retry button. This replaces the 3-question click quiz that
  every deck currently ships with.

**Content depth**

- A real-world case study — a named incident, business, or concrete classroom scenario.
- A common-faults table: symptom → likely cause → fix.
- A searchable jargon buster with 10–20 terms.
- A cross-deck pathway map linking 4–6 sibling decks in this library.
- An extended practical task with success criteria and an evidence checklist.

**Delivery**

- `<aside class="notes">` on **every** slide, each with a delivery cue and a
  timing estimate. The notes should add up to a coherent 60–90 minute lesson.

**Chrome and branding**

- `.back-to-index` link, `.site-credit` footer, `#circuit-canvas` particle
  background with `data-canvas-bg` on the title and closing slides.
- `.demo-meta` badge on the title slide matching the deck number and level shown
  on its `index.html` card.
- No changes to the brand palette (`--brand-orange`, `--brand-purple`, `--brand-teal`).

**Accessibility and robustness**

- Every widget operable by keyboard (Enter/Space) as well as pointer.
- Touch fallback (tap-to-select, tap-to-place) for anything drag-based.
- `aria-label` on controls, `aria-live="polite"` on score readouts,
  `aria-hidden="true"` on decorative icons and canvases.
- `@media (prefers-reduced-motion: reduce)` honoured by every animation.
- Layout survives `@media (max-width: 768px)`.

**Verification**

- No console errors on load or while using any widget.
- Quiz scores correctly and the results grade matches the score.
- Renders correctly at the 1920×1080 authoring size and at mobile width.
- Speaker view (**S**) shows the notes.

**Index**

- The deck's card in `index.html` has `data-updated` bumped to the upgrade date
  (this drives the "Recently added" widget), `data-upgraded="true"` (this drives
  the index **Upgraded** filter), and its `<p>` blurb refreshed if the scope
  changed.

---

## 2. Canonical slide blueprint

Follow this skeleton and drop topic content into it. Bracketed counts show where
a deck can flex.

| # | Slide |
|---|---|
| 1 | Title — `data-canvas-bg`, animated gradient heading, `.demo-meta` badge, qualification pill |
| 2 | Learning objectives — fragments with `fade-up` |
| 3 | How to use this deck — keyboard hints, "interactives are clickable and tappable" |
| 4 | Why this matters — hook, stats bar, a real consequence |
| 5–7 | Core concept slides — feature grid, comparison boxes, diagrams [3–5] |
| 8 | **Signature interactive #1** — the deck's headline widget |
| 9–11 | Applied detail — how it works in practice, step sequence, worked example [2–4] |
| 12 | **Signature interactive #2** |
| 13 | Real-world case study |
| 14 | Common faults — symptom → cause → fix table |
| 15 | **Signature interactive #3** — game or challenge, ideally timed with a `localStorage` best score |
| 16 | Practical task — brief, success criteria, evidence checklist |
| 17 | Jargon buster — searchable glossary |
| 18 | Where this fits — cross-deck pathway map |
| 19 | Quiz intro with score bar |
| 20–25 | Quiz Q1–Q6 |
| 26 | Results — grade and retry |
| 27 | Key takeaways — 4 pillars |
| 28 | Career pathways — roles, skills, stats bar |
| 29 | Next steps and further reading |
| 30 | Thank you — `data-canvas-bg` |

---

## 3. Interactive widget library

### 3.1 Copy directly from the reference deck

All line numbers refer to
[`inside-the-pc-components-ocn-level2-presentation.html`](inside-the-pc-components-ocn-level2-presentation.html).

| Widget | What the learner does | CSS | JS |
|---|---|---|---|
| Flip cards | Click or press Enter/Space to reveal the back of a card | 637–687 | `initFlipCards()` 1890–1900 |
| SVG hotspot explorer | Click numbered hotspots on an inline SVG; info panel updates. Quiz mode hides the answer for 1.5s first | 689–751 | `initMotherboard()` + `MB_INFO` 1878–1942 |
| Drag-and-drop sort | Drag shuffled chips into labelled bins; wrong answers shake. Tap-to-select touch fallback | 753–854 | `createChips()`, `initDnD()`, `handleDrop()` 1945–2078 |
| Timed challenge | 60s countdown over a DnD board, warning state at 10s, best time kept in `localStorage` | 843–854 | `startTimer()`, `stopTimer()` 2080–2109 |
| Scored quiz | `data-quiz="N"` sections, `.quiz-option[data-correct]`, progress pill, letter grade | 856–904 | `initQuiz()`, `updateQuizUI()`, `showResults()` 2126–2192 |
| Searchable glossary | Type to filter `.glossary-item` entries by their `data-terms` | 906–939 | `initGlossary()` 2112–2123 |
| Particle canvas | Ambient background that only paints on `data-canvas-bg` slides | 1136–1143 | `initCanvas()` 2195–2253 |

### 3.2 New widgets to build

Write these once for the deck you need them in, then reuse the pattern
elsewhere. Keep them in the same house style.

- **Step simulator** — Next/Back through a process with the current state
  highlighted on a diagram. Good for DORA, DNS resolution, boot sequence, OS
  install stages, incident response phases.
- **Rule / packet evaluator** — the learner edits a small rule table, fires test
  inputs, and sees allow/deny with the matching rule highlighted. Good for
  firewalls, validation rules, file permissions.
- **Live calculator** — sliders or inputs feeding a computed result with a bar or
  gauge. Good for time-to-crack, cost-per-GB, kWh to cost and CO₂, PSU wattage,
  effective permissions, SLA clocks.
- **Before/after slider** — drag a divider between a messy and a fixed state.
  Good for bad vs good CV, unrefactored vs refactored code, dirty vs clean data.
- **Decision tree** — branching yes/no cards ending in a verdict with a rationale.
  Good for troubleshooting, "I found a USB stick", printer faults.
- **Scenario judge** — show a scenario card, learner votes, reveal with feedback
  and a running score. Good for GDPR verdicts, safe-or-scam, correlation vs causation.
- **Sequence builder** — drag steps into the correct order, validate, and show the
  first wrong position. Good for crimping, build order, deployment pipelines, git workflow.
- **Terminal / log replay** — typed-out fake console output with a filter or search
  box over canned data. Good for `nslookup`, `nmap`, unit test output, event logs.
- **Mini sandbox** — a genuinely live tool where it is safe and works offline:
  HTML/CSS preview in an iframe, Caesar cipher tool, validation tester,
  hash-and-chain blockchain demo, contrast checker.
- **Card sort / matcher** — match term to definition, or threat to defence, with a
  scored check.
- **Myth buster** — a claim card flips to an evidence-backed verdict.
- **Design canvas** — drag devices or components onto a plan area against a budget
  or rule set. Good for small-office networks, smart homes, IoT rooms.

### 3.3 House rules for new code

- Hold state in a single `AppState` object at the top of the script block.
- Guard every listener with `if (el.dataset.bound) return; el.dataset.bound = 'true';`
- Initialise on `Reveal.on('ready')` and re-initialise on `Reveal.on('slidechanged')`.
- Everything stays inline in the single HTML file. No build step, no new
  dependencies beyond the Reveal.js / Font Awesome / Google Fonts CDNs already in use.
- Never rename a deck file — `index.html` links are hand-maintained.

---

## 4. Tier recipes

**Small tier — 14–17 slides, ~370–500 lines → 26–30 slides**

The biggest lift. These decks are missing the shared chrome as well as content.

1. Port the full CSS block from a medium-tier deck (e.g. `dns-in-action`), which
   brings `.back-to-index` and `.site-credit` with it.
2. Add the particle canvas and `data-canvas-bg` on title/closing.
3. Add roughly 12 slides: why-it-matters, two concept slides, three widgets, case
   study, faults table, glossary, pathway map, three extra quiz questions, results.
4. Add speaker notes to every slide, old and new.

**Medium tier — 15–17 slides, ~820–940 lines → 28–32 slides**

Chrome is already there; the content skeleton is generic.

1. Replace the "Demo Sequence" slide with a step simulator.
2. Replace the "Symptom Guide" slide with an interactive faults table or decision tree.
3. Add case study, glossary, pathway map, and two more widgets.
4. Expand the quiz to six questions plus results.
5. Add speaker notes throughout.

**Large tier — 17–23 slides, ~970–1180 lines → 30–34 slides**

Content is already strong; interactivity is not.

1. Convert existing static comparison and diagram slides into widgets in place.
2. Add two or three new widgets, glossary, and pathway map.
3. Expand the quiz to six questions plus results.
4. Add speaker notes throughout.

**Special cases**

- **#142 Network Diagram** is a bare 52-line Mermaid page, not a deck. Build it
  out into a full presentation: keep a topology diagram as the centrepiece and add
  a drag-to-build classroom LAN, cabling notes, and an IP plan.
- **#143 VEXcode Tutorial** is a scroll page on the VEX brand, not a Reveal deck.
  Keep the scroll format and the VEX palette. Add a sticky progress rail,
  per-section checkpoint questions, copy-code buttons, and a block-assembly
  interactive.

---

## 5. Agent workflow

1. **Claim first.** Change `- [ ]` to `- [~]` and append your branch name for the
   decks you are taking, then commit *that change on its own* before doing the
   work. This stops parallel agents colliding.
2. **Branch.** `cursor/upgrade-<topic>-<suffix>`. Take 3–6 decks per branch and PR.
3. **Upgrade** each deck against [section 1](#1-definition-of-done).
4. **Update `index.html`** — bump the card's `data-updated`, set
   `data-upgraded="true"`, and refresh the blurb if the scope changed.
5. **Verify** — open the file in a browser (or headless with a console listener),
   exercise every widget, run the quiz through to the results slide, press **S**
   for speaker view, and resize to mobile width.
6. **Tick.** Change `- [~]` to `- [x]` and append the PR number, then update the
   progress counter at the top of this file.
7. **Commit, push, open the PR.**

**Do not:** change the brand palette, add build tooling, add new CDN
dependencies, rename deck files, or edit another agent's claimed decks.

---

## 6. Priority order

1. Small-tier decks — the biggest quality gap: Programming, Website Development,
   Mobile Apps, Software Testing, and demos #72–#87.
2. High-traffic Core IT and Cyber Security decks.
3. Emerging Technology and Digital Skills large-tier decks.
4. Special cases last: #142 stub build-out and #143 scroll tutorial.

---

## 7. Deck checklist

Each entry shows the deck number, file, current tier and slide count, the target
slide count, and suggested widgets. Widget suggestions are a starting point, not
a mandate — swap them if something fits the topic better.

### IT Fundamentals — Demos

- [ ] **#1 Safe Working & ESD** — `safe-working-esd-ocn-level2-presentation.html` · medium · 16 → 30
  - Static-risk calculator (flooring, humidity, clothing), safe-vs-unsafe action sort, ESD bench hotspot photo, fried-DIMM case study
- [ ] **#2 Inside a Laptop** — `inside-a-laptop-ocn-level2-presentation.html` · medium · 16 → 30
  - Exploded-view hotspot teardown, disassembly sequence builder, screw-map memory game, right-to-repair angle
- [ ] **#3 BIOS / UEFI Setup** — `bios-uefi-setup-ocn-level2-presentation.html` · medium · 16 → 30
  - Simulated firmware menu with keyboard navigation, boot-order drag reorder, legacy vs UEFI slider, POST code lookup
- [ ] **#4 Installing an OS** — `installing-an-os-ocn-level2-presentation.html` · medium · 16 → 30
  - Install-stage step simulator, partition scheme visualiser, unattended vs manual compare, install-error triage
- [ ] **#5 Drivers & Device Manager** — `drivers-device-manager-ocn-level2-presentation.html` · medium · 16 → 30
  - Device Manager tree explorer with error codes, update-vs-rollback decision tree, symptom → fix table
- [ ] **#6 Storage Comparison** — `storage-comparison-ocn-level2-presentation.html` · medium · 15 → 30
  - Cost-per-GB and speed calculator, copy-race animation, pick-the-storage scenario judge

### IT Support / Service Delivery — Demos

- [ ] **#7 Printer Setup & Troubleshooting** — `printer-setup-troubleshooting-ocn-level2-presentation.html` · medium · 15 → 30
  - Fault decision tree, print-path hotspot diagram, queue and driver simulator
- [ ] **#8 Imaging & Deployment** — `imaging-and-deployment-ocn-level2-presentation.html` · medium · 16 → 30
  - Pipeline sequence builder, time-saved calculator (PCs × minutes), sysprep gotchas
- [ ] **#9 Remote Support Tools** — `remote-support-tools-ocn-level2-presentation.html` · medium · 16 → 30
  - Consent script role-play, tool comparison matrix, session checklist, safeguarding rules
- [ ] **#10 Helpdesk Ticket Lifecycle** — `helpdesk-ticket-lifecycle-ocn-level2-presentation.html` · medium · 16 → 30
  - Drag-a-ticket status board, priority matrix, write-a-ticket exercise with rubric
- [ ] **#11 Backup & Restore** — `backup-and-restore-ocn-level2-presentation.html` · medium · 16 → 30
  - Restore-drill simulator, 3-2-1 builder, RPO/RTO calculator
- [ ] **#12 Performance Monitoring** — `performance-monitoring-ocn-level2-presentation.html` · medium · 16 → 30
  - Counter gauges, bottleneck detective (given counters, name the culprit), Task Manager hotspots
- [ ] **#13 Account Permissions** — `account-permissions-ocn-level2-presentation.html` · medium · 16 → 30
  - Effective-permissions calculator, group membership drag, least-privilege scenarios
- [x] **#76 Service Catalogue** — `service-catalogue-ocn-level2-presentation.html` · small · 14 → 28 · (#40)
  - Catalogue builder, request form designer, service tier matcher
- [x] **#77 SLA Response Times** — `sla-response-times-ocn-level2-presentation.html` · small · 14 → 28 · (#40)
  - SLA clock simulator with priority matrix, breach calculator
- [x] **#78 Asset Tagging** — `asset-tagging-ocn-level2-presentation.html` · small · 14 → 28 · (#40)
  - Lifecycle sequence builder, label designer, audit spot-check game
- [ ] **#89 Software Updating** — `software-updating-ocn-level2-presentation.html` · medium · 16 → 30
  - Patch-risk ranker, update rings diagram, bad-update rollback case study

### Intro to Networking — Demos

- [ ] **#14 Cable Crimping** — `cable-crimping-ocn-level2-presentation.html` · medium · 16 → 30
  - T568B wire-order drag, crimp step sequencer, tester result reader, fault gallery
- [ ] **#15 Switch vs Router** — `switch-vs-router-ocn-level2-presentation.html` · medium · 16 → 30
  - Frame-vs-packet animation, MAC/ARP table builder, device chooser scenarios
- [ ] **#16 DHCP & IP Addressing** — `dhcp-ip-addressing-ocn-level2-presentation.html` · medium · 16 → 30
  - DORA step simulator, lease table simulator, APIPA and subnet diagnoser
- [ ] **#17 DNS in Action** — `dns-in-action-ocn-level2-presentation.html` · medium · 16 → 30
  - Recursive resolution stepper, record-type matcher, `nslookup` terminal replay, failure triage
- [ ] **#18 VLANs & Segmentation** — `vlans-segmentation-ocn-level2-presentation.html` · medium · 16 → 30
  - Port assignment board, tag/untag visual, broadcast domain calculator
- [ ] **#19 Wi-Fi Signal & Channels** — `wifi-signal-channels-ocn-level2-presentation.html` · medium · 16 → 30
  - Channel overlap picker (2.4/5/6 GHz), attenuation-by-material calculator, survey heatmap
- [ ] **#142 Network Diagram** — `network-diagram-ocn-level2-presentation.html` · **stub** · 0 → 28
  - Build out from scratch: topology hotspots, drag-to-build classroom LAN, cabling notes, IP plan

### Virtualisation — Demos

- [ ] **#20 Type 1 vs Type 2 Hypervisors** — `type1-vs-type2-hypervisors-ocn-level2-presentation.html` · medium · 16 → 30
  - Stack layer builder, use-case chooser, overhead visual
- [ ] **#21 VM Snapshots** — `vm-snapshots-ocn-level2-presentation.html` · medium · 16 → 30
  - Branching snapshot tree simulator, disk-cost calculator, "a snapshot is not a backup" myth buster
- [ ] **#22 Virtual Networks** — `virtual-networks-ocn-level2-presentation.html` · medium · 16 → 30
  - NAT / bridged / host-only packet path animation, mode chooser scenarios

### Databases — Demos

- [ ] **#39 ERD to Working Database** — `erd-to-working-database-ocn-level2-presentation.html` · medium · 16 → 30
  - ERD builder that emits DDL, cardinality drag, sample-data loader
- [ ] **#40 Normalisation Live Fix** — `normalisation-live-fix-ocn-level2-presentation.html` · medium · 16 → 30
  - 1NF/2NF/3NF step transformer on a live table, anomaly spotter
- [ ] **#41 SQL Query Builder** — `sql-query-builder-ocn-level2-presentation.html` · medium · 15 → 30
  - Clause-by-clause builder running against a mock table, JOIN visualiser
- [ ] **#42 Database Validation** — `database-validation-ocn-level2-presentation.html` · medium · 15 → 30
  - Rule tester (input → pass/fail), validation type matcher
- [ ] **#43 Referential Integrity Failure** — `referential-integrity-failure-ocn-level2-presentation.html` · medium · 15 → 30
  - Delete/cascade simulator, orphan-record spotter
- [ ] **#44 Import CSV to Database** — `import-csv-to-database-ocn-level2-presentation.html` · medium · 15 → 30
  - Column mapping drag, delimiter and type pitfalls, import error log triage

### Data Modelling / Analytics — Demos

- [ ] **#45 Absolute vs Relative References** — `absolute-vs-relative-references-ocn-level2-presentation.html` · medium · 15 → 30
  - Fill-handle simulator showing formula drift, `$` toggle grid
- [ ] **#46 Lookup Functions** — `lookup-functions-ocn-level2-presentation.html` · medium · 15 → 30
  - Lookup playground over a mock table, VLOOKUP vs XLOOKUP compare, `#N/A` triage
- [ ] **#47 What-If Modelling** — `what-if-modelling-ocn-level2-presentation.html` · medium · 15 → 30
  - Scenario sliders with live chart, data-table concept
- [ ] **#48 Goal Seek** — `goal-seek-ocn-level2-presentation.html` · medium · 15 → 30
  - Goal-seek solver widget, break-even chart
- [ ] **#49 Data Validation and Protection** — `data-validation-and-protection-ocn-level2-presentation.html` · medium · 15 → 30
  - Build-a-validated-sheet, cell lock/unlock simulator
- [ ] **#50 Macro Recording** — `macro-recording-ocn-level2-presentation.html` · large · 27 → 32
  - Action → recorded-code viewer, relative vs absolute recording, automation payback calculator
- [ ] **#79 Cleaning Messy Data** — `cleaning-messy-data-ocn-level2-presentation.html` · small · 14 → 28
  - Spot-the-problem cleaning game, before/after slider
- [ ] **#80 Pivot Table Analysis** — `pivot-table-analysis-ocn-level2-presentation.html` · small · 14 → 28
  - Drag fields to rows/columns/values with a live summary
- [ ] **#81 Correlation Warning** — `correlation-warning-ocn-level2-presentation.html` · small · 14 → 28
  - Scatter generator with r value, spurious correlation gallery, causation judge
- [ ] **#82 Power BI Dashboard** — `power-bi-dashboard-ocn-level2-presentation.html` · small · 14 → 28
  - Dashboard layout planner, chart-type chooser, KPI card design

### Core IT

- [ ] **#90 Virtualisation** — `virtualisation-ocn-level2-presentation.html` · large · 23 → 32
  - Lab planner, resource allocation calculator, cloud model matcher
- [ ] **#91 Building Networks** — `building-networks-ocn-level2-presentation.html` · medium · 17 → 32
  - Drag-to-build designer, IP plan generator, topology compare
- [ ] **#92 Making 568B Cables** — `making-568b-network-cables-ocn-level2-presentation.html` · medium · 16 → 30
  - Colour-order drag, crimp sequencer, tester diagnosis, straight vs crossover
- [x] **#93 Building Computers** — `building-computers-ocn-level2-presentation.html` · medium · 17 → 32 · (#48)
  - SVG fly-in assembler, compatibility checker (socket, RAM, PSU wattage), first-boot triage
- [x] **#94 Inside the PC** — `inside-the-pc-components-ocn-level2-presentation.html` · **reference deck** · 33 slides (#31)
  - Flip cards, motherboard hotspot explorer with quiz mode, drag-and-drop sort, timed challenge, 6-question quiz, glossary, particle canvas
- [ ] **#95 Storage Showdown** — `storage-showdown-ocn-level2-presentation.html` · medium · 16 → 30
  - Cost and speed calculator, copy-race, scenario judge
- [ ] **#96 Operating Systems Face-Off** — `os-face-off-ocn-level2-presentation.html` · medium · 15 → 30
  - Filterable feature matrix, OS chooser quiz, licence cost calculator
- [ ] **#97 Workstation Health & Safety** — `workstation-health-safety-ocn-level2-presentation.html` · medium · 15 → 30
  - Ergonomic desk hotspots with fix-it toggles, scored posture audit, DSE regulations
- [ ] **#98 Troubleshooting Like a Technician** — `troubleshooting-method-ocn-level2-presentation.html` · medium · 15 → 30
  - Five broken-scenario fault-finding simulator, hypothesis log, timed race
- [ ] **#99 Backups & Data Recovery** — `backups-data-recovery-ocn-level2-presentation.html` · medium · 15 → 30
  - 3-2-1 builder, ransomware timeline simulator, restore drill
- [ ] **#100 Parallels Desktop** — `parallels-virtualisation-ocn-level2-presentation.html` · small · 16 → 28
  - Setup sequencer, macOS/Windows compare, licensing and performance tips

### Cyber Security — Demos

- [ ] **#23 Wireshark Packet Capture** — `wireshark-packet-capture-ocn-level2-presentation.html` · medium · 16 → 30
  - Packet list explorer with a filter box over a canned capture, protocol colour key, authorisation gate
- [ ] **#24 Firewall Rules** — `firewall-rules-demo-ocn-level2-presentation.html` · medium · 17 → 30
  - Editable rule table with packet tester and top-down match highlight, rule-order pitfalls
- [ ] **#25 Port Scanning Safely** — `port-scanning-safely-ocn-level2-presentation.html` · medium · 16 → 30
  - Scan output reader, scope and authorisation checklist, port → service matcher
- [ ] **#26 Password Cracking Concepts** — `password-cracking-concepts-ocn-level2-presentation.html` · medium · 17 → 30
  - Entropy and time-to-crack calculator, hash vs plaintext demo, defence matcher
- [ ] **#27 Phishing Anatomy** — `phishing-anatomy-ocn-level2-presentation.html` · medium · 17 → 30
  - Clickable red-flag email dissector, header reader, report flow
- [ ] **#28 MFA & Authenticator Apps** — `mfa-authenticator-apps-ocn-level2-presentation.html` · medium · 17 → 30
  - Factor classifier, TOTP simulation, phishing-resistant vs push-fatigue compare
- [ ] **#29 USB Attack Awareness (Demo)** — `usb-attack-awareness-demo-ocn-level2-presentation.html` · medium · 17 → 30
  - HID attack timeline, found-a-USB decision tree, control matcher
- [ ] **#30 Flipper Zero Awareness** — `flipper-zero-awareness-ocn-level2-presentation.html` · medium · 17 → 30
  - Capability and legality matrix, safe demo script, defence checklist

### Cyber Security

- [ ] **#101 Firewalls** — `firewalls-ocn-level2-presentation.html` · large · 23 → 32
  - Rule evaluator, packet journey animation, port matcher, placement designer
- [ ] **#102 pfSense** — `pfsense-ocn-level2-presentation.html` · small · 17 → 30
  - Install and config sequencer, interface assignment simulator, rule builder, spare-PC build spec

### Offensive Cyber Security

- [ ] **#103 USB Attack Awareness (Rubber Ducky)** — `hak5-rubber-ducky-ocn-level2-presentation.html` · medium · 16 → 30
  - Keystroke payload timeline, defence layer builder, policy scenarios
- [ ] **#104 Metasploit** — `metasploit-ocn-level2-presentation.html` · medium · 18 → 32
  - Authorised testing lifecycle sequencer, module taxonomy explorer, ethics gate, mock console replay
- [ ] **#105 Password Power** — `password-security-ocn-level2-presentation.html` · medium · 15 → 30
  - Passphrase builder with strength meter, password manager comparison, breach-exposure concept
- [ ] **#106 Spot the Phish** — `spot-the-phish-ocn-level2-presentation.html` · medium · 15 → 32
  - Ten-message scored clinic with timer, red-flag reveal, class scoreboard
- [ ] **#107 Digital Footprint** — `digital-footprint-ocn-level2-presentation.html` · medium · 15 → 30
  - OSINT persona map builder, scored privacy checklist, before/after profile
- [ ] **#108 Malware Museum** — `malware-museum-ocn-level2-presentation.html` · medium · 15 → 30
  - Malware card sort (type → spread → defence), infection timeline, outbreak gallery
- [ ] **#109 Wi-Fi Security** — `wifi-security-ocn-level2-presentation.html` · medium · 15 → 30
  - Router hardening simulator with a live security score, WEP/WPA2/WPA3 compare
- [ ] **#110 Encryption Made Simple** — `encryption-basics-ocn-level2-presentation.html` · medium · 15 → 30
  - Live Caesar/XOR cipher tool, HTTPS handshake animation, symmetric vs asymmetric sort
- [ ] **#111 Staying Legal** — `staying-legal-data-protection-ocn-level2-presentation.html` · medium · 15 → 30
  - Six-scenario verdict judge with feedback, GDPR principle matcher, copyright and AUP cases
- [ ] **#112 O.MG Cable** — `omg-cable-ocn-level2-presentation.html` · small · 17 → 28
  - Real-vs-implant spotting compare, attack chain animation, procurement defences
- [ ] **#113 Flipper Zero** — `flipper-zero-ocn-level2-presentation.html` · small · 17 → 28
  - Capability explorer by radio band, legal boundary judge, blank-tag lab script
- [ ] **#114 WiFi Pineapple** — `wifi-pineapple-ocn-level2-presentation.html` · small · 17 → 28
  - Evil twin animation, client defences, authorised audit checklist

### Cyber Security — Level 5 Demos

- [ ] **#31 Vulnerable Web App Walkthrough** — `vulnerable-web-app-walkthrough-ocn-level5-presentation.html` · medium · 16 → 30
  - OWASP risk explorer, simulated injection sandbox, lab isolation checklist, report template
- [ ] **#32 Incident Response Mini-Demo** — `incident-response-mini-demo-ocn-level5-presentation.html` · medium · 16 → 30
  - Timed triage simulator (detect → contain → document), IR phase wheel, comms template
- [ ] **#33 Log Analysis** — `log-analysis-ocn-level5-presentation.html` · medium · 16 → 30
  - Searchable log viewer over sample data, event ID lookup, timeline builder, IOC spotter
- [ ] **#34 Disk Encryption** — `disk-encryption-ocn-level5-presentation.html` · medium · 16 → 30
  - Key and recovery flow diagram, BitLocker vs FileVault compare, lost-device cost calculator

### Emerging Technology (A/651/0447)

- [ ] **#115 Emerging Technology Overview** — `emerging-technology-ocn-level2-presentation.html` · large · 19 → 32
  - Adoption curve interactive, impact matrix, assessment command-word helper
- [ ] **#116 AI & Machine Learning** — `ai-ml-ocn-level2-presentation.html` · large · 18 → 32
  - Train-a-toy-classifier demo, supervised vs unsupervised sorter, bias case studies, hallucination spotter
- [ ] **#117 5G Technology** — `5g-ocn-level2-presentation.html` · large · 17 → 32
  - Latency race (3G/4G/5G), spectrum band explorer, smart city hotspots, health myth buster
- [ ] **#118 Blockchain** — `blockchain-ocn-level2-presentation.html` · large · 17 → 32
  - Live hash-and-chain demo where tampering visibly breaks the chain, consensus explainer, use-case judge, energy cost
- [ ] **#119 Internet of Things** — `iot-ocn-level2-presentation.html` · large · 19 → 32
  - Device → gateway → cloud flow builder, sensor picker, risk matrix, smart classroom design
- [ ] **#120 Quantum Computing** — `quantum-computing-ocn-level2-presentation.html` · large · 20 → 32
  - Superposition visualiser, classical vs quantum search race, post-quantum crypto timeline
- [ ] **#121 AR & VR** — `ar-vr-ocn-level2-presentation.html` · large · 21 → 32
  - Reality spectrum slider, use-case gallery, hardware compare, comfort and safety
- [ ] **#122 Meta Quest 3 & XR** — `meta-quest-3-xr-ocn-level2-presentation.html` · medium · 16 → 30
  - Headset hotspot tour, guardian setup sequencer, classroom safety checklist, XR careers
- [ ] **#123 Biotechnology & CRISPR** — `biotech-crispr-ocn-level2-presentation.html` · large · 18 → 32
  - Gene-edit sequence puzzle, ethics dilemma judge, bioinformatics and data link
- [ ] **#124 AI in Your Pocket** — `ai-prompting-ocn-level2-presentation.html` · medium · 15 → 30
  - Prompt improver sandbox with rubric scoring, hallucination spotting game, task suitability sorter
- [ ] **#125 Smart Home Build** — `smart-home-iot-design-ocn-level2-presentation.html` · medium · 16 → 30
  - Room design canvas, device → risk pairing, network plan
- [ ] **#126 Deepfakes & Misinformation** — `deepfakes-misinformation-ocn-level2-presentation.html` · medium · 15 → 30
  - Real vs AI image quiz with tell reveals, verification checklist builder, provenance and C2PA
- [ ] **#127 Wearables & Health Tech** — `wearables-health-tech-ocn-level2-presentation.html` · medium · 15 → 30
  - Sensor → phone → cloud flow builder, data ownership debate cards, accuracy myth buster
- [ ] **#128 Robots & Automation** — `robots-automation-ocn-level2-presentation.html` · medium · 15 → 30
  - Task automatability calculator, new-jobs generator, automation history timeline
- [ ] **#129 Green IT** — `green-it-ocn-level2-presentation.html` · medium · 16 → 30
  - kWh to cost and CO₂ calculator, e-waste routing game, lifecycle extension planner
- [x] **#145 Terafab** — `terafab-ocn-level2-presentation.html` · **new** · 32
  - Site hotspot explorer on the Grimes County overlay, chip-loop sequence builder, Earth vs orbit sort + timed round, 100M sq ft scale calculator

### Digital Skills & Employability

- [ ] **#130 Build Your First CV** — `cv-writing-ocn-level2-presentation.html` · medium · 15 → 30
  - CV builder with live preview and rubric score, before/after slider, keyword checker
- [ ] **#131 Spreadsheets That Work** — `spreadsheets-budgets-ocn-level2-presentation.html` · medium · 15 → 30
  - Budget builder with live totals and chart, formula matcher, conditional formatting demo
- [ ] **#132 Design a Poster / Flyer** — `poster-design-ocn-level2-presentation.html` · medium · 15 → 30
  - Before/after critique slider, contrast and palette tool, design brief judge
- [ ] **#133 Email & Online Etiquette** — `email-workplace-etiquette-ocn-level2-presentation.html` · medium · 15 → 30
  - Rewrite-the-email exercise with scoring, CC/BCC scenario judge, tone slider
- [ ] **#134 Cloud Collaboration** — `cloud-collaboration-ocn-level2-presentation.html` · medium · 15 → 30
  - Permission chooser scenarios, version history timeline, live conflict simulator
- [ ] **#135 IT Careers & Pathways in NI** — `it-careers-northern-ireland-ocn-level2-presentation.html` · medium · 15 → 30
  - Role explorer cards with skills and salary, skills → role matcher, action plan builder

### Cloud / Collaboration — Demos

- [ ] **#35 OneDrive / SharePoint Permissions** — `onedrive-sharepoint-permissions-ocn-level2-presentation.html` · medium · 16 → 30
  - Sharing link chooser, effective access calculator, oversharing scenarios
- [ ] **#36 Version History Restore** — `version-history-restore-ocn-level2-presentation.html` · medium · 16 → 30
  - Version timeline scrubber with restore, delete-recovery flow
- [x] **#72 SaaS/PaaS/IaaS Comparison** — `saas-paas-iaas-comparison-ocn-level2-presentation.html` · small · 14 → 28 · (#38)
  - Responsibility split drag, service classifier game
- [x] **#73 SharePoint/Teams Setup** — `sharepoint-teams-setup-ocn-level2-presentation.html` · small · 14 → 28 · (#38)
  - Site setup sequencer, structure planner, governance tips
- [x] **#74 Cloud Sync Conflict** — `cloud-sync-conflict-ocn-level2-presentation.html` · small · 14 → 28 · (#38)
  - Two-user edit simulator producing conflict copies, resolution decision tree
- [x] **#75 Storage Quota Management** — `storage-quota-management-ocn-level2-presentation.html` · small · 14 → 28 · (#38)
  - Quota analyser widget, safe cleanup rules, retention policy

### IoT — Demos

- [ ] **#37 IoT Sensor Demo** — `iot-sensor-demo-ocn-level2-presentation.html` · medium · 16 → 30
  - Simulated live sensor stream with thresholds and chart, wiring hotspots, dashboard build
- [ ] **#38 Smart Device Network Isolation** — `smart-device-network-isolation-ocn-level2-presentation.html` · medium · 16 → 30
  - Segmentation drag board, attack path animation
- [ ] **#83 micro:bit Sensor Demo** — `microbit-sensor-demo-ocn-level2-presentation.html` · small · 14 → 28
  - Block-code preview, data logging table, calibration steps
- [ ] **#84 Node-RED Flow** — `node-red-flow-ocn-level2-presentation.html` · small · 14 → 28
  - Mini drag-node flow canvas, debug pane, flow challenge
- [ ] **#85 MQTT Messaging** — `mqtt-messaging-ocn-level2-presentation.html` · small · 14 → 28
  - Publish/subscribe simulator with topics and wildcards, QoS compare, broker security
- [ ] **#86 IoT Security Teardown** — `iot-security-teardown-ocn-level2-presentation.html` · small · 14 → 28
  - Scored weakness checklist, default-credential case studies, hardening steps
- [ ] **#87 Packet Tracer Smart Home** — `packet-tracer-smart-home-ocn-level2-presentation.html` · small · 14 → 28
  - Topology hotspots, IoT device control simulator, scenario tasks

### Project & Maker

- [ ] **#136 Build a One-Page Website** — `html-css-first-website-ocn-level2-presentation.html` · medium · 16 → 32
  - Live HTML/CSS editor with iframe preview, tag matcher, colour playground, publish steps
- [ ] **#137 Block Coding a Game or Quiz** — `scratch-coding-game-ocn-level2-presentation.html` · medium · 16 → 30
  - Block assembly puzzle, sprite and event matcher, debugging challenge
- [ ] **#138 micro:bit Mini-Project** — `microbit-mini-project-ocn-level2-presentation.html` · medium · 16 → 30
  - Project chooser, flowchart → blocks sequencer, simulator preview, demo rubric
- [ ] **#139 Plan a Small-Office Network** — `small-office-network-design-ocn-level2-presentation.html` · medium · 16 → 32
  - Drag-to-design canvas with budget, IP plan generator, pitch rubric, security review
- [ ] **#140 Cable to Cloud** — `cable-to-cloud-ocn-level2-presentation.html` · medium · 16 → 30
  - Six-station relay board with timing, end-to-end packet journey animation
- [ ] **#141 VEX Robotics & Base Bot** — `vex-robotics-base-bot-ocn-level2-presentation.html` · medium · 18 → 32
  - Build step sequencer, motor and port config simulator, driver control mapping, challenge course
- [ ] **#143 VEXcode Tutorial** — `vexcode-tutorial.html` · **scroll page, not a deck**
  - Keep the scroll format and VEX palette. Add a sticky progress rail, section checkpoint questions, copy-code buttons, block assembly interactive
- [x] **#144 Introducing Strawbees** — `strawbees-intro-ocn-level2-presentation.html` · **new** · 32 · (#49)
  - Connector flip cards, joint hotspot explorer, rigidity load simulator, tetrahedron sequence builder, kit-role sort + timed challenge

### Programming — Demos

- [x] **#51 Debugger Walkthrough** — `debugger-walkthrough-ocn-level2-presentation.html` · small · 15 → 28 · (#33)
  - Step-through debugger simulator with breakpoints and a watch panel
- [x] **#52 Trace Table Demo** — `trace-table-demo-ocn-level2-presentation.html` · small · 15 → 28 · (#33)
  - Fillable, validated trace table, dry-run race
- [x] **#53 File Handling** — `file-handling-ocn-level2-presentation.html` · small · 15 → 28 · (#33)
  - Read/write simulator with modes, missing-file error scenarios, CSV vs txt
- [x] **#54 Input Validation** — `input-validation-ocn-level2-presentation.html` · small · 15 → 28 · (#33)
  - Live validator sandbox for normal, extreme and erroneous input, test plan builder, message writing
- [x] **#55 Refactoring Bad Code** — `refactoring-bad-code-ocn-level2-presentation.html` · small · 15 → 28 · (#33)
  - Before/after diff slider, code smell spotter, behaviour-preservation check
- [x] **#56 Git Version Control Basics** — `git-version-control-basics-ocn-level2-presentation.html` · small · 15 → 28 · (#33)
  - Command → repo state simulator, staging area animation, log timeline
- [x] **#88 GitHub & CI/CD** — `github-cicd-ocn-level2-presentation.html` · small · 16 → 30 · (#46)
  - PR review simulator, workflow builder, pipeline status animation, branch protection

### Website Development — Demos

- [x] **#57 Browser DevTools** — `browser-devtools-ocn-level2-presentation.html` · small · 14 → 28 · (#35)
  - Mock DevTools panel (Elements / Console / Network) with inspect challenges
- [x] **#58 Responsive Design** — `responsive-design-ocn-level2-presentation.html` · small · 14 → 28 · (#35)
  - Viewport width slider with live layout, breakpoint builder, mobile-first ordering
- [x] **#59 Accessibility Audit** — `accessibility-audit-ocn-level2-presentation.html` · small · 14 → 28 · (#35)
  - Live contrast checker, alt-text writing exercise, screen reader path simulator, scored WCAG checklist
- [x] **#60 Form Validation** — `form-validation-ocn-level2-presentation.html` · small · 15 → 28 · (#35)
  - Side-by-side HTML5 vs JS validation sandbox, error message design, edge case tests
- [x] **#61 W3C Validation** — `w3c-validation-ocn-level2-presentation.html` · small · 14 → 28 · (#34)
  - Validator error decoder, fix-the-markup game, workflow steps
- [x] **#62 Website Hosting** — `website-hosting-ocn-level2-presentation.html` · small · 14 → 28 · (#34)
  - Request path animation, 404 triage, deploy sequencer, hosting type compare

### Mobile Apps — Demos

- [x] **#63 Android Emulator Setup** — `android-emulator-setup-ocn-level2-presentation.html` · small · 14 → 28 · (#36)
  - AVD config builder, hardware profile compare, troubleshooting matrix
- [x] **#64 App Permissions** — `app-permissions-ocn-level2-presentation.html` · small · 14 → 28 · (#36)
  - Permission prompt simulator with risk score, least-privilege audit of a sample app
- [x] **#65 Sensor Input** — `sensor-input-ocn-level2-presentation.html` · small · 14 → 28 · (#36)
  - Tilt/shake simulator with a button fallback, sensor → app event matcher
- [x] **#66 Native vs Web vs Hybrid** — `native-vs-web-vs-hybrid-ocn-level2-presentation.html` · small · 14 → 28 · (#36)
  - Trade-off matrix, scenario chooser, cost/performance slider

### Software Testing — Demos

- [x] **#67 Good Bug Report** — `good-bug-report-ocn-level2-presentation.html` · small · 14 → 28 · (#37)
  - Report builder with rubric scoring, bad vs good compare, repro step ordering
- [x] **#68 Regression Testing** — `regression-testing-ocn-level2-presentation.html` · small · 14 → 28 · (#37)
  - Suite runner simulator (change code → see which tests break), regression pack builder
- [x] **#69 Unit Test Runner** — `unit-test-runner-ocn-level2-presentation.html` · small · 14 → 28 · (#37)
  - Pass/fail output reader, write-the-assertion exercise, red-green cycle animation
- [x] **#70 Usability Test Observation** — `usability-test-observation-ocn-level2-presentation.html` · small · 14 → 28 · (#37)
  - Note-taking simulator, coaching-vs-observing judge, findings severity ranking
- [x] **#71 Load/Stress Concept** — `load-stress-concept-ocn-level2-presentation.html` · small · 14 → 28 · (#37)
  - Load ramp simulator with response time chart, breaking point finder, safe lab rules

---

*Aligned to the OCN NI Level 2 Diploma in Information Technology content library.
Topic ideas and practical hooks for several of these decks come from
[PRESENTATION-IDEAS.md](PRESENTATION-IDEAS.md).*
