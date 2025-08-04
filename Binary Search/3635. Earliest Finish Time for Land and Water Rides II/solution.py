from math import inf
from bisect import bisect_right
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        arr1 = list(zip(landStartTime, landDuration))
        arr2 = list(zip(waterStartTime, waterDuration))
        arr1.sort()
        arr2.sort()

        def findEarliest(arr1, arr2):
            n = len(arr2)
            suf_min_finish = [inf] * (n+1)
            for i in range(n-1, -1, -1):
                suf_min_finish[i] = min(suf_min_finish[i+1], sum(arr2[i]))

            pre_min_duration = [inf] * n
            pre_min_duration[0] = arr2[0][1]
            for i in range(1, n):
                pre_min_duration[i] = min(pre_min_duration[i-1], arr2[i][1])

            res = float('inf')
            for t1, dur1 in arr1:
                j = bisect_right(arr2, t1+dur1, key=lambda x: x[0])
                res = min(res, suf_min_finish[j])
                if j-1 >= 0:
                    res = min(res, t1+dur1 + pre_min_duration[j-1])
                    
            return res
        
        return min(findEarliest(arr1, arr2), findEarliest(arr2, arr1))
        