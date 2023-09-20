# Intuition

special => all digits distinct

first thought: use dfs to explore all valid integer
since it relates to digits, maybe digit DP can help.

digits DP template:

*note. i means i-th digit*
```py
def dfs(i, hasLeadingZero, isGreaterThanLowerbound, isLowerThanUpperbound, bitmask):
    start = 0 if isGreaterThanLowerbound else int(low[i])
    end = 10 if isLowerThanUpperbound else int(high[i])+1

    res = 0
    for digit_within_range in range(start, end):
        # doing your work
        res += dfs(...)
    return res # number of special integers
```

since we want digits are distinct, we can use 10-bit bitmask as state to tell what digits we've already used.
then, we can know how to pick unused digit based on bitmask.
ex. 00..101 means we already used `2` and `0`

so,
- if 0 < digit <= 9, if digit already used which means `(bitmask>>d)&1`: we should skip this digit
- if digit == 0 and digit `0` is used and `0` is not part of leading zeros: we should skip it too

then we just explore all valid digit by:
```py
res += dfs(i+1,
           hasLeadingZero and d == 0,
           isGreaterThanLowerbound or d > int(low[i]),
           isLowerThanUpperbound or d < int(high[i]),
           nxt_state)
```
where next_state is:
```py
next_bitmask = bitmask
if d > 0 or not hasLeadingZero: # if 1 <= d <= 9 or (d == 0 and not leadingZero)
    next_bitmask |= (1<<d)
```

**Base Case**

if i == len(str(n)): return 1

