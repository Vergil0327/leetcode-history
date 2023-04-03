# O(2n)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        n = len(nums)
        res = flips = ones = 0
        while r < n:
            if nums[r] == 0:
                flips += 1
                ones += 1
            else:
                ones += 1
            r += 1

            while l < r and flips > k:
                if nums[l] == 0:
                    flips -= 1
                    ones -= 1
                else:
                    ones -= 1
                l += 1
            res = max(res, ones)
        return res
    

# O(n)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # if we encounter a 0 the we decrement K
            if nums[right] == 0:
                k -= 1
                
            # if K < 0 then we need to move the left part of the window forward
            # to try and remove the extra 0's
            if k < 0:
                 # if the left one was zero then we adjust K
                if nums[left] == 0:
                    k += 1

                # regardless of whether we had a 1 or a 0 we can move left side by 1
                # if we keep seeing 1's the window still keeps moving as-is
                left += 1
                
        return right - left + 1