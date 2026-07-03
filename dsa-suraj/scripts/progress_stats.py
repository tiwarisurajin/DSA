#!/usr/bin/env python3
"""
progress_stats.py

Scans implementations/ for problem writeups and reports completion stats:
- how many topics have a non-empty problems/ folder
- how many problem writeups exist total
- which topics are still fully queued

Usage:
    python scripts/progress_stats.py

No external dependencies — stdlib only, on purpose, so this runs anywhere
this repo is cloned without a setup step.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
IMPLEMENTATIONS_DIR = REPO_ROOT / "implementations"


def find_problem_files(topic_dir: Path) -> list[Path]:
    problems_dir = topic_dir / "problems"
    if not problems_dir.is_dir():
        return []
    return sorted(problems_dir.glob("*.md"))


def topic_is_complete(topic_dir: Path) -> bool:
    """A topic counts as complete if it has theory, cheatsheet, mistakes,
    revision docs AND at least one problem writeup."""
    required_files = ["theory.md", "cheatsheet.md", "mistakes.md", "revision.md"]
    has_required = all((topic_dir / f).is_file() for f in required_files)
    has_problems = len(find_problem_files(topic_dir)) > 0
    return has_required and has_problems


def main() -> int:
    if not IMPLEMENTATIONS_DIR.is_dir():
        print(f"Could not find implementations/ at {IMPLEMENTATIONS_DIR}", file=sys.stderr)
        return 1

    topics = sorted(p for p in IMPLEMENTATIONS_DIR.iterdir() if p.is_dir())

    total_problems = 0
    complete_topics = []
    queued_topics = []

    print(f"{'Topic':<40} {'Problems':>10} {'Status':>12}")
    print("-" * 64)

    for topic_dir in topics:
        problems = find_problem_files(topic_dir)
        total_problems += len(problems)
        complete = topic_is_complete(topic_dir)
        status = "COMPLETE" if complete else "queued"
        (complete_topics if complete else queued_topics).append(topic_dir.name)
        print(f"{topic_dir.name:<40} {len(problems):>10} {status:>12}")

    print("-" * 64)
    print(f"Topics complete: {len(complete_topics)}/{len(topics)}")
    print(f"Total problem writeups: {total_problems}")
    if queued_topics:
        print(f"\nNext up (in roadmap order): {queued_topics[0]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
