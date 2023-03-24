class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        SUM = sum(nums)

        @lru_cache(None)
        def dfs(i, targetSum, size):
            if targetSum == 0 and size == 0: return True
            if targetSum < 0 or size == 0: return False
            if i == n: return False

            if dfs(i+1, targetSum, size): return True
            if dfs(i+1, targetSum - nums[i], size-1): return True
            return False

        for size in range(1, n):
            if size * SUM % n != 0: continue
            sumA = size * SUM // n
            if dfs(0, sumA, size): return True
        return False

class Solution_TLE:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        SUM = sum(nums)

        @lru_cache(None)
        def dfs(i, bitmask):
            if i == n:
                total = size = 0
                for i in range(32):
                    if (bitmask>>i)&1:
                        total += nums[i]
                        size += 1
                if size == 0 or size == n: return False
                return total/size == (SUM-total)/(n-size)

            if dfs(i+1, bitmask): return True
            if dfs(i+1, bitmask | (1<<i)): return True
            return False
        return dfs(0, 0)

class Solution_TLE:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        SUM = sum(nums)

        @lru_cache(None)
        def dfs(i, total, size):
            if i == n:
                if size == 0 or size == n: return False
                return total/size == (SUM-total)/(n-size)
            if dfs(i+1, total, size): return True
            if dfs(i+1, total+nums[i], size+1): return True
            return False
        return dfs(0, 0, 0)

# bottom-up
class Solution_TLE:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        SUM = sum(nums)
        
        dp = [[False] * n for _ in range(SUM+1)]
        prevdp = [[False] * n for _ in range(SUM+1)]

        prevdp[0][0]
        for num in nums:
            for sumA in range(num, SUM+1):
                for size in range(1, n-1):
                    # if sumA-num < 0: continue
                    if prevdp[sumA-num][size-1]:
                        dp[sumA][size] = 1
                        if sumA * n == SUM * size: return True
                    dp, prevdp = prevdp, dp
        return False
    
class Solution_TLE:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        SUM = sum(nums)
        
        dp = [[False] * (n+1) for _ in range(SUM+1)]
        dp[0][0] = 1

        currSum = 0
        for num in nums:
            currSum += num
            for sumA in range(currSum, num-1, -1):
                # for size in range(n-1, 0, -1):
                for size in range(n//2+1, 0, -1):
                    if dp[sumA-num][size-1]:
                        dp[sumA][size] = 1
                        if size!=n and sumA * n == SUM * size: return True
        return False
    
# bottom-up DP + bitmask
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return False
        SUM = sum(nums)
        if SUM == 0: return True
        
        # dp[sum]: considering sum, dp[sum] means binary representation of choosing state of the array make split successfully
        # dp[sum]: 101 -> 用bitmask來代表 dp[sum][size] -> dp[sum][0] = True, dp[sum][1] = False, dp[sum][2] = True
        # 代表可以透過取0個跟取2個數來使得A sbuset的和為sum, 透過bitmask把上面bottom-up TLE解法進一步改良
        dp = [0] * (SUM+1)
        dp[0] = 1

        currSum = 0
        for num in nums:
            currSum += num
            for total in range(currSum, num-1, -1):
                dp[total] |= (dp[total-num]<<1)

                if total * n % SUM == 0:
                    size = total * n // SUM
                    if size != 0 and size != n and dp[total]&(1<<size): return True
        return False