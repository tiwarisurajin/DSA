# The Engineering Handbook

A book, not a doc. Read it in order the first time. Come back to individual chapters as reference.

**Status:** Chapters 1–3 complete. Chapters 4–27 queued (see the table below — this is the same honesty policy as the root README's Progress Dashboard).

## Table of Contents

| Ch. | Title | Status |
|---|---|:---:|
| 1 | [How Computers Actually Think](#chapter-1--how-computers-actually-think) | ✅ |
| 2 | [Memory, the Stack, and the Heap](#chapter-2--memory-the-stack-and-the-heap) | ✅ |
| 3 | [Time and Space Complexity](#chapter-3--time-and-space-complexity) | ✅ |
| 4 | Arrays & Pointers | ⬜ queued |
| 5 | Recursion, Deeply | ⬜ queued |
| 6 | Hashing | ⬜ queued |
| 7 | Trees | ⬜ queued |
| 8 | Graphs | ⬜ queued |
| 9 | Dynamic Programming | ⬜ queued |
| 10 | Bit Manipulation | ⬜ queued |
| 11 | Greedy Algorithms | ⬜ queued |
| 12 | Union-Find | ⬜ queued |
| 13 | Tries | ⬜ queued |
| 14 | Segment Trees & Fenwick Trees | ⬜ queued |
| 15 | Backtracking | ⬜ queued |
| 16 | The Interview Mindset | ⬜ queued |
| 17 | Debugging Like an Engineer | ⬜ queued |
| 18 | Writing Code People Can Read | ⬜ queued |
| 19 | Thinking Like an Engineer | ⬜ queued |
| 20 | Communicating Under Pressure | ⬜ queued |
| 21 | Systematic Learning & Revision | ⬜ queued |

---

## Chapter 1 — How Computers Actually Think

### 1.1 The machine doesn't know what a "list" is

When you write `my_list = [1, 2, 3]` in Python, you're working with an abstraction. The CPU underneath doesn't know what a list is. It knows three things: **read from an address**, **write to an address**, and **do arithmetic on values**. Everything else — lists, dictionaries, objects, even functions — is a story we tell the machine using those three primitives.

This matters for DSA because almost every complexity argument you'll ever make comes back to this fact. "Array access is O(1)" isn't a rule you memorize — it's a direct consequence of how memory addresses work (Chapter 2). If you understand *why* it's O(1), you'll never confuse it with, say, "search in an array is O(1)" (it isn't — you have to check addresses one at a time unless you already know the index).

### 1.2 The fetch-execute cycle, minimally

A CPU repeats a loop, roughly:

1. **Fetch** the next instruction from memory (the address is tracked by a register called the *program counter*).
2. **Decode** what the instruction means.
3. **Execute** it — maybe an addition, maybe a memory read, maybe a jump to a different instruction.
4. Repeat.

You don't need to know assembly to do well in interviews. You need this one idea: **every operation your code performs costs cycles, and the number of cycles as input size grows is what "time complexity" is actually measuring.** Big O isn't a math trick — it's an accounting of how many fetch-execute cycles you're asking the machine to run.

### 1.3 Why "constant time" is a simplification

`O(1)` doesn't mean "instant." It means "the number of cycles doesn't grow with input size `n`." Looking up `dict[key]` might take 5 cycles or 50 depending on hashing and cache behavior — but it doesn't take *more* cycles just because your dictionary has a million entries instead of ten (on average — see hash collisions in Chapter 6, queued). That's the property that matters.

### 1.4 Interview relevance

When an interviewer asks "why is this O(n) and not O(1)?", they're really asking: *can you trace what the machine has to physically do as input grows?* Being able to answer from first principles (not from memorized rules) is what separates candidates who "know Big O" from candidates who can derive the complexity of code they've never seen before — which is exactly what happens in every interview.

---

## Chapter 2 — Memory, the Stack, and the Heap

### 2.1 Two places your data can live

When your Python program runs, the values it creates live in one of two regions:

- **The Stack** — fast, small, automatically managed. Used for function call frames: local variables, return addresses, parameters.
- **The Heap** — slower, large, manually-ish managed (Python's garbage collector does the "manual" part for you). Used for objects that need to outlive the function that created them, or that are too large/dynamic for the stack.

### 2.2 What actually happens when you call a function

```python
def add(a, b):
    total = a + b
    return total

result = add(3, 4)
```

When `add(3, 4)` is called, a new **stack frame** is pushed containing `a=3`, `b=4`, and later `total=7`. When `add` returns, that frame is popped and destroyed. This is why local variables disappear after a function returns, and it's the entire mechanism behind **recursion** (Chapter 5, queued) — each recursive call gets its own stack frame, which is also exactly why deep recursion can cause a `RecursionError` / stack overflow: you're pushing more frames than the stack has room for.

### 2.3 Why this matters for space complexity

"Space complexity" isn't just "how much data structure did I create" — it includes the stack. A recursive function that recurses `n` deep has **O(n) space complexity from the call stack alone**, even if it never allocates a single list. This is the single most common thing beginners miss when analyzing recursive solutions: they count the heap allocations and forget the stack.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)   # O(n) stack frames at the deepest point
```

### 2.4 Mutable vs immutable, and why it's a memory question, not a syntax question

`int`, `str`, `tuple` are immutable in Python — operations on them create new objects on the heap rather than modifying in place. `list`, `dict`, `set` are mutable — they can be modified in place. This is *why* string concatenation in a loop is a classic performance bug:

```python
# O(n²) — each += creates a brand new string object on the heap
s = ""
for c in chars:
    s += c

# O(n) — list append is amortized O(1); join happens once
parts = []
for c in chars:
    parts.append(c)
s = "".join(parts)
```

### 2.5 Interview relevance

"What's the space complexity of your solution?" is asking you to count *every* region of memory your algorithm touches: input (usually not counted), output (sometimes counted, ask), auxiliary heap structures, and the call stack if you're recursive. Forgetting the call stack is one of the most common "gotcha" corrections interviewers make.

---

## Chapter 3 — Time and Space Complexity

*This chapter is the theory companion to [`docs/05_Time_Complexity.md`](./docs/05_Time_Complexity.md), which stays as the quick-reference version. Read this for the reasoning; read that for the lookup table.*

### 3.1 What Big O is actually for

Big O answers one question: **as input size `n` grows without bound, how does resource usage (time or space) grow relative to `n`?** It deliberately throws away constant factors and lower-order terms, because those depend on hardware, language, and implementation details that don't tell you anything about the *algorithm's* scalability.

`3n + 100` and `n` are both `O(n)` — the `100` and the `3` stop mattering once `n` is large enough. This is the entire point: Big O tells you how an algorithm *behaves at scale*, not how fast it runs on your laptop today.

### 3.2 Worst, best, and average case — and why interviews care about worst case

- **Worst case (Big O):** the maximum resources used over all inputs of size `n`. This is what interviewers almost always mean by default when they say "what's the complexity."
- **Best case (Big Ω, Omega):** the minimum. Rarely useful on its own — an algorithm that's O(1) best case and O(n²) worst case is still an O(n²) algorithm in practice.
- **Average case:** expected resources over a distribution of inputs. Useful for things like hash table lookups (O(1) average, O(n) worst case under pathological collisions) and quicksort (O(n log n) average, O(n²) worst case on already-sorted input with a bad pivot choice).
- **Tight bound (Big Θ, Theta):** used when best and worst case are the same order — e.g. summing an array is Θ(n): you always touch every element, no better, no worse.

**Why this matters in an interview:** if you say "this hash map lookup is O(1)" without qualification, a sharp interviewer may ask "always?" — and the correct answer is "average case, assuming a decent hash function and low load factor; worst case is O(n) under adversarial collisions." Saying that unprompted is a strong signal.

### 3.3 Amortized analysis, concretely

`list.append()` in Python is described as "O(1) amortized." Here's why, not just what: Python lists over-allocate. When a list of capacity 8 is full and you append a 9th element, Python doesn't grow the array by 1 — it reallocates to a larger capacity (roughly 1.125–2x growth depending on size) and copies everything over. That single append is O(n). But that expensive append only happens once every O(n) appends, so if you *spread that cost over all the appends*, each one costs O(1) on average — hence "amortized."

This is the same reasoning behind dynamic array resizing in general, and it's worth being able to derive, not just quote, because interviewers sometimes ask "why is append amortized O(1) and not just O(1)?" directly.

### 3.4 How to derive complexity from code, step by step

Given code you've never seen, the process is mechanical:

1. **Find the loops.** A single loop over `n` items → O(n). Nested loops over `n` and `m` → O(n·m). Nested loops over the *same* `n`, where the inner loop shrinks (e.g. `for j in range(i, n)`) → still O(n²), because the sum of a shrinking series is still quadratic (it's `n²/2`, and constants drop).
2. **Find the recursion, if any**, and count branches × depth. A recursive function that makes 2 calls and recurses `n` deep, with no memoization, is O(2ⁿ) — this is the classic naive Fibonacci trap.
3. **Check what's inside the loop.** A loop that does an O(1) operation `n` times is O(n) total. A loop that does an O(n) operation (like `list.index()`, which itself scans) `n` times is O(n²) total, even though there's only one `for` loop visible in the code — this is the single most common way people misjudge complexity by only counting visible loop nesting instead of the cost of what's *inside* the loop.
4. **Space:** count new data structures created (heap) + max recursion depth (stack). Don't count the input unless you're told to.

### 3.5 A worked misjudgment (this is a real, common mistake)

```python
def has_duplicate(nums):
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:   # <-- slice + membership check, both O(n)
            return True
    return False
```

This *looks* like a single O(n) loop. It's actually **O(n²)**: `nums[i+1:]` creates a new list slice (O(n)) and `in` on a list scans linearly (O(n)), and this happens inside a loop that runs n times. The visible loop nesting is 1, but the real work is quadratic. Compare:

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:      # O(1) average — set membership, not list membership
            return True
        seen.add(num)
    return False
```

This is genuinely O(n) — trading O(n) space for a hash set to collapse the inner check from O(n) to O(1) average. This exact trade (extra space for a hash structure → lower time complexity) is the single most common "optimize this" move in interviews, and it's the core idea behind the Arrays topic's [Two Sum problem](./implementations/03_Arrays/problems/001_two_sum.md).

### 3.6 Revision Checklist

- [ ] Can derive complexity from unfamiliar code, not just recall it for known problems
- [ ] Can explain amortized analysis with the dynamic array resizing example
- [ ] Know when to state "average case" vs "worst case" unprompted
- [ ] Can name the loop-hides-a-scan mistake and give an example
- [ ] Understand space complexity includes the call stack for recursive solutions

---

*Chapters 4–21 follow this same depth and will ship topic-by-topic alongside the matching `implementations/` folder — Arrays (Ch. 4) is next since `implementations/03_Arrays/` is already complete.*
