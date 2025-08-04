# Intuition

### Brute force

```py
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        arr1 = list(zip(landStartTime, landDuration))
        arr2 = list(zip(waterStartTime, waterDuration))

        def findEarliest(arr1, arr2):
            res = float('inf')
            for t1, dur1 in arr1:
                for t2, dur2 in arr2:
                    if t2 > t1+dur1:
                        res = min(res, t2+dur2) # t1 -> duration1 -> wait -> t2 -> duration2
                    else:
                        res = min(res, t1+dur1+dur2) # t1 -> duration -> (t2 already opened) -> duration2
            return res
        
        return min(findEarliest(arr1, arr2), findEarliest(arr2, arr1))
```

要優化也很簡單, 明顯可看出遍歷過程中, 重點是找出對於arr1[i]來說, 能滿足`t2 > t1+dur1`的這個分界點在哪
然後只要預先處理prefix_min, suffix_min後, 即可透過binary search找出該分界點`j`後
透過prefix_min[j-1], suffix_min[j]來更新res即可

```py

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
                # for t2, dur2 in arr2:
                #     if t2 > t1+dur1:
                #         res = min(res, t2+dur2) # t1 -> duration1 -> wait -> t2 -> duration2
                #     else:
                #         res = min(res, t1+dur1+dur2) # t1 -> duration -> (t2 already opened) -> duration2

                j = bisect_right(arr2, t1+dur1, key=lambda x: x[0]) # first position to satisfied t2 > t1+dur1
                res = min(res, suf_min_finish[j]) # if t2 > t1+dur1
                res = min(res, t1+dur1 + pre_min_duration[j-1]) # else
                    
            return res
        
        return min(findEarliest(arr1, arr2), findEarliest(arr2, arr1))
        
```