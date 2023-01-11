# DFS
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        canSkip = set()
        def dfs(node, parent):
            pathHasApple = hasApple[node]

            for nei in G[node]:
                if parent == nei: continue
                childHasApple = dfs(nei, node)
                pathHasApple = pathHasApple or childHasApple

            if not pathHasApple:
                canSkip.add(node)
            
            return pathHasApple
        dfs(0, -1)

        seconds = -1 # seconds should be 0 when we start at root node
        def dfs2(node, parent):
            nonlocal seconds
            seconds += 1
            for nei in G[node]:
                if nei in canSkip: continue
                if parent == nei: continue
                dfs2(nei, node)            
                seconds += 1

        dfs2(0, -1)
        return seconds
