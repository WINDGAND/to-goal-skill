# -*- coding: utf-8 -*-
"""Generate editorial README SVG assets — ink / bone / single crimson gate."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

# Dark hero (editorial ink) + light workflow (architectural paper)
# Avoid: teal/cyan glow, purple, neon cards, soft AI gradients
HERO_BG = "#0E0E0E"
HERO_INK = "#F2F0EA"
HERO_MUTE = "#A39E96"
HERO_FAINT = "#6F6A63"
HERO_RULE = "#2A2A2A"
GATE = "#B42318"

WF_BG = "#F4F3EF"
WF_INK = "#141414"
WF_MUTE = "#6B6760"
WF_FAINT = "#9A958C"
WF_RULE = "#D8D4CB"
WF_PAPER = "#EBE8E1"

ARROW = "\u2192"
MID = "\u00b7"

ZH = {
    "desc": "\u4e3a\u76ee\u6807\u6311\u9009 skill \u7ec4\u5408\u5e76\u6309\u8ba1\u5212\u6267\u884c\u9a8c\u6536",
    "line1": "\u4e3a\u76ee\u6807\u6311\u9009\u6700\u5408\u9002\u7684 skill \u7ec4\u5408",
    "line2": "\u5148\u6279\u51c6\uff0c\u518d\u6267\u884c\uff1b\u7528\u8bc1\u636e\u9a8c\u6536",
    "clarify": "\u6f84\u6e05",
    "match": "\u5339\u914d",
    "plan": "\u8ba1\u5212",
    "approve": "\u6279\u51c6",
    "execute": "\u6267\u884c",
    "verify": "\u9a8c\u6536",
    "retry": "\u91cd\u8bd5",
    "workflow": "\u5de5\u4f5c\u6d41",
    "headline": "\u5148\u6279\u51c6\uff0c\u518d\u52a8\u624b",
    "subhead": "\u7528\u8bc1\u636e\u8bf4\u5b8c\u6210\uff0c\u4e0d\u9760\u611f\u89c9",
    "retry_note": "\u7f3a\u53e3 "
    + ARROW
    + " \u56de\u5230\u5339\u914d\uff08\u6700\u591a 2 \u8f6e\uff09",
}


def write(name: str, content: str) -> None:
    path = OUT / name
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")
    print(f"wrote {path.name} ({path.stat().st_size} bytes)")


def hero(lang: str) -> str:
    if lang == "zh":
        line1, line2 = ZH["line1"], ZH["line2"]
        desc = ZH["desc"]
        stages = [
            ("01", ZH["clarify"]),
            ("02", ZH["match"]),
            ("03", ZH["approve"], True),
            ("04", ZH["execute"]),
            ("05", ZH["verify"]),
            ("06", ZH["retry"]),
        ]
        font = "PingFang SC, Microsoft YaHei, "
    else:
        line1 = "Pick the right skills for your goal"
        line2 = "Approve the plan. Verify with evidence."
        desc = "Orchestrate multiple agent skills through a gated plan and evidence-based verification."
        stages = [
            ("01", "Clarify"),
            ("02", "Match"),
            ("03", "Approve", True),
            ("04", "Execute"),
            ("05", "Verify"),
            ("06", "Retry"),
        ]
        font = ""

    rows = []
    y0 = 86
    for i, stage in enumerate(stages):
        num, label = stage[0], stage[1]
        is_gate = len(stage) > 2 and stage[2]
        y = y0 + i * 40
        fill = GATE if is_gate else HERO_INK
        weight = "700" if is_gate else "400"
        rows.append(
            f"""\
      <text x="780" y="{y}" fill="{HERO_FAINT}" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" letter-spacing="1">{num}</text>
      <text x="830" y="{y}" fill="{fill}" font-size="20" font-weight="{weight}">{label}</text>"""
        )
        if i < len(stages) - 1:
            rows.append(
                f'<line x1="780" y1="{y + 14}" x2="1136" y2="{y + 14}" stroke="{HERO_RULE}" stroke-width="1"/>'
            )

    return f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-labelledby="title desc">
  <title id="title">to-goal-skill</title>
  <desc id="desc">{desc}</desc>
  <rect width="1200" height="360" fill="{HERO_BG}"/>
  <text x="1180" y="300" text-anchor="end" fill="{HERO_RULE}" font-size="160" font-family="Georgia, Times New Roman, serif" font-weight="700" opacity="0.9">6</text>

  <g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, {font}sans-serif">
    <text x="48" y="52" fill="{HERO_MUTE}" font-size="12" letter-spacing="4" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">AGENT SKILL {MID} ORCHESTRATION</text>
    <text x="48" y="126" fill="{HERO_INK}" font-size="56" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" letter-spacing="-2">to-goal-skill</text>
    <rect x="48" y="146" width="56" height="3" fill="{GATE}"/>
    <text x="48" y="196" fill="{HERO_INK}" font-size="22">{line1}</text>
    <text x="48" y="232" fill="{HERO_MUTE}" font-size="20">{line2}</text>
    <text x="48" y="300" fill="{HERO_FAINT}" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">hard gates {MID} light default {MID} evidence first</text>
    <text x="48" y="326" fill="{HERO_FAINT}" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">Clarify {ARROW} Match {ARROW} Approve {ARROW} Run {ARROW} Verify</text>
  </g>

  <line x1="740" y1="40" x2="740" y2="320" stroke="{HERO_RULE}" stroke-width="1"/>
  <g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, {font}sans-serif">
    <text x="780" y="52" fill="{HERO_MUTE}" font-size="11" letter-spacing="3" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">PIPELINE</text>
{chr(10).join(rows)}
  </g>
</svg>
"""


