---
name: to-goal-skill
description: Use when the user invokes /to-goal-skill or to-goal-skill, or asks to combine/orchestrate multiple skills to finish a goal end-to-end (e.g. skill combo, orchestrate skills, multi-skill plan).
license: MIT
compatibility: Requires filesystem access to read installed skills; network + Node.js/npx for skills.sh discovery and optional installs. Portable Agent Skills (SKILL.md) format.
metadata:
  author: WINDGAND
  version: "1.2.0"
  attribution: "Clarify phase derived from Matt Pocock grill-me/grilling (MIT); matching adapted from vercel-labs find-skills; orchestrate/retry adapted from obra/superpowers writing-plans + executing-plans; verify adapted from obra/superpowers verification-before-completion"
---

# To Goal Skill

Meta-orchestrator: **Clarify → Match → Approve → Execute → Verify → Retry**.

Announce: `Using to-goal-skill to clarify, orchestrate skills, and verify the goal.`

Talk in the user’s language. This file is the process source of truth.

**Violating the letter of the Hard Gates is violating the spirit of this skill.**

## Complexity gate (first)

Before Phase 1, classify the request:

| Route | When | Action |
|-------|------|--------|
| **Decline** | Single obvious skill; pure Q&A; user wants no-plan hotfix; orchestration only “for structure” | One line: not using to-goal-skill → use that skill / answer / act. Stop. |
| **Continue** | Explicit invoke, or clearly needs 2+ skills / end-to-end combo | Enter pipeline below |

## Modes (default: light)

**Default = light.** Upgrade to **full** only if: user asks full/cloud search, or goal spans multiple sessions, or (ACs ≥3 **and** user did not ask to stay light/time-boxed).

| | Light (default) | Full |
|---|-----------------|------|
| Clarify | ≤1 round or one-shot Goal+ACs confirm | [references/grilling.md](references/grilling.md) |
| Match | Recipes → local only ([references/matching.md](references/matching.md)) | Recipes → local → cloud if needed |
| Retry approve | “auto-retry this goal” → reuse approval for attempts 2–3 (installs still need consent) | New card approval each retry |

Hard Gates always apply.

## Hard Gates

1. No matching/execution until Goal + Acceptance Criteria are confirmed.
2. No business-file edits / cloud installs until card approved **and** session `approved: true`.
3. No completion claims without fresh verification evidence.
4. No silent cloud installs — ask first.
5. Max 3 attempts (initial + 2 retries), then stop and report gaps.

Red flags / excuse counters: [references/pressure-evals.md](references/pressure-evals.md#discipline).

## Session state (portable latch)

Path: `docs/to-goal/.session.md` (or user-specified). Create/update **before** showing the card; keep in sync.

```markdown
# to-goal-skill session
active: true
mode: light
attempt: 1
approved: false
goal: ""
## Acceptance Criteria
- [ ] AC1: ... — verify: ...
## Skill Combo
- none yet
## Notes
- 
```

Rules:

- `approved: false` → do **not** edit business files; do **not** run `npx skills add …`
- Allowed while unapproved: chat, reads, and writes under `docs/to-goal/`
- On user approval: set `approved: true`, then execute
- On decline/finish: set `active: false` (or delete session)

Optional Cursor hard-block: see repo `integrations/cursor/`.

## Portability

Use host tools; do not assume Cursor/Claude/Codex-only APIs. Local skill roots include `~/.agents/skills`, `~/.cursor/skills`, `~/.claude/skills`, `~/.codex/skills`, `~/.trae-cn/skills`, and project `.agents/skills` / `.cursor/skills` / `.claude/skills`. Coarse-filter by description; read full `SKILL.md` only for shortlist.

## Phase 1 — Clarify

Light: draft Goal + ACs (each with verify; subjective → `needs-human-signoff`) and confirm.  
Full: follow [references/grilling.md](references/grilling.md).

## Phase 2 — Match

Follow [references/matching.md](references/matching.md): **recipes first** ([references/recipes.md](references/recipes.md)) → local inventory → cloud only in full (or if user asks). Combo ≤5; exclude `to-goal-skill` itself.

## Phase 3 — Orchestration card

Update session file, present **exactly** this card, wait for approval:

```markdown
## Goal
<one sentence>

## Acceptance Criteria
- [ ] AC1: <criterion> — verify: <method> [`needs-human-signoff` if needed]

## Skill Combo
| Skill | Source | Fit | Why |
|-------|--------|-----|-----|
| <name> | local / cloud (not installed) | excellent/good/partial | <one line> |

## Workflow
1. <step> — Skill: <name|none> — Covers: AC# — Done when: <signal>

## Install requests (if any)
- none

## Attempt
<n> of 3
Mode: <light|full>
Session: docs/to-goal/.session.md
```

Reject → revise card only. Re-clarify only if user asks. Approved installs → install, confirm loadable, then execute.  
Save/export card only if user asks (`docs/to-goal/YYYY-MM-DD-<slug>.md` if they defer).

## Phase 4 — Execute

Only when `approved: true`. For each step: announce → read that skill → follow it → one-line result + ACs advanced. Skill `none` → general capability.  
Blocked mid-flight → stop, return Phase 2→3 (same attempt until new card approved). Do not silently add skills.

## Phase 5 — Verify

No completion claims without fresh evidence. For each AC: identify → run → read → PASS/FAIL + evidence. `needs-human-signoff` → ask user; never auto-PASS.

```markdown
## Verification (<attempt> of 3)
| AC | Result | Evidence |
|----|--------|----------|
| AC1 | PASS/FAIL | <short evidence> |

## Outstanding gaps
- ...
```

## Phase 6 — Retry

On FAIL and attempts used under 3: keep Goal → Phase 2→3→4→5 → increment attempt. After 3: stop; summarize gaps; offer narrow / partial / switch. Do not loop.

## Evals

Before release: [references/pressure-evals.md](references/pressure-evals.md).

## Attribution

Clarify: Matt Pocock grill-me/grilling (MIT). Match: vercel-labs find-skills. Orchestrate/Retry: obra/superpowers writing-plans + executing-plans. Verify: verification-before-completion.
