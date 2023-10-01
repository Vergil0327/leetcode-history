# Intuition

```
[X X X X][X X X X]...[X X X X][X X X X]...
    {X X X X X X X X X X X X X X X} = target
```

根據觀察我們可以推敲出:

**presum[i]+k*presum[n]-presum[j] == target**

因此, **presum[i]+k*presum[n]-target == presum[j]**

所以這讓我想到prefix sum + hashmap
因此首先先把中間的repeating part從target給移除掉, 順便求出中間的`k`為多少(即有多少重複)

```py
k = 0
while target > presum[n-1]:
    target -= presum[n-1]
    k += 1
```

不管這個target subarray多大, 由於我們可以提前扣掉repeating part
所以我們要找的presum[j]永遠落在第一個`nums`裡

因此我們可以用hashmap紀錄: `{preifx_sum: index}`
由於移除之後target最多只可能橫跨兩個`nums`
所以我們首先先看單純一個nums能不能找出相對應的subarray

也就是這種可能性:

```
nums = [X X X X X X X X X X X X X X X X]
                j         i
target =       {X X X X X X}
```


```py
seen = {}
seen[0] = -1
res = inf
for i in range(n):
    if (pre := presum[i]-target) in seen:
        res = min(res, i-seen[pre])
    seen[presum[i]] = i
```

然後在看有沒有底下這種可能性:
- presum[i']為presum[i+n]
- presum[j]
- target = presum[i']-presum[j]

```
nums = [X X X X X X X X][X X X X X X X X]
                j          i'
target =       {X X X X X X}
```

```py
for i in range(n):
    if (pre := presum[i]+presum[n-1]-target) in seen:
        res = min(res, i+n-seen[pre])
```

# Concise Solution

```py
def minSizeSubarray(self, nums: List[int], target: int) -> int:
    total = sum(nums)
    n = len(nums)
    k = target // total
    target %= total
    if target == 0:
        return k * n

    dp = {0: -1}
    cur = 0
    res = inf
    for i, num in enumerate(nums + nums):
        cur += num
        if cur - target in dp:
            res = min(res, i - dp.get(cur - target))
        dp[cur] = i
    return res + k * n if res < inf else -1
```