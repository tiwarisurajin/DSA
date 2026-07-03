# Arrays — Cheatsheet

## Operation Complexities

| Operation | Complexity |
|---|---|
| `arr[i]` read/write | O(1) |
| `arr.append(x)` | O(1) amortized |
| `arr.pop()` | O(1) |
| `arr.pop(0)` / `arr.insert(0, x)` | O(n) |
| `x in arr` | O(n) |
| `arr.sort()` | O(n log n) |
| `sorted(arr)` | O(n log n), returns new list |
| `arr.reverse()` | O(n) |
| `len(arr)` | O(1) |
| `arr[i:j]` slice | O(j - i) — creates a new list |

Full reasoning in [`theory.md`](./theory.md).

## The Core Trade

```
O(n) inner scan (`in`, `.index()`) inside an O(n) outer loop = O(n²)
      ↓  pay O(n) space for a set/dict
O(1) average inner lookup inside an O(n) outer loop = O(n)
```
See [Two Sum](./problems/001_two_sum.md).

## Quick Recipes

**Prefix sum** (repeated range-sum queries):
```python
prefix = [0] * (len(arr) + 1)
for i, x in enumerate(arr):
    prefix[i + 1] = prefix[i] + x
# sum(arr[i:j]) == prefix[j] - prefix[i]
```

**Running best (Kadane-style)**:
```python
best_here = best_overall = arr[0]
for x in arr[1:]:
    best_here = max(x, best_here + x)
    best_overall = max(best_overall, best_here)
```

**Sort + sweep for intervals**:
```python
intervals.sort(key=lambda p: p[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

**Two-sum-style complement check**:
```python
seen = {}
for i, x in enumerate(arr):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

## Decision Cheatsheet

| Symptom in the problem | Reach for |
|---|---|
| "does X exist / what pairs with X" | Hash set/map |
| Repeated range-sum queries | Prefix sum |
| "contiguous subarray with max/min ___" | Kadane-style running best, or sliding window if there's a size/count constraint |
| Overlapping ranges/intervals | Sort, then single sweep |
| Need product/max/min excluding self at each index | Prefix + suffix precomputation |
