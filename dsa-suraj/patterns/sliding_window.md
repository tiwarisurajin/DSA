# Pattern: Sliding Window

## Recognition Clues

You're likely looking at a sliding window problem if the statement has:

- **"Contiguous subarray/substring"** — the word "contiguous" is the biggest tell. Non-contiguous → this is not sliding window (probably DP or backtracking instead).
- A **size constraint**: "subarray of size k", "window of length k" → fixed-size window.
- A **condition constraint** instead of a fixed size: "smallest subarray with sum ≥ target", "longest substring without repeating characters" → variable-size window.
- You're asked for a **min/max/count** over all contiguous windows, and brute force would be checking every window from scratch — an O(n²) or O(n³) approach that sliding window collapses to O(n).

## Decision Tree

```
Is the subarray/substring required to be CONTIGUOUS?
├── No  → not sliding window (consider subsequence DP / backtracking)
└── Yes → Is the window SIZE fixed (given k)?
          ├── Yes → Fixed-size sliding window
          └── No  → Is there a monotonic condition
                     (sum, count of distinct chars, etc.) that only
                     gets "worse" as the window grows?
                     ├── Yes → Variable-size sliding window (expand/shrink)
                     └── No  → sliding window won't work cleanly;
                               reconsider the problem
```

## Mental Model

Think of a **caterpillar inching along the array**: a `right` pointer always moves forward to grow the window, and a `left` pointer moves forward to shrink it — but neither pointer ever moves *backward*. That "never backward" property is exactly what makes the pattern O(n) instead of O(n²): you do at most `2n` total pointer moves across the entire run, not `n` moves per window.

The brute-force alternative recomputes something (a sum, a character count) from scratch for every window start. Sliding window's entire value is **incrementally updating** that state as the window edges move, instead of recomputing it.

## Template

**Fixed-size window:**
```python
def fixed_window(nums: list[int], k: int) -> int:
    """Example: max sum of any contiguous window of size k."""
    if len(nums) < k:
        raise ValueError("array shorter than window size")

    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]        # grow: add the new right element
        window_sum -= nums[right - k]    # shrink: drop the element leaving the window
        best = max(best, window_sum)

    return best
```

**Variable-size window:**
```python
def variable_window(nums: list[int], target: int) -> int:
    """Example: length of the smallest contiguous subarray with sum >= target."""
    left = 0
    window_sum = 0
    best_len = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]                 # always grow first

        while window_sum >= target:                # shrink while condition holds
            best_len = min(best_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return best_len if best_len != float("inf") else 0
```

## Complexity

- **Time: O(n).** `right` visits each index once. `left` also only ever moves forward, so across the *entire* run it visits each index at most once too — total pointer movement is bounded by `2n`, not `n` per window.
- **Space: O(1)** for numeric sums; **O(k) or O(alphabet size)** if the window tracks a frequency map (e.g. "longest substring with at most k distinct characters").

## Common Mistakes

1. **Resetting state instead of updating it incrementally.** If you find yourself calling `sum(window)` or rebuilding a frequency dict from scratch inside the loop, you've accidentally written brute force with extra steps — you're back to O(n²) or O(n·k).
2. **Using sliding window with negative numbers for a sum-based fixed condition.** The variable-size template above relies on the window sum being **monotonic** as you shrink (removing elements only decreases the sum). With negative numbers present, shrinking doesn't reliably move you toward or away from the target — the pattern breaks. Fixed-size sum windows are fine with negatives; variable-size condition windows generally aren't, unless the condition is on something else (like distinct character count, which is still monotonic).
3. **Off-by-one on the window size.** `right - left + 1` is the window length, not `right - left`. This is the single most common bug in interview attempts at this pattern.
4. **Forgetting to shrink in a `while`, not an `if`.** A single `if` only shrinks by one element per outer loop iteration, which is wrong when a single new `right` element requires shrinking by more than one from the left (common with distinct-character-count conditions).

## Variations

- **Fixed-size, single pass** (shown above) — e.g. max sum subarray of size k.
- **Variable-size, shrink-while-valid** (shown above) — e.g. smallest subarray with sum ≥ target.
- **Variable-size, shrink-while-invalid** — e.g. "longest substring without repeating characters": grow, and only shrink while the *current* window is invalid (contains a duplicate), rather than while some threshold is met.
- **Fixed-size with a frequency map** — e.g. "find all anagrams of p in s": window size = `len(p)`, track character counts instead of a sum.

## Practice Problems

Full writeups ship as `implementations/10_Sliding_Window_and_Two_Pointers/` is built out. Recommended order once that lands:
1. Maximum sum subarray of size K (fixed-size, warm-up)
2. Smallest subarray with a given sum (variable-size, shrink-while-valid)
3. Longest substring without repeating characters (variable-size, shrink-while-invalid)
4. Find all anagrams in a string (fixed-size, frequency map)
5. Minimum window substring (variable-size, frequency map — the hard version of this pattern)

## Related Patterns

- **Two Pointers** — sliding window is really a specialized two-pointer technique where both pointers move in the same direction. General two-pointer problems (pointers moving toward each other from opposite ends) are a separate, related pattern.
- **Monotonic Queue** — needed when you want the *max or min inside the window* efficiently (not just a sum), e.g. "sliding window maximum." Plain sliding window tracks aggregate state like sums/counts; it doesn't give you O(1) max/min without an additional structure.
