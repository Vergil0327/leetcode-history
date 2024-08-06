class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        time = [0]*n
        subtree_time = [defaultdict(int) for _ in range(n)] # subtree_time[node][child]: time from node to other child node
        def dfs(node, prev):
            t = 0
            for nxt in graph[node]:
                if nxt == prev: continue
                subtree_time[node][nxt] = dfs(nxt, node) + (1 if nxt%2 == 1 else 2)
                t = max(t, subtree_time[node][nxt])
            return t
        time[0] = dfs(0, -1)
        
        def reroot(node, prev, time_parent):
            children_time = [[t, i] for i, t in subtree_time[node].items()]
            children_time.sort(reverse=True)

            time[node] = max(time_parent, children_time[0][0] if children_time else 0)

            for nxt in graph[node]:
                if nxt == prev: continue
                
                time_neighbor = 0
                if len(children_time) > 0:
                    i = 0
                    if children_time[i][1] == nxt:
                        i += 1
                    if i < len(children_time):
                        time_neighbor = children_time[i][0]

                reroot(nxt, node, max(time_parent, time_neighbor) + (1 if node%2 else 2))

        reroot(0, -1, 0)
        return time
