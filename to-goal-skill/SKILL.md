---
name: to-goal-skill
description: Clarify a user goal and acceptance criteria, select a minimal local-first skill combo (local + skills.sh), orchestrate step-by-step execution, verify with evidence, and retry up to 2 times on gaps. Use when the user invokes /to-goal-skill or to-goal-skill, or wants multiple skills combined/orchestrated to complete a goal (e.g. skill combo, orchestrate skills, finish this goal end-to-end with skills).
license: MIT
compatibility: Requires filesystem access to read installed skills; network + Node.js/npx for skills.sh discovery and optional installs. Portable Agent Skills (SKILL.md) format.
metadata:
  author: WINDGAND
  version: "1.0.0"
  attribution: "Clarify phase derived from Matt Pocock grill-me/grilling (MIT); matching adapted from vercel-labs find-skills; orchestrate/retry adapted from obra/superpowers writing-plans + executing-plans; verify adapted from obra/superpowers verification-before-completion"
---

# To Goal Skill

Meta-orchestrator: **Clarify → Match → Plan → Approve → Execute → Verify → Retry**.

Announce at start: `Using to-goal-skill to clarify, orchestrate skills, and verify the goal.`

Talk to the user in their language. Keep this file’s instructions as the process source of truth.

## Hard Gates

1. **No matching/execution** until Goal + Acceptance Criteria are confirmed.
2. **No execution** until the user approves the orchestration card.
3. **No completion claims** without fresh verification evidence against Acceptance Criteria.
4. **No silent cloud installs** — ask first.
5. **Max 3 attempts** (initial + 2 retries). Then stop and report gaps.

## Portability

Follow the open Agent Skills layout (`SKILL.md` + optional `references/`). Use the host agent’s normal tools (shell, filesystem, sub-agents if any). Do **not** assume Cursor-only, Claude-only, or Codex-only tool names.

Discover local skills from the runtime’s usual skill roots (examples: `~/.agents/skills`, `~/.cursor/skills`, `~/.claude/skills`, `~/.codex/skills`, `~/.trae-cn/skills`, project `.agents/skills` / `.cursor/skills` / `.claude/skills`). Read each candidate’s `SKILL.md` frontmatter/body before assigning it.

## Phase 1 — Clarify (Goal + Acceptance Criteria)

Read and follow [references/grilling.md](references/grilling.md).

**Derived from Matt Pocock’s grill-me / grilling (MIT).**

Output that must be confirmed by the user:

- **Goal** — one clear success statement
- **Acceptance Criteria** — checklist; each item has a verify method; subjective items marked `needs-human-signoff`

## Phase 2 — Match Skills

Read and follow [references/matching.md](references/matching.md).

**Adapted from vercel-labs `find-skills`.**

Produce a minimal combo (≤5 skills) mapped to upcoming workflow steps. Local-first. Ask before any cloud install.

## Phase 3 — Orchestration Card (Approval Gate)

**Adapted from obra/superpowers `writing-plans` (shape) + `executing-plans` (review-before-act).** Differences: steps bind to skills (not file-level coding tasks); default is chat-only unless the user asks to save/export.

Present **exactly** this card and wait for approval:

```markdown
## Goal
<one sentence>

## Acceptance Criteria
- [ ] AC1: <criterion> — verify: <command/artifact/observation> [`needs-human-signoff` if needed]
- [ ] AC2: ...

## Skill Combo
| Skill | Source | Fit | Why |
|-------|--------|-----|-----|
| <name> | local / cloud (not installed) | excellent/good/partial | <one line; mention rejected alternatives if relevant> |

## Workflow
1. <step> — Skill: <name|none> — Covers: AC# — Done when: <signal>
2. ...

## Install requests (if any)
- none
- OR: request consent to run `npx skills add <owner/repo@skill> -g -y`

## Attempt
<n> of 3
```

If the user rejects: revise only the rejected parts and re-show the card (default). Return to Phase 1 only if they ask to re-clarify.

If they approve installs: run the install, re-check the skill is loadable, then execute.

### Save / export

Default: keep the card in chat. If the user asks to save/export, write a markdown file where they specify (or `docs/to-goal/YYYY-MM-DD-<slug>.md` if they defer).

## Phase 4 — Execute

**Adapted from obra/superpowers `executing-plans`.**

For each workflow step in order:

1. Announce: `Using <skill-or-general-capability> for step N: <title>`
2. Read that skill’s `SKILL.md` (and linked refs as needed) and follow it for the step’s scope
3. Prefer one skill covering multiple steps when the card says so — do not invent extra skills mid-flight
4. Stop on blockers; ask rather than guess
5. End the step with one line: result + which ACs it advanced

If a step has Skill `none`, use general capabilities as planned.

## Phase 5 — Verify

**Adapted from obra/superpowers `verification-before-completion`.**

Iron law: **no completion claims without fresh evidence.**

For each Acceptance Criterion:

1. IDENTIFY the verification action
2. RUN it (fresh)
3. READ the full result
4. Mark `PASS` or `FAIL` with evidence
5. For `needs-human-signoff`, ask the user to judge; do not auto-pass

Report:

```markdown
## Verification (<attempt> of 3)
| AC | Result | Evidence |
|----|--------|----------|
| AC1 | PASS/FAIL | <short evidence> |

## Outstanding gaps
- ...
```

All PASS → congratulate briefly with evidence pointers; stop.

## Phase 6 — Retry

On any FAIL, if attempts used < 3:

1. Keep the Goal; tighten understanding of gaps (short questions only if required)
2. Re-run **Phase 2 → 3 → 4 → 5** targeting outstanding ACs (may change skills/steps)
3. Increment Attempt on the new card

After 3 failed attempts: stop. Summarize gaps, skills tried, and ask what to do next. Do not loop further.

## Attribution

- Clarify: Derived from Matt Pocock’s grill-me / grilling (MIT)
- Match: Adapted from vercel-labs find-skills
- Orchestrate / Retry: Adapted from obra/superpowers writing-plans + executing-plans
- Verify: Adapted from obra/superpowers verification-before-completion
