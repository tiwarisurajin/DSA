# 004. Maximum Subarray (Kadane's Algorithm)

**Difficulty:** Medium
**Pattern:** 1D Dynamic Programming (Kadane's) — the array topic's first taste of DP before Topic 16 covers it properly
**Source:** LeetCode #53

## Problem Statement
Given an integer array `nums`, find the contiguous subarray with the largest sum, and return that sum.

## Constraints
- `1 <= len(nums) <= 10^5`
- Array can contain negative numbers.
- At least one element exists, so a valid (possibly single-element) subarray always exists.

## Observations
For any position `i`, the best subarray *ending exactly at `i`* is either: (a) just `nums[i]` alone, or (b) `nums[i]` appended to the best subarray ending at `i-1`. Whichever is bigger. This is a genuine dynamic programming recurrence — "best ending here" depends only on "best ending at the previous position" — even though it's simple enough to compute without an explicit DP array.

## Pattern
This is 1D DP in disguise, specifically the recurrence: `best_ending_here = max(nums[i], best_ending_here_prev + nums[i])`. It's included here in Arrays (not Topic 16, Dynamic Programming) because it's the single most common "first DP problem" people meet, and it fits naturally as an array technique before the DP topic formalizes the general recurrence-based approach.

## Brute Force
```python
def max_subarray_brute(nums: list[int]) -> int:
    n = len(nums)
    best = nums[0]
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            best = max(best, current_sum)
    return best
```
Complexity: O(n²) — every subarray's sum computed explicitly.

## Optimized
```python
def max_subarray(nums: list[int]) -> int:
    best_ending_here = nums[0]
    best_overall = nums[0]

    for x in nums[1:]:
        best_ending_here = max(x, best_ending_here + x)
        best_overall = max(best_overall, best_ending_here)

    return best_overall
```
Complexity: O(n) time, O(1) space. Trade being made: none — this is pure redundant-work elimination, same spirit as [002](./002_best_time_to_buy_sell_stock.md): track a running "best ending here" value instead of recomputing every subarray sum from scratch.

## Dry Run
`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| x | best_ending_here | best_overall |
|---|---|---|
| -2 (init) | -2 | -2 |
| 1 | max(1, -2+1=-1) = 1 | 1 |
| -3 | max(-3, 1-3=-2) = -2 | 1 |
| 4 | max(4, -2+4=2) = 4 | 4 |
| -1 | max(-1, 4-1=3) = 3 | 4 |
| 2 | max(2, 3+2=5) = 5 | **5** |
| 1 | max(1, 5+1=6) = 6 | **6** |
| -5 | max(-5, 6-5=1) = 1 | 6 |
| 4 | max(4, 1+4=5) = 5 | 6 |

Result: `6` (subarray `[4, -1, 2, 1]`).

## Complexity
Time: O(n) — single pass.
Space: O(1) — two scalar variables.

## Alternative Solutions
- **Divide and conquer:** split the array in half, recursively find the max subarray in the left half, right half, and the one crossing the midpoint, take the max of the three. O(n log n) — strictly worse than Kadane's O(n), but worth knowing because it's a common interviewer follow-up ("can you solve this differently?") and it generalizes to some 2D variants Kadane's doesn't handle as directly.

## Edge Cases
- All negative numbers, e.g. `[-3, -1, -2]` → correctly returns `-1` (the least-negative single element), because `best_ending_here` resets to just `x` whenever extending would be worse than starting fresh — it never forces you to include a positive number that doesn't exist.
- Single element, `[5]` → returns `5` directly.
- All positive numbers → equivalent to summing the whole array.

## Mistakes
- **Initializing `best_ending_here` and `best_overall` to `0` instead of `nums[0]`.** This silently breaks on all-negative arrays — with a `0` initial value, an all-negative input would incorrectly report `0` as the max subarray sum, even though `0` isn't actually a valid subarray sum from this input (every real subarray sum is negative). Always seed with the first element, not a "neutral" zero.
- **Confusing this with "maximum subarray *product*"** (a related but meaningfully different LeetCode problem, #152) which needs to track both a running max *and* min (because a negative times a negative can flip a bad running product into the new best) — the addition-based recurrence here does not extend directly to multiplication.

## Related Problems
- Maximum Product Subarray (LeetCode #152) — same shape, but needs tracking running min *and* max because of sign flips under multiplication.
- Maximum Subarray Sum Circular (LeetCode #918) — Kadane's applied twice (once normally, once to find the minimum subarray to exclude for the "wrap-around" case).
- Best Time to Buy and Sell Stock ([002](./002_best_time_to_buy_sell_stock.md)) — related "running best" shape, simpler recurrence.

## Revision Date
_(log dates revisited here)_
