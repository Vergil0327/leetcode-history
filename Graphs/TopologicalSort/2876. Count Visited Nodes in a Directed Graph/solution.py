class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        
        indeg = [0] * n
        for u, v in enumerate(edges):
          indeg[v] += 1

        queue = deque()
        for node, deg in enumerate(indeg):
          if deg == 0:
            queue.append(node)

        # topological sort to find cycles
        nodeNotInCycle = []
        while queue:
          for _ in range(len(queue)):
            node = queue.popleft()
            nodeNotInCycle.append(node)

            nxt = edges[node]
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
              queue.append(nxt)

        res = [0] * n

        nodeInCycle = [node for node, deg in enumerate(indeg) if deg > 0]
        for node in nodeInCycle:
          if res[node] != 0: continue

          cycle = set()
          while node not in cycle:
            cycle.add(node)
            node = edges[node]
          
          for node in cycle:
            res[node] = len(cycle)

        def dfs(node):
          if res[node] != 0: return res[node]

          res[node] =  dfs(edges[node])+1
          return res[node]

        for node in nodeNotInCycle:
          dfs(node)
        return res
