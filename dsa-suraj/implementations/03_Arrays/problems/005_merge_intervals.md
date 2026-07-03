# 005. Merge Intervals

**Difficulty:** Medium
**Pattern:** Sort + Single Sweep
**Source:** LeetCode #56

## Problem Statement
Given an array of intervals `[start, end]`, merge all overlapping intervals and return the resulting non-overlapping intervals, sorted by start.

## Constraints
- `1 <= len(intervals) <= 10^4`
- Intervals are given in no particular order.
- `start <= end` within each interval.

## Observations
Two intervals can only possibly overlap if they're near each other — and "near" only becomes meaningful once the intervals are sorted by start time. Once sorted, overlap checking only ever needs to compare each interval to the *most recently merged* one, never to every other interval — that's what turns this from an all-pairs comparison problem into a single linear sweep.

## Pattern
Sort first to impose an order that makes the problem local (compare only to a neighbor), then a single O(n) sweep. This exact "sort, then sweep" shape reappears constantly for interval problems (meeting rooms, insert interval, non-overlapping intervals).

## Brute Force
```python
def merge_brute(intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals)
    merged = []
    for interval in intervals:
        placed = False
        for m in merged:
            if interval[0] <= m[1] and m[0] <= interval[1]:  # overlap check
                m[0] = min(m[0], interval[0])
                m[1] = max(m[1], interval[1])
                placed = True
                break
        if not placed:
            merged.append(interval)
    return merged
```
Complexity: O(n²) worst case — for each interval, potentially scanning all previously merged intervals to find an overlap. Sorting helps correctness but this version doesn't exploit it for speed.

## Optimized
```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda pair: pair[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:                      # overlaps the last merged interval
            merged[-1][1] = max(last_end, end)
        else:                                        # no overlap — new interval
            merged.append([start, end])

    return merged
```
Complexity: O(n log n) time (dominated by the sort), O(n) space for the output (O(log n) to O(n) extra for the sort itself, depending on implementation). The key insight that makes the sweep O(n) instead of O(n²): after sorting, an interval can only possibly overlap the **most recently added** merged interval — never an earlier one — so only one comparison is needed per interval, not a scan of all merged intervals so far.

## Dry Run
`intervals = [[1,3],[2,6],[8,10],[15,18]]`

Sorted (already sorted here): `[[1,3],[2,6],[8,10],[15,18]]`

| current | merged before | last_end | overlaps? | merged after |
|---|---|---|---|---|
| init | — | — | — | `[[1,3]]` |
| [2,6] | `[[1,3]]` | 3 | 2 ≤ 3 → yes | `[[1,6]]` |
| [8,10] | `[[1,6]]` | 6 | 8 ≤ 6 → no | `[[1,6],[8,10]]` |
| [15,18] | `[[1,6],[8,10]]` | 10 | 15 ≤ 10 → no | `[[1,6],[8,10],[15,18]]` |

Result: `[[1,6],[8,10],[15,18]]`.

## Complexity
Time: O(n log n) — the sort dominates; the sweep itself is O(n).
Space: O(n) for the output array; sort's internal space depends on Python's Timsort (O(n) worst case).

## Alternative Solutions
- **Sweep line with separate start/end events:** create `(time, +1/-1)` events for every interval start/end, sort all events, sweep once tracking an "active count" — merges wherever the active count touches zero between intervals. Same O(n log n) complexity; more useful when adapted to counting overlaps (e.g. "minimum meeting rooms required") rather than just merging.

## Edge Cases
- Single interval → returned as-is, no merging needed.
- All intervals overlap into one, e.g. `[[1,4],[2,5],[3,6]]` → merges to `[[1,6]]`.
- Touching-but-not-overlapping intervals, e.g. `[[1,4],[4,5]]` — whether these count as "overlapping" depends on the exact problem wording (`start <= last_end` in the code above treats touching intervals as overlapping and merges them; using `start < last_end` instead would NOT merge them). **Read the problem statement carefully for this boundary** — it's the most common source of an off-by-one wrong answer on this problem.

## Mistakes
- **Forgetting to sort first.** Without sorting, overlap checking genuinely requires comparing every pair — there's no way to get the O(n log n) sweep without imposing order first.
- **Comparing the new interval to ALL previously merged intervals instead of just the last one.** This is exactly what makes the brute force O(n²) — once sorted, it's mathematically guaranteed that the current interval (having the smallest remaining start) can't overlap anything earlier than the most recently merged interval, so checking only the last one is both correct and sufficient.
- **Getting the touching-interval boundary condition (`<=` vs `<`) wrong** relative to what the specific problem asks for — see Edge Cases above.

## Related Problems
- Insert Interval (LeetCode #57) — same merge logic, applied while inserting a single new interval into an already-sorted, already-merged list.
- Non-overlapping Intervals (LeetCode #435) — sort + sweep again, but counting removals instead of merging.
- Meeting Rooms II (LeetCode #253) — the sweep-line-with-events variation mentioned above.

## Revision Date
_(log dates revisited here)_
