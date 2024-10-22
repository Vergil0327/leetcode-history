class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)

        graph = defaultdict(list)
        for child, p in enumerate(parent):
            if p > -1:
                graph[p].append(child)

        mod = 10**9 + 7
        base = 32
        power = [1] * (n+1)
        for i in range(1, n+1):
            power[i] = (power[i-1] * base) % mod
        
        forwardHash = [0] * n
        reverseHash = [0] * n
        length = [0] * n
        
        def dfs(i):
            length[i] = 1
            forwardHash[i] = 0
            cur = ord(s[i]) - ord("a") + 1

            for nxt in graph[i]:
                dfs(nxt)
                forwardHash[i] = (forwardHash[i] * power[length[nxt]] + forwardHash[nxt]) % mod
                length[i] += length[nxt]
            forwardHash[i] = (forwardHash[i]*base + cur) % mod

            reverseHash[i] = cur
            for j in range(len(graph[i])-1, -1, -1):
                nxt = graph[i][j]
                reverseHash[i] = (reverseHash[i] * power[length[nxt]] + reverseHash[nxt]) % mod
        
        # tree rooted at node 0
        dfs(0)
        return [forwardHash[i] == reverseHash[i] for i in range(n)]