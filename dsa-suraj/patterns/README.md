# Pattern Library

~15 patterns cover the large majority of interview problems. The goal of this folder is to teach **recognition** — given a new, unseen problem, which pattern does it smell like — not just to catalog solutions.

Every pattern doc follows [`templates/pattern_template.md`](../templates/pattern_template.md): recognition clues, decision tree, mental model, template code, complexity, common mistakes, practice problems, variations.

| Pattern | Status | Recognize it by |
|---|:---:|---|
| [Sliding Window](./sliding_window.md) | ✅ Complete | "contiguous subarray/substring" + a size or condition constraint |
| Two Pointers | ⬜ Queued | Sorted array, or comparing from both ends |
| Binary Search (on answer) | ⬜ Queued | "minimize the maximum" / "maximize the minimum" phrasing |
| DFS | ⬜ Queued | Explore-all-paths, tree/graph traversal, backtracking-adjacent |
| BFS | ⬜ Queued | Shortest path in unweighted graph, level-order |
| Backtracking | ⬜ Queued | "all combinations/permutations/subsets satisfying X" |
| Greedy | ⬜ Queued | "prove a local choice is always safe" |
| Dynamic Programming | ⬜ Queued | Overlapping subproblems + optimal substructure; "count ways" / "min/max cost" |
| Trie | ⬜ Queued | Prefix matching across many strings |
| Heap / Priority Queue | ⬜ Queued | "top K", "kth largest", merge K sorted |
| Union-Find | ⬜ Queued | Dynamic connectivity, "are these in the same group" |
| Prefix Sum | ⬜ Queued | Repeated range-sum queries |
| Topological Sort | ⬜ Queued | Ordering with dependencies (DAG) |
| Monotonic Stack | ⬜ Queued | "next greater/smaller element" |
| Monotonic Queue | ⬜ Queued | Sliding window max/min |

Sliding Window ships first because it composes directly with the Arrays topic that's already complete — see [`implementations/03_Arrays/`](../implementations/03_Arrays/).
