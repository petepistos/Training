#!/usr/bin/env python3
"""Add a consistent Back to Portal link to training and case-study pages.

This script updates HTML files in Introduction, Intermediate, Advanced, and
real-life-events. It is idempotent: running it again will not add duplicate
links or duplicate CSS.
"""

from __future__ import annotations

from pathlib import Path

MODULE_DIRS = ["Introduction", "Intermediate", "Advanced", "real-life-events"]

PORTAL_CSS = """
.portal-link{font-family:\"IBM Plex Mono\",monospace;font-size:11px;text-decoration:none;color:#1B2A4A;border:1px solid #D6CCBC;border-radius:5px;padding:7px 12px;background:#F5F1EB;white-space:nowrap;transition:all .15s;}
.portal-link:hover{background:#1B2A4A;color:#fff;border-color:#1B2A4A;}
""".strip()

PORTAL_LINK = '<a class="portal-link" href="../index.html">Back to Portal</a>'


def insert_css(text: str) -> str:
    if ".portal-link" in text:
        return text
    marker = "</style>"
    if marker not in text:
        raise ValueError("No </style> tag found")
    return text.replace(marker, PORTAL_CSS + "\n" + marker, 1)


def insert_link(text: str) -> str:
    if 'href="../index.html"' in text or "href='../index.html'" in text:
        return text

    # Introduction-style modules: header has a top-controls container.
    if '<div class="top-controls">' in text:
        return text.replace('<div class="top-controls">', '<div class="top-controls">\n    ' + PORTAL_LINK, 1)

    # Advanced and case-study modules: topbar contains logo block followed by nav-bar.
    topbar_close = "  </div>\n</div>\n\n<div class=\"nav-bar\""
    if topbar_close in text:
        return text.replace(topbar_close, "  </div>\n  " + PORTAL_LINK + "\n</div>\n\n<div class=\"nav-bar\"", 1)

    compact_topbar_close = "</div></div>\n<div class=\"nav-bar\""
    if compact_topbar_close in text:
        return text.replace(compact_topbar_close, "</div>" + PORTAL_LINK + "</div>\n<div class=\"nav-bar\"", 1)

    raise ValueError("Could not identify topbar insertion point")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    changed: list[Path] = []
    skipped: list[str] = []

    for dirname in MODULE_DIRS:
        module_dir = root / dirname
        if not module_dir.exists():
            skipped.append(f"{dirname}: directory not found")
            continue
        for html_file in sorted(module_dir.glob("*.html")):
            original = html_file.read_text(encoding="utf-8")
            try:
                updated = insert_link(insert_css(original))
            except ValueError as exc:
                skipped.append(f"{html_file.relative_to(root)}: {exc}")
                continue
            if updated != original:
                html_file.write_text(updated, encoding="utf-8")
                changed.append(html_file.relative_to(root))

    print(f"Updated files: {len(changed)}")
    for path in changed:
        print(f"- {path}")

    if skipped:
        print("Skipped files:")
        for item in skipped:
            print(f"- {item}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
