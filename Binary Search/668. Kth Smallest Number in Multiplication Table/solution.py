class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(num):
            r, c = m, 1
            count = 0
            while r > 0 and c <= n:
                if r * c <= num:
                    count += r
                    c += 1
                else:
                    r -= 1
            return count

        
        l, r = 1, m * n
        while l < r:
            mid = l + (r-l)//2
            if count(mid) < k:
                l = mid+1
            else:
                r = mid
        return l