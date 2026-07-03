# DSA Engineering Knowledge Base

> A structured, from-first-principles path from "knows basic Python" to "can solve a Google/Meta/Amazon interview problem on a whiteboard and explain why."

This is not a notes dump. It's an engineering knowledge base — every topic is taught, visualized, implemented, and drilled the way a Staff Engineer would onboard a new grad.

---

## Table of Contents

- [Why This Exists](#why-this-exists)
- [Learning Philosophy](#learning-philosophy)
- [Progress Dashboard](#progress-dashboard)
- [Repository Structure](#repository-structure)
- [Roadmap](#roadmap)
- [How To Use This Repo](#how-to-use-this-repo)
- [Study Workflow](#study-workflow)
- [Git Workflow](#git-workflow)
- [Engineering Principles](#engineering-principles)
- [Quick Links](#quick-links)
- [Contributing](#contributing)
- [License](#license)

---

## Why This Exists

Most DSA resources are either a wall of LeetCode links with no theory, or a theory textbook with no wiring to real interview problems. This repo tries to close that gap: every topic connects **mental model → pattern → template → problem → dry run → complexity → mistakes**, so nothing is memorized without being understood.

## Learning Philosophy

1. **Understand before you memorize.** You should be able to derive a solution's shape from first principles, not recall it.
2. **Patterns over problems.** ~15 patterns cover ~90% of interview problems. Learn the pattern, not the problem.
3. **Dry run everything.** If you can't trace your own code by hand, you don't understand it yet.
4. **Complexity is not optional.** Every solution states its time/space complexity and *why*.
5. **Mistakes are curriculum.** Every topic has a `mistakes.md` — the errors are as valuable as the solutions.
6. **Revisit on a schedule.** Spaced repetition beats one-and-done grinding. See [`progress/`](./progress).

## Progress Dashboard

Status legend: ✅ Complete &nbsp;|&nbsp; 🟡 In Progress &nbsp;|&nbsp; ⬜ Queued

| # | Topic | Theory | Problems | Cheatsheet | Status |
|---|-------|:---:|:---:|:---:|:---:|
| 01 | Basics of Programming | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 02 | Sorting | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 03 | Arrays | ✅ | ✅ | ✅ | ✅ **Complete** |
| 04 | Binary Search | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 05 | Strings | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 06 | Linked List | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 07 | Bit Manipulation | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 08 | Recursion & Backtracking | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 09 | Stack & Queue | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 10 | Sliding Window & Two Pointers | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 11 | Greedy | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 12 | Binary Trees | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 13 | Binary Search Trees | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 14 | Heaps | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 15 | Graphs | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 16 | Dynamic Programming | ⬜ | ⬜ | ⬜ | ⬜ Queued |
| 17 | Tries | ⬜ | ⬜ | ⬜ | ⬜ Queued |

**Patterns:** Sliding Window ✅ &nbsp;·&nbsp; 14 more queued (see [`patterns/README.md`](./patterns/README.md))

> This table is the source of truth for what's real in this repo right now. Nothing marked ✅ is a stub — open it and check.

## Repository Structure

```
.
├── README.md                   ← you are here
├── Engineering_Handbook.md     ← the "book" — deep theory, chapter by chapter
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── docs/                       ← standalone deep-dive docs (e.g. Time Complexity)
├── roadmaps/                   ← study order, timelines
├── patterns/                   ← pattern recognition system (the real leverage)
├── algorithms/                 ← classic algorithms (sorting, searching, graph algos)
├── implementations/            ← the 17-topic curriculum, one folder each
│   └── 03_Arrays/
│       ├── README.md
│       ├── theory.md
│       ├── cheatsheet.md
│       ├── mistakes.md
│       ├── revision.md
│       ├── problems/           ← full problem template per problem
│       └── templates/          ← reusable code templates for this topic
├── templates/                  ← global reusable templates (problem, pattern)
├── cheatsheets/                ← quick-reference sheets
├── examples/                   ← tiny visual/educational examples
├── interview/                  ← behavioral, technical, company-specific prep
├── notes/                      ← freeform working notes
├── progress/                   ← daily/weekly/monthly logs, revision calendar
├── resources/                  ← curated books, courses, papers
├── scripts/                    ← automation (progress stats, scaffolding)
├── assets/                     ← images/diagrams
└── .github/                    ← issue templates, PR template, CI
```

## Roadmap

See [`roadmaps/roadmap.md`](./roadmaps/roadmap.md) for the full ordered path with reasoning for the sequencing (why Arrays before Trees, why Sliding Window before DP, etc).

## How To Use This Repo

1. Read the relevant chapter in [`Engineering_Handbook.md`](./Engineering_Handbook.md) for the *why*.
2. Read `implementations/XX_Topic/theory.md` for the *what*.
3. Read the matching pattern in `patterns/` for the *how to recognize it*.
4. Solve problems in `implementations/XX_Topic/problems/` — brute force first, then optimize.
5. Log it in `progress/daily_log.md`.
6. Revisit failed/slow problems per `progress/revision_calendar.md`.

## Study Workflow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  Read Theory │ ──▶ │ Learn Pattern│ ──▶ │ Solve Brute │ ──▶ │   Optimize   │
└─────────────┘     └──────────────┘     └─────────────┘     └──────┬───────┘
                                                                     │
┌─────────────┐     ┌──────────────┐     ┌─────────────┐            │
│   Schedule   │ ◀── │  Log Mistake │ ◀── │  Dry Run +  │ ◀──────────┘
│   Revision   │     │  (if any)    │     │  Complexity │
└─────────────┘     └──────────────┘     └─────────────┘
```

## Git Workflow

- One commit per problem solved: `feat(arrays): solve two-sum with hashmap approach`
- One commit per topic completed: `docs(arrays): complete theory + cheatsheet`
- Daily log commits: `chore(progress): daily log 2026-07-03`
- Never commit broken/untested code to `main`.

## Engineering Principles

- **Correctness first, then complexity, then style.** In that order.
- **Name things for what they mean, not what they are.** `left`/`right` beats `i`/`j` when they're pointers with meaning.
- **Every optimization must be justified.** "It's faster" is not a justification — "we go from O(n²) to O(n) by trading O(n) space for a hashmap" is.
- **If you can't explain it out loud in under 60 seconds, you don't understand it yet.**

## Quick Links

- [Engineering Handbook](./Engineering_Handbook.md)
- [Time Complexity Deep Dive](./docs/05_Time_Complexity.md)
- [Pattern Library](./patterns/README.md)
- [Arrays (first complete topic)](./implementations/03_Arrays/README.md)
- [Roadmap](./roadmaps/roadmap.md)
- [Progress Tracker](./progress/daily_log.md)
- [Interview Prep](./interview/README.md)

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). This is currently a solo learning repo, but structured so it could take contributions later.

## License

[MIT](./LICENSE)

---

<sub>Built in public by Suraj — self-taught, Mumbai. Follow the build on Twitter/X. This repo doubles as the DSA knowledge base for a future learning-platform product.</sub>
