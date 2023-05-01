class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(set(nums))
        arr.sort()
        
        res = inf
        for i, num in enumerate(arr):
            target = num+(n-1)
            j = bisect.bisect_right(arr, target)
            res = min(res, n-(j-i))
        return res

        # X X X X X X [X X X]
        # i            j