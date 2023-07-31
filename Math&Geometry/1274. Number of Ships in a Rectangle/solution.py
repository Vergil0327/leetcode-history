# class Sea:
#     def hasShips(self, topRight, bottomLeft) -> bool:

class Solution:
    def countShips(self, sea: Sea, topRight: List[int], bottomLeft: List[int]):
        # (x2, y1)               (x1, y1)
        #               midX+1,midY+1
        #      midX,midY
        # (x2, y2)               (x1, y2)
        def dfs(topRight, bottomLeft):
            x1, y1 = topRight[0], topRight[1]
            x2, y2 = bottomLeft[0], bottomLeft[1]

            if sea.hasShips(topRight, bottomLeft) == 0:
                return 0
            if x1 < x2 or y1 < y2: return 0
            if x1 == x2 and y1 == y2: return 1

            midX = (x1+x2)//2
            midY = (y1+y2)//2
            
            tr = dfs((x1,y1), (midX+1, midY+1))
            bl = dfs((midX, midY), (x2,y2))
            br = dfs((x1, midY), (midX+1, y2))
            tl = dfs((midX, y1), (x2, midY+1))
            return tr+bl+br+tl
        return dfs(tuple(topRight), tuple(bottomLeft))