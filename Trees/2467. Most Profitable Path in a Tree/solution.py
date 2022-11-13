"""
Intuition:

1. construct adjancency list
2. find bob's path to root node
3. backtracking to find alice's max income and bob's position
4. stuck on how to find leaf node... later I found I can use `visited` set  to find if there's a way to go. if all the neighbor nodes are visited, and current node must be a leaf node.
"""
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        prev = {0: 0}
        def findBob(node, visited):
            if node == bob: return True

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    
                    prev[nei] = node
                    if findBob(nei, visited):
                        return True
            return False
        
        # find Bob's path
        findBob(0, set([0]))
        
        maxIncome = float("-inf")
        def dfs(state, node, visited, bobNode, path): 
            nonlocal maxIncome
            
            if node == bobNode:
                state += amount[node]//2
            else:
                if node not in path:
                    state += amount[node]

            nexts = set(graph[node])
            if len(nexts) == len(nexts & visited): # reach leaf node
                maxIncome = max(maxIncome, state)
                return

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)

                    path.add(bobNode)
                    dfs(state, nei, visited, prev[bobNode], path)
                    path.discard(bobNode) # backtracking
            
            return

        dfs(0, 0, set([0]), bob, set())
        return maxIncome

# concise solution
# https://leetcode.com/problems/most-profitable-path-in-a-tree/discuss/2807150/2-DFS-oror-1-DFS-oror-Simple-Approach-oror-C%2B%2B
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        
        graph = [[] for i in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # find parent and distance from node 0
        parent, dist = [0]*n, [0]*n
        def dfs(node, p = 0, d = 0):
            dist[node] = d
            parent[node] = p
            for nei in graph[node]:
                if nei == p: continue
                dfs(nei, node, d+1)
        dfs(0)    
        
        # update path from bob to root node 0
        curr = bob
        distBob = 0
        while curr != 0:
            if dist[curr] > distBob: # dist[curr] is alice's require steps
                amount[curr] = 0
            elif dist[curr] == distBob: # meeting point
                amount[curr] //= 2
            
            curr = parent[curr]
            distBob += 1
            
        # find total sum to each node
        inf = float("inf")
        def dfs2(node, amount, parent = 0):
            ret = amount[node]
            maxIncome = -inf
            for nei in graph[node]:
                if nei != parent:
                    maxIncome = max(maxIncome, dfs2(nei, amount, node))
            print(node, maxIncome, ret)
            # if node is leaf, we just return its amount
            if maxIncome == -inf:
                return ret
            else:
                return maxIncome+ret
        return dfs2(0, amount)
