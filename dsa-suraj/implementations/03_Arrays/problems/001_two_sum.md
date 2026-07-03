# 001. Two Sum

**Difficulty:** Easy
**Pattern:** [Hashing (time-for-space trade)](../theory.md#5-the-core-trade-off-pattern-time-for-space)
**Source:** LeetCode #1

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Assume exactly one solution exists, and you may not use the same element twice.

## Constraints
- `2 <= len(nums) <= 10^4`
- Answer indices, not values — order of the two returned indices doesn't matter.
- Exactly one valid pair exists.

## Observations
For each element `x`, the number we need to complete the pair is `target - x`. The brute-force approach checks every other element for that complement. The question is: can we know whether `target - x` exists **without scanning**?

## Pattern
This is a hashing problem: we want O(1) average lookups instead of O(n) linear scans, at the cost of O(n) space. Recognize it by: "does a specific value exist / what's paired with this value" phrasing.

## Brute Force
```python
def two_sum_brute(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
Complexity: O(n²) time — nested loop checks every pair. O(1) extra space. Not good enough once `n` approaches 10^4 (10^8 operations).

## Optimized
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []
```
Complexity: O(n) time, O(n) space. The trade being made: we pay O(n) space for a hash map so that "does the complement exist" becomes an O(1) average lookup instead of an O(n) scan — collapsing O(n²) to O(n) overall (see [theory.md §5](../theory.md#5-the-core-trade-off-pattern-time-for-space)).

## Dry Run
`nums = [2, 7, 11, 15]`, `target = 9`

| i | x | complement | seen before this step | complement in seen? | action |
|---|---|---|---|---|---|
| 0 | 2 | 7 | `{}` | No | add `seen[2] = 0` |
| 1 | 7 | 2 | `{2: 0}` | Yes | return `[0, 1]` |

## Complexity
Time: O(n) — single pass, each hash map operation is O(1) average.
Space: O(n) — the `seen` dictionary can hold up to `n` entries.

## Alternative Solutions
- **Sort + two pointers:** sort the array (O(n log n)), then use two pointers from opposite ends. Works, but you'd need to sort `(value, original_index)` pairs to preserve indices, and it's O(n log n) overall — strictly worse than the O(n) hash map approach for this exact problem. Only preferable if you already need the array sorted for other reasons.

## Edge Cases
- No valid pair — the problem guarantees one exists, but defensive code should handle "not found" (the implementation above returns `[]`).
- Duplicate values, e.g. `nums = [3, 3]`, `target = 6` — handled correctly because we check `complement in seen` *before* adding the current element, so an element can't pair with itself.
- Negative numbers — no special handling needed; the hash map approach works identically.

## Mistakes
- **Adding to `seen` before checking for the complement.** This would let an element pair with itself (e.g. `nums=[3], target=6` would incorrectly "succeed" if `3` were added first, then immediately looked up). Always check first, then add.
- **Using `nums.index(complement)` inside the loop instead of a hash map.** This looks like an O(n) solution (one visible loop) but `.index()` is itself O(n), making it O(n²) again — the exact "loop hides a scan" mistake from Handbook Chapter 3 §3.5.

## Related Problems
- 3Sum (LeetCode #15) — same complement idea, one dimension higher, usually needs sorting + two pointers instead of a hash map to avoid duplicate triplets cleanly.
- Two Sum II — Input Array Is Sorted (LeetCode #167) — same problem, but sorted input makes two pointers the better fit than hashing.

## Revision Date
_(log dates revisited here as you use this repo, e.g. "2026-07-10 — solved in 4 min, clean")_
