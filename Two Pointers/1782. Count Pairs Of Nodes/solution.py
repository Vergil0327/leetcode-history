class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        edgeCount = defaultdict(int) # {[u, v]: edge count}
        degrees = [0]*(n+1)
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            edgeCount[min(u, v), max(u, v)] += 1

        count = list(sorted(degrees))
        res = []
        for q in queries:
            valid = 0
            j = n
            for i in range(1, n+1):
                if i >= j:
                    valid += n-i
                    continue

                while j > i and count[i] + count[j] > q:
                    j -= 1
                valid += n-j

            for u, v in edgeCount:
                if degrees[u] + degrees[v] > q and degrees[u] + degrees[v] - edgeCount[u,v] <= q:
                    valid -= 1
            res.append(valid)                
        return res

