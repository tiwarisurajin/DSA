# Contributing

This started as a solo learning repo, but it's structured to accept contributions cleanly.

## Ground Rules

- **No placeholder content.** If a section isn't ready, don't add it — leave it off the Progress Dashboard instead of filling it with "coming soon."
- **Every problem follows the template.** See [`templates/problem_template.md`](./templates/problem_template.md). Missing sections (complexity, dry run, edge cases) will be asked for in review.
- **Every pattern follows the pattern template.** See [`templates/pattern_template.md`](./templates/pattern_template.md).
- **Code must run.** Include the Python version tested against if it matters. No untested snippets.
- **Cite sources for claims**, especially complexity claims that aren't obvious (e.g. amortized costs).

## Adding a New Problem

1. Copy `templates/problem_template.md` into `implementations/XX_Topic/problems/`.
2. Name it `NNN_kebab_case_problem_name.md` (zero-padded 3-digit number, incrementing).
3. Fill every section. Brute force AND optimized, even if brute force is "trivial."
4. Update the topic's `README.md` problem table.
5. Log it in `progress/daily_log.md`.

## Adding a New Topic

1. Create `implementations/NN_Topic_Name/` with `README.md`, `theory.md`, `cheatsheet.md`, `mistakes.md`, `revision.md`, `problems/`, `templates/`.
2. Update the root `README.md` Progress Dashboard.
3. Update `roadmaps/roadmap.md` if the sequencing changes.

## Commit Style

```
feat(topic): solve problem-name with approach
docs(topic): add theory section on X
fix(topic): correct complexity claim in cheatsheet
chore(progress): daily log YYYY-MM-DD
```

## Pull Requests

- One topic or one problem per PR — keep diffs reviewable.
- PR description should state what's ✅ complete vs still 🟡 in progress in that PR.
