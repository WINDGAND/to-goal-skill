# Skill Matching

Adapted from vercel-labs `find-skills` discovery and quality checks, plus local-first rules for `to-goal-skill`.

## Fit Tiers

Score every candidate skill against the current Goal (and the workflow step it would cover):

| Tier | Meaning |
|------|---------|
| `excellent` | Directly built for this job; instructions clearly cover the step |
| `good` | Strong match; minor gaps you can bridge without another skill |
| `partial` | Related but incomplete; would need another skill or heavy improvisation |
| `poor` | Weak / coincidental keyword overlap |

"One tier lower" means at least one full tier gap (e.g. local `partial` vs cloud `good`).

## Discovery Order

1. **Inventory local skills** the current agent can already load (user/global and project skill dirs for this runtime).
2. **Leaderboard / known high-quality sources** when relevant ([skills.sh](https://skills.sh/)).
3. **Cloud search**: `npx skills find <query>` with specific keywords; try alternate phrasings if needed.

## Local-First Policy

- If a local skill is `good` or `excellent` for a step, prefer it.
- Do **not** install cloud skills when local coverage is already adequate.
- Avoid accumulating low-use installs.

## When to Ask Before Installing Cloud Skills

Ask the user for consent to install **only if all** are true:

1. Best local fit is missing, `poor`, or at least **one tier below** the best cloud candidate
2. The cloud candidate is **high-reputation** (see below)
3. Installing would materially improve the plan (not a cosmetic upgrade)

Never install cloud skills silently.

## High-Reputation Bar (Cloud)

Treat a cloud skill as high-reputation if **any** of:

- Installs ≥ 1K, or
- Trusted publisher (`anthropics`, `vercel-labs`, `microsoft`, `mattpocock`, `obra`, or equally well-known official orgs), or
- Source repo stars ≥ 1K

**Hard caution:** installs < 100 → do not recommend unless the user explicitly wants an obscure skill.

When fits are close, break ties toward higher installs / stronger publisher reputation.

## Combo Rules

- Max **5** skills per attempt; prefer fewer.
- If one skill covers steps 1–3 well, assign that one skill to those steps — do not add extra skills for "structure".
- Prefer non-overlapping responsibilities.
- Exclude `to-goal-skill` itself from the combo (it is the orchestrator).

## No Adequate Skill

If neither local nor cloud yields at least `good` coverage:

1. Say what is missing
2. Build a **no-skill / few-skill** plan using general agent capabilities
3. Still present the approval card before acting
