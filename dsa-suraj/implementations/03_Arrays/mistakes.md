# Arrays — Mistakes Log

The specific, recurring ways this topic goes wrong. Each entry: what the mistake looks like, why it happens, how to catch it.

## 1. The "loop hides a scan" O(n²) trap

**Looks like:** One visible `for` loop, so it "feels" O(n).
```python
for x in arr:
    if x in some_list:   # <-- this is itself O(n)
        ...
```
**Why it happens:** People count loop nesting visually instead of the cost of what's inside each iteration.
**Catch it by:** For every operation inside a loop, ask "what's the complexity of THIS line by itself?" `in` on a list, `.index()`, and slicing (`arr[i:j]`) are the most common offenders — they're all O(n) even though they don't look like loops.
**Fix:** Swap the list for a set/dict when membership checking is the bottleneck.

## 2. Off-by-one on window/subarray length

**Looks like:** `right - left` instead of `right - left + 1` for a window length, or `<=` vs `<` on interval boundaries.
**Why it happens:** Fencepost errors are just genuinely easy to make under interview pressure.
**Catch it by:** Always dry-run on the smallest possible valid case (a window/subarray of length 1) and check the formula gives `1`, not `0`.

## 3. Wrong initial value for a "running best"

**Looks like:** Seeding `best = 0` when the array can be all-negative (breaks Kadane's — see [004](./problems/004_maximum_subarray.md#mistakes)), or seeding `min_so_far = 0` instead of `float('inf')` (breaks running-minimum tracking — see [002](./problems/002_best_time_to_buy_sell_stock.md#mistakes)).
**Why it happens:** `0` feels like a safe "neutral" default, but it's only neutral for sums of non-negative numbers.
**Catch it by:** Ask "what's the correct answer for the smallest possible input (one element)?" and seed with that, not with a guessed neutral value.

## 4. Forgetting the space cost of a "clever" one-liner

**Looks like:** `arr[i+1:]` inside a loop condition, or `sorted(arr)` called repeatedly instead of once.
**Why it happens:** Slicing and `sorted()` look cheap syntactically but both allocate new lists — O(n) time AND O(n) space, every time they're called.
**Catch it by:** Treat any slice or `sorted()` call inside a loop as a red flag worth double-checking.

## 5. Confusing "sort helps" with "sort is free"

**Looks like:** Reaching for `.sort()` as a first move without accounting for the O(n log n) cost it adds, then being surprised the overall solution isn't O(n).
**Why it happens:** Sorting genuinely does simplify a lot of array problems (see [Merge Intervals](./problems/005_merge_intervals.md)), so it becomes a reflex — but it's not free, and if a problem specifically calls for O(n), sorting rules that out.
**Catch it by:** State the sort's cost explicitly when you propose sorting as part of a solution — "this gets us to O(n log n) because of the sort" — rather than skipping straight to "so this is O(n)."

## How to use this log

Add to it. Every time an array problem trips you up in a way not already listed here, write it down with the same structure: looks like / why it happens / catch it by. The value of this file goes up over time, not down.
