from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def check(guess):
            cnt = 0
            curr = 0
            for sweet in sweetness:
                curr += sweet
                if curr >= guess:
                    curr = 0
                    cnt += 1
            return cnt >= (K+1)

        l, r = min(sweetness), sum(sweetness)
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l
