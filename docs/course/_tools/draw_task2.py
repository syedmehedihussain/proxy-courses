"""Task 2 hand-drawn diagrams: power-interest grid and use-case diagram."""
import os
import sys
from svgkit import *

outdir = sys.argv[1]


# ---------------------------------------------------------------- power-interest grid
def pi_grid(path):
    s = SVG(1100, 840)
    s.text(550, 38, "Proxy Courses: stakeholder power–interest grid", size=22, anchor="middle", weight="bold")
    X0, Y0, PW, PH = 130, 70, 900, 660  # plot area

    def px(v):
        return X0 + v / 10 * PW

    def py(v):
        return Y0 + PH - v / 10 * PH

    quads = [
        (0, 5, "KEEP SATISFIED", "high power · low interest", AMBER_BG, AMBER),
        (5, 5, "MANAGE CLOSELY", "high power · high interest", RED_BG, RED),
        (0, 0, "MONITOR", "low power · low interest", GREY_BG, MUTED),
        (5, 0, "KEEP INFORMED", "low power · high interest", BLUE_BG, BLUE),
    ]
    for ix, iy, name, sub, bg, col in quads:
        s.rect(px(ix), py(iy + 5), PW / 2, PH / 2, fill=bg, stroke="white", sw=3)
        tx = px(ix) + 16
        ty = py(iy + 5) + 30
        s.text(tx, ty, name, size=17, weight="bold", fill=col)
        s.text(tx, ty + 20, sub, size=12, fill=col)
    s.rect(X0, Y0, PW, PH, fill="none", stroke=LINE, sw=2)

    # axes
    s.line(X0, Y0 + PH, X0 + PW + 20, Y0 + PH, sw=2, end="arrow")
    s.line(X0, Y0 + PH, X0, Y0 - 20, sw=2, end="arrow")
    for v in range(0, 11, 2):
        s.text(px(v), Y0 + PH + 20, str(v), size=12, anchor="middle", fill=MUTED)
        s.text(X0 - 10, py(v) + 4, str(v), size=12, anchor="end", fill=MUTED)
    s.text(X0 + PW / 2, Y0 + PH + 50, "INTEREST in the project (1–10)  →", size=15, anchor="middle", weight="bold")
    s.items.append(
        f'<text x="60" y="{Y0 + PH / 2}" font-family="{FONT}" font-size="15" font-weight="bold" '
        f'text-anchor="middle" fill="{INK}" transform="rotate(-90 60 {Y0 + PH / 2})">POWER over the project (1–10)  →</text>'
    )

    # (id, label, interest, power, label side)
    pts = [
        ("S1", "Learners", 9.6, 6.2, "l"),
        ("S2", "Tutors", 8.9, 7.0, "l"),
        ("S3", "Course faculty (evaluator)", 8.0, 9.0, "l"),
        ("S4", "Project team / admins", 9.7, 8.1, "l"),
        ("S5", "IUB administration & CSE dept", 4.2, 9.0, "l"),
        ("S6", "Payment gateway provider", 2.0, 7.0, "r"),
        ("S7", "Faculty of tutored courses", 3.8, 6.0, "r"),
        ("S8", "Faculty advisors", 6.2, 3.7, "r"),
        ("S9", "Club executives", 7.2, 2.8, "r"),
        ("S10", "Parents / guardians", 6.0, 2.0, "r"),
        ("S11", "Private coaching centres", 3.0, 2.0, "r"),
        ("S12", "IUB IT services (email)", 2.0, 3.8, "r"),
    ]
    for sid, label, i, p, side in pts:
        x, y = px(i), py(p)
        s.circle(x, y, 8, fill=INK, stroke="white", sw=2)
        if side == "r":
            s.text(x + 14, y + 5, f"{sid} {label}", size=14)
        else:
            s.text(x - 14, y + 5, f"{sid} {label}", size=14, anchor="end")
    s.save(path)


