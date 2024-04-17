class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        memo = defaultdict(int) # (mouse row, mouse col, cat row, cat row, turn)
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        cat, mouse, food = [], [], [] # positions of cat, mouse and food
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "F":
                    food = [i,j]
                if grid[i][j] == "C":
                    cat = [i,j]
                if grid[i][j] == "M":
                    mouse = [i,j]

        MOUSE, CAT = 1, 2
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "#": continue
                if i == food[0] and j == food[1]: continue
                memo[i,j,food[0],food[1],MOUSE] = CAT # mouse turn, cat wins
                queue.append((i,j,food[0],food[1],MOUSE))

                memo[food[0],food[1],i,j,MOUSE] = MOUSE # mouse turn, mouse wins
                queue.append((food[0],food[1],i,j,MOUSE))
                
                memo[i,j,food[0],food[1],CAT] = CAT # cat turn, cat wins
                queue.append((i,j,food[0],food[1],CAT))
                
                memo[food[0],food[1],i,j,CAT] = MOUSE # cat turn, mouse wins
                queue.append((food[0],food[1],i,j,CAT))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "#": continue
                memo[i,j,i,j,MOUSE] = CAT # mouse turn, cat catches mouse
                queue.append((i,j,i,j,MOUSE))
                
                memo[i,j,i,j,CAT] = CAT # cat turn, cat catches mouse
                queue.append((i,j,i,j,CAT))

        def findNextStates(mi, mj, ci, cj, t):
            nextStates = []
            if t == MOUSE:
                # cat move
                for di, dj in dirs:
                    for jump in range(catJump+1):
                        row, col = ci+di*jump, cj+dj*jump
                        if row<0 or row>=m or col<0 or col>=n: continue
                        if grid[row][col] == "#": break
                        nextStates.append((mi,mj,row,col,CAT))
            if t == CAT:
                # mouse move
                for di, dj in dirs:
                    for jump in range(mouseJump+1):
                        row, col = mi+di*jump, mj+dj*jump
                        if row<0 or row>=m or col<0 or col>=n: continue
                        if grid[row][col] == "#": break
                        nextStates.append((row,col,ci,cj,MOUSE))

            return nextStates

        def allNextStatesWin(mi, mj, ci, cj, t):
            if t == MOUSE:
                for di, dj in dirs:
                    for jump in range(mouseJump+1):
                        row, col = mi+di*jump, mj+dj*jump
                        if row<0 or row>=m or col<0 or col>=n: continue
                        if grid[row][col] == "#": break
                        if memo[row,col,ci,cj,CAT] != CAT: return False
            if t == CAT:
                for di, dj in dirs:
                    for jump in range(catJump+1):
                        row, col = ci+di*jump, cj+dj*jump
                        if row<0 or row>=m or col<0 or col>=n: continue
                        if grid[row][col] == "#": break
                        if memo[mi,mj,row,col,MOUSE] != MOUSE: return False
            return True

        step = 0
        while queue:
            step += 1
            if step > 2000: return False

            for _ in range(len(queue)):
                mi, mj, ci, cj, t = queue.popleft()
                status = memo[mi, mj, ci, cj, t]

                for mii, mjj, cii, cjj, tt in findNextStates(mi, mj, ci, cj, t):
                    if memo[mii, mjj, cii, cjj, tt] != 0: continue

                    # 如果status=CAT, 而tt又等於CAT, 代表是cat turn, cat wins, 同理如果status=MOUSE, 那就是mouse turn mouse wins
                    # 所以這行一次涵蓋了兩種必贏的可能
                    if tt == status:
                        memo[mii, mjj, cii, cjj, tt] = status # 也是必贏
                        queue.append((mii, mjj, cii, cjj, tt))
                    elif allNextStatesWin(mii, mjj, cii, cjj, tt): # 必輸可能性
                        memo[mii, mjj, cii, cjj, tt] = MOUSE if tt == CAT else CAT # 看這輪`tt`是誰的回合, 誰回合就誰輸, cat turn =>  mouse win
                        queue.append((mii, mjj, cii, cjj, tt))
        
        # 最後就看起始狀態老鼠會是贏還輸
        return memo[mouse[0], mouse[1], cat[0], cat[1], 1] == MOUSE