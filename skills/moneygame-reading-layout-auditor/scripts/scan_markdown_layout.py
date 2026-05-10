#!/usr/bin/env python3
"""Quick Markdown layout scan for MoneyGameSurvivalGuide chapters."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


LONG_PARAGRAPH = 520
VERY_LONG_PARAGRAPH = 760
LONG_LINE = 150
LONG_TABLE_LINE = 130
LIST_RUN = 8
UNICODE_BULLETS = ("•", "👉", "→")


def display_width(text: str) -> int:
    width = 0
    for ch in text:
        width += 2 if ord(ch) > 127 else 1
    return width


def flush_paragraph(findings, path, start_line, lines):
    if not lines:
        return
    text = " ".join(line.strip() for line in lines)
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return
    length = len(compact)
    if length >= VERY_LONG_PARAGRAPH:
        severity = "High"
    elif length >= LONG_PARAGRAPH:
        severity = "Medium"
    else:
        return
    findings.append(
        {
            "severity": severity,
            "path": path,
            "line": start_line,
            "kind": "long_paragraph",
            "message": f"paragraph length {length} chars",
        }
    )


def scan_file(path: Path):
    findings = []
    lines = path.read_text(encoding="utf-8").splitlines()
    paragraph = []
    paragraph_start = 0
    list_run_start = None
    list_run_count = 0

    image_refs = []

    def end_list_run(current_line: int):
        nonlocal list_run_start, list_run_count
        if list_run_count >= LIST_RUN:
            findings.append(
                {
                    "severity": "Medium",
                    "path": path,
                    "line": list_run_start,
                    "kind": "dense_list",
                    "message": f"{list_run_count} consecutive list items before line {current_line}",
                }
            )
        list_run_start = None
        list_run_count = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        is_heading = stripped.startswith("#")
        is_blank = stripped == ""
        is_list = bool(re.match(r"^(\s*[-*+]\s+|\s*\d+\.\s+)", line))
        is_table = stripped.startswith("|") and stripped.endswith("|")
        is_block = stripped.startswith(">") or stripped.startswith("<")
        is_image = "![" in stripped and "](" in stripped
        is_unicode_bullet = stripped.startswith(UNICODE_BULLETS)

        if is_image:
            for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", stripped):
                image_refs.append((idx, match.group(1)))

        if is_unicode_bullet:
            findings.append(
                {
                    "severity": "Medium",
                    "path": path,
                    "line": idx,
                    "kind": "unicode_bullet_not_markdown",
                    "message": "line may collapse into the previous paragraph in Markdown renderers",
                }
            )

        if is_list:
            if list_run_start is None:
                list_run_start = idx
            list_run_count += 1
        else:
            end_list_run(idx)

        if is_table and display_width(line) >= LONG_TABLE_LINE:
            findings.append(
                {
                    "severity": "Medium",
                    "path": path,
                    "line": idx,
                    "kind": "wide_table_line",
                    "message": f"table display width {display_width(line)}",
                }
            )

        if not is_table and display_width(line) >= LONG_LINE:
            findings.append(
                {
                    "severity": "Low",
                    "path": path,
                    "line": idx,
                    "kind": "long_source_line",
                    "message": f"line display width {display_width(line)}",
                }
            )

        if is_blank or is_heading or is_list or is_table or is_block:
            flush_paragraph(findings, path, paragraph_start, paragraph)
            paragraph = []
            paragraph_start = 0
        else:
            if not paragraph:
                paragraph_start = idx
            paragraph.append(line)

    flush_paragraph(findings, path, paragraph_start, paragraph)
    end_list_run(len(lines) + 1)

    for line_no, ref in image_refs:
        if ref.startswith(("http://", "https://", "#")):
            continue
        image_path = (path.parent / ref).resolve()
        if not image_path.exists():
            findings.append(
                {
                    "severity": "Critical",
                    "path": path,
                    "line": line_no,
                    "kind": "missing_image",
                    "message": f"missing image: {ref}",
                }
            )

    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Markdown files to scan")
    args = parser.parse_args()

    all_findings = []
    for item in args.files:
        path = Path(item)
        if not path.exists() or path.suffix.lower() != ".md":
            continue
        all_findings.extend(scan_file(path))

    order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
    all_findings.sort(key=lambda f: (order[f["severity"]], str(f["path"]), f["line"]))

    counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    for finding in all_findings:
        counts[finding["severity"]] += 1

    print("# Markdown Layout Scan")
    print()
    print("| Severity | Count |")
    print("|---|---:|")
    for severity in ["Critical", "High", "Medium", "Low"]:
        print(f"| {severity} | {counts[severity]} |")
    print()
    print("| Severity | File | Line | Kind | Message |")
    print("|---|---|---:|---|---|")
    cwd = Path.cwd()
    for finding in all_findings:
        try:
            rel = Path(finding["path"]).resolve().relative_to(cwd)
        except ValueError:
            rel = finding["path"]
        print(
            f"| {finding['severity']} | `{rel}` | {finding['line']} | "
            f"{finding['kind']} | {finding['message']} |"
        )


if __name__ == "__main__":
    main()
