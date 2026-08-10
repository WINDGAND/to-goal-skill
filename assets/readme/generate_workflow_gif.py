# -*- coding: utf-8 -*-
"""
Dark editorial workflow GIF — matches hero ink palette.
Motion: continuous progress rail (not PPT step flashing).
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent

# Match hero-zh / hero-en
BG = (14, 14, 14)
INK = (242, 240, 234)
MUTE = (163, 158, 150)
FAINT = (111, 106, 99)
RULE = (42, 42, 42)
GATE = (180, 35, 24)
WHITE = (255, 255, 255)

W, H = 1200, 300
FPS = 24
DURATION = 5.6

# Rail geometry
RAIL_Y = 188
RAIL_X0 = 64
RAIL_X1 = 1136
# Milestone x positions along the rail (clarify, match, plan, GATE, execute, verify)
MILESTONES = [100, 280, 460, 640, 860, 1040]


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    if bold:
        candidates = [
            r"C:\Windows\Fonts\msyhbd.ttc",
            r"C:\Windows\Fonts\msyh.ttc",
            r"C:\Windows\Fonts\simhei.ttf",
        ]
    else:
        candidates = [
            r"C:\Windows\Fonts\msyh.ttc",
            r"C:\Windows\Fonts\simsun.ttc",
            r"C:\Windows\Fonts\consola.ttf",
            r"C:\Windows\Fonts\segoeui.ttf",
        ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def ease_in_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 0.5 - 0.5 * math.cos(math.pi * t)


def copy_for(lang: str) -> dict:
    if lang == "zh":
        return {
            "eyebrow": "HOW IT WORKS",
            "headline": "先批准，再动手",
            "subhead": "用证据说完成，不靠感觉",
            "steps": [
                ("01", "澄清"),
                ("02", "匹配"),
                ("03", "计划"),
                ("GATE", "批准"),
                ("04", "执行"),
                ("05", "验收"),
            ],
            "retry": "缺口 → 回到匹配 · 最多 2 轮",
            "meta": "hard gates · evidence first",
            "out": "workflow-zh.gif",
        }
    return {
        "eyebrow": "HOW IT WORKS",
        "headline": "Approve before edits.",
        "subhead": "Prove done with evidence.",
        "steps": [
            ("01", "Clarify"),
            ("02", "Match"),
            ("03", "Plan"),
            ("GATE", "OK"),
            ("04", "Execute"),
            ("05", "Verify"),
        ],
        "retry": "Gaps → rematch · max 2 retries",
        "meta": "hard gates · evidence first",
        "out": "workflow-en.gif",
    }


def progress_at(t: float) -> float:
    """
    0..1 progress along rail.
    Hold empty → draw → hold full → retract for loop.
    """
    if t < 0.7:
        return 0.0
    if t < 3.1:
        return ease_in_out((t - 0.7) / 2.4)
    if t < 4.4:
        return 1.0
    if t < DURATION:
        return ease_in_out(1.0 - (t - 4.4) / (DURATION - 4.4))
    return 0.0


def draw_frame(progress: float, copy: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    font_mono = load_font(11)
    font_h = load_font(28, bold=True)
    font_sub = load_font(15)
    font_num = load_font(12)
    font_label = load_font(16, bold=True)
    font_gate = load_font(15, bold=True)
    font_small = load_font(12)

    # Left accent bar (matches hero)
    d.rectangle([0, 0, 5, H], fill=INK)
    # Hairline frame
    d.rectangle([0, 0, W - 1, H - 1], outline=RULE, width=1)

    d.text((40, 28), copy["eyebrow"], fill=MUTE, font=font_mono)
    d.text((40, 54), copy["headline"], fill=INK, font=font_h)
    # Crimson mark under headline (same motif as hero title bar)
    d.rectangle([40, 92, 96, 95], fill=GATE)
    d.text((40, 108), copy["subhead"], fill=MUTE, font=font_sub)

    gate_idx = 3
    gate_x = MILESTONES[gate_idx]
    gw, gh = 72, 56
    gate_left = gate_x - gw // 2
    gate_right = gate_x + gw // 2

    def draw_rail_segment(x0: float, x1: float, color) -> None:
        if x1 - x0 < 2:
            return
        d.rounded_rectangle([x0, RAIL_Y - 2, x1, RAIL_Y + 2], radius=2, fill=color)

    # Gray track in two segments — interrupted by the gate (no line through the stamp)
    draw_rail_segment(RAIL_X0, gate_left - 2, RULE)
    draw_rail_segment(gate_right + 2, RAIL_X1, RULE)

    # Crimson progress, also segmented so nothing sticks out of the gate
    fill_x = RAIL_X0 + (RAIL_X1 - RAIL_X0) * progress
    if fill_x > RAIL_X0 + 1:
        draw_rail_segment(RAIL_X0, min(fill_x, gate_left - 2), GATE)
    if fill_x > gate_right + 2:
        draw_rail_segment(gate_right + 2, fill_x, GATE)

    # Leading tip only when outside the gate body
    tip_r = 5
    if progress > 0.001 and not (gate_left - 4 <= fill_x <= gate_right + 4):
        d.ellipse(
            [fill_x - tip_r, RAIL_Y - tip_r, fill_x + tip_r, RAIL_Y + tip_r],
            fill=GATE,
        )

    for i, (num, label) in enumerate(copy["steps"]):
        x = MILESTONES[i]
        reached = fill_x >= x - 4
        is_gate = i == gate_idx

        if is_gate:
            gx, gy = gate_left, RAIL_Y - gh // 2
            if reached:
                d.rectangle([gx, gy, gx + gw, gy + gh], fill=GATE)
                d.rectangle(
                    [gx + 3, gy + 3, gx + gw - 3, gy + gh - 3],
                    outline=WHITE,
                    width=1,
                )
                tw = d.textlength(label, font=font_gate)
                d.text((x - tw / 2, RAIL_Y - 12), label, fill=WHITE, font=font_gate)
                tw2 = d.textlength(num, font=font_mono)
                d.text((x - tw2 / 2, RAIL_Y + 10), num, fill=WHITE, font=font_mono)
            else:
                d.rectangle([gx, gy, gx + gw, gy + gh], outline=RULE, width=1)
                tw = d.textlength(label, font=font_gate)
                d.text((x - tw / 2, RAIL_Y - 12), label, fill=FAINT, font=font_gate)
                tw2 = d.textlength(num, font=font_mono)
                d.text((x - tw2 / 2, RAIL_Y + 10), num, fill=FAINT, font=font_mono)
            continue

        node_c = GATE if reached else RULE
        d.ellipse([x - 4, RAIL_Y - 4, x + 4, RAIL_Y + 4], fill=node_c)
        if reached:
            d.ellipse([x - 2, RAIL_Y - 2, x + 2, RAIL_Y + 2], fill=INK)

        num_c = MUTE if reached else FAINT
        lab_c = INK if reached else FAINT
        tw_num = d.textlength(num, font=font_num)
        d.text((x - tw_num / 2, RAIL_Y - 42), num, fill=num_c, font=font_num)
        tw = d.textlength(label, font=font_label)
        d.text((x - tw / 2, RAIL_Y + 18), label, fill=lab_c, font=font_label)

    d.text((40, 268), copy["retry"], fill=FAINT, font=font_small)
    tw = d.textlength(copy["meta"], font=font_mono)
    d.text((W - 40 - tw, 268), copy["meta"], fill=FAINT, font=font_mono)

    return img


def render(lang: str) -> Path:
    copy = copy_for(lang)
    n = int(DURATION * FPS)
    frames = []
    for i in range(n):
        t = i / FPS
        frames.append(draw_frame(progress_at(t), copy))
    # Seamless loop
    frames[-1] = frames[0].copy()

    out = OUT / copy["out"]
    frames[0].save(
        out,
        save_all=True,
        append_images=frames[1:],
        duration=int(1000 / FPS),
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"wrote {out.name} ({out.stat().st_size / 1024:.0f} KB, {len(frames)} frames)")
    return out


if __name__ == "__main__":
    render("zh")
    render("en")
