# DP + Binary Search

## Intuition

第一個最大區間可以透過binary search找到

```py
res = 0
for i in range(n - 1, -1, -1):
    j = bisect.bisect_right(prizePositions, prizePositions[i] + k)
    dist = j - i
    res = max(res, dist)
```

在逐個找的時候，我們可以同步維護一個dp array，使得

`dp[i] : the maximum number of prize for prizePositions[i:]`

這樣當我們在`i`位置找到最大distance時，涵蓋的範圍為`[i:j)`
dp[j]則為從j到n-1，也就是prizePositions[j:]這範圍內的最大涵蓋區間
因此選擇兩個區間的最大涵蓋範圍即為: `dist + dp[j]`

```py
res = 0
for i in range(n - 1, -1, -1):
    j = bisect.bisect_right(prizePositions, prizePositions[i] + k)
    dist = j - i
    res = max(res, dist+dp[j]) # dist is maximum number of prize for [i:j),  dp[j] covered [j:]
    dp[i] = max(dist, dp[i + 1])
```

# DP + Sliding Window

## Intuition

同樣地，第一次的最大區間也可以透過sliding window找出來


```py
# sliding window 左閉右開 [l,r)
res = l = r = 0
while r < n:
    num = positions[r]
    r += 1

    while l < r and num-positions[l] > k:
        l += 1
    res = max(res, r-l)
```

所以同樣地，我們可以再找最大區間的途中，同時用一個dp array紀錄到目前為止的最大涵蓋範圍

`dp[i] : the maximum number of prize for positions[:i]`

然後可以這樣更新dp: `dp[r] = max(dp[r-1], r-l)`

由於r-l涵蓋的區間為[l,r), dp[l]為`0`到`l`為止 (positions[0:l]) 的最大涵蓋
因此兩個區間的最大範圍為 `r-l + dp[l]` 取 max

```py
dp = [0] * (n+1)

res = l = r = 0
while r < n:
    num = positions[r]
    r += 1

    while l < r and num-positions[l] > k:
        l += 1

    # r會從1開始
    dp[r] = max(dp[r-1], r-l)
    res = max(res, r-l + dp[l])
return res
```