---
name: to-goal-skill
description: Use when the user invokes /to-goal-skill or to-goal-skill, or asks to combine/orchestrate multiple skills to finish a goal end-to-end (e.g. skill combo, orchestrate skills, multi-skill plan).
license: MIT
compatibility: Requires filesystem access to read installed skills; network + Node.js/npx for skills.sh discovery and optional installs. Portable Agent Skills (SKILL.md) format.
metadata:
  author: WINDGAND
  version: "1.3.6"
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

Scope can sharpen mid-clarify: if answers shrink the job to a one-step fix, de-escalate — announce Decline and just do it.

## Modes (default: light)

**Default = light.** Upgrade to **full** only if: user asks full/cloud search, or goal spans multiple sessions, or (ACs ≥3 **and** user did not ask to stay light/time-boxed). This table is the only upgrade authority — recipe Mode fields are advisory, and only user-confirmed ACs count toward the ACs ≥3 trigger.

| | Light (default) | Full |
|---|-----------------|------|
| Clarify | Subjective/vague goal → **≥1 targeted question round first** (one-shot confirm forbidden); already-specific goal → one-shot Goal+ACs confirm | [references/grilling.md](references/grilling.md) |
| Match | Recipes → local ([references/matching.md](references/matching.md)) | Recipes → local → cloud if needed |
| Retry approve | “auto-retry this goal” → reuse approval for attempts 2–3 **only after** attempt-1 card was approved (installs still need consent); reuse void if the retry card changes skills/ACs — re-approve | New card approval each retry |

Hard Gates always apply. Hurry / “just do it” never waives them.

## Hard Gates

1. No matching/execution until Goal + Acceptance Criteria are confirmed — built from the user's own answers (what's wrong now / what they want / how they'll judge), paraphrased back for an explicit yes, never from agent guesses.
2. No business-file edits, **no new deliverables** (code, pages, PRD/issues/docs outside `docs/to-goal/`), and no cloud installs until card approved **and** session `approved: true`.
3. No completion claims without fresh verification evidence.
4. No silent cloud installs — ask first.
5. Max 3 attempts (initial + 2 retries), then stop and report gaps.

**Red flags — STOP:** skip clarify or the read-back paraphrase; draft Goal/ACs for a subjective/vague request without first asking what's wrong now, what effect is wanted, and how the user will judge; edit or create deliverables before approval; claim done without verify; silent `npx skills add`; auto-PASS `needs-human-signoff`; loop past 3 attempts; force pipeline on a Decline-route task; treat “auto-retry” as skip-first-approval; overrun declared Scope without re-carding; pre-claim AC progress during Execute.

| Excuse | Reality |
|--------|---------|
| "User is in a hurry" / "just do it" / "don't ask" | Stay **light**; still confirm Goal+ACs and get card approval — zero deliverables before that |
| "The need is obvious — no need to ask" | Subjective/vague is never obvious: "obvious" = guessing. Ask what's wrong / what's wanted / how they'll judge first |
| "User said 你看着办 — my pick is confirmed" | Proceed, but flag the direction as agent's guess in the card; related ACs stay `needs-human-signoff` |
| "User replied 嗯 / 我看看 — close enough" | Ambiguous replies are never approval — ask “是否批准？” and wait for an explicit word |
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
- After Match, record the shortlist + rejection reasons in the session file — Retry reuses it
- The card must match the session file word for word; Verify runs against the latest approved session

## Portability

Use host tools; do not assume Cursor/Claude/Codex-only APIs. Skill roots include `~/.agents/skills`, `~/.cursor/skills`, `~/.claude/skills`, `~/.codex/skills`, `~/.trae-cn/skills`, and project `.agents/skills` / `.cursor/skills` / `.claude/skills`. Coarse-filter by description; read full `SKILL.md` only for shortlist.

## Phase 1 — Clarify

**Never draft Goal/ACs from guesses — build them from the user's own words.**

1. **Split intents.** Several asks in one message (e.g. 按钮触感 + 动画效果) → list them; clarify each separately, one AC set per intent.
2. **Inspect before asking.** Gather observable facts yourself first (code, screenshot, running behavior) — never make the user describe what you can look at. Ask with facts: "现在是 scale(0.95)·100ms，你嫌太生硬还是太肉？"
3. **Vagueness test.** If you cannot write the observable end-state **in the user's own words** (which element / what property / what direction), the request is vague — asking is mandatory, one-shot confirm forbidden. When in doubt, treat as vague. (Hints: feel/look/motion/style, "better/smoother/nicer", 手感/触感/动画/视觉/风格/体验/丝滑/好看…)
4. **Ask one targeted round** — ≤5 numbered questions, prioritized, skippable, each with your recommended answer:
   - **现状** — what exactly is unsatisfying now? (which element, which moment, what feels wrong)
   - **期望** — what should it look/feel like instead? (direction, reference, "like X")
   - **验收** — how will the user judge the result? (what they will look at / try)
   Low-information answers ("都行 / 你看着办") → follow up with A/B contrast options; if the user insists you decide, proceed but flag the direction as **agent's guess** in the card and mark all related ACs `needs-human-signoff`.
