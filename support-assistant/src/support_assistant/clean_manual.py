"""
Clean a manual converted from Word to Markdown, ready for chunking.

Usage:
    uv run python src/clean_manual.py raw/manual.docx
    uv run python src/clean_manual.py raw/manual.md --apply-terms

Input can be a .docx (converted with markitdown first) or an already converted .md.
Writes two files to knowledge/manual/:
    <name>.md                 the cleaned manual
    <name>.cleanup-report.md  what was changed, and what needs a human look

Generic conversion fixes live in this script. Manual-specific fixes
(garbled phrases, heading renames, terminology) live in config/clean_rules.yaml.
"""

import argparse
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

import yaml

RULES_FILE = Path("config/clean_rules.yaml")
OUT_DIR = Path("knowledge/manual")

HEADING = re.compile(r"^(#{1,6})\s*(.*?)\s*$")
TOP_NUMBERED = re.compile(r"^(\d+)\.\s")          # "3. Click Save" at column 0
BROKEN_SUBLIST_START = re.compile(r"^\*\s+\d+\.\s+")  # "* 1. First and last name"
BROKEN_SUBLIST_NEXT = re.compile(r"^ {1,2}\d+\.\s+")   # "  2. Phone number"
IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
INTERNAL_LINK = re.compile(r"\[([^\]]+)\]\(#[^)]*\)")
TOC_LINE = re.compile(r"^\[.*?\s\d+\**\]\(#[^)]*\)\s*$")
ZERO_WIDTH = re.compile("[\u200b\u200c\u200d\u2060\ufeff\u00ad]")
VERSION = re.compile(r"\(Version\s+([\d.]+)\)", re.I)

# Lines that interrupt a numbered list without ending it (notes, tips, examples,
# sub-items, captions). A numbered list that restarts at "1." after one of these
# is treated as a continuation.
INTERRUPTER = re.compile(
    r"^(\s+\S|[*+-]\s|\*\*(NB|TIPS?|Note|Important|Please note)\b|NB:|\*Example|\*Image|Image\s*-)",
    re.I,
)
CAPTION_PREFIX = re.compile(r"^(table|image|example|nb|tips?|note|important|please note)\b", re.I)


class Report:
    def __init__(self):
        self.counts = Counter()
        self.items = {}  # section name -> list of lines

    def add(self, section, text):
        self.items.setdefault(section, []).append(text)

    def count(self, key, n=1):
        self.counts[key] += n


