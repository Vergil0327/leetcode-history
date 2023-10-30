from typing import List
from math import inf

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        mod = 10**9 + 7

        packages.sort()

        res = inf
        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]: continue # doesn't fit

            l = boxSize = 0
            for size in box:
                r = bisect.bisect_right(packages, size)
                boxSize = (boxSize + size * (r-l))
                l = r
            res = min(res, boxSize)
        
        return -1 if res == inf else (res - sum(packages))%mod
