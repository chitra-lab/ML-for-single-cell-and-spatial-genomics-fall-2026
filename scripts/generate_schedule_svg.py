#!/usr/bin/env python3
"""Generate assets/course-schedule.svg from the ROWS data below.

Rationale: GitHub's markdown sanitizer strips style=/font color= and its
KaTeX renderer blocks \\colorbox, so the color-coded schedule is rendered as
a plain SVG instead. Text layout (column widths, wrapping, row heights) is
computed from estimated Helvetica/Arial glyph widths so nothing clips or
overlaps -- do not hand-edit the generated SVG XML; edit ROWS and rerun.
"""
import os

# Standard Helvetica glyph widths (per 1000 em), used to estimate Arial
# rendering widths for wrapping/layout since GitHub uses its own font stack.
HELV_WIDTHS = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667,
    "'": 191, '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333,
    '.': 278, '/': 278,
    '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556,
    '7': 556, '8': 556, '9': 556,
    ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015,
    'A': 667, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778,
    'H': 722, 'I': 278, 'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722,
    'O': 778, 'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722,
    'V': 667, 'W': 944, 'X': 667, 'Y': 667, 'Z': 611,
    '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556, '`': 333,
    'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556,
    'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833, 'n': 556,
    'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556,
    'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 500,
    '{': 334, '|': 260, '}': 334, '~': 584,
}
DEFAULT_WIDTH = 556
BOLD_FACTOR = 1.08  # Arial Bold runs ~8% wider than regular per glyph
SAFETY_MARGIN = 1.2  # cushion for viewers whose browser substitutes a wider fallback font than Arial/Helvetica


def text_width(s, font_size, bold=False):
    w = sum(HELV_WIDTHS.get(ch, DEFAULT_WIDTH) for ch in s) / 1000.0 * font_size
    w = w * BOLD_FACTOR if bold else w
    return w * SAFETY_MARGIN


def wrap_text(s, max_width, font_size, bold=False):
    words = s.split(' ')
    lines, cur = [], ''
    for word in words:
        trial = word if not cur else cur + ' ' + word
        if not cur or text_width(trial, font_size, bold) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---- Colors ----
COLORS = {
    'homework': '#0969DA',
    'lab': '#1A7F37',
    'quiz': '#9A6700',
    'oral': '#CF222E',
    'project': '#8250DF',
}
TEXT = '#1F2328'
SUBTEXT = '#57606A'
BORDER = '#D0D7DE'
STRIPE = '#FBFBFC'
HEADER_BG = '#F6F8FA'

# ---- Schedule data ----
# Each row: date, class number (None for no-class/special rows), topic,
# whether the topic itself is bold (special announcement rows), and a list
# of (note text, color key) tuples -- each rendered on its own line.
ROWS = [
    ('9/1', '1', 'Introduction + single-cell primer', False,
     [('HW1 released (due 9/17)', 'homework')]),
    ('9/3', '2', 'Linear algebra/probability refresher; prelab', False,
     [('Introduce Final Project', 'project')]),
    ('9/8', '3', 'Linear dimensionality reduction 1: PCA', False, []),
    ('9/10', '4', 'Linear dimensionality reduction 2: NMF', False, []),
    ('9/15', '5', 'Linear dimensionality reduction 3: probabilistic matrix factorization + in-class lab', False,
     [('Lab 1 in class (Report due 9/21)', 'lab')]),
    ('9/17', '6', 'Deep learning primer + AE', False,
     [('Quiz 1', 'quiz'), ('HW1 due', 'homework'), ('HW2 released (due 9/29)', 'homework')]),
    ('9/22', '7', 'Deep dimensionality reduction: VAE + contrastive learning', False, []),
    ('9/24', '8', 'Deep dimensionality reduction: FMs + in-class lab', False,
     [('Lab 2 in class (Report due 9/28)', 'lab')]),
    ('9/29', '9', 'Manifold learning / graphs 1: definitions + ISOMAP', False,
     [('Quiz 2', 'quiz'), ('HW2 due', 'homework'), ('HW3 released (due 10/13)', 'homework')]),
    ('10/1', '10', 'Manifold learning / graphs 2: random walks', False,
     [('Project proposal due', 'project')]),
    ('10/6', '11', 'Manifold learning / graphs 3: t-SNE/UMAP, Markov chains', False, []),
    ('10/8', '12', 'Manifold learning / graphs 4 (cont.) + in-class lab', False,
     [('Lab 3 in class (Report due 10/12)', 'lab')]),
    ('10/13', '13', 'Graph clustering', False,
     [('Quiz 3', 'quiz'), ('HW3 due', 'homework'), ('HW4 released (due 11/3)', 'homework')]),
    ('10/15', '14', 'Guest lecture: Atul Deshpande (SOM)', False, []),
    ('10/20', '15', 'Graph clustering (cont.) + GNNs', False, []),
    ('10/22', None, 'NO CLASS: Fall break', True,
     [('Oral Exam 1 (date TBD)', 'oral')]),
    ('10/27', '16', 'Spatial SVGs + neural fields (e.g. GASTON) + point processes (segmentation)', False, []),
    ('10/29', '17', 'Spatial (cont.) + in-class lab', False,
     [('Lab 4 in class (Report due 11/2)', 'lab')]),
    ('11/3', '18', 'Optimal transport I: Monge/Kantorovich/Wasserstein distance', False,
     [('Quiz 4', 'quiz'), ('HW4 due', 'homework'), ('HW5 released (due 11/17)', 'homework')]),
    ('11/5', '19', 'Optimal transport II: Sinkhorn', False, []),
    ('11/10', '20', 'OT 3: Gromov-Wasserstein, Dynamic OT, (semi-)balanced/unbalanced, applications', False, []),
    ('11/12', '21', 'OT 4 + in-class lab: score/flow/conditional flow matching', False,
     [('Lab 5 in class (Report due 11/16)', 'lab'), ('Project Preliminary Report due', 'project')]),
    ('11/17', '22', 'Guest lecture: Min-zhi Jiang (Biostats)', False,
     [('Quiz 5', 'quiz'), ('HW5 due', 'homework')]),
    ('11/19', '23', 'Guest lecture: Vishaka Gopalan (NIH) + Shashwat Kumar (BME)', False, []),
    ('11/24', None, 'NO CLASS: Thanksgiving break', True, []),
    ('11/26', None, 'NO CLASS: Thanksgiving break', True, []),
    ('12/1', '24', 'Guest lecture: Yiqun Chen (Biostats/CS)', False, []),
    ('12/3', '25', 'Project presentations', True, []),
    ('12/8', '26', 'Project presentations', True, []),
    ('12/10', '27', 'Project presentations', True,
     [('Final report due 12/12', 'project'), ('Oral Exam 2 (on final project)', 'oral')]),
]

LEGEND = [
    ('Homework', 'homework'), ('Lab', 'lab'), ('Quiz', 'quiz'),
    ('Oral Exam', 'oral'), ('Project', 'project'),
]

# ---- Font sizes (bumped up from the original 12.5/13pt pass for legibility) ----
FONT_BODY = 15
FONT_HEADER = 15.5
FONT_LEGEND = 14.5

# ---- Geometry ----
TABLE_X0 = 12
TABLE_WIDTH = 835
TABLE_X1 = TABLE_X0 + TABLE_WIDTH
VIEWBOX_WIDTH = TABLE_X0 * 2 + TABLE_WIDTH  # keep in sync with GitHub's readme column width

PAD_LEFT = 10
RIGHT_PAD = 10
COL_GAP = 16

BASELINE_OFFSET = 21   # row top -> first line baseline
LINE_INCREMENT = 20    # baseline -> next baseline (must exceed FONT_BODY to avoid vertical overlap)
BOTTOM_PAD = 12         # last baseline -> row bottom (descender clearance)
assert LINE_INCREMENT > FONT_BODY, 'line spacing must exceed font size or wrapped lines will overlap'

HEADER_BASELINE_OFFSET = 24
HEADER_ROW_HEIGHT = 37

TOP_MARGIN = 14
LEGEND_BASELINE = TOP_MARGIN + 20
TABLE_TOP = LEGEND_BASELINE + 18


def col_width(texts, font_size, bold_flags=None):
    if bold_flags is None:
        bold_flags = [False] * len(texts)
    return max(text_width(t, font_size, b) for t, b in zip(texts, bold_flags))


date_texts = [r[0] for r in ROWS]
class_texts = [r[1] for r in ROWS if r[1] is not None]
note_texts = [n for r in ROWS for n, _ in r[4]]

date_col_w = max(col_width(date_texts, FONT_BODY), text_width('Date', FONT_HEADER, True)) + COL_GAP
class_col_w = max(col_width(class_texts, FONT_BODY), text_width('Class', FONT_HEADER, True)) + COL_GAP
notes_col_w = max(col_width(note_texts, FONT_BODY, [True] * len(note_texts)),
                   text_width('Notes', FONT_HEADER, True)) + RIGHT_PAD

DATE_X = TABLE_X0 + PAD_LEFT
CLASS_X = DATE_X + date_col_w
TOPIC_X = CLASS_X + class_col_w
NOTES_X = TABLE_X1 - notes_col_w
TOPIC_WIDTH = NOTES_X - COL_GAP - TOPIC_X

assert TOPIC_WIDTH >= 200, f'topic column too narrow ({TOPIC_WIDTH:.0f}px) -- widen TABLE_WIDTH or shorten notes'

# Sanity: every note must fit inside its own column without wrapping unexpectedly.
notes_available_width = TABLE_X1 - NOTES_X
for note, _ in [(n, c) for r in ROWS for n, c in r[4]]:
    w = text_width(note, FONT_BODY, True)
    assert w <= notes_available_width + 1, (
        f'note "{note}" ({w:.0f}px) overflows notes column ({notes_available_width:.0f}px)'
    )

svg = []
svg.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VIEWBOX_WIDTH} 0" '
    f'font-family="Arial, Helvetica, sans-serif">'
)  # height patched in below once computed

body = []

# Legend
lx = TABLE_X0
body.append(f'<text x="{lx}" y="{LEGEND_BASELINE}" font-size="{FONT_LEGEND}" font-weight="bold" fill="{SUBTEXT}">Legend:</text>')
lx += text_width('Legend:', FONT_LEGEND, True) + 18
for label, key in LEGEND:
    body.append(f'<text x="{lx:.1f}" y="{LEGEND_BASELINE}" font-size="{FONT_LEGEND}" font-weight="bold" fill="{COLORS[key]}">{label}</text>')
    lx += text_width(label, FONT_LEGEND, True) + 18

# Header row
y = TABLE_TOP
body.append(f'<rect x="{TABLE_X0}" y="{y}" width="{TABLE_WIDTH}" height="{HEADER_ROW_HEIGHT}" fill="{HEADER_BG}" stroke="{BORDER}" stroke-width="1"/>')
hy = y + HEADER_BASELINE_OFFSET
for label, x in [('Date', DATE_X), ('Class', CLASS_X), ('Topic', TOPIC_X), ('Notes', NOTES_X)]:
    body.append(f'<text x="{x:.1f}" y="{hy}" font-size="{FONT_HEADER}" font-weight="bold" fill="{TEXT}">{label}</text>')
y += HEADER_ROW_HEIGHT

for i, (date, cls, topic, topic_bold, notes) in enumerate(ROWS):
    topic_lines = wrap_text(topic, TOPIC_WIDTH, FONT_BODY, topic_bold)
    n_lines = max(len(topic_lines), len(notes), 1)
    row_h = BASELINE_OFFSET + (n_lines - 1) * LINE_INCREMENT + BOTTOM_PAD

    if i % 2 == 1:
        body.append(f'<rect x="{TABLE_X0}" y="{y}" width="{TABLE_WIDTH}" height="{row_h}" fill="{STRIPE}"/>')
    body.append(f'<rect x="{TABLE_X0}" y="{y}" width="{TABLE_WIDTH}" height="{row_h}" fill="none" stroke="{BORDER}" stroke-width="1"/>')

    base = y + BASELINE_OFFSET
    body.append(f'<text x="{DATE_X}" y="{base}" font-size="{FONT_BODY}" fill="{TEXT}">{date}</text>')
    if cls is not None:
        body.append(f'<text x="{CLASS_X:.1f}" y="{base}" font-size="{FONT_BODY}" fill="{SUBTEXT}">{cls}</text>')

    weight = ' font-weight="bold"' if topic_bold else ''
    for li, line in enumerate(topic_lines):
        ty = base + li * LINE_INCREMENT
        body.append(f'<text x="{TOPIC_X:.1f}" y="{ty}" font-size="{FONT_BODY}"{weight} fill="{TEXT}">{line}</text>')

    for ni, (note, key) in enumerate(notes):
        ny = base + ni * LINE_INCREMENT
        body.append(f'<text x="{NOTES_X:.1f}" y="{ny}" font-size="{FONT_BODY}" font-weight="bold" fill="{COLORS[key]}">{note}</text>')

    y += row_h

VIEWBOX_HEIGHT = y + 4
svg[0] = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VIEWBOX_WIDTH} {VIEWBOX_HEIGHT}" '
    f'font-family="Arial, Helvetica, sans-serif">'
)
svg.append(f'<rect x="0" y="0" width="{VIEWBOX_WIDTH}" height="{VIEWBOX_HEIGHT}" fill="#ffffff"/>')
svg.extend(body)
svg.append('</svg>')

out_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'course-schedule.svg')
with open(out_path, 'w') as f:
    f.write('\n'.join(svg) + '\n')

print(f'Wrote {out_path}')
print(f'viewBox: 0 0 {VIEWBOX_WIDTH} {VIEWBOX_HEIGHT}')
print(f'columns -> date_x={DATE_X} class_x={CLASS_X:.1f} topic_x={TOPIC_X:.1f} topic_w={TOPIC_WIDTH:.1f} notes_x={NOTES_X:.1f} notes_w={notes_available_width:.1f}')
