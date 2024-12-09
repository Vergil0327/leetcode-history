# Intuition

# Approach - Brute Force

```py
perms = permutations(strength)

res = inf
for arr in perms:
    t = egy = 0
    x = 1
    for num in arr:
        times = ceil(num/x)
        egy += x * times
        t += times

        egy = 0
        x += K
    res = min(res, t)
return res
```

time: O(n! * n)

# Approach - DP

看到這限制: `1 <= n <= 8`
我們可以用top-down DP + bitmask as choosing state來找出最小所需次數

對於當前strength[i], 所需時間為`ceil(strength[i]/x)`

```py
def dfs(x, state):
    if state.bit_count() == n: return 0

    res = inf
    for i in range(n):
        if (state>>i)&1: continue
        t = ceil(strength[i]/x)
        res = min(res, dfs(x+K, state | (1<<i)) + t)
    return res
```

另外其實一開始還有想到利用binary search去猜這個minimum time:

```py
l, r = 0, sum(strength)

while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

但其實是沒有單調性的, 也就是沒有合適的`check`能驗證當前`mid`, 因此binary search不可行