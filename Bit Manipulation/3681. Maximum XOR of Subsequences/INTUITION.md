# Intuition

A linear basis (also called XOR basis) is a set of numbers that can represent all possible XOR combinations of a larger set, but in a minimal, non-redundant way.

**Key Properties:**

- Span: You can create any XOR value that's possible from the original set
Linear independence: No element in the basis can be created by XORing other basis elements
- Minimality: It's the smallest such set

**How the Algorithm Works:**

Building the basis:
```python
for x in nums:
    for b in basis:
        x = min(x, x^b)  # Reduce x using existing basis elements
    if x > 0:
        basis.append(x)  # x is linearly independent
```

The key insight is x = min(x, x^b) - this finds the lexicographically smaller value between x and x^b.

Example:
nums = [1, 2, 3, 4]

Processing 1: basis = [1]
Processing 2: basis = [2, 1] 
Processing 3: 
  - 3^2 = 1, min(3,1) = 1
  - 1^1 = 0, so x becomes 0
  - x=0, don't add to basis
Processing 4: basis = [4, 2, 1]
Finding maximum XOR:

```python
res = 0
for b in basis:
    res = max(res, res^b)  # Greedily pick larger XOR
```
This greedily builds the maximum possible XOR by deciding whether to include each basis element.

**Why It Works:**

The basis captures all possible XOR combinations efficiently
Any subset XOR from the original array can be represented using the basis
The greedy approach works because the basis is sorted, so we always try larger contributions first