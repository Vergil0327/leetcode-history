class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        rotate = [[""]*m for _ in range(n)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                rotate[j][m-1-i] = box[i][j]

        for j in range(m):
            rock = 0
            i0 = -1
            for i in range(n-1, -1, -1):
                if i0 < 0:
                    i0 = i

                if rotate[i][j] == "#":
                    rock += 1
                    rotate[i][j] = "."
                elif rotate[i][j] == ".":
                    continue
                else: # obstacle
                    while rock:
                        rotate[i0][j] = "#"
                        i0, rock = i0-1, rock-1
                    i0 = -1
            while rock:
                rotate[i0][j] = "#"
                i0, rock = i0-1, rock-1
            
        return rotate