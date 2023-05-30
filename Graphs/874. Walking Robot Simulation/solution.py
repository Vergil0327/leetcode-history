class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        N = [0,1]
        E = [1,0]
        S = [0,-1]
        W = [-1,0]
        dirs = [N,E,S,W]
        curDir = 0

        res = 0
        walls = set(tuple(obs) for obs in obstacles)
        pos = [0,0]
        for cmd in commands:
            if cmd == -1:
                curDir = (curDir+1)%4
            elif cmd == -2:
                curDir = ((curDir-1)+4)%4
            else:
                while cmd:
                    nxt = (pos[0]+dirs[curDir][0], pos[1]+dirs[curDir][1])
                    if nxt in walls: break
                    
                    pos = nxt
                    res = max(res, pos[0]**2 + pos[1]**2)
                    cmd -= 1
        return res

