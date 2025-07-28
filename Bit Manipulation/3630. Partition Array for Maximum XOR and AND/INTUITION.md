# Intuition


max AND: single element. AND的特性會導致AND越多數值越小
XOR(nums) = XOR(A) XOR XOR(B)

首先想到brute force, 遍歷所有可能AND state, 然後剩餘未選的數再去用dfs找出max XOR
但可惜這樣會MLE (memory limit exceeded)

```py
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        @cache
        def dfs(i, visited, curr):
            if i >= n:
                return curr + (self.total_xor^curr)
            if (visited>>i)&1: return dfs(i+1, visited, curr)
            return max(
                dfs(i+1, visited, curr),
                dfs(i+1, visited, curr^nums[i]),
            )

        n = len(nums)
        state = (1<<n) - 1
        submask = state
        res = 0
        while submask > 0:
            val_and = -1
            self.total_xor = 0
            for i in range(n):
                if (submask>>i)&1:
                    if val_and == -1:
                        val_and = nums[i]
                    else:
                        val_and &= nums[i]
                else:
                    self.total_xor ^= nums[i]

            res = max(res, dfs(0, submask, self.total_xor) + val_and)
            submask = (submask-1)&state

        return res
```

代表不能用dfs + memorization

但後續就真想不到, linear basis覺得實在太難
解答難以理解, 僅供參考(利用到**Gaussian elimination over GF(2) (linear basis)**)