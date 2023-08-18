class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def lcm(a, b):
            return a*b//gcd(a,b)

        res = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            if gcd(res[-1], nums[i]) == 1:
                res.append(nums[i])
            else:
                res[-1] = lcm(res[-1], nums[i])
        
        nums = res
        res = [nums[-1]]
        n = len(nums)

        allCoprime = True
        for i in range(n-2, -1, -1):
            if gcd(res[-1], nums[i]) == 1:
                res.append(nums[i])
            else:
                allCoprime = False
                res[-1] = lcm(res[-1], nums[i])

        res.reverse()
        
        if allCoprime: return res
        return self.replaceNonCoprimes(res)