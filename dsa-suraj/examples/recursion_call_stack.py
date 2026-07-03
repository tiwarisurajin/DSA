"""
recursion_call_stack.py

Visualizes what's actually happening on the call stack during recursion,
tying directly to Engineering_Handbook.md Chapter 2 (Memory, the Stack, and the Heap).

Run it directly: python examples/recursion_call_stack.py
"""

def factorial(n: int, depth: int = 0) -> int:
    indent = "  " * depth
    print(f"{indent}-> factorial({n}) called, stack frame pushed (depth={depth})")

    if n == 0:
        print(f"{indent}   base case hit, returning 1")
        return 1

    result = n * factorial(n - 1, depth + 1)

    print(f"{indent}<- factorial({n}) returning {result}, stack frame popped")
    return result


if __name__ == "__main__":
    print("Tracing factorial(4) — watch the stack grow, then unwind:\n")
    answer = factorial(4)
    print(f"\nFinal answer: {answer}")
    print(
        "\nNotice: 5 stack frames existed simultaneously at the deepest point "
        "(factorial(4) through factorial(0)) — this is exactly why recursive "
        "space complexity includes call-stack depth, not just heap allocations. "
        "See Engineering_Handbook.md Chapter 2, section 2.3."
    )
