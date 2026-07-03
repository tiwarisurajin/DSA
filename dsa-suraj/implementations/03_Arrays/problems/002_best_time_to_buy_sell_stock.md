# 002. Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Pattern:** Single Pass (track running minimum)
**Source:** LeetCode #121

## Problem Statement
Given an array `prices` where `prices[i]` is the stock price on day `i`, find the maximum profit from buying on one day and selling on a later day. Return `0` if no profit is possible.

## Constraints
- `1 <= len(prices) <= 10^5`
- You must buy before you sell (buy day index < sell day index).
- Only one transaction allowed.

## Observations
For any given sell day `j`, the best possible buy day is whichever earlier day had the **lowest price**. So instead of checking every buy/sell pair, we only need to track the lowest price seen *so far* as we scan forward.

## Pattern
Single-pass with running state. Not sliding window (there's no contiguous "window" being resized) — it's simpler: one pointer, one piece of running state (the minimum seen so far).

## Brute Force
```python
def max_profit_brute(prices: list[int]) -> int:
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best
```
Complexity: O(n²) — every buy/sell pair checked explicitly.

## Optimized
```python
def max_profit(prices: list[int]) -> int:
    min_price_so_far = float("inf")
    best_profit = 0

    for price in prices:
        min_price_so_far = min(min_price_so_far, price)
        best_profit = max(best_profit, price - min_price_so_far)

    return best_profit
```
Complexity: O(n) time, O(1) space. Trade being made: none needed here — this isn't a time-for-space trade, it's recognizing that the brute force is doing **redundant work**: it recomputes "best buy day so far" from scratch for every sell day, when that value can be tracked incrementally in one pass.

## Dry Run
`prices = [7, 1, 5, 3, 6, 4]`

| price | min_price_so_far (before) | min_price_so_far (after) | price - min_price_so_far | best_profit |
|---|---|---|---|---|
| 7 | ∞ | 7 | 0 | 0 |
| 1 | 7 | 1 | 0 | 0 |
| 5 | 1 | 1 | 4 | 4 |
| 3 | 1 | 1 | 2 | 4 |
| 6 | 1 | 1 | 5 | **5** |
| 4 | 1 | 1 | 3 | 5 |

Result: `5` (buy at 1, sell at 6).

## Complexity
Time: O(n) — single pass.
Space: O(1) — two scalar variables.

## Alternative Solutions
- This is technically the simplest case of Kadane's algorithm (see [004](./004_maximum_subarray.md)) applied to the array of day-over-day price *differences* rather than prices directly — `max_profit(prices)` equals the maximum subarray sum of `[prices[i+1] - prices[i] for i in range(len(prices)-1)]`. Same O(n) result, more moving parts — the direct running-minimum approach above is preferred for clarity.

## Edge Cases
- Strictly decreasing prices, e.g. `[7, 6, 4, 3, 1]` → no profitable transaction exists, correctly returns `0` (never updates `best_profit` above its initial value).
- Single price, `[5]` → no valid sell day, returns `0` (loop body runs once, `best_profit` stays 0).
- Empty list — not valid per constraints (`len >= 1`), but the implementation degrades gracefully (returns `0`) if called anyway.

## Mistakes
- **Trying to adapt the brute force with a single loop that tracks max, not min.** A common wrong instinct is tracking the running *maximum* price and computing `max_price - price`, which finds the best day to have *sold*, not bought — this gets the direction backwards and produces wrong (or negative-then-clamped) answers.
- **Forgetting that buy must come before sell.** The running-minimum approach handles this implicitly because `min_price_so_far` only ever reflects prices *before* the current day — but if you rewrite this without care (e.g. computing global min and global max independently), you can accidentally "buy" after you "sell."

## Related Problems
- Best Time to Buy and Sell Stock II (LeetCode #122) — multiple transactions allowed, becomes a greedy "sum all positive day-over-day gains" problem.
- Maximum Subarray ([004](./004_maximum_subarray.md)) — structurally the same "track a running best" idea applied to a different transformation of the input.

## Revision Date
_(log dates revisited here)_
