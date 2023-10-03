from sortedcontainers import SortedSet
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        presum = [[0]*n for _ in range(101)]
        for v in range(1, 101):
            for i in range(n):
                if nums[i] == v:
                    presum[v][i] = (presum[v][i-1] if i-1 >= 0 else 0) + 1
                else:
                    presum[v][i] = (presum[v][i-1] if i-1 >= 0 else 0)

        res = []
        for l, r in queries:
            ans = inf
            prev = -1
            for v in range(1, 101):
                intersect = presum[v][r] - (presum[v][l-1] if l-1 >= 0 else 0) > 0
                if intersect:
                    if prev > 0:
                        ans = min(ans, v-prev)
                    prev = v
            res.append(-1 if ans == inf else ans)
        return res
