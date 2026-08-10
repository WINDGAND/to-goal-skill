# -*- coding: utf-8 -*-
"""Editorial sequence-strip GIF — no flowchart boxes."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent

BG = (244, 243, 239)
INK = (20, 20, 20)
MUTE = (107, 103, 96)
FAINT = (154, 149, 140)
RULE = (216, 212, 203)
GATE = (180, 35, 24)
WHITE = (255, 255, 255)

W, H = 1200, 280
FPS = 16
DURATION = 5.0


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
            r"C:\Windows\Fonts\segoeui.ttf",
        ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


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
                ("04", "执行"),
                ("05", "验收"),
            ],
            "gate": "批准",
            "gate_en": "GATE",
            "retry": "缺口 → 回到匹配 · 最多 2 轮",
            "out": "workflow.zh.gif",
        }
    return {
        "eyebrow": "HOW IT WORKS",
        "headline": "Approve before edits.",
        "subhead": "Prove done with evidence.",
        "steps": [
            ("01", "Clarify"),
            ("02", "Match"),
            ("03", "Plan"),
            ("04", "Execute"),
            ("05", "Verify"),
        ],
        "gate": "OK",
        "gate_en": "GATE",
        "retry": "Gaps → rematch · max 2 retries",
        "out": "workflow.en.gif",
    }


def draw_frame(active: int, copy: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    font_mono = load_font(11)
    font_h = load_font(30, bold=True)
    font_sub = load_font(16)
    font_num = load_font(13)
    font_label = load_font(18, bold=True)
    font_gate = load_font(16, bold=True)
    font_gate_en = load_font(10)
    font_retry = load_font(13)

    d.rectangle([0, 0, W - 1, H - 1], outline=RULE, width=1)
    d.rectangle([0, 0, W, 4], fill=INK)

    d.text((48, 28), copy["eyebrow"], fill=MUTE, font=font_mono)
    d.text((48, 52), copy["headline"], fill=INK, font=font_h)
    d.text((48, 96), copy["subhead"], fill=MUTE, font=font_sub)

    # Baseline
    y_base = 190
    d.line([(48, y_base), (1152, y_base)], fill=RULE, width=1)

    # Step positions: 3 before gate, gate, 2 after
    # xs for five steps
    step_xs = [80, 230, 380, 720, 920]
    gate_x = 560

    for i, ((num, label), x) in enumerate(zip(copy["steps"], step_xs)):
        on = i == active
        num_c = GATE if on else FAINT
        lab_c = GATE if on else INK
        # tick
        d.line([(x, y_base - 8), (x, y_base + 8)], fill=num_c if on else INK, width=2)
        d.text((x - 6, y_base - 48), num, fill=num_c, font=font_num)
        d.text((x - 6, y_base + 18), label, fill=lab_c, font=font_label)
        if on:
            d.rectangle([x - 6, y_base + 46, x + 52, y_base + 48], fill=GATE)

    # Gate stamp — always crimson; enlarge slightly when active
    gate_on = active == 5
    gw = gh = 92 if gate_on else 88
    gx, gy = gate_x - gw // 2, y_base - gh // 2
    d.rectangle([gx, gy, gx + gw, gy + gh], fill=GATE)
    d.rectangle([gx + 5, gy + 5, gx + gw - 5, gy + gh - 5], outline=WHITE, width=1)
    tw = d.textlength(copy["gate"], font=font_gate)
    d.text((gate_x - tw / 2, y_base - 12), copy["gate"], fill=WHITE, font=font_gate)
    tw2 = d.textlength(copy["gate_en"], font=font_gate_en)
    d.text((gate_x - tw2 / 2, y_base + 14), copy["gate_en"], fill=WHITE, font=font_gate_en)

    # Retry note bottom-left so it does not collide with steps
    d.text((48, 250), copy["retry"], fill=MUTE, font=font_retry)

    return img


def timeline() -> list[int]:
    """Highlight in true pipeline order: Clarify → Match → Plan → Gate → Execute → Verify."""
    # active index: 0..4 = steps, 5 = gate (drawn between plan and execute)
    sequence = [0, 1, 2, 5, 3, 4]
    n = int(DURATION * FPS)
    frames = []
    for i in range(n):
        t = i / FPS
        if t < 0.9:
            frames.append(-1)
        elif t < 3.3:
            u = (t - 0.9) / 2.4
            slot = min(len(sequence) - 1, int(u * len(sequence)))
            frames.append(sequence[slot])
        else:
            frames.append(-1)
    return frames


def render(lang: str) -> Path:
    copy = copy_for(lang)
    frames = [draw_frame(a, copy) for a in timeline()]
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
