class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        guessSet = set([(u, v) for u, v in guesses])
        
        self.correct = 0
        def dfs(node, parent):
            if (parent, node) in guessSet:
                self.correct += 1

            for nei in graph[node]:
                if nei == parent: continue
                dfs(nei, node)    
        dfs(0, -1)
        
        self.res = 0
        def reroot(node, parent, correct):
            if correct >= k:
                self.res += 1
                
            for nei in graph[node]:
                if nei == parent: continue
                shift = 0
                if (node, nei) in guessSet:
                    shift -= 1
                if (nei, node) in guessSet:
                    shift += 1
                reroot(nei, node, correct+shift)
        reroot(0, -1, self.correct)
        
        return self.res
#         0: [0,1], [1,2], [1,3], [2,4]
#         1: [1,0], [1,2], [1,3], [2,4]
#         2: [1,0], [2,1], [1,3], [2,4]
#         3: [1,0], [2,1], [3,1], [2,4]
#         4: [1,0], [2,1], [3,1], [4,2]
