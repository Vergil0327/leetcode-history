class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(lambda: deque())
        for u, v in tickets:
            graph[u].append(v)

        n = len(tickets)
        res = [""] * (n+1)

        i = n+1
        def dfs(cur):
            nonlocal i

            while graph[cur]:
                nxt = graph[cur].popleft()
                dfs(nxt)
            i -= 1
            res[i] = cur

        dfs("JFK")
        return res
