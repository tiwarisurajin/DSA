"""
Reusable template: Kadane-style running best, for "max/min contiguous subarray" problems.
See: implementations/03_Arrays/problems/004_maximum_subarray.md
"""

def running_best(arr: list[int]) -> int:
    best_ending_here = best_overall = arr[0]
    for x in arr[1:]:
        best_ending_here = max(x, best_ending_here + x)
        best_overall = max(best_overall, best_ending_here)
    return best_overall
