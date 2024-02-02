# Intuitin

explore digit within [low, high] => digit DP

template:

```py
low = str(low)
high = str(high)
while len(low) < len(high):
    low = "0" + low
n = len(low)

self.arr = []
def dfs(i, leading, greaterThanLow, lowerThanHigh, digits):
    if i == n:
        self.arr.append(digits)
        return

    start = 0 if greaterThanLow else int(low[i])
    end = 10 if lowerThanHigh else int(high[i])+1

    for d in range(start, end):
        if digits == 0 or digits%10+1 == d:
            dfs(i+1,
                leading and d == 0,
                greaterThanLow or d > int(low[i]),
                lowerThanHigh or d < int(high[i]),
                digits*10+d)
```

we explore sequential digits by dfs and store in `digits`.
and condition is clear, we can explore next recursion only if current digit equals previous digit + 1

base case:

if i == n, we have valid sequential digits and add to result array.

