class Robot:

    def __init__(self, width: int, height: int):
        m = self.m = height
        n = self.n = width
        self.robot = [0,0]
        self.dirs = {
            (0,1): "East",
            (1,0): "North",
            (0,-1): "West",
            (-1,0): "South",
        }
        self.nextDir = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.dir = (0,1)


    def step(self, num: int) -> None:
        if num == 0: return

        m, n = self.m, self.n
        mod = 2*m+2*n-4
        r, c = self.robot
        
        num %= mod
        if num == 0:
            num += mod

        while num > 0:
            dr, dc = self.dir

            if self.dirs[self.dir] == "East":
                step = min(n-1-c, num)
                row, col = r+dr*step, c+dc*step
                r, c = row, col
                
                num -= step
                if num == 0: break

                # counterclockwise if hit the wall
                if c == n-1:
                    self.dir = self.nextDir[self.dir]

            elif self.dirs[self.dir] == "West":
                step = min(c, num)
                row, col = r+dr*step, c+dc*step
                r, c = row, col
                
                num -= step
                if num == 0: break

                # counterclockwise if hit the wall
                if c == 0:
                    self.dir = self.nextDir[self.dir]

            elif self.dirs[self.dir] == "North":
                step = min(m-1-r, num)
                row, col = r+dr*step, c+dc*step
                r, c = row, col
                
                num -= step
                if num == 0: break

                # counterclockwise if hit the wall
                if r == m-1:
                    self.dir = self.nextDir[self.dir]

            else: # self.dirs[self.dir] == "South":
                step = min(r, num)
                row, col = r+dr*step, c+dc*step
                r, c = row, col
                
                num -= step
                if num == 0: break

                # counterclockwise if hit the wall
                if r == 0:
                    self.dir = self.nextDir[self.dir]

        self.robot = [r, c]
        
    def getPos(self) -> List[int]:
        return [self.robot[1], self.robot[0]]
        
    def getDir(self) -> str:
        return self.dirs[tuple(self.dir)]