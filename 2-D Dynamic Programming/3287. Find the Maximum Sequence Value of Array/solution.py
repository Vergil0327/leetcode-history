class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def dfsL(i, size):
            if i < 0:
                return set([0]) if size == 0 else set()

            res = set()
            x = dfsL(i-1, size)
            y = dfsL(i-1, size-1)
            for seg in y:
                res.add(seg|nums[i])
            return res | x

        @cache
        def dfsR(i, size):
            if i >= n:
                return set([0]) if size == 0 else set()

            res = set()
            x = dfsR(i+1, size)
            y = dfsR(i+1, size-1)
            for seg in y:
                res.add(seg|nums[i])
            return res | x

        res = 0
        for split in range(k, n-k+1):
            left = dfsL(split-1, k)
            right = dfsR(split, k)

            for x in left:
                for y in right:
                    res = max(res, x^y)
        return res
