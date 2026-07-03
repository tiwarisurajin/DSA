# Time Complexity Handbook

## 1. What is Time Complexity?
Time complexity describes how the running time of an algorithm grows as the input size (n) increases.

## 2. Why does it matter?
- Compare algorithms
- Predict scalability
- Avoid Time Limit Exceeded (TLE)

## 3. Common Complexities
- O(1) Constant
- O(log n) Logarithmic
- O(n) Linear
- O(n log n) Linearithmic
- O(n²) Quadratic
- O(2^n) Exponential
- O(n!) Factorial

## 4. Big O vs Theta vs Omega
- Big O: Worst-case upper bound
- Theta: Tight bound
- Omega: Best-case lower bound

## 5. Python Operations
| Operation | Complexity |
|---|---|
| list.append | O(1) amortized |
| list.pop() | O(1) |
| list.pop(0) | O(n) |
| dict lookup | O(1) average |
| set lookup | O(1) average |
| sort() | O(n log n) |

## 6. Interview Tips
Always explain complexity before and after coding.

## 7. Revision Checklist
- [ ] Can explain Big O
- [ ] Know common complexities
- [ ] Know Python operation complexities