def load_input(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        from markitdown import MarkItDown
        return MarkItDown().convert(str(path)).text_content
    return path.read_text(encoding="utf-8")


# ---------- Step 1: character and inline cleanup ----------

def clean_inline(text: str, rep: Report) -> str:
    n = len(ZERO_WIDTH.findall(text))
    text = ZERO_WIDTH.sub("", text)
    rep.count("invisible characters removed", n)

    text = text.replace("\u00a0", " ")

    n = len(IMAGE.findall(text))
    text = IMAGE.sub("", text)
    rep.count("image placeholders removed", n)

    n = len(INTERNAL_LINK.findall(text))
    text = INTERNAL_LINK.sub(r"\1", text)
    rep.count("internal links turned into plain text", n)

    n = len(re.findall(r"</?u>", text))
    text = re.sub(r"</?u>", "", text)
    rep.count("underline tags removed", n)
    return text


# ---------- Step 2: line-level cleanup ----------

def remove_toc(lines, rep):
    out, removed = [], 0
    for line in lines:
        if TOC_LINE.match(line.strip()) or line.strip().lower() == "table of contents":
            removed += 1
            continue
        out.append(line)
    rep.count("table-of-contents lines removed", removed)
    return out


def clean_headings(lines, rep):
    out = []
    for line in lines:
        m = HEADING.match(line)
        if m:
            hashes, text = m.groups()
            text = text.replace("**", "").strip().rstrip(":→").strip()
            if not text:
                rep.count("empty headings removed")
                continue
            line = f"{hashes} {text}"
        # lines left empty after removing an image, e.g. "*![](...)*" -> "**"
        if line.strip() in {"*", "**", "***"}:
            continue
        out.append(line.rstrip())
    return out


def promote_fake_headings(lines, rep):
    """Turn standalone bold/italic lines and standalone questions into headings."""
    out, level = [], 0
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            level = len(m.group(1))
            out.append(line)
            continue
        prev_blank = i == 0 or not lines[i - 1].strip()
        s = line.strip()
        candidate = None
        emph = re.fullmatch(r"(\*\*|\*)([^*]+)\1", s)
        if emph and prev_blank:
            candidate = emph.group(2).strip()
        elif prev_blank and s.endswith("?") and len(s) <= 80 and not re.match(r"^[\d*+-]", s):
            candidate = s
        if (
            candidate
            and len(candidate) <= 80
            and not candidate.endswith(".")
            and not CAPTION_PREFIX.match(candidate)
        ):
            new_level = min(level + 1, 6) if level else 1
            out.append(f"{'#' * new_level} {candidate}")
            level = level or 1  # later questions nest under a promoted top heading
            rep.add("Promoted to heading (check the level)", f"`{'#' * new_level} {candidate}`")
            rep.count("lines promoted to headings")
            continue
        out.append(line)
    return out


def fix_broken_sublists(lines, rep):
    """markitdown turns some sub-lists into '* 1. ...' followed by '  2. ...'."""
    out, in_broken = [], False
    for line in lines:
        if BROKEN_SUBLIST_START.match(line):
            in_broken = True
            out.append("   - " + BROKEN_SUBLIST_START.sub("", line))
            rep.count("broken sub-list items repaired")
            continue
        if in_broken and BROKEN_SUBLIST_NEXT.match(line):
            out.append("   - " + BROKEN_SUBLIST_NEXT.sub("", line))
            rep.count("broken sub-list items repaired")
            continue
        in_broken = False
        out.append(line)
    return out


def renumber_lists(lines, rep):
    """Continue step numbering that restarted at 1 after an NB/TIP/example."""
    out = []
    last_num, offset, continuable = 0, 0, False
    section = ""
    for line in lines:
        m = HEADING.match(line)
        if m:
            section = m.group(2)
            last_num, offset, continuable = 0, 0, False
            out.append(line)
            continue
        if not line.strip():
            out.append(line)
            continue
        num = TOP_NUMBERED.match(line)
        if num:
            k = int(num.group(1))
            if k == 1 and continuable and last_num > 0:
                offset = last_num
                rep.add(
                    "Renumbered steps (check these)",
                    f"{section}: list restarted at 1, continued from {last_num + 1}",
                )
            elif k == last_num + 1 and k + offset != last_num + 1:
                offset = 0
            new = k + offset
            if new != k:
                line = TOP_NUMBERED.sub(f"{new}. ", line, count=1)
                rep.count("steps renumbered")
            last_num, continuable = new, True
            out.append(line)
            continue
        if INTERRUPTER.match(line):
            out.append(line)  # keep list state
            continue
        # A paragraph like "you can skip steps 3 and 4" also continues the list
        refs = [int(x) for x in re.findall(r"\bsteps?\s+(\d+)", line, re.I)]
        if last_num and (last_num + 1) in refs:
            out.append(line)
            continue
        last_num, offset, continuable = 0, 0, False
        out.append(line)
    return out


# ---------- Step 3: rules from the YAML file ----------

def apply_fixes(text, fixes, rep):
    for old, new in fixes.items():
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            rep.count("text fixes applied", n)
            rep.add("Text fixes applied", f"'{old}' -> '{new}' ({n}x)")
    return text


def apply_heading_renames(lines, renames, rep):
    seen = Counter()
    out = []
    for line in lines:
        m = HEADING.match(line)
        if m:
            level, text = len(m.group(1)), m.group(2)
            seen[(level, text)] += 1
            for r in renames:
                if r["level"] == level and r["old"] == text and r.get("nth", seen[(level, text)]) == seen[(level, text)]:
                    line = f"{'#' * level} {r['new']}"
                    rep.add("Headings renamed", f"'{text}' -> '{r['new']}'")
                    rep.count("headings renamed")
                    break
        out.append(line)
    return out


def match_case(src, repl):
    return repl[0].upper() + repl[1:] if src[0].isupper() else repl


def handle_terms(text, terms, apply, rep):
    for old in sorted(terms, key=len, reverse=True):
        pattern = re.compile(rf"\b{re.escape(old)}\b", re.I)
        hits = pattern.findall(text)
        if not hits:
            continue
        new = terms[old]
        if apply:
            text = pattern.sub(lambda m: match_case(m.group(0), new), text)
            rep.add("Terminology replaced", f"'{old}' -> '{new}' ({len(hits)}x)")
        else:
            rep.add("Terminology found (not changed; use --apply-terms)", f"'{old}' ({len(hits)}x) -> suggested '{new}'")
    return text


# ---------- Step 4: things only a human can judge ----------

def flag_for_review(lines, dutch_words, rep):
    heading_counts = Counter()
    for i, line in enumerate(lines, 1):
        m = HEADING.match(line)
        if m:
            heading_counts[m.group(2)] += 1
        for w in dutch_words:
            if re.search(rf"\b{re.escape(w)}\b", line, re.I):
                rep.add("Possible untranslated Dutch", f"line {i}: {line.strip()[:100]}")
                break
        # glued capitals like "DThe", "THEIn": two+ capitals then a capitalized word
        for tok in re.findall(r"\b[A-Z]{1,4}(?:The|In|If|A|An|Th)\w*\b", line):
            if not re.fullmatch(r"[A-Z]+s?", tok):
                rep.add("Suspicious glued words", f"line {i}: '{tok}' in: {line.strip()[:80]}")
        if re.match(r"^\*\*(NB|TIP)\*?\*?:?\*?\*?\s*$", line.strip()):
            rep.add("Empty NB/TIP notes", f"line {i}")
        if line.strip().endswith(":") and i < len(lines) and not lines[i].strip() and (i + 1 >= len(lines) or HEADING.match(lines[i + 1])):
            rep.add("Lines ending in a colon with nothing after (check for missing content)", f"line {i}: {line.strip()[:80]}")
    for h, n in heading_counts.items():
        if n > 1:
            rep.add("Duplicate headings (fine if the parent differs)", f"'{h}' ({n}x)")


def collapse_blank_lines(lines):
    out = []
    for line in lines:
        if not line.strip() and out and not out[-1].strip():
            continue
        out.append(line)
    while out and not out[0].strip():
        out.pop(0)
    return out


# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path)
    ap.add_argument("--apply-terms", action="store_true", help="replace terminology from the rules file")
    ap.add_argument("--rules", type=Path, default=RULES_FILE)
    ap.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = ap.parse_args()

    if not args.input.exists():
        sys.exit(f"Input not found: {args.input}")
    rules = yaml.safe_load(args.rules.read_text(encoding="utf-8")) if args.rules.exists() else {}
    rep = Report()

    text = load_input(args.input)
    version = VERSION.search(text)

    # TOC first: it is recognised by its links, which clean_inline removes
    text = "\n".join(remove_toc(text.splitlines(), rep))
    text = clean_inline(text, rep)
    text = apply_fixes(text, rules.get("fixes") or {}, rep)

    lines = text.splitlines()
    lines = clean_headings(lines, rep)
    lines = promote_fake_headings(lines, rep)
    lines = apply_heading_renames(lines, rules.get("heading_renames") or [], rep)
    lines = fix_broken_sublists(lines, rep)
    lines = renumber_lists(lines, rep)
    lines = collapse_blank_lines(lines)

    text = "\n".join(lines)
    text = handle_terms(text, rules.get("terms") or {}, args.apply_terms, rep)
    lines = text.splitlines()
    flag_for_review(lines, rules.get("dutch_words") or [], rep)

    front = [
        "---",
        f"source_file: {args.input.name}",
        f"manual_version: {version.group(1) if version else 'unknown'}",
        f"cleaned_on: {date.today().isoformat()}",
        f"terms_applied: {str(args.apply_terms).lower()}",
        "---",
        "",
    ]

    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.input.stem
    out_md = args.out_dir / f"{stem}.md"
    out_rep = args.out_dir / f"{stem}.cleanup-report.md"
    out_md.write_text("\n".join(front + lines) + "\n", encoding="utf-8")

    r = [f"# Cleanup report: {args.input.name}", "", "## Automatic changes", ""]
    r += [f"- {k}: {v}" for k, v in rep.counts.items() if v]
    for section, items in rep.items.items():
        r += ["", f"## {section}", ""] + [f"- {x}" for x in items]
    out_rep.write_text("\n".join(r) + "\n", encoding="utf-8")

    print(f"Cleaned manual: {out_md}")
    print(f"Report:         {out_rep}")
    for k, v in rep.counts.items():
        if v:
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
