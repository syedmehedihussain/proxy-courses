"""Task 3 hand-drawn diagrams: annotated wireframes and the login screen before/after."""
import os
import sys
from svgkit import *

outdir = sys.argv[1]
PH_W, PH_H = 390, 844


def phone(s, x, y, title=None):
    s.rect(x - 10, y - 10, PH_W + 20, PH_H + 20, fill="#d9dee4", stroke=INK, sw=2, rx=36)
    s.rect(x, y, PH_W, PH_H, fill="white", stroke="#9aa5b1", sw=1, rx=26)
    s.text(x + 24, y + 26, "9:41", size=12, weight="bold", fill=MUTED)
    s.text(x + PH_W - 24, y + 26, "4G ▮▮▮", size=12, anchor="end", fill=MUTED)
    if title:
        s.text(x + PH_W / 2, y - 26, title, size=16, anchor="middle", weight="bold")


def btn(s, x, y, w, h, label, primary=True, size=15):
    if primary:
        s.rect(x, y, w, h, fill=BLUE, stroke=BLUE, rx=10)
        s.text(x + w / 2, y + h / 2 + 5, label, size=size, anchor="middle", weight="bold", fill="white")
    else:
        s.rect(x, y, w, h, fill="white", stroke=BLUE, sw=1.6, rx=10)
        s.text(x + w / 2, y + h / 2 + 5, label, size=size - 1, anchor="middle", weight="bold", fill=BLUE)


def placeholder_lines(s, x, y, w, n, gap=14):
    for i in range(n):
        s.rect(x, y + i * gap, w * (0.95 if i < n - 1 else 0.6), 7, fill="#dfe3e8", stroke="none", rx=3)


def notes(s, x, y, items, width_chars=58, size=14):
    """Numbered notes; wraps long text roughly by characters."""
    cy = y
    for n, head, body in items:
        s.callout(x + 12, cy - 5, n)
        s.text(x + 34, cy, head, size=size, weight="bold")
        cy += size * 1.4
        words, line = body.split(), ""
        for w_ in words:
            if len(line) + len(w_) + 1 > width_chars:
                s.text(x + 34, cy, line, size=size - 1, fill=MUTED)
                cy += size * 1.3
                line = w_
            else:
                line = (line + " " + w_).strip()
        if line:
            s.text(x + 34, cy, line, size=size - 1, fill=MUTED)
            cy += size * 1.3
        cy += 14
    return cy


