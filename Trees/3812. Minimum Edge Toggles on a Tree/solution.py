"""
Intuition

目標是將所有節點都toggle成target
所以如果我們利用post-order DFS, 從葉子節點出發
如果該節點不同於target, 那麼代表肯定要toggle該edge
如此一來, 整個情況就變成一路從最後的葉子節點翻回跟節點
像推骨牌一樣, 也沒有其他情形需要考慮, 不同於target就是得toggle

所以我們一邊進行post-order DFS, 一邊記錄該edge index
最後再判斷根節點有沒有翻成target即可

如果不同於target, 返回[-1]
如果相等, 返回一路上翻過的所有edge index
"""


class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append([v, i])
            graph[v].append([u, i])

        start = list(map(int, start))
        target = list(map(int, target))

        self.res = []
        def dfs(node, prev, edgeIdx):
            for nxt, idx in graph[node]:
                if nxt == prev: continue
                dfs(nxt, node, idx)

            if start[node] != target[node] and edgeIdx != -1:
                self.res.append(edgeIdx)
                start[node] = 1 - start[node]
                start[prev] = 1 - start[prev]
        
        dfs(0, 0, -1)

        if start[0] != target[0]:
            return [-1]

        self.res.sort()
        return self.res
