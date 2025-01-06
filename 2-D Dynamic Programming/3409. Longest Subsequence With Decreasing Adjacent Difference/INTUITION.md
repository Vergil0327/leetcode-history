# Intuition

brute force

```py
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        @cache
        def dfs(i, diff):
            if i >= len(nums): return 0

            res = 0
            for j in range(i+1, len(nums)):
                if (d := abs(nums[j]-nums[i])) <= diff:
                    res = max(res, dfs(j, d)+1)
            return res
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, inf))
        return res+1
```

O(n^3) => TLE

see constraints: we can see that this `1 <= nums[i] <= 300` is unusually small
maybe we can use this constraint to shrink our value range and reduce time complexity

```
nums = XXXXXX num2 num1
```

let dp[num1][diff]: the longest length of subsequence ending at `num1` with difference less than or equal to `diff`

state transfer: `dp[num1][diff] = dp[num2][diff]+1`

```py
mx = max(nums)
dp = [[0]*(mx+1) for _ in range(mx+1)]

for diff in range(mx+1):
    dp[nums[0]][diff] = 1

for num1 in nums[1:]:
    for diff in range(mx+1):
        # abs(num1-num2) = diff
        # num2 = diff+num1 or num1-diff
        curr  = 0
        if (num2 := diff+num1) <= mx:
            curr = max(curr, dp[num2][diff]+1)

        if (num2 := num1-diff) >= 0:
            curr = max(curr, dp[num2][diff]+1)

        dp[num1][diff] = max(dp[num1][diff], curr)

    # remember our definetion: dp[num][diff], the longest length of subseq. ending at num with diffrence **less than or equal to** `diff`
    for diff in range(mx-1, -1, -1):
        dp[num1][diff] = max(dp[num1][diff], dp[num1][diff+1])
```

要特別注意中間的num1, num2更新不能寫成下面形式, 因為num2可能等於num1, 這樣在第二段更新時的參考值就會是錯的:

```py
for diff in range(mx+1):
    # abs(num1-num2) = diff
    # num2 = diff+num1 or num1-diff
    if (num2 := diff+num1) <= mx:
        dp[num1][diff] = max(dp[num1][diff], dp[num2][diff]+1)

    if (num2 := num1-diff) >= 0:
        dp[num1][diff] = max(dp[num1][diff], dp[num2][diff]+1)
```

由於上面是針對num1, num2兩點間的更新, 但別忘了我們對`diff`的定義
dp[num][diff]是指在結束於`num`且最終差值小於等於`diff`的最大長度

所以我們得在對dp[num1][diff]求max, 透過diff由大到小遍歷得出在小於等於`diff`時的最大長度

```py
for diff in range(mx-1, -1, -1):
    dp[num1][diff] = max(dp[num1][diff], dp[num1][diff+1])
```

那最終答案就是從所有可能裡面遍歷搜索即可, 可能停在任何一個`nums[i]`, 也可能是任何一個差值`diff`: `max(dp[num][diff] for num in nums for diff in range(mx+1))`