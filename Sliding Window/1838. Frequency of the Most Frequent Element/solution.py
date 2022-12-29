# Sorting + PrefixSum
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        l, r = 0, 0
        maxFreq = 0
        while r < n:
            num = nums[r]
            r += 1

            while num*(r-l) - (presum[r]-presum[l]) > k:
                l += 1
            
            maxFreq = max(maxFreq, r-l)
        return maxFreq

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        # XXXXX {mid XXXX index}
        def check(index):
            l, r = 0, index
            while l < r:
                mid = l + (r-l)//2
                if presum[index+1] - presum[mid] + k < (index-mid+1) * nums[index]:
                    l = mid+1
                else:
                    r = mid
            return index-l+1

        res = 0
        for i in range(n):
            res = max(res, check(i))
        return res