from collections import defaultdict


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False

            if rank[px] >= rank[py]:
                rank[px] += rank[py]
                parent[py] = px
            else:
                rank[py] += rank[px]
                parent[px] = py
            return True
        
        for x, y in swaps:
            union(x, y)

        connected = defaultdict(list)
        for i in range(n):
            connected[find(i)].append([i, nums[i]]) # [position, value]

        def calculate(arr: list):
            """
            Why this formula?
            Let's say we have values [v1, v2, v3, v4, v5] and E = 2 even positions.

            - sumAll = v1 + v2 + v3 + v4 + v5 (total of all values)
            - sumTopE = v5 + v4 (sum of 2 largest values)

            If we put the top E values on even positions:

            ```
            Contribution = (v5 + v4) - (v3 + v2 + v1)
                        = (v5 + v4) - (sumAll - v5 - v4)
                        = (v5 + v4) - sumAll + (v5 + v4)
                        = 2 * sumTopE - sumAll
            ```
            """
            sumAll = 0
            E = len(list(filter(lambda x: x[0]%2 == 0, arr))) # even position
            arr.sort(key=lambda x:x[1], reverse=True)
            
            sumTopE = 0
            for idx, val in arr:
                if E > 0:
                    E -= 1
                    sumTopE += val
                sumAll += val

            return 2 * sumTopE - sumAll

        res = 0
        for component in connected.values():
            res += calculate(component)
        return res
            
