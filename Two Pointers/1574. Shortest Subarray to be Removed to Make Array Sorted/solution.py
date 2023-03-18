class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1
        
        while l+1 < n and arr[l] <= arr[l+1]:
            l += 1

        while r-1 >= 0 and arr[r] >= arr[r-1]:
            r -= 1
        
        res = min(n-l-1, r) # remove arr[l+1:] or arr[:r]
        if l > r: return res
        
        for i in range(0, l+1):
            while r < n and arr[r] < arr[i]:
                r += 1
            res = min(res, max(0, r-i-1))

        return res
# [1,2,3,10], 4 ,[2,3,5]
#         l       r
# arr[:l] non-decreasing
# arr[r:] non-decreasing
# arr[l] <= arr[r]