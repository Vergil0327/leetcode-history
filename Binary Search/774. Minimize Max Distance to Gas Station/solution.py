from math import ceil
from typing import List

class Solution:
     def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def OK(D):
            k = 0
            for i in range(len(stations)-1):
                k += ceil(abs(stations[i]-stations[i+1])/D)-1

            return k <= K

        l, r = 0, 0
        for i in range(len(stations)-1):
            r = max(r, abs(stations[i]-stations[i+1]))

        while r-l < 1e-6: # Answers within 10^-6 of the true value will be accepted as correct.
            mid = l + (r-l)/2
            if OK(mid):
                r = mid
            else:
                l = mid
        return l