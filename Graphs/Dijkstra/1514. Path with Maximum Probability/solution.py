"""
Time complexity of the code below is O(E+ElogN)_ which turns out to be O(ElogN) where N is the number of Nodes and E is the number of edges.

Explanation for the same:
Maximum Nodes in the priority queue can Be E(Edges), And we know that each operation in the priority queue takes O(logx) time where x is the size of the priority queue, Here it turns out to be O(logE), Which in fact can be written as O(logN). Reason begin worst value of E can be N*(N-1)/2 ~ N2. So logE can be written as logN2 = 2*logN = logN. Hence the time complexity required due to priority queue is O(N)

Also in the question we are creating adjacency list, For which we are looping E times. Hence the time complexity due to the same is O(E).

Total time complexity O(E+ElogN) = O(max(E, ElogN) = (E*logN).
"""
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            u, v = edge
            graph[u].append([-prob, v])
            graph[v].append([-prob, u])

        maxH = [[-1, start]]
        visited = set()
        while maxH:
            prob, curr = heapq.heappop(maxH)
            visited.add(curr)
            
            if curr == end:
                return -prob

            for probNei, nei in graph[curr]:
                if nei in visited: continue
                heapq.heappush(maxH, [-(-prob * -probNei), nei])
        return 0