5. **Read-back before matching.** Paraphrase standalone: "我理解的是：现状痛点 X → 你想要 Y → 你会用 Z 判断。对吗？" Only on an explicit yes, draft Goal + ACs quoting the user's answers. Card approval never substitutes for this yes.
6. **AC rules.** Every AC has a verify method. Subjective ACs: `needs-human-signoff` + embed the user's stated expectation (e.g. "按钮按压有明确下沉与回弹（用户要求：'有段落感'）") — bare "better/nicer" is never an AC; where possible, pair with an objective proxy (duration, fps, layout shift). Already-specific requests (user stated target + acceptance) may use one-shot draft + confirm, with every assumption explicitly marked.

Full: follow [references/grilling.md](references/grilling.md).

## Phase 2 — Match

Follow [references/matching.md](references/matching.md): recipes → local → cloud only in full (or if user asks). Combo ≤5; exclude `to-goal-skill` itself.

## Phase 3 — Orchestration card

Update the session file first — the card must match it word for word (the card is a rendering of the session) — then present **exactly** this card and wait for an explicit approval word (可以 / 批准 / 开干 / OK / LGTM). Ambiguous replies (“嗯”, “我看看”) are not approval: ask “是否批准？” and wait.

```markdown
> N ACs (M need your signoff) · installs: K cloud · touches: X areas

## Goal
<one sentence>

## Scope
In: <what's included> · Out: <explicitly not doing> · Touches: <files/areas>

## Acceptance Criteria
- [ ] AC1: <criterion; subjective → embed user's stated expectation> — verify: <method> [`needs-human-signoff` if subjective]

## Skill Combo
| Skill | Source | Fit | Why |
|-------|--------|-----|-----|
| <name> | local / cloud (not installed) | excellent/good/partial/预估 | <what its SKILL.md covers> |

## Workflow
1. <step> — Skill: <name|none> — Covers: AC# — Done when: <signal>

## Install requests (if any)
- <name> — fallback if declined: <plan>   (or “- none”)

## Attempt
<n> of 3 — after 3, stop and report gaps
Mode: <light|full>
Session: docs/to-goal/.session.md
```

Reject → revise card only; each revision carries a one-line “与上版相比” delta. Re-clarify whenever understanding shifts — any direction-level correction from the user (here or mid-execution) counts as the ask. Approved installs → install, confirm loadable **and fit ≥ the card's claim** (read its SKILL.md against the steps; misfit → Phase 2), then execute.  
Save/export only if user asks (suggest `docs/to-goal/YYYY-MM-DD-<slug>.md`).

## Phase 4 — Execute

Only when `approved: true`. For each step: announce ("步骤 k/n") → read that skill → follow it → report one line ("步骤 k/n 完成" + files touched + method used if skill `none`) and log it to the session file. Never pre-claim AC progress — AC verdicts belong to Verify. After each step, sanity-check later steps' premises; a step made moot → skip with a one-line reason (not blocked).

A user message mid-execution pauses the pipeline — respond first, then continue / re-card. A failed step = blocked after one identical retry; never improvise around a skill's instructions. Blocked mid-flight → Phase 2→3 (same attempt until new card approved). Leaving the card's declared Scope counts as blocked — stop and re-card with the delta. Do not silently add skills.

End of execution: list actual changes (file + action) and reconcile them against the card's Scope, line by line.

## Phase 5 — Verify

No completion claims without fresh evidence. Evidence must be reproducible — command + key output / screenshot / artifact path; adjectives don't count; all of it produced after this attempt's last edit. For each AC: identify → run → read → PASS / FAIL / BLOCKED + evidence (BLOCKED = evidence unobtainable → Outstanding gaps, never counts as done). Each FAIL carries a one-line cause (direction / execution / environment) so Retry switches route instead of re-colliding. `needs-human-signoff` → stage the check (URL / file / before-after screenshot or recording) and ask a specific verdict question; never auto-PASS; record the outcome in the session file. Plus one scope-adjacent regression check: per touched area, one neighboring behavior still works (or N/A + why).

```markdown
## Verification (<attempt> of 3)
| AC | Result | Evidence |
|----|--------|----------|
| AC1 | PASS/FAIL/BLOCKED | <command + key output / screenshot / path> |

## Scope reconciliation
match / deviates: <diff>

## Needs your signoff (if any)
- AC#: <staged check> — <specific verdict question>

## Outstanding gaps
- <gap> — next: Retry / user-waived / dropped
```

## Phase 6 — Retry

Route by the FAIL's cause: **direction** → back to Phase 1, re-clarify the affected ACs; **execution** → Phase 2→3→4→5, reusing the session shortlist + last cause — the new card states what changed this round ("这次换了什么"); **environment** → fix the env or ask the user, no attempt consumed. Attempts count plan-level retries only; the user redirecting mid-way = back to Clarify on a fresh sequence. Same cause twice in a row = loop: switch route or stop — never a third same-cause run. Max 3 attempts (initial + 2 retries). Auto-retry (user consented): announce "第 k 次尝试自动进行；若改 skill / AC 会重新请你批" before each.

After 3, stop with a closing report: 可用状态 per change (keep / rollback) → gaps, each with its cause → options in plain words (narrow = 缩小目标保住核心 / partial = 交付已完成部分 / switch = 换方向重来) + your recommendation. Set `active: false` unless the user picks one.

## Attribution

Clarify: Matt Pocock grill-me/grilling (MIT). Match: vercel-labs find-skills. Orchestrate/Retry: obra/superpowers writing-plans + executing-plans. Verify: verification-before-completion.
