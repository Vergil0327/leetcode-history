# Intuition

最少一天吃1個
最多一天吃cap個 (cap = queries[i][2])
得0, 1, 2, ..., i-1, i依序吃, 吃完才下一個

代表我們希望在favDay能吃的糖果數目範圍落在`[1 * days+1, cap*(days+1)]` (both inclusive).

所以如果有個`prefix sum ＝ [x, x, x, x, ...]`
那麼落在`[1 * days+1, cap*(days+1)]`範圍內的都是我們可以吃到的
我想可以用binary search 找出合法的prefix_sum[i:j]區間
1. sum(candiesCount[:i]) >= 1*days+1
2. sum(candiesCount[:j]) >= cap*(days+1)

如果presum[i] >= 1*days+1, 那麼至少要 t >= i-1 才會是合法區間(presum是1-indexed)
如果presum[j] >= cap*(days+1), 那麼t <= j-1都是合法區間

所以:
```py
res = []
for t, d, cap in queries:
    l, r = d+1, cap*(d+1)
    i = bisect.bisect_left(presum, l)
    j = bisect.bisect_left(presum, r)
    res.append(i-1 <= t <= j-1)
return res
```

time: $O(queries.length * log(candiesCount.length))$

# Other Solution

但其實我們不需要用binary search

我們先求出一個0-indexed的prefix sum
`presum = list(accumulate(candiesCount)) # 0-indexed`

再來一樣, 我們必須判斷範圍有沒有落在`[day+1:cap*(day+1)]`
- 如果wanted_type = 0, 那麼presum[0]必須 > day, 這樣days+1就會落在type=0
- 如果wanted_type > 0, 那麼:
  - 前面presum[t-1]+1必須不超過`cap*(day+1)`
  - 然後presum[t]必須大於`day` (一天吃一個)


```py
def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
    presum = list(accumulate(candiesCount)) # 0-indexed
    res = []
    for t, day, cap in queries:
        eaten_least = day # 至少一天得吃一個
        if t == 0:
            res.append(presum[t] > eaten_least)
        else:
            to_be_eaten = presum[t-1] + 1
            res.append(to_be_eaten <= ((day + 1) * cap) and presum[t] > eaten_least)
    return res
```