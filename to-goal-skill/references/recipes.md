# Skill recipes (to-goal-skill)

Use in **Phase 2 before** local inventory. Pick the best-fitting recipe, then verify each named skill exists locally (or plan install). Adapt ACs to the user’s Goal; keep verify methods concrete.

If no recipe fits: skip to local inventory per [matching.md](matching.md).

---

## R1 — Marketing / product landing page

**Use when:** ship a landing or promo page (brand, hero, CTA).

| Skill | Role |
|-------|------|
| `frontend-design` or `impeccable` / `high-end-visual-design` | UI / visual quality |
| `verification-before-completion` (or general verify) | Evidence pass |
| `playwright` / browser tools (optional) | Visual / interaction check |

**Default mode:** light if ≤2 ACs; full if brand system + multi-page.

**Starter ACs:**

- [ ] AC1: Route `/` (or agreed URL) loads — verify: HTTP 200 / app opens
- [ ] AC2: First viewport has brand, one headline, one CTA, dominant visual — verify: screenshot
- [ ] AC3: Looks on-brand / premium — verify: `needs-human-signoff`

---

## R2 — Bugfix + proof

**Use when:** reproduce, fix, and prove a defect is gone.

| Skill | Role |
|-------|------|
| `systematic-debugging` | Root cause before patch |
| `test-driven-development` (when tests exist / fit) | Fail then fix |
| domain skill or general coding | Implement fix |

**Default mode:** light for single known bug; full if unclear system boundary.

**Starter ACs:**

- [ ] AC1: Failure reproduced (or documented as intermittent with steps) — verify: command/log/screenshot
- [ ] AC2: Fix landed — verify: diff / tests
- [ ] AC3: Original failure no longer reproduces — verify: same repro steps PASS

---

## R3 — PRD → trackable issues

**Use when:** turn a product idea/spec into PRD then implementation issues.

| Skill | Role |
|-------|------|
| `brainstorming` (optional) | Clarify before PRD |
| `to-prd` or `prd` | PRD artifact |
| `to-issues` | Slice into issues |

**Default mode:** full (usually ≥3 ACs).

**Starter ACs:**

- [ ] AC1: PRD exists at agreed path/tracker — verify: file or issue URL
- [ ] AC2: Issues are vertical slices with acceptance notes — verify: issue list
- [ ] AC3: Scope/out-of-scope explicit — verify: section present; `needs-human-signoff` on priority

---

## R4 — README + i18n

**Use when:** create or upgrade README and ship a second language.

| Skill | Role |
|-------|------|
| `create-readme` or `crafting-effective-readmes` | README structure |
| `readme-i18n` | Localization / language switch |

**Default mode:** light.

**Starter ACs:**

- [ ] AC1: Primary README answers install + usage — verify: headings present
- [ ] AC2: Second language file or switcher works — verify: linked file opens / switcher renders
- [ ] AC3: Tone/clarity OK — verify: `needs-human-signoff`

---

## R5 — Deck or document deliverable

**Use when:** the primary output is `.pptx`, `.docx`, or `.pdf`.

| Skill | Role |
|-------|------|
| `pptx` / `docx` / `pdf` | Authoring |
| `copy-editing` or `humanizer-zh` (optional) | Prose polish |

**Default mode:** light for single artifact; full if multi-stakeholder review.

**Starter ACs:**

- [ ] AC1: File opens at agreed path — verify: file exists + opens
- [ ] AC2: Required sections present — verify: checklist against outline
- [ ] AC3: Audience-ready — verify: `needs-human-signoff`
