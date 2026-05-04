from bisect import bisect_right

class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        # candidates store (v, d) where v = nums[i] and d = i - nums[i]
        candidates = []
        for i, v in enumerate(nums):
            if i >= v:
                candidates.append((v, i - v))
        
        # Sort ascending by v.
        # Tie-breaker: descending by d (i - v) to prevent picking identical v's
        candidates.sort(key=lambda x: (x[0], -x[1]))
        
        # Find Longest Non-Decreasing Subsequence on the 'd' values
        lis = []
        for _, d in candidates:
            # For a non-decreasing subsequence, use bisect_right
            idx = bisect_right(lis, d)
            if idx == len(lis):
                lis.append(d)
            else:
                lis[idx] = d
                
        return len(lis)