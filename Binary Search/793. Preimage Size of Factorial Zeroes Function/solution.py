class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailingZeros(n):
            count = 0
            while n // 5 > 0:
                count += n // 5
                n //= 5
            return count

        # bisect_right
        l, r = 0, 2**32
        while l < r:
            mid = l + (r-l)//2
            if trailingZeros(mid) > k:
                r = mid
            else:
                l = mid+1
        right = l

        # bisect_left
        l, r = 0, 2**32
        while l < r:
            mid = l + (r-l)//2
            if trailingZeros(mid) < k:
                l = mid+1
            else:
                r = mid
        left = l
        
        return right-left
