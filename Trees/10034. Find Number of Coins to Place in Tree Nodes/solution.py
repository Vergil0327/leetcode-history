from sortedcontainers import SortedList
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(edges)+1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        res = [1]*n
        def dfs(node, prev):
            sl = SortedList([cost[node]])
            for nei in graph[node]:
                if nei == prev: continue
                arr = dfs(nei, node)
                for weight in arr:
                    sl.add(weight)

            if len(sl) == 3:
                c = 1
                for num in sl:
                    c *= num
                res[node] = c if c >= 0 else 0
            elif len(sl) > 3:
                ans = 0
                neg, pos = [], []
                for i in range(3):
                    if sl[i] < 0:
                        neg.append(sl[i])
                    if sl[len(sl)-1-i] >= 0:
                        pos.append(sl[len(sl)-1-i])

                if len(pos) == 3:
                    ans = max(ans, pos[0]*pos[1]*pos[2])
                if len(neg) >= 2 and pos:
                    ans = max(ans, neg[0]*neg[1]*pos[0])
                    
                res[node] = ans if ans >= 0 else 0
                return SortedList(neg+pos)
            
            return sl
        dfs(0, -1)
        return res
            