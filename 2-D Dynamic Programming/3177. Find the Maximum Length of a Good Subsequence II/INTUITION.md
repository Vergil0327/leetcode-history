# Intuition

求極值, 往dynamic programming方面想
先試著照著目標定義:

**dp[i][j]: the length of the longest subsequence till index i with at most j positions such that seq[i] != seq[i + 1]**

```
{X X X X X X} X
              i
```

再來看狀態如何轉移, 仔細觀察一下其實對於當前的nums[i], 我們只關心先前的subseq是結尾於nums[i]或是非nums[i]

1. 對於dp[i-1]結尾跟nums[i]一樣的: dp[i][j] = dp[idx of previous nums[i]][j]+1
2. 對於dp[i-1]結鬼是跟nums[i]不一樣的: dp[any idx but not nums[i]][j-1]+1

所以我們可以記錄每個nums[i]的prevIdx, 然後遍歷prevIdx更新dp[i][j]:

1. 如果nums[prevIdx] == nums[i], dp[i][j] = dp[prevIdx][j]+1
2. 如果nums[prevIdx] != nums[i], dp[i][j] = dp[prevIdx][j-1]+1

```py
n = len(nums)
dp = [[0]*(k+1) for _ in range(n)]
prevIdx = dict()

for i in range(n):
    for j in range(k, -1, -1):
        for idx in (prevIdx.values() or [0]):
            if nums[idx] == nums[i]:
                dp[i][j] = max(dp[i][j], dp[idx][j]+1)
            else:
                dp[i][j] = max(dp[i][j], dp[idx][j-1]+1 if j-1>=0 else 1)

    prevIdx[nums[i]] = i
return max(dp[i][k] for i in range(n))
```

但這樣會TLE, 所以我們得更進一步優化時間複雜度
這邊能看到對於nums[idx] != nums[i]的情況, 其實我們並不關心那些nums[idx]是啥
所有跟nums[i]不同的都一是同仁, 只關心他們在`j-1`時的值, 所以我們可以額外在一個dp `max_dp_so_far`紀錄這些值
這樣用max_dp_so_far[j-1]更新

另外我們調換一下dp, 改成dp[j][i]
並且我們只關心跟nums[i]相同或不同, 所以dp[j][i]改成dp[j][nums[i]]: **the length of the longest subsequence with at most j positions such that seq[i] != seq[i + 1] and ended at nums[i]**

```py
dp = [defaultdict(int) for _ in range(k+1)]
max_dp_so_far = [0]*(k+1)

for i in range(n):
    for j in range(k, -1, -1):
        dp[j][nums[i]] = max(dp[j][nums[i]]+1, max_dp_so_far[j-1]+1 if j-1>=0 else 0)
        max_dp_so_far[j] = max(max_dp_so_far[j], dp[j][nums[i]])
return max(max_dp_so_far)
```