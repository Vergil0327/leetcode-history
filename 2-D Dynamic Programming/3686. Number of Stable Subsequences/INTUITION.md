# Intuition

題意能很直覺想到top-down dp
time, space都是O(n * 2 * 2)
```py
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        @lru_cache(None)
        def dfs(i, p1, p2):
            if i >= n:
                if p1 != -1 or p2 != -1:
                    return 1
                return 0
            res = dfs(i+1, p1, p2)

            p = nums[i]%2
            if not (p1 == p2 == p):
                res += dfs(i+1, p2, p)
            return res%mod
        dfs.cache_clear()
        return dfs(0, -1, -1)
```

但可惜會MLE (memory limit exceeded)

常見優化方式就是利用一個memo list去記憶而非使用decorator

```py
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        memo = [[[0] * 3 for _ in range(3)] for _ in range(n+1)]
        def dfs(i, p1, p2):
            if i >= n:
                if p1 != 2 or p2 != 2:
                    return 1
                return 0
            if memo[i][p1][p2] != 0: return memo[i][p1][p2]
            
            memo[i][p1][p2] = dfs(i+1, p1, p2)

            p = nums[i]%2
            if not (p1 == p2 == p):
                memo[i][p1][p2] += dfs(i+1, p2, p)
            return memo[i][p1][p2]%mod

        return dfs(0, 2, 2)
```

如此一來就過了

# Space-Optimized

但這題有個更好的空間優化方式是:

我們定義兩個dp list: `numEven`跟`numOdd`

numEven[x]: 到目前為止的方法數, 其中結尾含有x個連續even number
numOdd[x]: 到目前為止的方法數, 其中結尾含有x個連續odd number

那這樣狀態轉移就是分情況討論:

1. nums[i] % 2 == 0:
   - 取用偶數nums[i]:
   - numEven[2] += numEven[1]
   - numEven[1] += 1 + numOdd[1] + numOdd[2]
     - 1代表[nums[i]], new numEven subseq starting with nums[i]
2. nums[i] % 2 == 1:
   - 取用奇數nums[i]:
   - numOdd[2] += numOdd[1]
   - numOdd[1] += 1 + numEven[1] + numEven[2]
     - 1代表[nums[i]], new numOdd subseq starting with nums[i]

```py
class Solution:
    def threeConsecutive(self, nums: List[int]) -> int:
        mod = 1000000007
        numEven = [0] * 3
        numOdd = [0] * 3

        for num in nums:
            numCur = numEven if num % 2 == 0 else numOdd
            numOpp = numOdd if num % 2 == 0 else numEven

            numCur[2] += numCur[1]
            numCur[1] += 1 + numOpp[1] + numOpp[2]

            numCur[1] %= mod
            numCur[2] %= mod

        return (numEven[1] + numEven[2] + numOdd[1] + numOdd[2]) % mod
```
