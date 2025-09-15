class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = []
        for x in nums:
            for b in basis:
                x = min(x, x^b)
            if x > 0:
                basis.append(x)
        
        res = 0
        basis.sort(reverse=True)
        for b in basis:
            res = max(res, res^b)

        return res