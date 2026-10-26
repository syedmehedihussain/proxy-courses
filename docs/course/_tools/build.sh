#!/usr/bin/env bash
# Rebuild every course diagram as SVG + PNG.
# Needs: python3, graphviz (dot), librsvg (rsvg-convert).  Run from anywhere:
#   bash docs/course/_tools/build.sh
set -euo pipefail
cd "$(dirname "$0")"
T1="../1. Software Process/diagrams"
T2="../2. Requirements/diagrams"
T3="../3. Design/diagrams"
mkdir -p "$T1" "$T2" "$T3"

# Hand-drawn diagrams (Python -> SVG)
python3 draw_task1.py "$T1/lifecycle.svg"
python3 draw_task2.py "$T2"
[ -f draw_task3.py ] && python3 draw_task3.py "$T3"

# Graphviz diagrams (.dot -> SVG)
for d in "$T1" "$T2" "$T3"; do
  for f in "$d"/*.dot; do
    [ -e "$f" ] || continue
    dot -Tsvg "$f" -o "${f%.dot}.svg"
  done
done

# Every SVG -> PNG at 1.5x for crisp slides and print
for d in "$T1" "$T2" "$T3"; do
  for f in "$d"/*.svg; do
    [ -e "$f" ] || continue
    rsvg-convert -z 1.5 -b white "$f" -o "${f%.svg}.png"
  done
done
echo "Diagrams rebuilt."
