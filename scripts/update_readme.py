#!/usr/bin/env python3
"""
Updates the README.md problems table based on .py files in the repo root.

File naming convention: {company}_{problem_name}.py
Required header fields (first 20 lines):
    # date: YYYY-MM-DD
    # topics: arrays, hash set
    # difficulty: easy
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
README_PATH = REPO_ROOT / "README.md"
TABLE_START = "<!-- PROBLEMS_TABLE_START -->"
TABLE_END = "<!-- PROBLEMS_TABLE_END -->"

SKIP_FILES = {"update_readme.py"}

HEADER_FIELDS = ("date", "topics", "difficulty")


def parse_header(filepath: Path) -> dict[str, str]:
    """Read metadata fields from the standardized file header (first 20 lines)."""
    fields: dict[str, str] = {}
    try:
        with open(filepath, encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= 20:
                    break
                m = re.match(r"#\s*(\w+):\s*(.+)", line.strip())
                if m:
                    key, value = m.group(1).lower(), m.group(2).strip()
                    if key in HEADER_FIELDS:
                        fields[key] = value
    except OSError:
        pass
    return fields


def parse_filename(filename: str) -> tuple[str, str]:
    """Extract (company, problem_name) from a filename like google_two_sum.py."""
    stem = Path(filename).stem
    parts = stem.split("_")
    company = parts[0].capitalize()
    problem = " ".join(word.capitalize() for word in parts[1:])
    return company, problem


def main() -> None:
    # Collect .py files in repo root matching the naming convention
    py_files = [
        f
        for f in REPO_ROOT.glob("*.py")
        if re.match(r"[a-z]+(?:_[a-z0-9]+)+\.py$", f.name)
        and f.name not in SKIP_FILES
    ]

    # Sort chronologically by # date: from file header
    py_files.sort(key=lambda f: parse_header(f).get("date", "9999"))

    # Build table
    header = "| # | Problem | Company | Topics | Difficulty |"
    sep    = "|---|---------|---------|--------|------------|"
    rows = []

    for i, filepath in enumerate(py_files, start=1):
        company, problem = parse_filename(filepath.name)
        meta = parse_header(filepath)
        topics     = meta.get("topics", "—")
        difficulty = meta.get("difficulty", "—")
        link = f"[{problem}]({filepath.name})"
        rows.append(f"| {i} | {link} | {company} | {topics} | {difficulty} |")

    table = "\n".join([header, sep] + rows)
    new_block = f"{TABLE_START}\n{table}\n{TABLE_END}"

    # Replace block in README
    content = README_PATH.read_text(encoding="utf-8")

    if TABLE_START not in content or TABLE_END not in content:
        print("ERROR: table markers not found in README.md")
        raise SystemExit(1)

    new_content = re.sub(
        rf"{re.escape(TABLE_START)}.*?{re.escape(TABLE_END)}",
        new_block,
        content,
        flags=re.DOTALL,
    )

    if new_content == content:
        print("README.md already up to date.")
        return

    README_PATH.write_text(new_content, encoding="utf-8")
    print(f"README.md updated ({len(py_files)} problems).")


if __name__ == "__main__":
    main()
