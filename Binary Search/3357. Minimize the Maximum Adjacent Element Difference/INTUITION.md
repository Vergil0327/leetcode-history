# Intuition

> [by @AlexWice](https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/solutions/6053410/python-binary-search-interval-stabbing/)
> Binary search for the answer.
> 
> Let's say we are trying to decide whether bound is an answer. Every wildcard ? next to a positive value a induces an interval `[a-bound, a+bound]`. Wildcards like a?b induce the interval `[a-bound,a+bound] INTERSECT [b-bound,b+bound]`.
> 
> At the end, we have some intervals and we want to know whether all of them can be stabbed by two points. The choice for these points will be greedy from the left and right as these extreme intervals must have a point on them chosen.
> 
> If we have chosen points lo, hi, then additionally they must have abs(lo - hi) <= bound, or the choice is valid without having to switch between lo and hi.


The key idea is:

1. Binary search over the potential maximum difference bound that we want to minimize. For a given bound, we check whether it's possible to replace all -1 values in the array such that the maximum adjacent difference doesn't exceed bound.
2. Missing values (-1) are treated in groups (consecutive -1s). Each group of -1s is either:
   1. Surrounded by positive neighbors (`a?b` or `a??b`).
   2. At the edge of the array (`a?` or `a??`).
3. For each group of -1s, we create intervals for possible replacements such that the replacements respect the bound. These intervals represent the range of possible values we can use to replace the -1s.
4. After constructing these intervals, we check if it's possible to cover all intervals using **at most** two points (this corresponds to choosing two values x and y for replacements).


# Approach

### Splits the array into contiguous groups of positive numbers and -1s using groupby

```py
groups = [list(grp) for k, grp in groupby(A, key=lambda x: x>0)]
```

### Initialization and Classification of Groups

```py
singles = []  # Tracks groups like a? or a??
doubles = []  # Tracks groups like a?b or a??b
base = 0  # Tracks the maximum difference between adjacent positive numbers
```

- singles: Tracks groups of -1s that are at the edge of the array or have only one neighbor.
- doubles: Tracks groups of -1s that are surrounded by positive numbers (e.g., a?b or a??b).
- base: Tracks the maximum difference between adjacent positive numbers in the original array. This sets the lower bound for the binary search.


**For positive groups**: e.g., [5, 3], calculate the largest difference (base) between consecutive elements.

```py

for i, grp in enumerate(groups):
    if grp[0] != -1:  # Positive group
        for j in range(len(grp) - 1):
            base = max(base, abs(grp[j] - grp[j+1]))
        continue

```

**Process `-1` Groups**:

For -1 groups, determine their neighbors:
- If there’s a previous group, the last element of that group is a neighbor.
- If there’s a next group, the first element of that group is a neighbor.

```py
neighbors = []
if i - 1 >= 0:
    neighbors.append(groups[i-1][-1])
if i + 1 < len(groups):
    neighbors.append(groups[i+1][0])
neighbors.sort()
```

**Classify Neighboring Intervals**

Store intervals:
1. singles for groups with one neighbor.
2. doubles for groups with two neighbors

```py
if len(neighbors) == 1:
    singles.append([*neighbors, len(grp) > 1])
if len(neighbors) == 2:
    doubles.append([*neighbors, len(grp) > 1])
```

**Binary Search to Minimize d**

- For a given bound, calculate all intervals induced by the -1s.
- Single neighbors induce [a - bound, a + bound].
- Two neighbors induce intersections of intervals [a - bound, a + bound] and [b - bound, b + bound].

```py
def possible(bound):
    intervals = []
    for a, len2 in singles:
        intervals.append([a - bound, a + bound])  # Single neighbor
    for a, b, len2 in doubles:
        if len2:  # More Than One `-1`s
            intervals.append([a - bound, a + bound])
            intervals.append([b - bound, b + bound])
        else:  # One `-1`
            lo = b - bound
            hi = a + bound
            if lo > hi: return 0
            intervals.append([lo, hi])


```

**Check Two-Point Coverage**

Determine if two points (`lo`, `hi`) can "stab" all intervals.
If `lo` and `hi` are too far apart, check if the condition holds for two-point coverage.

```py
lo = min(e for s, e in intervals)  # Leftmost interval end
hi = max(s for s, e in intervals)  # Rightmost interval start

if lo + bound < hi:
    if not all(
        any(abs(a - p) <= bound and abs(b - p) <= bound for p in [lo, hi]) 
        for a, b, l in doubles
    ):
        return 0

```

**Use binary search to find the smallest d such that all conditions are satisfied.**

```py
# seach space: [base, max(A)]
bisect_left(range(10**9), 1, base, max(A), key=possible)
```