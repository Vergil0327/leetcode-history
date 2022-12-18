class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degrees = [0] * (n+1)

        neighbors = [set() for _ in range(n+1)]
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)
            degrees[u] += 1
            degrees[v] += 1
        
        oddDeg = [node for node, deg in enumerate(degrees) if deg%2 != 0]
        
        # since 2 extra edges at most, it's impossible to add less than 2 edges
        if len(oddDeg) > 4: return False

        # since the graph can be disconnected, every graph is valid
        if len(oddDeg) == 0: return True

        if len(oddDeg) == 2:
            u, v = oddDeg[0], oddDeg[1]
            if u not in neighbors[v]: # we can link together
                return True
            else: # we need to find another independent node to link for both of them
                for node in range(1, n+1):
                    if node != u and node != v and (node not in neighbors[u] and node not in neighbors[v]):
                        return True
                return False
        
        # len(oddDeg) == 4
        # since 2 extra edges at most, it'll be valid only if they are able to link together
        remain = set(oddDeg)
        for i in range(4):
            for j in range(i+1, 4):
                if i == j: continue
                u, v = oddDeg[i], oddDeg[j]
                if u not in neighbors[v]:
                    otherTwo = [node for node in remain if node != u and node != v]
                    a, b = otherTwo[0], otherTwo[1]
                    if a not in neighbors[b]:
                        return True
        return False