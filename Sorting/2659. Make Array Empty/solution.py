class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        arr = []
        for i, num in enumerate(nums):
            arr.append((num, i))
        arr.sort()

        n = len(nums)
        res = n # n remove operation

        prevIdx = 0
        for i, (num, j) in enumerate(arr):
            if j < prevIdx: # rotate
                res += n-i # rotate distance
            prevIdx = j
            
        return res
