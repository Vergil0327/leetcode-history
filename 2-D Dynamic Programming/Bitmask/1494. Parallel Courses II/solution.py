class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        indeg = [0] * n
        for u, v in relations:
            u, v = u-1, v-1 # to 0-indexed
            graph[u].append(v)
            indeg[v] += 1
        
        @cache
        def dfs(state, indeg):
            if not state: return 0

            available = []
            for i in range(n):
                if (state>>i)&1 and indeg[i] == 0:
                    available.append(i)

            res = inf
            for kPicks in itertools.combinations(available, min(k, len(available))):
                nxtState, nxtIndeg = state, list(indeg)

                for course in kPicks:
                    nxtState ^= (1<<course)

                    for nei in graph[course]:
                        nxtIndeg[nei] -= 1
            
                res = min(res, dfs(nxtState, tuple(nxtIndeg))+1)
            return res

        return dfs((1<<n)-1, tuple(indeg))
