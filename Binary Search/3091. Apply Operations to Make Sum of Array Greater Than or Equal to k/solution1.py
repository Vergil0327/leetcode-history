class Solution:
    def minOperations(self, k: int) -> int:
        def check(mid):
            for i in range(mid+1):
                if (1+i) * (mid-i+1) >= k: return True
            return False
                
        l, r = 0, k
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l
