# UnionFind: O(n), n = len(stones)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = 10000
        parent = {}
        rank = {}
        mapX = defaultdict(list)
        mapY = defaultdict(list)
        for x,y in stones:
            stoneId = x*N+y # hash (x,y) into integer as key
            parent[stoneId] = stoneId
            rank[stoneId]= 1
            mapX[x].append(stoneId)
            mapY[y].append(stoneId)

        def find(node):
            p = parent[node]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb: return False

            if rank[pa] >= rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
            return True

        # Union row by row
        for x, ids in mapX.items():
            stone0 = ids[0]
            for i in range(1, len(ids)):
                stone = ids[i]
                union(stone0, stone)

        # Union column by column
        for y, ids in mapY.items():
            stone0 = ids[0]
            for i in range(1, len(ids)):
                stone = ids[i]
                union(stone0, stone)

        groupParents = set(find(p) for p in parent.values())
        size = sum(rank[parentId]-1 for parentId in groupParents)
        return size

# Union-Find: ans = stones.size-groups.size
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            parent[py] = px
        
        def key(x, y):
            return x*10000+y

        row = defaultdict(list)
        col = defaultdict(list)
        for x, y in stones:
            parent[key(x,y)] = key(x,y)
            row[x].append(key(x,y))
            col[y].append(key(x,y))
        
        for ids in row.values():
            root = ids[0]
            for stoneID in ids[1:]:
                union(root, stoneID)
        
        for ids in col.values():
            root = ids[0]
            for stoneID in ids[1:]:
                union(root, stoneID)
            
        group = set()
        for x, y in stones:
            group.add(find(key(x, y)))

        return n - len(group)

# DFS: O(n^2), total number of stones
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(stone, visited):
            visited.add(stone)
            for nxt in stones:
                if tuple(nxt) not in visited:
                    if stone[0] == nxt[0] or stone[1] == nxt[1]:
                        dfs(tuple(nxt), visited)

        visited = set()
        connected = 0
        for stone in stones:
            if tuple(stone) not in visited:
                dfs(tuple(stone), visited)
                connected += 1

        return len(stones) - connected
