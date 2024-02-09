"""
key points:
- we don't need to check if every num in our valid solutions can be divided by current num
  -> divisibility is transitive
- we only need to check if num is valid or not by this line: if nums[i] % nums[j] == 0:
- store our update path in prev array
"""

class SolutionBottomUp:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        dp = [1]*N
        prev = [-1 for _ in range(N)]

        nums.sort()
        for i in range(N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] == dp[j]+1:
                        prev[i] = j

        largest = max(dp)
        for i, ptr in enumerate(prev):
            if dp[i] == largest:
                res = [nums[i]]
                
                while ptr != -1:
                    res.append(nums[ptr])
                    ptr = prev[ptr]
                
                return res

# https://leetcode.com/problems/largest-divisible-subset/discuss/1259966/Python-3-Graph-dfs-with-memo-O(E%2BV)-time-and-O(max(E-V))-space
class SolutionDFS:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        
        graph = defaultdict(set) # all integers in nums are unique
        for i in range(n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    graph[nums[i]].add(nums[j])
        
        memo = {}
        def dfs(num):
            if num in memo:
                return memo[num]

            if not graph[num]:
                memo[num] = [num]
                return [num]
            else:
                largest = max([dfs(nxt) for nxt in graph[num]], key=len)
                memo[num] = [num] + largest
                return memo[num]
            
        res = max([dfs(num) for num in nums], key=len)
        return res

# https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python
# Amazing Solution
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        DP = {-1: set()} # -1: set as base case
        for num in sorted(nums):
            DP[num] = max((DP[i] for i in DP if num % i == 0), key=len) | {num}
        return max(DP.values(), key=len)
    
# dp[nums[i]]: 最大數為nums[i], %nums[i]為0的set
# 狀態轉移:往前找個nums[j]如果nums[i]%nums[j] == 0, 那麼dp[nums[j]]裡的每個數也都滿足
# 所以我們就能更新dp[nums[i]]
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)
        dp = [set([nums[i]]) for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]|{nums[i]}, key=len)

        return max(dp, key=len)