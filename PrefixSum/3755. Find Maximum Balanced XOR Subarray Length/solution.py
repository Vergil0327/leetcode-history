from itertools import accumulate


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        preXor = list(accumulate(nums, lambda x, y: x^ y, initial=0))
        preOdd = [0]
        for num in nums:
            preOdd.append(preOdd[-1] + int(num%2 == 1))

        seen = {(0, 0): -1}
        res = 0
        for i in range(n):

            odd = preOdd[i+1]
            even = i+1 - odd
            xor = preXor[i+1]

            key = (xor, odd-even)
            if key in seen:
                res = max(res, i - seen[key])
            if key not in seen:
                seen[key] = i
        return res