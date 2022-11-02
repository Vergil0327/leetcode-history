import collections

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
		    # it's impossible to mutate to end when end is not in bank
        if end not in bank: return -1
        
		    # make sure our graph (adjacency list) contains start
        arr = list(set(bank + [start]))
        
		    # construct graph (n^2)
        graph = collections.defaultdict(list)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                u, v = arr[i], arr[j]
                cnt = 0
                for c1, c2 in zip(u, v):
                    if c1 != c2: cnt += 1
                if cnt == 1:
                    graph[u].append(v)
                    graph[v].append(u)
        
		    # BFS template
        visited = set(start)
        queue = collections.deque([start])
        mutations = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                
                if node == end:
                    return mutations
                
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            mutations += 1
        
        return -1

# we can further optimize BFS solution by simulating mutation directly rather than constructing adjacency list in advance
class OptimalSolution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        
        banks = set(bank + [start])
        visited = set(start)
        queue = collections.deque([start])
        mutations = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                gene = queue.popleft()
                
                if gene == end:
                    return mutations

                for i in range(len(gene)): # O(8)
                    for mut in ["A","C","G","T"]: # O(4)
                        if mut == gene[i]: continue
                        nei = gene[:i] + mut + gene[i+1:]
                        if nei not in visited and nei in banks:
                            visited.add(nei)
                            queue.append(nei)
            mutations += 1
        
        return -1