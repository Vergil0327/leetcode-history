"""
We are given a tree, so there is exactly one unique path between any two nodes.
For every unordered pair of nodes (u, v) that belong to the same group, we need to add the distance between them (number of edges on their path).

Instead of computing distances for all pairs directly (which would be too slow), we observe:

- Every path between two nodes contributes 1 to the answer for each edge on that path.
- So, we can reverse the thinking:
    - For each edge, count how many valid (u, v) pairs of the same group have their path passing through that edge.
    - Add this count to the total answer.
Thus, the problem becomes counting, for every edge and every group, how many same-group node pairs are separated by that edge.
"""

class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        groupCount = Counter(group)
        self.ans = 0

        def dfs(node, prev):
            count = Counter()
            count[group[node]] = 1
            for next in graph[node]:
                if next == prev:
                    continue

                """
                Edge contribution logic

                While returning from child v to parent u, for each group g:
                - inSubtree = counts[v][g]
                - outsideSubtree = totalInGroup[g] - inSubtree
                - Any pair with one node inside v's subtree and one outside must pass through edge (u, v).
                
                Contribution of current edge for group g: `inSubtree * outsideSubtree`
                Add this value to the global answer.
                """
                subCount = dfs(next, node)
                for g, c in subCount.items():
                    self.ans += c * (groupCount[g] - c)

                # merge small hashmap. swap if needed
                if len(subCount) > len(count):
                    count, subCount = subCount, count
                count.update(subCount)

            return count

        dfs(0, -1)
        return self.ans