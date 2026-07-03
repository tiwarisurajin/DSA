"""
Reusable template: complement/existence lookup via hash map.
Use when a problem asks "does X exist" / "what pairs with X" repeatedly.
See: implementations/03_Arrays/problems/001_two_sum.md
"""

def hash_lookup_pattern(arr: list[int], target: int) -> list[int]:
    seen = {}
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []
