# Roadmap

The 17-topic order in `implementations/` isn't arbitrary — each topic is chosen so it either introduces exactly one new idea, or gives you the prerequisite for the next few topics.

## The order, and why

| Order | Topic | Why here, not elsewhere |
|---|---|---|
| 01 | Basics of Programming | Baseline: I/O, control flow, functions. Skip if already solid — it's here so the repo doesn't assume anything. |
| 02 | Sorting | Almost every later topic (binary search, greedy, intervals) leans on "assume the input is sorted." Learn the sorts and their complexities before you need them as tools. |
| 03 | Arrays | The universal base structure. Two Sum, prefix sums, and the brute-force→hashmap trade-off pattern show up everywhere downstream. **Done first, fully, as the quality template for the rest of the repo.** |
| 04 | Binary Search | Needs sorting (02) to make sense. It's not just "search a sorted array" — it's a pattern for any monotonic search space, which shows up again in later optimization problems. |
| 05 | Strings | Mostly array techniques applied to a specialized array-like structure, plus a few string-only tricks (KMP, palindromes). Comes right after Arrays while those patterns are fresh. |
| 06 | Linked List | First topic with no random access — forces you to think in pointers instead of indices. Deliberately placed after Arrays so the contrast is obvious. |
| 07 | Bit Manipulation | Self-contained, mostly independent — placed here as a change of pace before recursion gets heavy. |
| 08 | Recursion & Backtracking | The single biggest unlock for everything after this point. Trees, graphs, and DP all lean on recursive thinking. |
| 09 | Stack & Queue | Needs recursion (08) conceptually — a stack is literally what your call stack is doing implicitly; this topic makes it explicit and gives you the tool for iterative DFS, monotonic stack problems, and BFS's underlying queue. |
| 10 | Sliding Window & Two Pointers | Needs arrays (03) + the pointer thinking from Linked Lists (06). One of the highest interview-frequency patterns — deliberately mid-roadmap so it's fresh going into the harder topics. |
| 11 | Greedy | Needs sorting (02) and the "is there always a locally-best choice" reasoning that's easiest to teach once you've seen enough brute-force alternatives to compare against. |
| 12 | Binary Trees | Needs recursion (08) as a hard prerequisite. Trees ARE recursive structures — you cannot shortcut this. |
| 13 | Binary Search Trees | A specialization of 12 — needs Binary Trees' traversal patterns plus Binary Search's (04) invariant-based thinking. |
| 14 | Heaps | Needs trees (12) conceptually (it's a tree underneath) and shows up constantly paired with greedy (11) problems. |
| 15 | Graphs | Generalizes trees (12) — a tree is just a graph with no cycles. Needs stack/queue (09) for DFS/BFS implementations. |
| 16 | Dynamic Programming | The hardest topic, deliberately last among the "core" topics. Needs recursion (08) as a hard prerequisite — DP is recursion + memoization, full stop. |
| 17 | Tries | A specialized tree (12) for string (05) problems. Placed last because it's narrower-scope than the others — high value for specific problem types, lower frequency overall. |

## Suggested pacing

This is a guideline, not a rule — adjust to your actual schedule.

| Weeks | Focus |
|---|---|
| 1 | Basics, Sorting, Arrays (start problems) |
| 2 | Finish Arrays, Binary Search, Strings |
| 3 | Linked List, Bit Manipulation |
| 4 | Recursion & Backtracking (go slow here — it's the unlock) |
| 5 | Stack & Queue, Sliding Window & Two Pointers |
| 6 | Greedy, Binary Trees |
| 7 | Binary Search Trees, Heaps |
| 8 | Graphs |
| 9–10 | Dynamic Programming (budget two weeks — it's genuinely harder) |
| 11 | Tries, revision pass on weak topics |
| 12 | Mock interviews, company-specific prep (see `interview/`) |

## After the 17 core topics

Once the core roadmap is done, the Engineering Handbook's later chapters (Union-Find, Segment Trees, Fenwick Trees) are optional depth for competitive-programming-adjacent interview rounds — most product companies won't require them, but they show up at trading firms, some FAANG "hard" rounds, and CP-flavored interviews.
