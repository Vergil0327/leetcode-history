class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        areaSum = 0
        bottomLeft = [inf, inf] # x,y
        topRight = [-inf, -inf] # x,y
        vertices = set()
        for x, y , a, b in rectangles:
            bottomLeft[0] = min(bottomLeft[0], x)
            bottomLeft[1] = min(bottomLeft[1], y)
            topRight[0] = max(topRight[0], a)
            topRight[1] = max(topRight[1], b)
            areaSum += (a-x) * (b-y)
            
            # find 4 vertices, O(4)
            for vertex in [(x,y),(a,y),(x,b),(a,b)]:
                if vertex in vertices:
                    vertices.remove(vertex)
                else:
                    vertices.add(vertex)

        targetArea = (topRight[0]-bottomLeft[0]) * (topRight[1]-bottomLeft[1])
        if targetArea != areaSum: return False
        if len(vertices) != 4: return False

        verticesList = sorted(vertices) # time: 4log4 = O(1)
        return verticesList[0] == tuple(bottomLeft) and verticesList[-1] == tuple(topRight)