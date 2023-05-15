from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        m, n = len(slots1), len(slots2)
        slots1.sort()
        slots2.sort()
        
        res = []
        i = j = 0
        while i < m and j < n:
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]

            l, r = max(start1, start2), min(end1, end2)
            if r-l >= duration:
                return [l, l+duration]
        
            if end1 < end2:
                i += 1
            else:
                j += 1
        return res
