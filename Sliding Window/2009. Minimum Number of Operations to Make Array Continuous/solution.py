class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(set(nums))
        arr.sort()

        res = inf
        l = r = 0
        windowLen = 0
        while r < len(arr):
            num = arr[r]
            windowLen += 1
            r += 1
            while l < r and num > arr[l]+(n-1):
                windowLen -= 1
                l += 1
            res = min(res, n-(r-l))
        return res