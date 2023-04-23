class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        GCD = gcd(nums[0], nums[1])
        for i in range(1, n-1):
            GCD = gcd(GCD, gcd(nums[i], nums[i+1]))
        if GCD > 1: return -1
        
        if 1 in set(nums):
            return len([num for num in nums if num != 1])
        
        l, r = n, 2**32
        
        def check(mid):
            found = False
            res = -1
            for length in range(2, mid+1):
                for i in range(n-length+1):
                    j = i+length-1
                    GCD = nums[i]
                    for k in range(i, j+1):
                        GCD = gcd(GCD, nums[k])
                        if GCD == 1:
                            found = True
                            break
                    if found:
                        res = 2*length-2 + i + (n-1-j)
                        break
                if found:
                    break
            return res <= mid
                    
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l

# Optimized
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        counter = Counter(nums)
        if counter[1] > 0: return n-counter[1]

        res = inf
        for l in range(n):
            GCD = nums[l]
            for r in range(l+1, n):
                GCD = gcd(GCD, nums[r])
                if GCD == 1:
                    res = min(res, r-l+(n-1))
        return res if res != inf else -1