# ------------------------------------------------------------------ offering page
def offering(path):
    s = SVG(1040, 960)
    s.text(520, 34, "Wireframe 1: Offering page (mobile, 390 × 844)", size=22, anchor="middle", weight="bold")
    X, Y = 40, 90
    phone(s, X, Y)
    # top bar
    s.text(X + 20, Y + 64, "←", size=22, weight="bold")
    s.text(X + 56, Y + 62, "CSE211 · Autumn 2026", size=16, weight="bold")
    s.line(X, Y + 80, X + PH_W, Y + 80, stroke="#e4e7eb", sw=1)
    # video
    s.rect(X + 16, Y + 92, PH_W - 32, 198, fill="#cbd2d9", stroke="none", rx=10)
    s.circle(X + PH_W / 2, Y + 185, 30, fill="white", stroke="none")
    s.path(f"M{X + PH_W / 2 - 9},{Y + 168} L{X + PH_W / 2 + 15},{Y + 185} L{X + PH_W / 2 - 9},{Y + 202} z", fill=INK, stroke="none")
    s.rect(X + 28, Y + 256, 170, 24, fill=INK, stroke="none", rx=12)
    s.text(X + 113, Y + 273, "▶ Free intro video · 2:30", size=12, anchor="middle", fill="white", weight="bold")
    s.callout(X + PH_W - 10, Y + 100, "1")
    # tutor row
    s.circle(X + 44, Y + 330, 24, fill="#dfe3e8", stroke="none")
    s.text(X + 80, Y + 324, "Tanvir A.", size=16, weight="bold")
    s.rect(X + 80, Y + 334, 186, 24, fill=GREEN_BG, stroke=GREEN, sw=1, rx=12)
    s.text(X + 173, Y + 351, "✓ Verified A in CSE211", size=12, anchor="middle", fill=GREEN, weight="bold")
    s.callout(X + PH_W - 10, Y + 330, "2")
    s.text(X + 20, Y + 390, "★ 4.7  (32 reviews)  ·  58 subscribers", size=14, weight="bold")
    s.callout(X + PH_W - 10, Y + 385, "3")
    # demo card
    s.rect(X + 16, Y + 408, PH_W - 32, 96, fill=PURPLE_BG, stroke=PURPLE, sw=1.2, rx=10)
    s.text(X + 30, Y + 434, "Free live demo", size=15, weight="bold", fill=PURPLE)
    s.text(X + 30, Y + 456, "Sat 8 Nov · 8 pm · Meet", size=13)
    s.text(X + 30, Y + 476, "3 of 20 seats left", size=13, weight="bold", fill=RED)
    btn(s, X + 222, Y + 448, 140, 40, "Book free seat", primary=False, size=14)
    s.callout(X + PH_W - 10, Y + 420, "4")
    # what you get
    s.text(X + 20, Y + 534, "What you get this semester", size=15, weight="bold")
    for i, t in enumerate(["12 recorded classes (YouTube, unlisted)", "Notes PDF for every topic",
                           "Weekly live group class", "Add 1-to-1 session: ৳200 each"]):
        s.text(X + 24, Y + 560 + i * 22, "•  " + t, size=13)
    s.callout(X + PH_W - 10, Y + 548, "5")
    # reviews
    s.text(X + 20, Y + 672, "Reviews", size=15, weight="bold")
    placeholder_lines(s, X + 20, Y + 684, PH_W - 50, 3)
    # sticky bottom bar
    s.rect(X, Y + PH_H - 112, PH_W, 112, fill="white", stroke="#e4e7eb", sw=1)
    s.text(X + 16, Y + PH_H - 88, "৳500 / semester", size=15, weight="bold")
    s.text(X + PH_W - 16, Y + PH_H - 88, "Refund within 14 days", size=12, anchor="end", fill=MUTED)
    btn(s, X + 16, Y + PH_H - 74, PH_W - 32, 52, "Subscribe – ৳500", size=17)
    s.callout(X + PH_W - 10, Y + PH_H - 74, "6")

    notes(s, 490, 120, [
        ("1", "Free intro video first", "A free look before paying (proposal goal). Large 16:9 thumbnail with "
              "the length shown, so learners know the cost in time."),
        ("2", "Privacy-preserving trust badge", "Shows only “Verified A in CSE211”, never the transcript "
              "(win-win 2.13, NFR-05). Green = verified, used the same way everywhere."),
        ("3", "Social proof in one line", "Rating, review count and subscribers. Recognition rather than "
              "recall: no need to open another page to compare tutors."),
        ("4", "«extend» Book free demo (UC-04)", "Only shown when the demo has seats. Seats left in red "
              "creates honest urgency. Secondary (outline) style so it never competes with Subscribe."),
        ("5", "Plain list of what ৳500 buys", "Sets expectations and cuts refund requests. The add-on "
              "price is shown up front, with no surprises at checkout."),
        ("6", "One primary action, in the thumb zone", "Sticky full-width 358 × 52 px button at the "
              "bottom; the label states the price. See the Fitts's Law calculation in 3.9."),
    ])
    s.save(path)


