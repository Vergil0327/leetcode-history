class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        oneIndices = [i for i, v in enumerate(nums) if v == 1]
        n = len(oneIndices)
        if n == 0: return k*2

        presum = list(accumulate(oneIndices))
        def calPresum(left, right):
            if left > right: return 0
            return presum[right] - (presum[left - 1] if left-1 >= 0 else 0)

        def calDist(l, r):
            dylanIdx = (l+r)//2
            return calPresum(dylanIdx+1, r) - calPresum(l, dylanIdx-1) + (dylanIdx-l-r+dylanIdx) * oneIndices[dylanIdx]
        
        mx = max(1, k-maxChanges)
        res = inf
        for m in range(mx, min(n, k, mx+3)+1):
            for l in range(n-m+1):
                r = l+m-1

                steps = (k-m)*2 # choose m points for operation2, (k-m) for operation1
                steps += calDist(l, r)
                res = min(res, steps)
        return res
