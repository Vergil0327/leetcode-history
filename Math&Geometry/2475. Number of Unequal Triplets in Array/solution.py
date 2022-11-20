# Optimzed O(n)
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/discuss/2831702/O(n)
# intuition

# Lets say we have 4 kinds of numbers in m, denote them as a, b, c, d, and their frequency m[a], m[b], m[c], m[d]
# What we want to find is
# m[a] * m[b] * m[c]
# m[a] * m[b] * m[d]
# m[a] * m[c] * m[d]
# m[b] * m[c] * m[d]
# Actually, there are nC3 kinds of combinations we have to consider.
# If you look closer, the above combinations can be reduce as

#        left             cnt           right
# (0)                   * m[a] * (m[b] + m[c] + m[d])
# (m[a])                * m[b] * (m[c] + m[d])
# (m[a] + m[b])         * m[c] * (m[d])
# (m[a] + m[b] + m[c])  * m[d] * (0)
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = left = 0
        right = len(nums)
        
        for v, cnt in counter.items():
            right -= cnt
            res += left * cnt * right
            left += cnt
        return res

# Brute Force
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        cnt += 1
                    
        return cnt