# ------------------------------------------------------------------ checkout page
def checkout(path):
    s = SVG(1040, 960)
    s.text(520, 34, "Wireframe 2: Checkout (mobile, 390 × 844)", size=22, anchor="middle", weight="bold")
    X, Y = 40, 90
    phone(s, X, Y)
    s.text(X + 20, Y + 64, "✕", size=20, weight="bold")
    s.text(X + PH_W / 2, Y + 62, "Checkout", size=17, anchor="middle", weight="bold")
    s.line(X, Y + 80, X + PH_W, Y + 80, stroke="#e4e7eb", sw=1)
    # stepper
    for i, (lab, done) in enumerate([("Offering", True), ("Pay", True), ("Done", False)]):
        cx = X + 80 + i * 115
        s.circle(cx, Y + 112, 13, fill=BLUE if done else "white", stroke=BLUE, sw=1.6)
        s.text(cx, Y + 117, str(i + 1), size=12, anchor="middle", weight="bold", fill="white" if done else BLUE)
        s.text(cx, Y + 145, lab, size=12, anchor="middle", fill=MUTED)
        if i < 2:
            s.line(cx + 15, Y + 112, cx + 100, Y + 112, stroke=BLUE if i == 0 else "#cbd2d9", sw=2)
    s.callout(X + PH_W - 10, Y + 100, "1")
    # summary
    s.rect(X + 16, Y + 166, PH_W - 32, 112, fill=SOFT, stroke="#cbd2d9", sw=1, rx=10)
    s.text(X + 30, Y + 194, "CSE211 · Tanvir A.", size=16, weight="bold")
    s.text(X + 30, Y + 218, "Semester subscription · Autumn 2026", size=13, fill=MUTED)
    s.line(X + 30, Y + 234, X + PH_W - 30, Y + 234, stroke="#cbd2d9", sw=1)
    s.text(X + 30, Y + 262, "Total", size=15, weight="bold")
    s.text(X + PH_W - 30, Y + 262, "৳500", size=20, anchor="end", weight="bold")
    s.callout(X + PH_W - 10, Y + 176, "2")
    # refund box
    s.rect(X + 16, Y + 292, PH_W - 32, 64, fill=GREEN_BG, stroke=GREEN, sw=1, rx=10)
    s.text(X + 30, Y + 318, "Full refund until 9 Nov 2026", size=14, weight="bold", fill=GREEN)
    s.text(X + 30, Y + 340, "or before the 3rd live class, whichever is first", size=12, fill=GREEN)
    s.callout(X + PH_W - 10, Y + 300, "3")
    # methods
    s.text(X + 20, Y + 392, "Pay with", size=15, weight="bold")
    for i, (m, sel) in enumerate([("bKash  (used last time)", True), ("Nagad", False), ("Debit / credit card", False)]):
        yy = Y + 406 + i * 62
        s.rect(X + 16, yy, PH_W - 32, 52, fill=BLUE_BG if sel else "white", stroke=BLUE if sel else "#cbd2d9",
               sw=1.6 if sel else 1, rx=10)
        s.circle(X + 42, yy + 26, 9, fill="white", stroke=BLUE if sel else "#9aa5b1", sw=2)
        if sel:
            s.circle(X + 42, yy + 26, 4.5, fill=BLUE, stroke=BLUE, sw=0)
        s.text(X + 62, yy + 31, m, size=15, weight="bold" if sel else "normal")
    s.callout(X + PH_W - 10, Y + 414, "4")
    s.rect(X + 16, Y + 604, PH_W - 32, 54, fill="white", stroke="#cbd2d9", sw=1, rx=10, dash="4 3")
    s.text(X + 30, Y + 627, "You approve the payment in the bKash app.", size=12)
    s.text(X + 30, Y + 646, "Proxy Courses never sees your PIN.", size=12, fill=MUTED)
    s.callout(X + PH_W - 10, Y + 612, "5")
    # sticky
    s.rect(X, Y + PH_H - 112, PH_W, 112, fill="white", stroke="#e4e7eb", sw=1)
    btn(s, X + 16, Y + PH_H - 96, PH_W - 32, 52, "Pay ৳500 with bKash", size=17)
    s.text(X + PH_W / 2, Y + PH_H - 22, "Back to offering", size=13, anchor="middle", fill=BLUE, weight="bold")
    s.callout(X + PH_W - 10, Y + PH_H - 96, "6")

    notes(s, 490, 120, [
        ("1", "Progress + exit always visible", "“Step 2 of 3” lowers memory load; ✕ lets the user leave "
              "at any time with nothing charged (Mandel rule 1: user in control)."),
        ("2", "Summary in the user's words", "Course code, tutor, semester and total, so the learner can "
              "confirm without going back to the offering page."),
        ("3", "Refund rule as a real date", "Turns the rule (FR-25, win-win 2.13) into a date the "
              "learner doesn't have to work out. Green box = reassurance, same meaning across the app."),
        ("4", "Sensible default, easy to change", "Last-used method is pre-selected; each option is a "
              "52 px tall row, easy to tap with a thumb."),
        ("5", "Trust note", "Says where approval happens and that card or PIN data is never stored (NFR-06)."),
        ("6", "Button says exactly what happens", "“Pay ৳500 with bKash” updates with the method chosen. "
              "Same place and style as Subscribe on the previous screen (Mandel rule 3: consistency)."),
    ])
    s.save(path)


