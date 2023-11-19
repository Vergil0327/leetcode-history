class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)

        # arr[i] = [r, l, original index]
        arr = [[max(queries[i][0], queries[i][1]), min(queries[i][0], queries[i][1]), i] for i in range(n)]
        arr.sort(reverse=True)

        res = [-1]*(len(queries))
        j = len(heights)-1
        monostack = deque()

        for r, l, idx in arr:
            while j > r:
                while monostack and monostack[0][0] <= heights[j]:
                    monostack.popleft()
                monostack.appendleft([heights[j], j])

                j -= 1

            if l == r or heights[r] > heights[l]:
                res[idx] = r
            else:
                index = bisect_right(monostack, heights[l], key=lambda x:x[0])
                if index < len(monostack):
                    res[idx] = monostack[index][1]
        return res
