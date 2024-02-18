# Intuition

由於要找出連續數, 直覺先想到排序, 再來我們每個數有一次`+1`的操作

一開始從兩種選擇開始, 然後看能不能繼續接下去
i=0
nums[i]
nums[i]+1

再來看i=1
nums[i+1]
由於已經排序, 我們就往回看存不存在一個nums[i+1]-1 或是 (nums[i]+1)-1

```
[X X X X X X X]
             i
```

所以也就是對於nums[i]來說, 我們要看有沒有nums[i]-1或是nums[i]存在, 有的話就能接在後面長度+1
所以定義dp[num]: the maximum number of elements that we can select ended at num
由於要快速查找nums[i]跟nums[i]-1, dp我們用hashmap表示

首先我們可以選擇自立門戶:
```py
dp_next = defaultdict(int)
dp_next[num] = 1
dp_next[num+1] = 1
```

我們只關注nums[i]-1跟nums[i], 所以:
```py
dp_next[num-1] = dp[num-1]
dp_next[num] = max(dp_next[num], dp[num])
```

再來就是可以接在後面的條件:
```py
if num-1 in dp:
    dp_next[num] = max(dp_next[num], dp[num-1]+1)
    res = max(res, dp_next[num])

if num in dp:
    dp_next[num+1] = max(dp_next[num+1], dp[num]+1)
    res = max(res, dp_next[num+1])
```

# Complexity

- time complexity: $O(n)$
- space complexity: $O(n)$