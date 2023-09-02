class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        res = l = r = 0
        window = defaultdict(int)
        windowSum = 0
        while r < n:
            window[nums[r]] += 1
            windowSum += nums[r]
            r += 1
        
            while l < r and r-l > k:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                windowSum -= nums[l]
                l += 1

            if r-l == k and len(window) >= m:
                res = max(res, windowSum)
        return res