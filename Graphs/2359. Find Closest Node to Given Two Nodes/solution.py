class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, distance, dist):
            if dist[node] != -1: return
            dist[node] = distance

            nxt = edges[node]
            if nxt != -1:
                dfs(nxt, distance+1, dist)
        
        dist1 = [-1] * len(edges) 
        dist2 = [-1] * len(edges) 
        dfs(node1, 0, dist1)
        dfs(node2, 0, dist2)

        res = -1
        currMinMax = inf
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                if max(dist1[i], dist2[i]) < currMinMax:
                    currMinMax = max(dist1[i], dist2[i])
                    res = i
        return res