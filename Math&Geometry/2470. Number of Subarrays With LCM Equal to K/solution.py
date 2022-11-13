from typing import List

# LCM only grow larger when subarray's size grow bigger
class Solution:
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a%b
        return a

    def lcm(self, a, b):
        gcd = self.gcd(a, b)
        # return (a//gcd ) * (b//gcd) * gcd
        return (a*b)//gcd

    # O(n^2)
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        count = 0
        for i in range(n):
            num = nums[i]
            lcm = num
            for j in range(i, n):
                lcm = self.lcm(lcm, nums[j])
                if lcm == k:
                    count += 1
                elif lcm > k:
                    break
        return count
        

# Optimized Solution: https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/discuss/2808843/O(n-d(k))
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        lcmMap = defaultdict(lambda: 0) # store previous subarray's LCM
        for num in nums:
            lcmMap[num] += 1
            
            tmp = defaultdict(lambda: 0)
            for prevLcm, cnt in lcmMap.items():
                lcm = self.lcm(num, prevLcm)
                
                if lcm == k: res += cnt
                tmp[lcm] += cnt
            lcmMap, tmp = tmp, lcmMap
        return res
    
    def subarrayLCM_Optimized(self, nums: List[int], k: int) -> int:
        res = 0
        lcmMap = defaultdict(lambda: 0)
        for num in nums:
            lcmMap[num] += 1
            
            tmp = defaultdict(lambda: 0)
            for prevLcm, cnt in lcmMap.items():
                lcm = self.lcm(num, prevLcm)
                
                if lcm == k: res += cnt
                if k%lcm == 0: # we can do even better by filtering
                    tmp[lcm] += cnt
            lcmMap, tmp = tmp, lcmMap
        return res

    def gcd(self, a, b):
        while b > 0:
            a, b = b, a%b
        return a
    def lcm(self, a, b):
        gcd = self.gcd(a, b)
        # return (a//gcd ) * (b//gcd) * gcd
        return (a*b)//gcd