# ------------------------------------------------------------------ login before / after
def login(path):
    s = SVG(1240, 1290)
    s.text(620, 36, "Login screen: flawed version and corrected version", size=22, anchor="middle", weight="bold")
    # BEFORE
    X, Y = 60, 110
    phone(s, X, Y, "BEFORE (flawed)")
    s.rect(X + 95, Y + 70, 200, 150, fill="#dfe3e8", stroke="none", rx=8)
    s.text(X + 195, Y + 152, "BIG LOGO", size=18, anchor="middle", fill=MUTED, weight="bold")
    s.callout(X + 305, Y + 80, "1")
    s.rect(X + 40, Y + 270, 310, 40, fill="white", stroke="#d5d9de", sw=1, rx=2)
    s.text(X + 52, Y + 296, "Username", size=14, fill="#c4c9cf")
    s.callout(X + 360, Y + 290, "2")
    s.rect(X + 40, Y + 324, 310, 40, fill="white", stroke="#d5d9de", sw=1, rx=2)
    s.text(X + 52, Y + 350, "••••••", size=14, fill="#c4c9cf")
    s.text(X + 40, Y + 398, "Error 401", size=12, fill="#e58e8e")
    s.callout(X + 120, Y + 393, "3")
    s.rect(X + 40, Y + 420, 72, 26, fill="#9aa5b1", stroke="none", rx=2)
    s.text(X + 76, Y + 438, "LOGIN", size=11, anchor="middle", fill="white")
    s.rect(X + 118, Y + 420, 72, 26, fill="#9aa5b1", stroke="none", rx=2)
    s.text(X + 154, Y + 438, "RESET", size=11, anchor="middle", fill="white")
    s.callout(X + 210, Y + 433, "4")
    s.rect(X + 40, Y + 480, 310, 70, fill="#eef1f4", stroke="#d5d9de", sw=1)
    s.text(X + 195, Y + 522, "CAPTCHA  x7Gq2", size=16, anchor="middle", fill=MUTED, italic=True)
    s.callout(X + 360, Y + 500, "5")
    s.text(X + 195, Y + 800, "contact admin to register", size=10, anchor="middle", fill="#c4c9cf")
    s.callout(X + 330, Y + 795, "6")

    # AFTER
    X2 = 700
    phone(s, X2, Y, "AFTER (corrected)")
    s.text(X2 + 24, Y + 90, "Proxy Courses", size=18, weight="bold", fill=BLUE)
    s.text(X2 + 24, Y + 130, "Log in", size=26, weight="bold")
    s.text(X2 + 24, Y + 156, "Use your IUB student email", size=14, fill=MUTED)
    s.text(X2 + 24, Y + 200, "IUB email", size=14, weight="bold")
    s.rect(X2 + 24, Y + 210, 342, 52, fill="white", stroke=RED, sw=1.8, rx=8)
    s.text(X2 + 38, Y + 242, "2310690@gmail.com", size=15)
    s.text(X2 + 24, Y + 282, "⚠ Use your @iub.edu.bd address", size=13, fill=RED, weight="bold")
    s.text(X2 + 24, Y + 322, "Password", size=14, weight="bold")
    s.rect(X2 + 24, Y + 332, 342, 52, fill="white", stroke="#7b8794", sw=1.4, rx=8)
    s.text(X2 + 38, Y + 364, "••••••••", size=15)
    s.text(X2 + 352, Y + 364, "Show", size=13, anchor="end", fill=BLUE, weight="bold")
    s.text(X2 + 366, Y + 412, "Forgot password?", size=13, anchor="end", fill=BLUE, weight="bold")
    btn(s, X2 + 24, Y + 436, 342, 52, "Log in", size=17)
    s.text(X2 + PH_W / 2, Y + 528, "New to Proxy Courses?", size=13, anchor="middle", fill=MUTED)
    btn(s, X2 + 24, Y + 540, 342, 48, "Create an account", primary=False, size=15)
    for n, yy in [("1", Y + 96), ("2", Y + 230), ("3", Y + 278), ("4", Y + 456), ("5", Y + 380), ("6", Y + 560)]:
        s.callout(X2 + PH_W + 2, yy, n)

    # problem / fix table
    rows = [
        ("1", "Huge logo pushes the form down", "Small wordmark; the form starts in the top third"),
        ("2", "Placeholder-only “Username”: email or student ID?", "Visible label “IUB email” + example; placeholder never replaces the label"),
        ("3", "“Error 401”, pale red, far from the field", "Plain-language error under the field it belongs to, with the fix"),
        ("4", "Tiny 72×26 LOGIN next to RESET (wipes the form)", "One full-width 342×52 primary button; RESET removed"),
        ("5", "CAPTCHA on every login; no show-password", "“Show” toggle; CAPTCHA only after 5 failed tries (rate limit)"),
        ("6", "No sign-up or reset path; low-contrast text", "“Forgot password?” + “Create an account”; all text ≥ 4.5:1 contrast"),
    ]
    ty = 1046
    s.text(60, ty - 22, "Problem (before)", size=15, weight="bold", fill=RED)
    s.text(640, ty - 22, "Fix (after)", size=15, weight="bold", fill=GREEN)
    for i, (n, a, b) in enumerate(rows):
        yy = ty + i * 36
        s.callout(40, yy - 5, n)
        s.text(60, yy, a, size=14)
        s.text(640, yy, b, size=14)
    s.save(path)


offering(os.path.join(outdir, "wireframe-offering.svg"))
checkout(os.path.join(outdir, "wireframe-checkout.svg"))
login(os.path.join(outdir, "login-before-after.svg"))
