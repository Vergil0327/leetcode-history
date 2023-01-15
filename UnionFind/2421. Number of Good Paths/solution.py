class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        # Union-Find
        parent = list(range(n))
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for edge in edges:
            edge.sort(key=lambda x:vals[x])
        edges.sort(key=lambda x:(vals[x[1]]))

        res = 0
        counter = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            count = defaultdict(int)
            count[vals[i]] = 1
            counter[i] = count

        for u, v in edges:
            pu, pv = find(u), find(v)
            # choose node with larger value in edge which is vals[v]
            res += counter[pu][vals[v]] * counter[pv][vals[v]]
            
            if pu > pv:
                parent[pv] = pu
                counter[pu][vals[v]] += counter[pv][vals[v]]
            else:
                parent[pu] = pv
                counter[pv][vals[v]] += counter[pu][vals[v]]

        return res + n

        # [5,1,4,2,1,5,4,3]
        # [[1,0],[2,0],[3,2],[4,2],[5,4],[6,4],[6,7]]
        # 7(3)-6(4)-4(1)-2(4)-3(2)
        #      |          |
        #      5(5)       |
        #                 |
        #            1(1)-0(5)