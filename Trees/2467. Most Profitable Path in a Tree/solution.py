"""
Intuition:

1. construct adjancency list
2. find bob's path to root node
3. backtracking to find alice's max income and bob's position
4. stuck on how to find leaf node... later I found I can use `visited` set  to find if there's a way to go. if all the neighbor nodes are visited, and current node must be a leaf node.

首先我們能用DFS預先計算bob的移動路線
nxtBobPos[i] 代表 bob在i節點時的下一個位置

再來用dfs來看alice's path並同時確認bob position
Alice at 0 and Bob at bob first

"""
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        nxtBobPos = {0: 0}
        def findBobPath(root, parent):
            if root == bob:
                return True

            for nei in graph[root]:
                if nei == parent: continue
                nxtBobPos[nei] = root
                if findBobPath(nei, root): return True
            return False
        
        # find Bob's path
        findBobPath(0, set([0]))
        
        maxIncome = float("-inf")
        def dfs(state, node, visited, bobNode, path): 
            nonlocal maxIncome
            
            if node == bobNode:
                state += amount[node]//2
            elif node not in path:
                state += amount[node]

            nexts = set(graph[node])
            if len(nexts) == len(nexts & visited): # reach leaf node
                maxIncome = max(maxIncome, state)
                return

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)

                    path.add(bobNode)
                    dfs(state, nei, visited, nxtBobPos[bobNode], path)
                    path.discard(bobNode) # backtracking
            
            return

        dfs(0, 0, set([0]), bob, set())
        return maxIncome

# I found that We can use post-order DFS traversal rather than backtracking
class SolutionOptimized:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        nxtBobPos = {0: 0}
        def findBob(root, parent):
            if root == bob:
                return True

            for nei in graph[root]:
                if nei == parent: continue
                nxtBobPos[nei] = root
                if findBob(nei, root): return True
            return False
        
        # find Bob's path
        findBob(0, set([0]))
        
        def dfs(node, parent, bobNode, path): 
            ret = 0
            if node == bobNode:
                ret = amount[node]//2
            elif node not in path:
                ret = amount[node]

            maxIncome = float("-inf")

            for nei in graph[node]:
                if nei != parent: # we don't need visited set, we can use parent node to find leaf node and stop traversal
                    path.add(bobNode)
                    maxIncome = max(maxIncome, dfs(nei, node, nxtBobPos[bobNode], path))
                    path.discard(bobNode) # backtracking bob's position

            if maxIncome == float('-inf'): # alice at leaf node
                return ret
            else:
                return maxIncome + ret

        return dfs(0, 0, bob, set())

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

            # if node is leaf, we just return its amount
            if maxIncome == -inf:
                return ret
            else:
                return maxIncome+ret
        return dfs2(0, amount)
