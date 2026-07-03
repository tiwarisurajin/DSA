# The Think-Aloud Protocol

A repeatable structure for any live coding interview, regardless of the specific problem.

## 1. Clarify before you code (60–90 seconds)

Ask about:
- **Input shape and constraints.** Size bounds (does it change your approach — is O(n²) fine for n=100 but not n=10^6?), value ranges, can values be negative/duplicate/empty.
- **Output shape.** Return the value, the indices, or modify in place?
- **Edge cases the interviewer cares about.** Empty input? No valid answer exists?

Restate the problem back in your own words. This alone catches a meaningful fraction of misunderstandings before you've written a line of code.

## 2. State a brute force out loud, even if you already see the optimal solution

- "The brute force here would be [X], which is O(...) — I think we can do better by [Y]." This does two things: proves you can identify a correct-but-slow baseline (a real skill), and gives the interviewer a checkpoint to redirect you if you're about to over-engineer.

## 3. Narrate the pattern recognition

- Say which pattern you're reaching for and *why*, using the recognition clues from `patterns/`: "this is asking for a contiguous subarray with a sum constraint, so I'm thinking sliding window."
- If you're unsure between two patterns, say so — thinking out loud through the uncertainty is more valuable to the interviewer than silent certainty.

## 4. Code, narrating major decisions only

- Don't narrate every line ("now I'm writing a for loop") — narrate *decisions* ("I'm using a dict here instead of a list because I need O(1) lookups").
- If you get stuck, say what you're stuck on specifically, rather than going silent. "I'm not sure if this handles the case where all elements are equal — let me trace through that" is a strong signal, not a weak one.

## 5. State complexity unprompted

- Before the interviewer asks, say: "this is O(n) time because of the single pass, O(n) space for the hash map."
- If there's a worst-case vs average-case distinction (hash maps, quicksort), say which one you mean.

## 6. Test your own code before declaring done

- Pick a small example (not the one from the problem statement — a different one) and trace it by hand against your code.
- Explicitly check at least one edge case out loud: "let me check the empty input case... yes, that returns [] correctly."

## 7. When you're told you're wrong

- Don't argue reflexively and don't collapse instantly either. Ask *what* input breaks it: "can you give me an example where this fails?" Tracing a concrete counterexample is almost always faster than abstract back-and-forth, and shows you debug systematically under pressure — which is closer to what the interviewer is actually evaluating than whether you got it right the first time.

## Common failure modes this protocol prevents

| Failure mode | What it signals to the interviewer |
|---|---|
| Coding immediately without clarifying | Doesn't gather requirements before building — a real engineering red flag, not just an interview one |
| Going silent when stuck | Hard to debug with, hard to pair-program with |
| Never stating complexity | Either doesn't know, or doesn't think it matters — both bad |
| Getting defensive when corrected | Hard to give feedback to on a real team |
