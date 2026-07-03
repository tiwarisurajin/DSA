# Arrays — Theory

## 1. What an array actually is

An array is a block of memory addresses that are **contiguous** — element `i` lives at `base_address + i * element_size`. This single fact is the source of every complexity property below. There's no searching involved to find element `i`; it's arithmetic.

Python's `list` isn't technically a raw array — it's a dynamic array of *pointers* to objects (since Python values can be different types/sizes). But the indexing math is the same: `list[i]` computes an address directly. That's why `list[i]` is O(1) regardless of list length.

## 2. Why indexing is O(1) but searching is O(n)

- **Indexing (`arr[i]`)**: you already know `i`, so it's one arithmetic computation + one memory read. O(1).
- **Searching (`x in arr`, `arr.index(x)`)**: you don't know where `x` is, so in the general (unsorted) case you must check elements one at a time until found or exhausted. O(n).

This distinction is the single most common source of accidental O(n²) algorithms: using `in` or `.index()` on a list *inside* a loop, not realizing each call is itself O(n) (see [`mistakes.md`](./mistakes.md)).

## 3. Static vs dynamic arrays

- **Static array** (e.g. a C-style array, or a fixed-size array in typed languages): allocated once at a fixed size. Inserting past capacity requires manually allocating a new, larger block and copying everything over.
- **Dynamic array** (Python's `list`, Java's `ArrayList`, C++'s `vector`): handles that resizing for you automatically. When capacity is exceeded, it allocates a new block (typically 1.5–2x the old size) and copies existing elements over. This is why `append` is **amortized** O(1) rather than strictly O(1) — see Engineering Handbook Chapter 3, section 3.3 for the full derivation.

## 4. Core operation complexities

| Operation | Complexity | Why |
|---|---|---|
| `arr[i]` (read/write by index) | O(1) | direct address computation |
| `arr.append(x)` | O(1) amortized | occasional O(n) resize, spread over many O(1) appends |
| `arr.pop()` (remove last) | O(1) | no shifting needed |
| `arr.pop(0)` (remove first) | O(n) | every remaining element must shift left one position |
| `arr.insert(i, x)` | O(n) | every element after index `i` must shift right |
| `x in arr` | O(n) | linear scan, no shortcuts without sorting |
| `arr.sort()` | O(n log n) | Python uses Timsort |
| `len(arr)` | O(1) | length is tracked, not recomputed |

## 5. The core trade-off pattern: time for space

The single highest-leverage idea in this entire topic: **an O(n) inner scan (`x in arr`) can almost always be collapsed to O(1) average by paying O(n) space for a hash set or hash map.** This shows up in nearly every array problem that starts brute-force at O(n²):

```
Brute force:  for each element, scan the rest of the array  → O(n²) time, O(1) space
Optimized:    for each element, check/build a hash set       → O(n)  time, O(n) space
```

You'll see this exact move in [Two Sum](./problems/001_two_sum.md), and it's worth being able to state out loud in an interview: *"I'm trading O(n) extra space for a hash map to bring the lookup from O(n) down to O(1) average, which drops the overall complexity from O(n²) to O(n)."* That sentence, said unprompted, is a strong signal to an interviewer.

## 6. Prefix sums — precompute once, query many times

If you need the sum of any subarray `arr[i:j]` repeatedly, don't recompute it each time (O(n) per query). Precompute a prefix sum array once (O(n)), then any range sum is O(1):

```python
prefix = [0] * (len(arr) + 1)
for i, x in enumerate(arr):
    prefix[i + 1] = prefix[i] + x

# sum of arr[i:j] (exclusive of j) is now:
range_sum = prefix[j] - prefix[i]
```

This same "precompute once, O(1) query" idea generalizes beyond sums — [Product of Array Except Self](./problems/003_product_of_array_except_self.md) does the identical trick with running products instead of sums.

## 7. Two pointers on arrays

When an array is sorted (or can be treated as such), two pointers moving toward each other from opposite ends let you eliminate a nested loop. This is a large enough idea to get its own pattern doc once the pattern library expands past Sliding Window — for now, [Merge Intervals](./problems/005_merge_intervals.md) shows a related "sort first, then single sweep" technique.

## Revision Checklist

- [ ] Can explain why array indexing is O(1) but search is O(n) from the memory model, not just from memorization
- [ ] Can derive why `append` is amortized O(1)
- [ ] Can spot the time-for-space hash trade unprompted when reading brute-force O(n²) code
- [ ] Can build and use a prefix sum array from scratch
