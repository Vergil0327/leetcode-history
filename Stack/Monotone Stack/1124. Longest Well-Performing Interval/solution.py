class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        presum = [0]
        for h in hours:
            if h > 8:
                presum.append(presum[-1]+1)
            else:
                presum.append(presum[-1]-1)
        
        monostack = []
        for i in range(n):
            if not monostack or presum[i] < presum[monostack[-1]]:
                monostack.append(i)

        res = 0
        for i in range(n, -1, -1): # presum.size == n+1
            while monostack and presum[monostack[-1]] < presum[i]:
                res = max(res, i-monostack.pop())
        return res
