class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # handle row first by topological sort
        nxtRow = defaultdict(list)
        indegRow = [0]*(k+1)
        for u, v in rowConditions:
            nxtRow[u].append(v)
            indegRow[v] += 1

        queue = deque()
        for node, deg in enumerate(indegRow):
            if deg == 0 and node > 0:
                queue.append(node)

        rows = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                rows.append(node)

                for nei in nxtRow[node]:
                    indegRow[nei] -= 1
                    if indegRow[nei] == 0:
                        queue.append(nei)

        if len(rows) != k: return []

        # handle column order by topological sort
        nxtCol = defaultdict(list)
        indegCol = [0]*(k+1)
        for u, v in colConditions:
            nxtCol[u].append(v)
            indegCol[v] += 1

        queue = deque()
        for node, deg in enumerate(indegCol):
            if deg == 0 and node > 0:
                queue.append(node)
        
        cols = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                cols.append(node)

                for nei in nxtCol[node]:
                    indegCol[nei] -= 1
                    if indegCol[nei] == 0:
                        queue.append(nei)

        if len(cols) != k: return []

        rowOrder = defaultdict(int) # node: row
        for row, node in enumerate(rows):
            rowOrder[node] = row

        colOrder = defaultdict(int) # node: col
        for col, node in enumerate(cols):
            colOrder[node] = col

        mat = [[0]*k for _ in range(k)]
        for node in range(1, k+1):
            mat[rowOrder[node]][colOrder[node]] = node
        return mat
