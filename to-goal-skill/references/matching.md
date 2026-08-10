# Skill Matching

Adapted from vercel-labs `find-skills`, plus local-first rules and built-in recipes for `to-goal-skill`.

## Fit Tiers

| Tier | Meaning |
|------|---------|
| `excellent` | Directly built for this job; instructions clearly cover the step |
| `good` | Strong match; minor gaps you can bridge without another skill |
| `partial` | Related but incomplete; would need another skill or heavy improvisation |
| `poor` | Weak / coincidental keyword overlap |

"One tier lower" means at least one full tier gap (e.g. local `partial` vs cloud `good`).

## Discovery Order

1. **Recipes first** (below): if one fits, use its skill list + starter ACs (adapt to installed names).
2. **Local inventory**: coarse-filter by name/description; read full `SKILL.md` only for shortlist. Confirm recipe skills exist; swap missing ones for equal/better local fits.
3. **Cloud** ([skills.sh](https://skills.sh/) / `npx skills find <query>`): **full mode only**, or when the user asks.

**Light mode (default):** stop after step 2 unless the user asks for cloud search/install.

## Recipes

Pick the best fit, then verify skills exist locally (or plan install). If none fit → continue with local inventory.

### R1 — Landing / promo page

**When:** marketing or product landing (brand, hero, CTA).  
**Skills:** `frontend-design` or `impeccable` / `high-end-visual-design`; optional browser/`playwright` for checks.  
**Mode:** light if ≤2 ACs.  
**Starter ACs:** `/` loads (HTTP 200); first viewport has brand + headline + CTA + dominant visual (screenshot); looks on-brand — `needs-human-signoff`.

### R2 — Bug fix + proof

**When:** reproduce, fix, prove gone.  
**Skills:** `systematic-debugging`; `test-driven-development` when tests fit; domain/general coding for the patch.  
**Mode:** light for a single known bug.  
**Starter ACs:** failure reproduced (log/screenshot); fix landed (diff/tests); repro no longer fails.

### R3 — PRD → issues

**When:** idea/spec → PRD → implementation issues.  
**Skills:** optional `brainstorming`; `to-prd` or `prd`; `to-issues`.  
**Mode:** usually full.  
**Starter ACs:** PRD at agreed path/URL; issues are vertical slices; scope/out-of-scope explicit (`needs-human-signoff` on priority).

### R4 — README + i18n

**When:** create/upgrade README and a second language.  
**Skills:** `create-readme` or `crafting-effective-readmes`; `readme-i18n`.  
**Mode:** light.  
**Starter ACs:** primary README has install + usage; second language/switcher works; clarity — `needs-human-signoff`.

### R5 — Deck or document

**When:** primary output is `.pptx` / `.docx` / `.pdf`.  
**Skills:** `pptx` / `docx` / `pdf`; optional `copy-editing` or `humanizer-zh`.  
**Mode:** light for one artifact.  
**Starter ACs:** file opens; required sections present; audience-ready — `needs-human-signoff`.

## Local-First Policy

- Prefer local `good` / `excellent` fits; do not install when local coverage is adequate.
- Prefer a recipe combo when it maps cleanly; do not add skills for “structure”.
- Avoid low-use installs.

## When to Ask Before Installing Cloud Skills

Ask only if **all** are true:

1. Best local fit is missing, `poor`, or at least one tier below the best cloud candidate  
2. Cloud candidate is high-reputation (installs ≥ 1K, or trusted publisher `anthropics` / `vercel-labs` / `microsoft` / `mattpocock` / `obra` / equivalent, or repo stars ≥ 1K)  
3. Install would materially improve the plan  

Never install silently. Installs under 100 → do not recommend unless the user asks for that obscure skill.

## Combo Rules

- Max **5** skills; prefer fewer; non-overlapping roles.
- One skill may cover multiple steps.
- Exclude `to-goal-skill` itself from the combo.

## No Adequate Skill

If recipe + local (+ cloud when allowed) lack at least `good` coverage: say what is missing, build a no-skill / few-skill plan, still present the approval card before acting.
