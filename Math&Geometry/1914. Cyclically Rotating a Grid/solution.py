class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for i in range(min(m, n)//2):
            r = m - 2*i
            c = n - 2*i
            arr = []
            for y in range(i, i+c):
                arr.append(grid[i][y])
            for x in range(i+1, i+r):
                arr.append(grid[x][i+c-1])
            for y in range(i+c-2, i-1, -1):
                arr.append(grid[i+r-1][y])
            for x in range(i+r-2, i, -1):
                arr.append(grid[x][i])
            
            kk = k % len(arr)
            arr = arr[kk:] + arr[:kk]
            arr = deque(arr)

            y = i
            for _ in range(i, i+c):
                grid[i][y] = arr.popleft()
                y += 1
            x = i + 1
            for _ in range(i+1, i+r):
                grid[x][i+c-1] = arr.popleft()
                x += 1
            y = i + c - 2
            for _ in range(i+c-2, i-1, -1):
                grid[i+r-1][y] = arr.popleft()
                y -= 1
            x = i + r - 2
            for _ in range(i+r-2, i, -1):
                grid[x][i] = arr.popleft()
                x -= 1
        return grid

# Brute force: simulation process
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        layer = min(m//2, n//2)

        for i in range(layer):
            mm = m-i*2
            nn = n-i*2
            perimeter = (mm+nn)*2-4
            kk = k%perimeter

            for _ in range(kk):
                tmp = grid[i][i]
                r = c = i
                
                direction = [0,1]
                for _ in range(nn-1):
                    grid[r][c] = grid[r][c+1]
                    r += direction[0]
                    c += direction[1]
                
                direction = [1,0]
                for _ in range(mm-1):
                    grid[r][c] = grid[r+1][c]
                    r += direction[0]
                    c += direction[1]
                
                direction = [0,-1]
                for _ in range(nn-1):
                    grid[r][c] = grid[r][c-1]
                    r += direction[0]
                    c += direction[1]
                
                direction = [-1,0]
                for _ in range(mm-2):
                    grid[r][c] = grid[r-1][c]
                    r += direction[0]
                    c += direction[1]
                grid[r][c] = tmp

        return grid

