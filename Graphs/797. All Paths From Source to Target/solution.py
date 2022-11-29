"""
DFS with backtracking

DAG -> since graph is acylic, we don't need `visited` to avoid going back
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        path = []
        res = []
        def dfs(root, path):
            path.append(root)

            if root == n-1:
                res.append(path.copy())

            for nxt in graph[root]:
                dfs(nxt, path)

            path.pop()
            return

        dfs(0, path)
        return res
