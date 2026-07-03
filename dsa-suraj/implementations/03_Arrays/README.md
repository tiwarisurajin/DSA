# 03 — Arrays

**Status: ✅ Complete** — theory, 5 fully worked problems, cheatsheet, mistakes log, revision schedule.

Arrays are the base structure everything else builds on. If you internalize the brute-force-to-optimized trade-offs here (usually "trade O(n) space for a hashmap/set to collapse an O(n) inner scan"), you'll recognize the same move in Strings, Trees, and Graphs later.

## Contents

- [`theory.md`](./theory.md) — what an array actually is in memory, and why its operations have the complexities they do
- [`cheatsheet.md`](./cheatsheet.md) — quick reference for operation complexities and common techniques
- [`mistakes.md`](./mistakes.md) — the specific ways people get array problems wrong
- [`revision.md`](./revision.md) — spaced revision schedule for this topic's problems
- [`problems/`](./problems/) — full writeups, template-complete
- [`templates/`](./templates/) — reusable code templates for array techniques

## Problems

| # | Problem | Pattern | Difficulty | Status |
|---|---|---|---|:---:|
| 001 | [Two Sum](./problems/001_two_sum.md) | Hashing | Easy | ✅ |
| 002 | [Best Time to Buy and Sell Stock](./problems/002_best_time_to_buy_sell_stock.md) | Single Pass / Kadane-adjacent | Easy | ✅ |
| 003 | [Product of Array Except Self](./problems/003_product_of_array_except_self.md) | Prefix/Suffix Products | Medium | ✅ |
| 004 | [Maximum Subarray (Kadane's)](./problems/004_maximum_subarray.md) | Dynamic Programming (1D) | Medium | ✅ |
| 005 | [Merge Intervals](./problems/005_merge_intervals.md) | Sort + Sweep | Medium | ✅ |

## Prerequisites

- [Engineering Handbook, Chapter 1–3](../../Engineering_Handbook.md) for memory model and complexity reasoning
- Basic Python: lists, loops, functions

## What comes next

Once this is solid, [Binary Search](../04_Binary_Search/) and the [Sliding Window pattern](../../patterns/sliding_window.md) both build directly on array intuition built here.
