class Solution:
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        Q = set(map(tuple, queens))
        print(Q)
        m = n = 8
        res = []

        r, c = king
        while c < n and (r, c) not in Q:
            c += 1
        if c < n:
            res.append([r, c])

        r, c = king
        while c >= 0 and (r, c) not in Q:
            c -= 1
        if c >= 0:
            res.append([r, c])

        r, c = king
        while r < m and (r, c) not in Q:
            r += 1
        if r < m:
            res.append([r, c])

        r, c = king
        while r >= 0 and (r, c) not in Q:
            r -= 1
        if r >= 0:
            res.append([r, c])

        r, c = king
        while r < m and c < n and (r, c) not in Q:
            r, c = r + 1, c + 1

        if 0 <= r < m and 0 <= c < n:
            res.append([r, c])

        r, c = king
        while r >= 0 and c < n and (r, c) not in Q:
            r, c = r - 1, c + 1
        if 0 <= r < m and 0 <= c < n:
            res.append([r, c])

        r, c = king
        while r < m and c >= 0 and (r, c) not in Q:
            r, c = r + 1, c - 1
        if 0 <= r < m and 0 <= c < n:
            res.append([r, c])

        r, c = king
        while r >= 0 and c >= 0 and (r, c) not in Q:
            r, c = r - 1, c - 1
        if 0 <= r < m and 0 <= c < n:
            res.append([r, c])
        return res


# Optimized


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        m = n = 8
        res = []
        seen = [[False] * n for _ in range(m)]

        for r, c in queens:
            seen[r][c] = True

        directions = [-1, 0, 1]

        for dx in directions:
            for dy in directions:

                if dx == 0 and dy == 0:
                    continue

                x, y = king

                while dx + x >= 0 and dx + x < m and dy + y >= 0 and dy + y < n:

                    x += dx
                    y += dy

                    if seen[x][y]:
                        res.append([x, y])
                        break  # to discard other queens in same row and column

        return res
