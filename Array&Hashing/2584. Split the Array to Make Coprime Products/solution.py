class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        def getFactors(num):
            res = []
            for f in range(2, int(sqrt(num))+1):
                if num%f == 0:
                    res.append(f)
                    while num%f == 0:
                        num //= f
            if num > 1:
                res.append(num)
            return res

        right = defaultdict(int)
        factors = []
        for num in nums:
            facs = getFactors(num)
            for fac in facs:
                right[fac] += 1
            factors.append(facs)

        left = defaultdict(int)
        for i in range(n-1): # check split at i
            for fac in factors[i]:
                left[fac] += 1

                right[fac] -= 1
                if right[fac] == 0: # doesn't share fac in both left and right anymore
                    del left[fac]
                    if len(left) == 0:
                        return i
        return -1
