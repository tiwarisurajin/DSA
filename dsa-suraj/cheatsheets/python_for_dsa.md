# Python for DSA — Cheatsheet

The Python-specific syntax/stdlib you actually need for interview-style DSA, in one place, so you're not context-switching to documentation mid-problem.

## Built-in Data Structures

| Need | Use | Notes |
|---|---|---|
| Dynamic array | `list` | See [Arrays theory](../implementations/03_Arrays/theory.md) |
| Hash map | `dict` | O(1) average get/set/delete |
| Hash set | `set` | O(1) average membership; use for dedup + fast lookup |
| Stack | `list` (`.append`/`.pop`) | Both O(1); don't use `.pop(0)` — that's O(n) |
| Queue | `collections.deque` | `.append`/`.popleft` both O(1); a plain `list` is O(n) for `.pop(0)` |
| Priority queue / heap | `heapq` | Min-heap only — negate values for a max-heap |
| Ordered counts | `collections.Counter` | Subclass of dict, `.most_common(k)` is genuinely useful |
| Default-valued dict | `collections.defaultdict` | Avoids `if key not in dict: dict[key] = []` boilerplate |

## `heapq` quick reference

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
smallest = heapq.heappop(heap)          # 1 — heapq is min-heap only

# Max-heap trick: negate on the way in and out
max_heap = []
heapq.heappush(max_heap, -5)
largest = -heapq.heappop(max_heap)      # 5

# Turn an existing list into a heap in O(n) (not O(n log n))
nums = [5, 1, 8, 2]
heapq.heapify(nums)

# k largest / smallest without a full sort
heapq.nlargest(2, nums)                  # O(n log k)
heapq.nsmallest(2, nums)
```

## `collections.deque` quick reference

```python
from collections import deque

q = deque()
q.append(1)        # add to right, O(1)
q.appendleft(0)     # add to left, O(1)
q.popleft()          # remove from left, O(1) — this is what makes it a proper queue
q.pop()               # remove from right, O(1)
```

## Sorting with custom keys

```python
# Sort by a computed key, not the raw value
intervals.sort(key=lambda pair: pair[0])

# Sort descending
nums.sort(reverse=True)

# Multi-key sort: by length first, then alphabetically
words.sort(key=lambda w: (len(w), w))
```

## Common gotchas specific to Python

- **Mutable default arguments.** `def f(arr=[]):` reuses the SAME list across calls — always use `def f(arr=None): arr = arr if arr is not None else []`.
- **Shallow copy vs deep copy.** `new = old` doesn't copy — both names point to the same list. `new = old[:]` or `new = old.copy()` gives a shallow copy (fine for lists of immutables; not enough for nested lists — use `copy.deepcopy` there).
- **Integer overflow doesn't exist in Python** — but if you're translating a solution to a language that does have fixed-width integers (relevant if an interviewer asks "how would this differ in Java/C++"), say so.
- **`is` vs `==`** — `is` checks identity, `==` checks value equality. Almost always want `==` for DSA problems; `is` is only correct for `None` checks (`if x is None`).
- **String immutability** means `s += char` in a loop is O(n) per operation, O(n²) total — build a list and `"".join()` instead (see [Handbook Ch. 2 §2.4](../Engineering_Handbook.md#24-mutable-vs-immutable-and-why-its-a-memory-question-not-a-syntax-question)).

## `itertools` worth knowing

```python
from itertools import permutations, combinations

list(permutations([1, 2, 3]))       # all orderings, useful for backtracking sanity checks
list(combinations([1, 2, 3], 2))     # all size-2 subsets
```
Rarely the actual solution (usually too slow for real constraints), but useful for brute-force baselines and for generating test cases by hand.
