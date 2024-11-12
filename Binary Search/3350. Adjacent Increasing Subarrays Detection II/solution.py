class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        max_length = [0] * (n+1)
        for i in range(n):
            if nums[i] > nums[i-1]:
                max_length[i+1] = max_length[i] + 1
            else:
                max_length[i+1] = 1

        def check(k):
            for i in range(1, n+1):
                if i-k >= 0 and max_length[i] >= k and max_length[i-k] >= k:
                    return True
            return False
        
        l, r = 1, n//2
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l