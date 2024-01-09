# follow-up of 300. Longest Increasing Subsequence
# => it's like 2-Dimension LIS

import bisect
import functools
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # tricks here! sort envelopes width in increasing order, then height in decreasing order
        # after that, we can get rid of width because heights will always be valid to find LIS greedily
        heights = [h for w,h in sorted(envelopes, key=lambda x: (x[0], -x[1]))] 
        sequence = self.findLIS(heights)
        return len(sequence)
    
    def findLIS(self, nums: List[int]) -> int:
        tails = []
        
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return tails

# O(n^2)
# sort envelopes by width, what we want is longest increasing subsequence of height
class SolutionTLE:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()

        n = len(envelopes)
        dp = [1] * n

        for i in range(n):
            for j in range(0, i):
                # both width & height are must strictly smaller
                # even though we already sort envelopes by width, we still need to check width,
                # because width can be duplicate. ex. [[4, 3], [4, 5]]
                # we don't want to pick [4,5] after [4, 3]
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# O(n^2)
class SolutionTLE:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(i, envelop):
            w, h = envelop

            if i == n:
                return 0
            
            num = dfs(i+1, envelop)
            if envelopes[i][0] > w and envelopes[i][1] > h:
                num = max(num, dfs(i+1, (envelopes[i][0], envelopes[i][1])) + 1)
            return num
        
        inf = float("inf")
        return dfs(0, (-inf, -inf))