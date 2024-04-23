class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        parent = list(range(m*n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py

        for i in range(m):
            tmp = [(matrix[i][j], i*n+j)for j in range(n)]
            tmp.sort()

            for j in range(1, n):
                if tmp[j-1][0] == tmp[j][0]:
                    union(tmp[j-1][1], tmp[j][1])

        for j in range(n):
            tmp = [(matrix[i][j], i*n+j) for i in range(m)]
            tmp.sort()

            for i in range(1, m):
                if tmp[i-1][0] == tmp[i][0]:
                    union(tmp[i-1][1], tmp[i][1])

        group = defaultdict(list)
        for i in range(m):
            for j in range(n):
                p = i*n + j
                group[find(p)].append(p)

        arr = sorted([(matrix[i][j], i*n+j, i, j) for i in range(m) for j in range(n)])

        res = [[0]*n for _ in range(m)]
        rowRank = [0]*m # row[i]: max rank in i-th row
        colRank = [0]*n # col[i]: max rank in i-th col

        for _, p, r, c in arr:
            if res[r][c] > 0: continue # <---- avoid multiple update
            
            rank = 0
            for member in group[find(p)]:
                row, col = member//n, member%n
                rank = max(rank, rowRank[row])
                rank = max(rank, colRank[col])

            for member in group[find(p)]:
                row, col = member//n, member%n
                res[row][col] = rank+1

                # update back rowRank & colRank
                rowRank[row] = rank+1
                colRank[col] = rank+1
        return res
