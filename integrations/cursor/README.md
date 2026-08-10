# Optional Cursor hard-gate for to-goal-skill

Portable skill behavior does **not** require this. Install only if you want Cursor to **block** business file edits and `npx skills add` while `docs/to-goal/.session.md` has `active: true` and `approved: false`.

Without these hooks, agents still follow the documentation gates in `to-goal-skill/SKILL.md`.

## Install (project)

From the **repository root** of the project where you run agents (copy or submodule this folder as needed):

1. Ensure Node.js is on `PATH` (`node -v`).
2. Merge hooks into `.cursor/hooks.json` (or copy this file if you have none):

```bash
mkdir -p .cursor/hooks
cp integrations/cursor/hooks/to-goal-gate.js .cursor/hooks/to-goal-gate.js
```

Point `hooks.json` commands at the copied script, for example:

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "command": "node .cursor/hooks/to-goal-gate.js",
        "matcher": "Write|StrReplace|EditNotebook|Delete|Shell",
        "failClosed": false
      }
    ],
    "beforeShellExecution": [
      {
        "command": "node .cursor/hooks/to-goal-gate.js",
        "matcher": "skills\\s+add|npx\\s+skills",
        "failClosed": false
      }
    ]
  }
}
```

A ready-to-adapt template lives next to this README: [`hooks.json`](./hooks.json) (paths assume the skill repo is the project root).

3. Optional rule: copy [`rules/to-goal-session.mdc`](./rules/to-goal-session.mdc) into the project’s `.cursor/rules/` and enable when using to-goal-skill.
4. Reload Cursor hooks (save `hooks.json` or restart Cursor). Check **Hooks** output if unsure.

## Behavior

| Condition | Result |
|-----------|--------|
| No `docs/to-goal/.session.md` | Allow (hook idle) |
| `active: true` and `approved: false` | Deny business writes; deny `npx skills add` |
| Same, path under `docs/to-goal/` | Allow |
| `approved: true` or `active: false` | Allow |

`failClosed` is **false** so a broken hook does not freeze the agent; fix the script if it misbehaves.

## Uninstall

Remove the hook entries from `.cursor/hooks.json` and delete the copied script/rule.
