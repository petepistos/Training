#!/usr/bin/env python3
"""Static link audit for the Pistos Security Awareness Training repository.

The script scans HTML files for repository-local href/src references and verifies
that each target exists on disk. It ignores external URLs, mailto/tel links,
JavaScript pseudo-links, fragments, data URIs, and in-page anchors.

Usage:
    python scripts/link_audit.py
    python scripts/link_audit.py --root .
    python scripts/link_audit.py --training-only
"""

from __future__ import annotations

import argparse
import html.parser
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

DEFAULT_SCOPES = [
    "index.html",
    "Introduction",
    "Intermediate",
    "Advanced",
    "real-life-events",
]

TRAINING_ONLY_SCOPES = [
    "index.html",
    "Introduction",
    "Intermediate",
    "Advanced",
]

MODULE_FOLDERS = {"Introduction", "Intermediate", "Advanced", "real-life-events"}

IGNORED_SCHEMES = {
    "http",
    "https",
    "mailto",
    "tel",
    "javascript",
    "data",
    "blob",
}

CHECKED_ATTRIBUTES = {"href", "src"}


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in CHECKED_ATTRIBUTES and value:
                self.refs.append((name, value.strip(), self.getpos()[0]))


def iter_html_files(root: Path, training_only: bool) -> list[Path]:
    files: list[Path] = []
    scopes = TRAINING_ONLY_SCOPES if training_only else DEFAULT_SCOPES
    for scope in scopes:
        path = root / scope
        if path.is_file() and path.suffix.lower() == ".html":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.html")))
    return sorted(set(files))


def is_ignored_reference(ref: str) -> bool:
    if not ref or ref.startswith("#"):
        return True
    parsed = urlsplit(ref)
    return parsed.scheme.lower() in IGNORED_SCHEMES


def resolve_reference(source_file: Path, ref: str) -> Path | None:
    if is_ignored_reference(ref):
        return None
    parsed = urlsplit(ref)
    if parsed.netloc:
        return None
    path_part = unquote(parsed.path)
    if not path_part:
        return None
    return (source_file.parent / path_part).resolve()


def audit(root: Path, training_only: bool) -> tuple[list[str], list[str], list[Path]]:
    root = root.resolve()
    html_files = iter_html_files(root, training_only)
    broken: list[str] = []
    suspicious: list[str] = []

    for html_file in html_files:
        try:
            text = html_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            broken.append(f"{html_file.relative_to(root)}: cannot read as UTF-8")
            continue

        parser = LinkParser()
        parser.feed(text)

        has_portal_link = False
        for attr, ref, line in parser.refs:
            target = resolve_reference(html_file, ref)
            if target is None:
                continue
            try:
                target.relative_to(root)
            except ValueError:
                broken.append(
                    f"{html_file.relative_to(root)}:{line}: {attr}=\"{ref}\" points outside repository"
                )
                continue
            if target.name == "index.html" and target.parent == root:
                has_portal_link = True
            if not target.exists():
                broken.append(
                    f"{html_file.relative_to(root)}:{line}: missing target for {attr}=\"{ref}\" -> {target.relative_to(root)}"
                )

        # User-facing module and case-study pages should offer a path back to
        # the root portal. This is suspicious rather than broken because pages
        # can still function without it.
        if html_file.parent.name in MODULE_FOLDERS and not has_portal_link:
            suspicious.append(
                f"{html_file.relative_to(root)}: no explicit href back to ../index.html found"
            )

    return broken, suspicious, html_files


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit repository-local HTML href/src references.")
    parser.add_argument("--root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument(
        "--training-only",
        action="store_true",
        help="Scan only index.html and the three main training folders.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    broken, suspicious, checked = audit(root, args.training_only)

    print("Pistos Training Link Audit")
    print(f"Files checked: {len(checked)}")
    print(f"Broken links: {len(broken)}")
    print(f"Suspicious findings: {len(suspicious)}")

    if broken:
        print("\nBroken links:")
        for item in broken:
            print(f"- {item}")

    if suspicious:
        print("\nSuspicious findings:")
        for item in suspicious:
            print(f"- {item}")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
