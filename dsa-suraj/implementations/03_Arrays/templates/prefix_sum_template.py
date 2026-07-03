"""
Reusable template: prefix sum for O(1) range-sum queries after O(n) preprocessing.
See: implementations/03_Arrays/theory.md#6-prefix-sums
"""

def build_prefix_sum(arr: list[int]) -> list[int]:
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix: list[int], i: int, j: int) -> int:
    """Sum of arr[i:j] (j exclusive), O(1) after prefix is built."""
    return prefix[j] - prefix[i]
