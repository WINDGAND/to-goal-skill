---
name: to-goal-skill
description: Use when the user invokes /to-goal-skill or to-goal-skill, or asks to combine/orchestrate multiple skills to finish a goal end-to-end (e.g. skill combo, orchestrate skills, multi-skill plan).
license: MIT
compatibility: Requires filesystem access to read installed skills; network + Node.js/npx for skills.sh discovery and optional installs. Portable Agent Skills (SKILL.md) format.
metadata:
  author: WINDGAND
  version: "1.2.2"
  attribution: "Clarify phase derived from Matt Pocock grill-me/grilling (MIT); matching adapted from vercel-labs find-skills; orchestrate/retry adapted from obra/superpowers writing-plans + executing-plans; verify adapted from obra/superpowers verification-before-completion"
---

# To Goal Skill

Meta-orchestrator: **Clarify → Match → Approve → Execute → Verify → Retry**.

Announce: `Using to-goal-skill to clarify, orchestrate skills, and verify the goal.`

Talk in the user’s language. This file is the process source of truth.

**Violating the letter of the Hard Gates is violating the spirit of this skill.**

## Complexity gate (first)

| Route | When | Action |
|-------|------|--------|
| **Decline** | Single obvious skill; pure Q&A; no-plan hotfix; orchestration only “for structure”; **or** user says orchestrate/to-goal-skill but the job is still a tiny one-step fix | One line: skip to-goal-skill → use that skill / answer / act. Stop. Explicit invoke does **not** force Continue on a trivial task. |
| **Continue** | Explicit invoke **and** clearly needs 2+ skills / end-to-end combo | Enter pipeline below |

## Modes (default: light)

**Default = light.** Upgrade to **full** only if: user asks full/cloud search, or goal spans multiple sessions, or (ACs ≥3 **and** user did not ask to stay light/time-boxed).

| | Light (default) | Full |
|---|-----------------|------|
| Clarify | ≤1 round or one-shot Goal+ACs confirm | [references/grilling.md](references/grilling.md) |
| Match | Recipes → local ([references/matching.md](references/matching.md)) | Recipes → local → cloud if needed |
| Retry approve | “auto-retry this goal” → reuse approval for attempts 2–3 **only after** attempt-1 card was approved (installs still need consent) | New card approval each retry |

Hard Gates always apply. Hurry / “just do it” never waives them.

## Hard Gates

1. No matching/execution until Goal + Acceptance Criteria are confirmed.
2. No business-file edits, **no new deliverables** (code, pages, PRD/issues/docs outside `docs/to-goal/`), and no cloud installs until card approved **and** session `approved: true`.
3. No completion claims without fresh verification evidence.
4. No silent cloud installs — ask first.
5. Max 3 attempts (initial + 2 retries), then stop and report gaps.

**Red flags — STOP:** skip clarify; edit or create deliverables before approval; claim done without verify; silent `npx skills add`; auto-PASS `needs-human-signoff`; loop past 3 attempts; force pipeline on a Decline-route task; treat “auto-retry” as skip-first-approval.

| Excuse | Reality |
|--------|---------|
| "User is in a hurry" / "just do it" / "don't ask" | Stay **light**; still confirm Goal+ACs and get card approval — zero deliverables before that |
| "I agree to auto-retry" | Reuse approval for attempts **2–3** only; attempt **1** still needs the card |
| "I'll verify after done" | Evidence first, then completion claims |
| "Looks fine to me" | `needs-human-signoff` → ask the user |
| "They asked to orchestrate a typo/hotfix" | **Decline**; one-step jobs skip this skill |

## Session state

Path: `docs/to-goal/.session.md` (or user-specified). Create/update **before** showing the card.

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
```

- `approved: false` → no business-file edits; no `npx skills add`
- Allowed while unapproved: chat, reads, writes under `docs/to-goal/`
- On approval → `approved: true` then execute; on finish/decline → `active: false`

## Portability

Use host tools; do not assume Cursor/Claude/Codex-only APIs. Skill roots include `~/.agents/skills`, `~/.cursor/skills`, `~/.claude/skills`, `~/.codex/skills`, `~/.trae-cn/skills`, and project `.agents/skills` / `.cursor/skills` / `.claude/skills`. Coarse-filter by description; read full `SKILL.md` only for shortlist.

## Phase 1 — Clarify

Light: draft Goal + ACs (each with verify; subjective → `needs-human-signoff`) and confirm.  
Full: follow [references/grilling.md](references/grilling.md).

## Phase 2 — Match

Follow [references/matching.md](references/matching.md): recipes → local → cloud only in full (or if user asks). Combo ≤5; exclude `to-goal-skill` itself.

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
Save/export only if user asks (`docs/to-goal/YYYY-MM-DD-<slug>.md` if they defer).

## Phase 4 — Execute

Only when `approved: true`. For each step: announce → read that skill → follow it → one-line result + ACs advanced. Skill `none` → general capability.  
Blocked mid-flight → Phase 2→3 (same attempt until new card approved). Do not silently add skills.

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

## Attribution

Clarify: Matt Pocock grill-me/grilling (MIT). Match: vercel-labs find-skills. Orchestrate/Retry: obra/superpowers writing-plans + executing-plans. Verify: verification-before-completion.
