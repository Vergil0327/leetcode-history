# Intuition

一開始想法很簡單, 由於`1 <= n <= 14`, 所以我們就遍歷每個節點作為起始
然後嘗試以它作為palindrome的`middle`往外進行DFS, 並以bitmask標記所有訪問過的節點

- if (visited_bitmask>>node)&1: node is visited

再來由於prlindrome可以是odd-length以及even-length, 我們就兩種都考慮即可

```py
import itertools
from collections import defaultdict
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        @cache
        def expand(nodeL, nodeR, visited):
            nextsL = defaultdict(list)
            for nxt in graph[nodeL]:
                if (visited>>nxt)&1: continue
                nextsL[label[nxt]].append(nxt)

            nextsR = defaultdict(list)
            for nxt in graph[nodeR]:
                if (visited>>nxt)&1: continue
                nextsR[label[nxt]].append(nxt)
            
            res = 2
            for key in nextsL:
                if key not in nextsR: continue
                for l in nextsL[key]:
                    for r in nextsR[key]:
                        if (visited>>l)&1: continue
                        if (visited>>r)&1: continue
                        if l == r: continue
                        state = visited
                        state |= 1<<l
                        state |= 1<<r
                        res = max(res, expand(l, r, state)+2)
            return res
        
        res = 1 # single node can be palindrome
        for node in range(n):
            visited = 1<<node

            nexts = defaultdict(list)
            for nxt in graph[node]:
                nexts[label[nxt]].append(nxt)
            
            # middle: single node
            for key in nexts:
                if len(nexts[key]) < 2: continue
                
                for l, r in itertools.combinations(nexts[key], 2):
                    state = visited
                    state |= 1<<l
                    state |= 1<<r
                    res = max(res, 1 + expand(l, r, state))
            
            # middle: two node
            for nxt in nexts[label[node]]:
                state = visited
                state |= 1<<nxt
                if node > nxt:
                    node, nxt = nxt, node
                res = max(res, expand(node, nxt, state))
            
        return res
```

可惜上述想法會TLE
但仔細看了看nexts[label]這個資料其實不用每次都重新計算
我們可以預先計算然後給`expand`及遍歷起始節點時使用

所以改成以下情形:

1. 預先計算nexts[node][label]
2. 為了避免重複計算, 以及有效進行cache, 我們在進行`expand(nodeL, nodeR)`時, 總是讓`nodeL < nodeR`來讓cache更有效率

```py
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
```
