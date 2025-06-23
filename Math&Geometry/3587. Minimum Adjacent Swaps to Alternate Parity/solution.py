class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        even = []
        odd = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        if abs(len(even) - len(odd)) > 1:
            return -1

        # swaps for allocating indices[i] to even index position
        def count(indices):
            swaps = j = 0
            for i in range(0, n, 2):
                swaps += abs(indices[j] - i)
                j += 1
            return swaps
        
        res = float('inf')
        if len(even) >= len(odd):
            res = min(res, count(even))
        if len(odd) >= len(even):
            res = min(res, count(odd))

        return res
