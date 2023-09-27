from sortedcontainers import SortedList
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        presum = list(itertools.accumulate(nums))

        sl = SortedList([(0, n-1, presum[n-1])]) # [l, r, -segment_sum of nums[l:r]]
        sortedSum = SortedList([presum[n-1]])

        res = [0] * n
        for i, idx in enumerate(removeQueries):
            j = sl.bisect_right((idx, inf, inf))-1

            # break segment up into two small segments
            l, r, tot = sl.pop(j)
            sortedSum.remove(tot)
            
            ## break
            tot -= nums[idx]
            rightSum = presum[r]-presum[idx]
            leftSum = tot-rightSum
            sl.add((l, idx-1, leftSum))
            sl.add((idx+1, r, rightSum))

            ## find max segment sum
            sortedSum.add(leftSum)
            sortedSum.add(rightSum)
            res[i] = sortedSum[-1]

        return res


class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        n = len(nums)
        
        parent = list(range(n))
        result = [0 for _ in range(n)]
        rank = [0 for _ in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)

            if px <= py:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]

        for i in range(n-1, -1, -1):
            idx = removeQueries[i]
            rank[idx] = nums[idx]

            if idx > 0 and rank[idx-1] > 0:
                union(idx-1, idx)

            if idx < n-1 and rank[idx+1] > 0:
                union(idx, idx+1)

            if i > 0:
                result[i-1] = max(result[i], rank[find(idx)])

        return result