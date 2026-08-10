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

Rate fit only after reading the candidate's `SKILL.md` (the shortlist rule already requires this). Cloud candidates not yet installed: rate from listing info and mark Fit as `预估` in the card. The card's **Why** column must cite what the skill's SKILL.md actually covers — never its name or vibe.

## Discovery Order

1. **Recipes first** (below): use one only when the goal squarely matches its **When** clause — resemblance ≠ fit; when unsure, fall through to step 2. Adapt to installed skills by description/role, not by name.
2. **Local inventory**: coarse-filter by name/description; read full `SKILL.md` only for shortlist. Confirm recipe skills exist; swap missing ones for equal/better local fits.
3. **Cloud** ([skills.sh](https://skills.sh/) / `npx skills find <query>`): **full mode only**, or when the user asks.

**Light mode (default):** stop after step 2 unless the user asks for cloud search/install. If the best local fit is below `good`, the card's Install-requests section must note "本地匹配一般；可升级 full 搜云端" — inform, never auto-search.

## Recipes

Pick the best fit, then verify skills exist locally (or plan install). If none fit → continue with local inventory.

**Starter ACs are drafting material, not authority:** merge / dedupe / rewrite them into the user-confirmed ACs — never append alongside or replace them. Only user-confirmed ACs count toward the full-mode trigger (ACs ≥3).

### R1 — Landing / promo page

**When:** marketing or product landing (brand, hero, CTA).  
**Skills:** `frontend-design` or `impeccable` / `high-end-visual-design`; optional browser/`playwright` for checks.  
**Mode:** light.  
**Starter ACs:** `/` loads (HTTP 200); first viewport has brand + headline + CTA + dominant visual (screenshot); looks on-brand — `needs-human-signoff`.

### R2 — Bug fix + proof

**When:** reproduce, fix, prove gone.  
**Skills:** `systematic-debugging`; `test-driven-development` when tests fit; domain/general coding for the patch.  
**Mode:** light for a single known bug.  
**Starter ACs:** failure reproduced (log/screenshot); fix landed (diff/tests); repro no longer fails.

### R3 — PRD → issues

**When:** idea/spec → PRD → implementation issues.  
**Skills:** optional `brainstorming`; `to-prd` or `prd`; `to-issues`.  
**Mode:** advisory only — the Modes table in SKILL.md is the sole upgrade authority.  
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

Never install silently. Installs under 100 → do not recommend unless the user asks for that obscure skill. When asking, include the candidate's maintenance freshness if visible (last commit/release); long-unmaintained → drop the recommendation one notch.

## Combo Rules

- Max **5** skills; prefer fewer; non-overlapping roles. Overlapping candidates → most-specific-wins (description most narrowly covering the step); ≤1 skill per role; log near-miss losers in the session file.
- One skill may cover multiple steps.
- Exclude `to-goal-skill` itself from the combo.

## No Adequate Skill

If recipe + local (+ cloud when allowed) lack at least `good` coverage: say what is missing, build a no-skill / few-skill plan, still present the approval card before acting.
