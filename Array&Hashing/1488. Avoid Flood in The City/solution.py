from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        dryDay = SortedList()
        rainDay = defaultdict(lambda: -1)
        res = [-1] * n
        for i in range(n):
            if rains[i] == 0:
                dryDay.add(i)
            else:
                if rainDay[rains[i]] == -1: # let it rain
                    rainDay[rains[i]] = i
                else: # must dry before rain
                    idx = dryDay.bisect_right(rainDay[rains[i]])
                    if idx == len(dryDay): return []

                    res[dryDay[idx]] = rains[i]
                    dryDay.pop(idx)
                    rainDay[rains[i]] = i

        while dryDay:
            idx = dryDay.pop()
            res[idx] = 1
        return res