def workflow(lang: str) -> str:
    if lang == "zh":
        title = "to-goal-skill " + ZH["workflow"]
        desc = (
            ZH["clarify"]
            + f" {ARROW} "
            + ZH["match"]
            + f" {ARROW} "
            + ZH["plan"]
            + f" {ARROW} "
            + ZH["approve"]
            + f" {ARROW} "
            + ZH["execute"]
            + f" {ARROW} "
            + ZH["verify"]
        )
        headline = ZH["headline"]
        subhead = ZH["subhead"]
        labels = [
            ("01", ZH["clarify"]),
            ("02", ZH["match"]),
            ("03", ZH["plan"]),
            ("04", ZH["execute"]),
            ("05", ZH["verify"]),
        ]
        gate = ZH["approve"]
        retry = "\u7f3a\u53e3 " + ARROW + " \u56de\u5230\u5339\u914d " + MID + " \u6700\u591a 2 \u8f6e"
        font = "PingFang SC, Microsoft YaHei, "
    else:
        title = "to-goal-skill workflow"
        desc = f"Clarify {ARROW} Match {ARROW} Plan {ARROW} Approve {ARROW} Execute {ARROW} Verify"
        headline = "Approve before edits."
        subhead = "Prove done with evidence."
        labels = [
            ("01", "Clarify"),
            ("02", "Match"),
            ("03", "Plan"),
            ("04", "Execute"),
            ("05", "Verify"),
        ]
        gate = "OK"
        retry = f"Gaps {ARROW} rematch {MID} max 2 retries"
        font = ""

    step_xs = [80, 230, 380, 720, 920]
    steps = []
    for (num, label), x in zip(labels, step_xs):
        steps.append(
            f"""\
      <line x1="{x}" y1="182" x2="{x}" y2="198" stroke="{WF_INK}" stroke-width="1.5"/>
      <text x="{x - 6}" y="162" fill="{WF_FAINT}" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">{num}</text>
      <text x="{x - 6}" y="228" fill="{WF_INK}" font-size="18" font-weight="600">{label}</text>"""
        )

    return f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{desc}</desc>
  <rect width="1200" height="280" fill="{WF_BG}"/>
  <rect x="0" y="0" width="1200" height="280" fill="none" stroke="{WF_RULE}" stroke-width="1"/>
  <rect x="0" y="0" width="1200" height="4" fill="{WF_INK}"/>

  <g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, {font}sans-serif">
    <text x="48" y="36" fill="{WF_MUTE}" font-size="11" letter-spacing="3" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">HOW IT WORKS</text>
    <text x="48" y="74" fill="{WF_INK}" font-size="30" font-weight="700">{headline}</text>
    <text x="48" y="108" fill="{WF_MUTE}" font-size="16">{subhead}</text>

    <line x1="48" y1="190" x2="1152" y2="190" stroke="{WF_RULE}" stroke-width="1"/>
{chr(10).join(steps)}

    <g id="gate">
      <rect x="516" y="146" width="88" height="88" fill="{GATE}"/>
      <rect x="521" y="151" width="78" height="78" fill="none" stroke="#FFFFFF" stroke-width="1"/>
      <text x="560" y="186" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700">{gate}</text>
      <text x="560" y="208" text-anchor="middle" fill="#FFFFFF" font-size="10" letter-spacing="2" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">GATE</text>
    </g>

    <text x="48" y="258" fill="{WF_MUTE}" font-size="13">{retry}</text>
  </g>
</svg>
"""


if __name__ == "__main__":
    write("hero-en.svg", hero("en"))
    write("hero-zh.svg", hero("zh"))
    write("workflow.en.svg", workflow("en"))
    write("workflow.zh.svg", workflow("zh"))
