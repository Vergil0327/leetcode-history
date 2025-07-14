import itertools
from collections import defaultdict
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        nexts = [defaultdict(list) for _ in range(n)]
        for node in range(n):
            for nxt in graph[node]:
                nexts[node][label[nxt]].append(nxt)

        @cache
        def expand(nodeL, nodeR, visited):
            res = 2
            for key in nexts[nodeL]:
                if key not in nexts[nodeR]: continue
                for l in nexts[nodeL][key]:
                    for r in nexts[nodeR][key]:
                        if (visited>>l)&1: continue
                        if (visited>>r)&1: continue
                        if l == r: continue
                        state = visited
                        state |= 1<<l
                        state |= 1<<r
                        if l > r:
                            l, r = r, l
                        res = max(res, expand(l, r, state)+2)
            return res
        
        res = 1 # single node can be palindrome
        for node in range(n):            
            visited = 1<<node
            # middle: single node
            for key in nexts[node]:
                if len(nexts[node][key]) < 2: continue
                
                for l, r in itertools.combinations(nexts[node][key], 2):
                    state = visited
                    state |= 1<<l
                    state |= 1<<r
                    if l > r:
                        l, r = r, l
                    res = max(res, 1 + expand(l, r, state))
            
            # middle: two node
            for nxt in nexts[node][label[node]]:
                state = visited
                state |= 1<<nxt
                if node > nxt:
                    node, nxt = nxt, node
                res = max(res, expand(node, nxt, state))
            
        return res
