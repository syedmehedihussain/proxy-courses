"""Tiny SVG helper used by the draw_*.py scripts. No dependencies."""
import math
from xml.sax.saxutils import escape

FONT = "Noto Sans, Liberation Sans, Arial, sans-serif"

# Palette (kept small and print-friendly)
INK = "#1f2933"
MUTED = "#52606d"
LINE = "#3e4c59"
SOFT = "#f5f7fa"
BLUE = "#2563eb"
BLUE_BG = "#e8f0fe"
GREEN = "#15803d"
GREEN_BG = "#e7f6ec"
AMBER = "#b45309"
AMBER_BG = "#fdf3e1"
RED = "#b91c1c"
RED_BG = "#fdecec"
PURPLE = "#6d28d9"
PURPLE_BG = "#f1ebfd"
GREY_BG = "#eef1f4"


class SVG:
    def __init__(self, w, h, bg="white"):
        self.w, self.h = w, h
        self.items = []
        if bg:
            self.items.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>')

    # ---- primitives -------------------------------------------------------
    def rect(self, x, y, w, h, fill="white", stroke=LINE, sw=1.5, rx=0, dash=None, opacity=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' fill-opacity="{opacity}"' if opacity is not None else ""
        self.items.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{o} '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>'
        )

    def ellipse(self, cx, cy, rx, ry, fill="white", stroke=LINE, sw=1.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.items.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
        )

    def circle(self, cx, cy, r, fill="white", stroke=LINE, sw=1.5):
        self.items.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def line(self, x1, y1, x2, y2, stroke=LINE, sw=1.5, dash=None, end=None, start=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        me = f' marker-end="url(#{end})"' if end else ""
        ms = f' marker-start="url(#{start})"' if start else ""
        self.items.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}{me}{ms}/>'
        )

    def path(self, d, stroke=LINE, sw=1.5, fill="none", dash=None, end=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        me = f' marker-end="url(#{end})"' if end else ""
        self.items.append(f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}"{da}{me}/>')

    def text(self, x, y, s, size=14, anchor="start", weight="normal", fill=INK, italic=False):
        st = ' font-style="italic"' if italic else ""
        self.items.append(
            f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{fill}"{st}>{escape(str(s))}</text>'
        )

    def lines(self, x, y, rows, size=14, gap=1.3, **kw):
        """Several text rows; y is the baseline of the first row."""
        for i, r in enumerate(rows):
            self.text(x, y + i * size * gap, r, size=size, **kw)

    # ---- composites -------------------------------------------------------
    def box(self, x, y, w, h, title, rows=(), fill=SOFT, stroke=LINE, size=14, rx=8, title_fill=INK, sw=1.5):
        self.rect(x, y, w, h, fill=fill, stroke=stroke, rx=rx, sw=sw)
        cx = x + w / 2
        if rows:
            self.text(cx, y + 22, title, size=size, anchor="middle", weight="bold", fill=title_fill)
            self.lines(cx, y + 22 + size * 1.45, rows, size=size - 2, anchor="middle", fill=MUTED)
        else:
            self.text(cx, y + h / 2 + size * 0.35, title, size=size, anchor="middle", weight="bold", fill=title_fill)

    def actor(self, x, y, label, size=14, stroke=INK):
        """Stick figure; (x, y) is the top of the head."""
        self.circle(x, y + 12, 12, fill="white", stroke=stroke, sw=2)
        self.line(x, y + 24, x, y + 62, stroke=stroke, sw=2)
        self.line(x - 22, y + 38, x + 22, y + 38, stroke=stroke, sw=2)
        self.line(x, y + 62, x - 18, y + 92, stroke=stroke, sw=2)
        self.line(x, y + 62, x + 18, y + 92, stroke=stroke, sw=2)
        self.text(x, y + 112, label, size=size, anchor="middle", weight="bold")

    def callout(self, x, y, n, r=12):
        self.circle(x, y, r, fill=RED, stroke=RED)
        self.text(x, y + 5, n, size=13, anchor="middle", weight="bold", fill="white")

    # ---- output -----------------------------------------------------------
    def save(self, path):
        defs = f"""<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker>
  <marker id="open" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10" fill="none" stroke="{LINE}" stroke-width="1.5"/></marker>
  <marker id="tri" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="14" markerHeight="14" orient="auto-start-reverse">
    <path d="M0,0 L12,6 L0,12 z" fill="white" stroke="{LINE}" stroke-width="1.3"/></marker>
  <marker id="arrowred" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>
</defs>"""
        body = "\n".join(self.items)
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
            f'viewBox="0 0 {self.w} {self.h}">\n{defs}\n{body}\n</svg>\n'
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)


def ellipse_edge(cx, cy, rx, ry, tx, ty):
    """Point on an ellipse's border in the direction of (tx, ty)."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    t = 1 / math.sqrt((dx / rx) ** 2 + (dy / ry) ** 2)
    return cx + dx * t, cy + dy * t


def box_edge(x, y, w, h, tx, ty):
    """Point on a rectangle's border in the direction of (tx, ty)."""
    cx, cy = x + w / 2, y + h / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (w / 2) / abs(dx) if dx else float("inf")
    sy = (h / 2) / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s
