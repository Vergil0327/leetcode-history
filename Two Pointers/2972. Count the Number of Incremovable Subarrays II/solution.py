class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        r = n - 1
        while r > 0 and nums[r-1] < nums[r]:
            r -= 1
        if r == 0:
            return n * (n + 1) // 2
        
        L = prev = -1
        for l in range(n):
            if nums[l] > prev:
                L = l
                prev = nums[l]
            else:
                break

        # {XXXX}XXXX{XXXX}
        #  l  L      r
        ans = n - (r-1)
        for l in range(L+1):
            while r < n and nums[l] >= nums[r]:
                r += 1
            # 此時nums[l] < nums[r] => [l+1, r-1]為removable subarray
            ans += n - (r-1)
        return ans
