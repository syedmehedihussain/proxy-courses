"""Task 1 diagram: tailored lifecycle (Scrum + XP, 7 sprints, 2 exam gates)."""
import sys
from svgkit import *

out = sys.argv[1]

L, WK, TOP = 200, 108, 70  # label column, week width, top
W = L + 14 * WK + 70
s = SVG(W, 830)
s.text(W / 2, 36, "Proxy Courses: tailored life cycle (Scrum + XP, 14 weeks, 7 sprints, 2 exam gates)",
       size=22, anchor="middle", weight="bold")


def wx(week):  # left x of a week (1-based)
    return L + (week - 1) * WK


# Week axis
for wk in range(1, 15):
    s.rect(wx(wk), TOP, WK, 28, fill=GREY_BG, stroke="#cbd2d9", sw=1)
    s.text(wx(wk) + WK / 2, TOP + 19, f"W{wk}", size=13, anchor="middle", fill=MUTED, weight="bold")

rows = [("Sprint (time-box)", 108, 70), ("Lectures", 186, 34), ("Course task due", 228, 46),
        ("Artefacts", 282, 96), ("Product build", 386, 56), ("Reviews", 450, 70)]
for name, y, h in rows:
    s.rect(14, y, L - 24, h, fill=SOFT, stroke="#cbd2d9", sw=1, rx=6)
    s.text(24, y + h / 2 + 5, name, size=14, weight="bold")

sprints = [
    ("S1", "Inception & process", "L1–2", "Task 1 · Process", ["Proposal", "Process-model choice", "Life-cycle plan"],
     "Repo, CI skeleton", BLUE, BLUE_BG),
    ("S2", "Requirements", "L3", "Task 2 · Requirements", ["PRD v1.0 / SRS", "Use cases, ER,", "state, DFD"],
     "Clickable mock-up", GREEN, GREEN_BG),
    ("S3", "Design & metrics", "L4", "Task 3 + Task 4", ["Module design", "Wireframes", "FP count"],
     "Schema + auth", PURPLE, PURPLE_BG),
    ("S4", "Quality + build 1", "L5", "Task 5 · Quality", ["Quality scenarios", "Availability targets"],
     "Verification, offers", AMBER, AMBER_BG),
    ("S5", "Testing + build 2", "L5", "Task 6 · Testing", ["Test plan", "Test cases (WB/BB)"],
     "M1 core flow demo", BLUE, BLUE_BG),
    ("S6", "Project mgmt + build 3", "L6–7", "Task 7 · Estimation", ["COCOMO, PERT", "WBS, Gantt, EVA"],
     "M2 features", GREEN, GREEN_BG),
    ("S7", "Risk & release", "L8", "Task 8 · Risk", ["Risk register, RMMM", "Final report"],
     "Release candidate", PURPLE, PURPLE_BG),
]
for i, (sid, name, lec, task, arts, build, col, bg) in enumerate(sprints):
    x = wx(1 + 2 * i) + 4
    w = 2 * WK - 8
    s.rect(x, 108, w, 70, fill=bg, stroke=col, sw=2, rx=8)
    s.text(x + w / 2, 134, f"{sid} · 2 weeks", size=15, anchor="middle", weight="bold", fill=col)
    s.text(x + w / 2, 156, name, size=13, anchor="middle")
    s.rect(x, 186, w, 34, fill="white", stroke="#cbd2d9", sw=1, rx=6)
    s.text(x + w / 2, 208, lec, size=13, anchor="middle", fill=MUTED)
    s.rect(x, 228, w, 46, fill=col, stroke=col, rx=6)
    s.text(x + w / 2, 257, task, size=14, anchor="middle", weight="bold", fill="white")
    s.rect(x, 282, w, 96, fill="white", stroke="#cbd2d9", sw=1, rx=6)
    s.lines(x + w / 2, 306, arts, size=13, anchor="middle")
    s.rect(x, 386, w, 56, fill="white", stroke="#cbd2d9", sw=1, rx=6)
    s.text(x + w / 2, 419, build, size=13, anchor="middle")
    s.rect(x, 450, w, 70, fill="white", stroke="#cbd2d9", sw=1, rx=6)
    s.lines(x + w / 2, 472, ["Sprint review", "+ retrospective", "Faculty viva"], size=12, anchor="middle", fill=MUTED)

# Planning cadence inside each sprint
s.text(L, 545, "Inside every sprint:  Planning (day 1)  →  daily stand-up  →  pair programming + PR review (XP)  "
               "→  CI tests on every push  →  review + retro (last day)", size=13, fill=MUTED)

# Configuration management band
s.rect(L, 560, 14 * WK, 30, fill=GREY_BG, stroke=LINE, sw=1, rx=6)
s.text(L + 7 * WK, 580, "Configuration management (Lecture 6), all semester: Git branches, PR review, "
                        "tagged baselines, GitHub Actions CI", size=13, anchor="middle", weight="bold")
s.rect(14, 560, L - 24, 30, fill=SOFT, stroke="#cbd2d9", sw=1, rx=6)
s.text(24, 580, "Throughout", size=14, weight="bold")

# Milestones and gates
s.rect(14, 604, L - 24, 150, fill=SOFT, stroke="#cbd2d9", sw=1, rx=6)
s.text(24, 684, "Milestones", size=14, weight="bold")
s.line(L, 650, L + 14 * WK, 650, stroke=LINE, sw=2)
ms = [
    (0.35, "M0", "Proposal", "approved", BLUE, "d"),
    (4, "M1", "Requirements", "baseline v1.0", GREEN, "d"),
    (6, "M2", "Design", "baseline", PURPLE, "d"),
    (6.6, "G1", "Midterm", "exam gate", RED, "g"),
    (10, "M3", "Core-flow", "prototype", BLUE, "d"),
    (12, "M4", "Test-ready", "release", GREEN, "d"),
    (13.6, "M5", "Final report", "+ demo", PURPLE, "d"),
    (14.0, "G2", "Final", "exam gate", RED, "g"),
]
for wk, mid, a, b, col, kind in ms:
    x = L + wk * WK
    if kind == "g":
        s.rect(x - 9, 641, 18, 18, fill=RED, stroke=RED)
        s.text(x, 712, f"{mid} {a}", size=13, anchor="middle", weight="bold", fill=RED)
        s.text(x, 728, b, size=12, anchor="middle", fill=RED)
    else:
        s.path(f"M{x},{636} L{x + 13},{650} L{x},{664} L{x - 13},{650} z", stroke=col, fill=col)
        s.text(x, 626, f"{mid} {a}", size=13, anchor="middle", weight="bold", fill=col)
        s.text(x, 684, b, size=12, anchor="middle", fill=MUTED)

# Legend
s.path(f"M{L + 10},780 L{L + 22},792 L{L + 10},804 L{L - 2},792 z", fill=BLUE, stroke=BLUE)
s.text(L + 32, 797, "Milestone (artefact baselined in Git)", size=13)
s.rect(L + 330, 783, 18, 18, fill=RED, stroke=RED)
s.text(L + 358, 797, "Exam gate (no sprint work due)", size=13)
s.text(L + 620, 797, "Week numbers are planned and move with the lecture schedule.", size=13, fill=MUTED, italic=True)

s.save(out)
