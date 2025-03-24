from math import log, floor

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            start = floor(log(l, 4))+1
            end = floor(log(r, 4))+1
            ops = 0
            for i in range(start-1, end+1):
                interval = [max(l, pow(4, i)), min(r, pow(4, i+1)-1)]
                ops += max(0, (i+1) * (interval[1]-interval[0]+1))
            res += ceil(ops/2)
        return res
