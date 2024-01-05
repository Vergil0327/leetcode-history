class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fires, seen = [], set()
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fires.append((i, j))
                    seen.add((i, j))
                    queue.append((i, j))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # If we stay for 'days' days.
        def check(days):
            fire, seen = fires[::], set()
            
            # Let the fire spreads for 'days' days.
            while days > 0:
                newfire = []
                for i, j in fire:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in seen:
                            # If the fire reach us before we move, we fail.
                            if ni == 0 and nj == 0:
                                return False
                            seen.add((ni, nj))
                            newfire.append((ni, nj))
                fire = newfire[::]
                days -= 1

            # Then let the fire and us move by turn (fire first, then people can move to safe place).
            safe = [(0, 0)]
            while safe:
                
                # Fire spreads first.
                newfire = []
                for i, j in fire:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in seen:
                            # If the fire reaches bot-right cell, if we are just one step close to bot-right cell
                            # We can still reach it, otherwise we fail. (Please refer to picture 2)
                            if ni == m - 1 and nj == n - 1:
                                if not ((m - 2, n - 1) in safe or (m - 1, n - 2) in safe):
                                    return False
                            seen.add((ni, nj))
                            newfire.append((ni, nj))
                fire = newfire[::]
                
                # We move then.
                newsafe = []
                for i, j in safe:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        # If we can reach bot-right cell, success.
                        if ni == m - 1 and nj == n - 1:
                            return True
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in seen:   
                            seen.add((ni, nj))
                            newsafe.append((ni, nj))
                safe = newsafe[::]
                
            # If there is no more cell for us to move before reaching bot-right cell, we fail.
            return False


        # check if always safe:
        while queue:
            i, j = queue.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    queue.append((ni, nj))
        queue = collections.deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in seen:
                    if ni == m - 1 and nj == n - 1:
                        return 10 ** 9 
                    seen.add((ni, nj))
                    queue.append((ni, nj))


        # Binary search to find maximum days:
        l, r = 0, m*n
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1

        return l if check(l) else -1