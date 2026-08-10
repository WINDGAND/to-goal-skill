#!/usr/bin/env node
/**
 * Optional Cursor hook: block business writes / skill installs while
 * docs/to-goal/.session.md has active:true and approved:false.
 *
 * stdin: JSON hook payload from Cursor
 * stdout: { permission, user_message?, agent_message? }
 */

const fs = require("fs");
const path = require("path");

function readStdin() {
  try {
    return fs.readFileSync(0, "utf8");
  } catch {
    return "";
  }
}

function allow(extra = {}) {
  process.stdout.write(JSON.stringify({ permission: "allow", ...extra }));
  process.exit(0);
}

function deny(userMessage, agentMessage) {
  process.stdout.write(
    JSON.stringify({
      permission: "deny",
      user_message: userMessage,
      agent_message: agentMessage,
    })
  );
  process.exit(0);
}

function findSessionFile(cwd) {
  if (!cwd) return null;
  const candidate = path.join(cwd, "docs", "to-goal", ".session.md");
  if (fs.existsSync(candidate)) return candidate;
  return null;
}

function parseSession(text) {
  const active = /^\s*active:\s*true\s*$/im.test(text);
  const approved = /^\s*approved:\s*true\s*$/im.test(text);
  return { active, approved };
}

function collectPaths(obj, out = []) {
  if (!obj || typeof obj !== "object") return out;
  for (const [k, v] of Object.entries(obj)) {
    if (typeof v === "string" && /path|file|target/i.test(k)) out.push(v);
    else if (v && typeof v === "object") collectPaths(v, out);
  }
  return out;
}

function isToGoalPath(p, cwd) {
  if (!p) return false;
  const norm = path.normalize(p).replace(/\\/g, "/").toLowerCase();
  const rel = path.normalize(path.relative(cwd || "", p)).replace(/\\/g, "/").toLowerCase();
  return (
    norm.includes("/docs/to-goal/") ||
    rel.startsWith("docs/to-goal/") ||
    rel === "docs/to-goal/.session.md"
  );
}

function isWriteLikeTool(toolName) {
  const n = String(toolName || "");
  return /^(Write|StrReplace|EditNotebook|Delete|DeleteFile|ApplyPatch|CreateFile|EditFile)$/i.test(
    n
  );
}

function shellLooksLikeInstall(command) {
  const c = String(command || "");
  return /npx\s+skills\s+add\b/i.test(c) || /skills\s+add\b/i.test(c);
}

const raw = readStdin();
let payload = {};
try {
  payload = raw ? JSON.parse(raw) : {};
} catch {
  allow();
}

const cwd =
  payload.cwd ||
  payload.workspace_root ||
  (Array.isArray(payload.workspace_roots) && payload.workspace_roots[0]) ||
  process.env.CURSOR_PROJECT_DIR ||
  process.cwd();

const sessionPath = findSessionFile(cwd);
if (!sessionPath) allow();

let session;
try {
  session = parseSession(fs.readFileSync(sessionPath, "utf8"));
} catch {
  allow();
}

if (!session.active || session.approved) allow();

const toolName = payload.tool_name || payload.toolName || payload.tool || "";
const toolInput = payload.tool_input || payload.toolInput || payload.input || {};
const command =
  payload.command || toolInput.command || toolInput.cmd || toolInput.script || "";

const event = payload.hook_event_name || payload.event || "";

// beforeShellExecution style
if (event === "beforeShellExecution" || (!toolName && command)) {
  if (shellLooksLikeInstall(command)) {
    deny(
      "to-goal-skill session is active but not approved. Approve the orchestration card first.",
      "Blocked npx skills add: set approved: true in docs/to-goal/.session.md after user approval."
    );
  }
  allow();
}

if (isWriteLikeTool(toolName)) {
  const paths = collectPaths(toolInput);
  if (paths.length === 0) {
    deny(
      "to-goal-skill: writes blocked until you approve the orchestration card.",
      "Session active with approved:false. Only docs/to-goal/* may be written before approval."
    );
  }
  const allAllowed = paths.every((p) => isToGoalPath(p, cwd));
  if (!allAllowed) {
    deny(
      "to-goal-skill: business file edits blocked until orchestration card approval.",
      "Update docs/to-goal/.session.md approved: true only after the user approves the card."
    );
  }
  allow();
}

if (String(toolName).toLowerCase() === "shell" && shellLooksLikeInstall(command)) {
  deny(
    "to-goal-skill session is active but not approved. Approve the orchestration card first.",
    "Blocked skill install while approved:false."
  );
}

allow();
