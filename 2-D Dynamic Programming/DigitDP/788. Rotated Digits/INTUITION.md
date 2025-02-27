# Intuition

classic digit DP problem

digit string ranges from 1 to n, and we just need to know if current constructed string has changed or not

thus, we can define `def dfs(i, leading, lowerThanHigh, higherThanLow, changed): the number of good rotated string`

and description also give us what digit can make string "changed" (2,5,6,9) and what digit is invalid (3,4,7). rest of digits are just valid but can't make string "changed"

then, logic is simple:

```py
def dfs(i, leading, lowerThanHigh, higherThanLow, changed):
    if i >= m: return 1 if changed else 0

    start = 0 if higherThanLow else int(low[i])
    end = 10 if lowerThanHigh else int(high[i])+1

    res = 0
    for d in range(start, end):
        if d in {3,4,7}: continue # invalid digits
        res += dfs(i+1,
                    leading and d == 0,
                    lowerThanHigh or d < int(high[i]),
                    higherThanLow or d > int(low[i]),
                    changed or d in {2,5,6,9})
    return res
```