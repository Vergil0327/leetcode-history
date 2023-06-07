class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        n = len(patience)
        time = [-1]*n
        queue = deque([(0,0)])
        while queue:
            for _ in range(len(queue)):
                node, sec = queue.popleft()
                if time[node] != -1: continue
                time[node] = sec * 2 # back-and-forth, *= 2
                for nei in graph[node]:
                    if time[nei] != -1: continue
                    queue.append([nei, sec+1])

        res = 0
        for node in range(1, n):
            msg = time[node] // patience[node]
            if time[node] % patience[node] == 0:
                msg -= 1
            res = max(res, time[node] + msg * patience[node])
        return res+1
