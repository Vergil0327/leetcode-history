class SolutionPrefixSum:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            prefixSum[i] = prefixSum[i-1]+nums[i-1]

        maxSum = 0
        
        window = defaultdict(lambda: 0)
        
        l, r = 0, 0
        while r < len(nums):
            num = nums[r]
            r += 1
            
            window[num] += 1
            
            while r-l >= k:
                if len(window) == k:
                    maxSum = max(maxSum, prefixSum[r]-prefixSum[l])
                num = nums[l]
                l += 1
                
                window[num] -= 1
                if window[num] == 0:
                    del window[num]
        
        return maxSum

# we don't really need prefixSum
# we can use a varaible to store current window sum
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        windowSum = 0
        
        window = defaultdict(lambda: 0)
        
        l, r = 0, 0
        while r < len(nums):
            num = nums[r]
            windowSum += num
            r += 1
            
            window[num] += 1
            
            while r-l >= k:
                if len(window) == k:
                    maxSum = max(maxSum, windowSum)
                num = nums[l]
                windowSum -= num
                l += 1
                
                window[num] -= 1
                if window[num] == 0:
                    del window[num]
        
        return maxSum