# ---------------------------------------------------------------- use-case diagram
def use_case(path):
    s = SVG(1440, 1010)
    s.text(720, 34, "Proxy Courses: use-case diagram (v1)", size=22, anchor="middle", weight="bold")
    s.rect(270, 58, 860, 920, fill="#fbfcfd", stroke=LINE, sw=2, rx=6)
    s.text(290, 84, "Proxy Courses (system boundary)", size=15, weight="bold", fill=MUTED)

    RX, RY = 118, 33
    uc = {
        "UC01": (440, 130, ["Register & verify", "IUB email"]),
        "UC02": (505, 215, ["Search tutors", "by course code"]),
        "UC03": (535, 300, ["View offering &", "intro video"]),
        "UC04": (850, 300, ["Book free", "live demo"]),
        "UC05": (535, 395, ["Subscribe to", "offering (৳500)"]),
        "UC06": (850, 395, ["Pay via", "payment gateway"]),
        "UC07": (520, 485, ["Rate & review", "tutor"]),
        "UC08": (485, 570, ["Request", "refund"]),
        "UC09": (430, 660, ["Book advising", "slot"]),
        "UC10": (480, 800, ["Apply as tutor", "(upload transcript)"]),
        "UC11": (480, 890, ["Publish offering", "& demos"]),
        "UC12": (930, 655, ["Verify tutor", "application"]),
        "UC13": (930, 560, ["Process", "refund"]),
        "UC14": (930, 750, ["Generate monthly", "tutor payouts"]),
        "UC15": (930, 890, ["Publish advising", "slots"]),
    }

    def edge(u, tx, ty):
        cx, cy, _ = uc[u]
        return ellipse_edge(cx, cy, RX, RY, tx, ty)

    # actors
    s.actor(115, 345, "Learner")
    s.actor(115, 770, "Tutor")
    s.actor(1300, 560, "Admin")
    s.actor(1300, 840, "Advisor")
    s.text(115, 477, "(any verified IUB student)", size=12, anchor="middle", fill=MUTED)
    # generalisation: Tutor is a Learner
    s.line(115, 768, 115, 490, end="tri", sw=1.6)
    s.text(125, 610, "generalisation:", size=12, fill=MUTED)
    s.text(125, 626, "a tutor is also", size=12, fill=MUTED)
    s.text(125, 642, "a learner", size=12, fill=MUTED)

    # external systems
    def ext(x, y, w, h, name, sub):
        s.rect(x, y, w, h, fill=GREY_BG, stroke=LINE, sw=1.6, rx=4)
        s.text(x + w / 2, y + 20, "«system»", size=12, anchor="middle", fill=MUTED)
        s.text(x + w / 2, y + 40, name, size=14, anchor="middle", weight="bold")
        if sub:
            s.text(x + w / 2, y + 58, sub, size=12, anchor="middle", fill=MUTED)

    ext(1215, 92, 180, 70, "Email service", "Resend / SMTP")
    ext(1215, 355, 180, 76, "Payment gateway", "bKash · Nagad · card")

    # associations
    LA = (140, 390)
    for u in ["UC01", "UC02", "UC03", "UC05", "UC07", "UC08", "UC09"]:
        x, y = edge(u, *LA)
        s.line(LA[0], LA[1], x, y)
    TA = (140, 815)
    for u in ["UC10", "UC11"]:
        x, y = edge(u, *TA)
        s.line(TA[0], TA[1], x, y)
    AA = (1275, 605)
    for u in ["UC12", "UC13", "UC14"]:
        x, y = edge(u, *AA)
        s.line(AA[0], AA[1], x, y)
    VA = (1275, 885)
    x, y = edge("UC15", *VA)
    s.line(VA[0], VA[1], x, y)
    PG = (1215, 393)
    for u in ["UC06", "UC13"]:
        x, y = edge(u, *PG)
        s.line(PG[0], PG[1], x, y)
    EM = (1215, 127)
    for u in ["UC01", "UC04"]:
        x, y = edge(u, *EM)
        s.line(EM[0], EM[1], x, y)

    # include / extend
    a = edge("UC05", 850, 395)
    b = edge("UC06", 535, 395)
    s.line(a[0], a[1], b[0], b[1], dash="7 5", end="open")
    s.text((a[0] + b[0]) / 2, 386, "«include»", size=13, anchor="middle", fill=BLUE, weight="bold")
    a = edge("UC04", 535, 300)
    b = edge("UC03", 850, 300)
    s.line(a[0], a[1], b[0], b[1], dash="7 5", end="open")
    s.text((a[0] + b[0]) / 2, 291, "«extend»", size=13, anchor="middle", fill=PURPLE, weight="bold")
    s.text((a[0] + b[0]) / 2, 350, "[demo has free seats]", size=11, anchor="middle", fill=PURPLE)

    # ellipses on top
    for u, (cx, cy, rows) in uc.items():
        s.ellipse(cx, cy, RX, RY, fill="white", stroke=BLUE, sw=1.8)
        s.text(cx, cy - 13, u.replace("UC", "UC-"), size=11, anchor="middle", fill=BLUE, weight="bold")
        s.text(cx, cy + 3, rows[0], size=13, anchor="middle")
        s.text(cx, cy + 19, rows[1], size=13, anchor="middle")

    # legend
    s.text(290, 945, "Solid line = association · hollow triangle = generalisation", size=12, fill=MUTED)
    s.text(290, 963, "Dashed open arrow = «include» (base → included) / «extend» (extension → base)", size=12, fill=MUTED)
    s.save(path)


pi_grid(os.path.join(outdir, "power-interest-grid.svg"))
use_case(os.path.join(outdir, "use-case-diagram.svg"))
