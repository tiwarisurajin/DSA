# 003. Product of Array Except Self

**Difficulty:** Medium
**Pattern:** Prefix/Suffix precomputation (same family as [theory.md §6](../theory.md#6-prefix-sums--precompute-once-query-many-times), applied to products)
**Source:** LeetCode #238

## Problem Statement
Given an array `nums`, return an array `answer` where `answer[i]` is the product of every element in `nums` except `nums[i]`. Must run in O(n) time **without using division**, and (follow-up) in O(1) extra space excluding the output array.

## Constraints
- `2 <= len(nums) <= 10^5`
- The product of any prefix or suffix fits in a 32-bit integer.
- No division allowed — this rules out the tempting "compute total product, then divide by `nums[i]`" shortcut (which also breaks on zeros anyway).

## Observations
`answer[i]` is exactly `(product of everything to the left of i) * (product of everything to the right of i)`. If we precompute "product of everything to the left" for every index in one pass, and "product of everything to the right" in another pass, we can combine them in a third O(n) pass — no division needed anywhere.

## Pattern
Same shape as prefix sums (theory.md §6), just with multiplication instead of addition, and done from both directions (prefix AND suffix).

## Brute Force
```python
def product_except_self_brute(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        answer.append(product)
    return answer
```
Complexity: O(n²) — for every index, rescan the whole array.

## Optimized
```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # Pass 1: answer[i] becomes "product of everything to the left of i"
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Pass 2: multiply in "product of everything to the right of i"
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```
Complexity: O(n) time, O(1) extra space (the output array doesn't count toward the space constraint per the problem's own follow-up). Trade being made: two clean linear passes replace an O(n) rescan per index, without ever dividing.

## Dry Run
`nums = [1, 2, 3, 4]`

**Pass 1 (left products):**
| i | answer[i] (=prefix before update) | prefix (after) |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 1 | 2 |
| 2 | 2 | 6 |
| 3 | 6 | 24 |

After pass 1: `answer = [1, 1, 2, 6]`

**Pass 2 (right products, multiplied in, right to left):**
| i | suffix (before) | answer[i] *= suffix | suffix (after) |
|---|---|---|---|
| 3 | 1 | 6 * 1 = 6 | 4 |
| 2 | 4 | 2 * 4 = 8 | 12 |
| 1 | 12 | 1 * 12 = 12 | 24 |
| 0 | 24 | 1 * 24 = 24 | 24 |

Final: `answer = [24, 12, 8, 6]`. Check `answer[0] = 2*3*4 = 24` ✓.

## Complexity
Time: O(n) — two linear passes.
Space: O(1) extra — `prefix` and `suffix` are scalars; the output array is required regardless of approach and isn't counted.

## Alternative Solutions
- **Division approach** (compute total product, divide by `nums[i]` per index): simpler to write, but explicitly disallowed by the problem, and breaks entirely if any element is `0` (and needs special-casing for exactly one zero vs multiple zeros) — the prefix/suffix approach handles zeros correctly with no special-casing at all, which is itself a good reason to prefer it even when division is allowed.

## Edge Cases
- Exactly one zero in the array, e.g. `[1, 0, 3]` → every index except the zero's own index gets `0` (because their product includes the zero); the zero's own index gets the product of everything else. The prefix/suffix approach handles this with no extra logic — worth tracing by hand once to confirm.
- Two or more zeros → every output is `0`. Also handled automatically.
- Array of length 2 (minimum per constraints) → `answer = [nums[1], nums[0]]`.

## Mistakes
- **Reaching for division "just to get something working" first**, then forgetting to remove it — costs the "no division" requirement and silently breaks on zero-containing inputs even if the interviewer didn't explicitly test for it.
- **Doing prefix and suffix as two separate output arrays** (`prefix[]`, `suffix[]`, then a third pass to multiply them into `answer[]`) — correct, but uses O(n) extra space instead of O(1). Worth knowing the O(n)-space version first, then tightening it to reuse `answer` itself as the prefix array (as shown above) to satisfy the space follow-up.

## Related Problems
- Trapping Rain Water (LeetCode #42) — same "precompute left-max and right-max in two passes" shape, applied to a max instead of a product.
- Maximum Subarray ([004](./004_maximum_subarray.md)) — different technique, but same spirit of "one informative pass instead of nested rescans."

## Revision Date
_(log dates revisited here)_
