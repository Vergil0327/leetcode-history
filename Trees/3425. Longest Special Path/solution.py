class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(int))
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        self.res = [0, 1] # longest length, minimum number of nodes in longest path
        depth = defaultdict(int)
        self.prefix_sum = [0]

        def dfs(node, parent, start, cur_depth):
            prev_depth = depth[nums[node]]
            depth[nums[node]] = cur_depth
            start = max(start, prev_depth)

            length = cur_depth-start
            window_weight = self.prefix_sum[-1] - self.prefix_sum[start]
            if window_weight > self.res[0]:
                self.res = [window_weight, length]
            elif window_weight == self.res[0]:
                self.res[1] = min(self.res[1], length)

            for nxt in graph[node]:
                if nxt == parent: continue

                self.prefix_sum.append(self.prefix_sum[-1] + graph[node][nxt]) # <- append new value to prefix_sum
                dfs(nxt, node, start, cur_depth+1)
                self.prefix_sum.pop() # <- pop up value with backtracking

            depth[nums[node]] = prev_depth

        dfs(0, -1, 0, 1)
        return self.res