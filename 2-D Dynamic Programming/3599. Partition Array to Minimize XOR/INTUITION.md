# Intuition

直覺想到把整個做法用top-down dp (DFS + memorization)模擬出來
每段subarray要盡可能找出最大XOR值
然後在所有合法結果中, 找出minimum XOR

```py
class Solution:
    def minXor(self, nums: List[int], K: int) -> int:
        n = len(nums)

        memo = [[inf]*(K+1) for _ in range(n+1)]
        def dfs(i, k):
            if memo[i][k] < inf: return memo[i][k]

            if i >= n:
                return inf if k != 0 else 0
            if k <= 0: return inf

            xor = 0
            for j in range(i, n):
                xor ^= nums[j]
                memo[i][k] = min(memo[i][k], max(xor, dfs(j+1, k-1)))
            return memo[i][k]
        
        return dfs(0, K)
```

可惜這樣會TLE

這邊些能優化的地方, 不加上這些會TLE:

1. 首先是我們可以預處理prefix XOR, 那這樣我們要的XOR(nums[i:j]) = prexor[j+1] XOR prexor[i] where prexor is 1-indexed and both i, j are inclusive for nums[i:j]
2. base condition:
    - if k == 1: return prexor[n]^prexor[i]: 不需要再往後嘗試dfs

3. 將@cache 轉成2-d array
4. (最重要!!!)遍歷的範圍改成`for j in range(i, n-k+1):`, 因為要準確分成k個subarray, 所以扣除當前subarray後面必須至少預留`k-1`個item