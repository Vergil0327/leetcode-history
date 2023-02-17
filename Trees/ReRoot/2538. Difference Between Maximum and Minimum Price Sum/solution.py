# Now becomes TLE for python, 2023
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        leaves = [node for node, deg in enumerate(indegree) if deg == 1]

        cache = {}
        def dfs(node, prev):
            if (node, prev) in cache:
                return cache[(node, prev)]

            pathsum = 0
            for nei in graph[node]:
                if nei == prev: continue
                pathsum = max(pathsum, dfs(nei, node))

            cache[(node, prev)] = pathsum + price[node]
            return cache[(node, prev)]
        
        res = 0
        for node in leaves:
            res = max(res, dfs(node, node) - price[node])
        return res


# Re-root
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        n = len(price)
        subtreeSum = [0] * n

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            pathsum = 0
            for child in graph[node]:
                if child == parent: continue
                pathsum = max(pathsum, dfs(child, node))
            subtreeSum[node] = pathsum + price[node]
            return subtreeSum[node]

        maxDiff = 0
        def reroot(node, parent, parentContribution):
            nonlocal maxDiff

            candidate1, candidate2 = 0, 0
            maxContribution1, secondContribution = 0, 0
            for child in graph[node]:
                if child == parent: continue

                if subtreeSum[child] > maxContribution1:
                    secondContribution, candidate2 = maxContribution1, candidate1
                    maxContribution1, candidate1 = subtreeSum[child], child
                elif subtreeSum[child] > secondContribution:
                    secondContribution, candidate2 = subtreeSum[child], child

            path1 = maxContribution1
            path2 = parentContribution
            maxDiff = max(maxDiff, max(path1, path2))
            for child in graph[node]:
                if child == parent: continue
                if child == candidate1:
                    reroot(child, node, price[node] + max(secondContribution, parentContribution))
                else:
                    reroot(child, node, price[node] + max(maxContribution1, parentContribution))

        dfs(0, -1)
        reroot(0, -1, 0)

        return maxDiff
