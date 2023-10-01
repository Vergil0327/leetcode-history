class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        minAND = nums[0]
        for i in range(1, n):
            minAND &= nums[i]
    
        def check(mid):
            target = minAND/mid
            
            cur = nums[0]
            cnt = 0
            for i in range(n):
                cur &= nums[i]
                if cur <= target:
                    cnt += 1
                    if i+1 < n:
                        cur = nums[i+1]
            return cnt >= mid
        
        l, r = 1, n
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l
