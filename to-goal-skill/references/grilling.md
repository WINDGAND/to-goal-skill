# Goal Clarification (Grilling)

Derived from Matt Pocock’s grill-me / grilling (MIT).
Adapted for `to-goal-skill`: the output is a **Goal** plus **Acceptance Criteria**, not an implementation design doc.

## Purpose

Interview the user until you share an understanding of:

1. What success looks like (Goal)
2. How quality completion will be judged (Acceptance Criteria)

Do not proceed to skill matching until the user confirms shared understanding.

## Design Tree

Map the problem as a **design tree**: every decision branches into decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled — questions you can ask *now* without guessing unanswered upstream choices.

Ask the whole frontier in one round. Number each question and give your recommended answer. Wait for answers before the next round.

### Question format

```
❓ **Q1** - **<question title>**: <question body; multiple choice when helpful>

➡️ <your recommended answer>
```

A question that depends on another still-open question belongs in a *later* round.

## Facts vs Decisions

- **Facts** (filesystem, repo state, installed skills, tool output): look them up yourself. Prefer a sub-agent when available. Do not ask the user for anything you can discover.
- **Decisions** (scope, tradeoffs, success bar): put each to the user and wait.

Do not block the whole round on fact-finding: only questions downstream of an unsettled fact wait; ask the rest of the frontier now.

## Acceptance Criteria Rules

While grilling, drive toward Acceptance Criteria that are usable in verification:

- Prefer **binary / observable** criteria (command output, artifact exists, behavior observed).
- Each criterion must include **how to verify**.
- Vague praise ("better", "nicer", "about right") is not allowed unless marked `needs-human-signoff`.
- Subjective criteria are allowed only when labeled `needs-human-signoff` (human judges at verify time).

### Useful frontier themes (adapt as needed)

- Primary outcome vs nice-to-haves
- Explicit out-of-scope
- Constraints (stack, time, tools, risk)
- Definition of done / quality bar
- Evidence required for each done claim

## Light mode (from parent skill)

**Light is the default** in `to-goal-skill`. At most **one** frontier round, or present a drafted Goal + Acceptance Criteria for a single confirmation. Still forbid proceeding without user confirmation. Do not skip verify methods on ACs.

## Done Condition

The clarify phase is done when:

1. The frontier is empty (no silent assumptions left) — or light mode confirmation is done
2. Goal + Acceptance Criteria are written clearly
3. The user confirms shared understanding

Then continue to skill matching inside `to-goal-skill`.
