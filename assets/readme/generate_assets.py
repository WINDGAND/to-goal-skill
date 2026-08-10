# -*- coding: utf-8 -*-
"""Generate README hero SVGs (ink / bone / crimson gate). Workflow GIFs: generate_workflow_gif.py."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

BG = "#0E0E0E"
INK = "#F2F0EA"
MUTE = "#A39E96"
FAINT = "#6F6A63"
RULE = "#2A2A2A"
GATE = "#B42318"

ARROW = "\u2192"
MID = "\u00b7"

ZH = {
    "desc": "\u4e3a\u76ee\u6807\u6311\u9009 skill \u7ec4\u5408\u5e76\u6309\u8ba1\u5212\u6267\u884c\u9a8c\u6536",
    "line1": "\u4e3a\u76ee\u6807\u6311\u9009\u6700\u5408\u9002\u7684 skill \u7ec4\u5408",
    "line2": "\u5148\u6279\u51c6\uff0c\u518d\u6267\u884c\uff1b\u7528\u8bc1\u636e\u9a8c\u6536",
    "clarify": "\u6f84\u6e05",
    "match": "\u5339\u914d",
    "approve": "\u6279\u51c6",
    "execute": "\u6267\u884c",
    "verify": "\u9a8c\u6536",
    "retry": "\u91cd\u8bd5",
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
        fill = GATE if is_gate else INK
        weight = "700" if is_gate else "400"
        rows.append(
            f"""\
      <text x="780" y="{y}" fill="{FAINT}" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" letter-spacing="1">{num}</text>
      <text x="830" y="{y}" fill="{fill}" font-size="20" font-weight="{weight}">{label}</text>"""
        )
        if i < len(stages) - 1:
            rows.append(
                f'<line x1="780" y1="{y + 14}" x2="1136" y2="{y + 14}" stroke="{RULE}" stroke-width="1"/>'
            )

    return f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-labelledby="title desc">
  <title id="title">to-goal-skill</title>
  <desc id="desc">{desc}</desc>
  <rect width="1200" height="360" fill="{BG}"/>
  <text x="1180" y="300" text-anchor="end" fill="{RULE}" font-size="160" font-family="Georgia, Times New Roman, serif" font-weight="700" opacity="0.9">6</text>

  <g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, {font}sans-serif">
    <text x="48" y="52" fill="{MUTE}" font-size="12" letter-spacing="4" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">AGENT SKILL {MID} ORCHESTRATION</text>
    <text x="48" y="126" fill="{INK}" font-size="56" font-weight="700" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" letter-spacing="-2">to-goal-skill</text>
    <rect x="48" y="146" width="56" height="3" fill="{GATE}"/>
    <text x="48" y="196" fill="{INK}" font-size="22">{line1}</text>
    <text x="48" y="232" fill="{MUTE}" font-size="20">{line2}</text>
    <text x="48" y="300" fill="{FAINT}" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">hard gates {MID} light default {MID} evidence first</text>
    <text x="48" y="326" fill="{FAINT}" font-size="13" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">Clarify {ARROW} Match {ARROW} Approve {ARROW} Run {ARROW} Verify</text>
  </g>

  <line x1="740" y1="40" x2="740" y2="320" stroke="{RULE}" stroke-width="1"/>
  <g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, {font}sans-serif">
    <text x="780" y="52" fill="{MUTE}" font-size="11" letter-spacing="3" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">PIPELINE</text>
{chr(10).join(rows)}
  </g>
</svg>
"""


if __name__ == "__main__":
    write("hero-en.svg", hero("en"))
    write("hero-zh.svg", hero("zh"))
