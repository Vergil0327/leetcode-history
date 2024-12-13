class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)
        lnext = {
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0),
            (1, 0): (0, 1),
        }
        rnext = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
        }
        xAxis = [-inf, inf] # LEFT, RIGHT
        yAxis = [-inf, inf] # UP, DOWN

        pos = [0,0]
        for cycle in range(4):
            for inct in instructions:
                if inct != "G":
                    if inct == "L":
                        direction = lnext[direction]
                    if inct == "R":
                        direction = rnext[direction]
                else:
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                if pos[0] > 0:
                    xAxis[0] = max(xAxis[0], pos[0])
                if pos[0] < 0:
                    xAxis[1] = min(xAxis[1], pos[0])
                if pos[1] > 0:
                    yAxis[0] = max(yAxis[0], pos[1])
                if pos[1] < 0:
                    yAxis[1] = min(yAxis[1], pos[1])
        if pos == [0,0]: return True

        for cycle in range(4):
            for inct in instructions:
                if inct != "G":
                    if inct == "L":
                        direction = lnext[direction]
                    if inct == "R":
                        direction = rnext[direction]
                else:
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                if (xAxis[0] > -inf and pos[0] > xAxis[0]) or (xAxis[1] < inf and pos[0] < xAxis[1]): return False
                if (yAxis[0] > -inf and pos[1] > yAxis[0]) or (yAxis[1] < inf and pos[1] < yAxis[1]): return False

        return True
    
class Solution:
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)