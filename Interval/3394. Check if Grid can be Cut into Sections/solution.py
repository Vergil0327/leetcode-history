class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # check hotizontal cut
        rectangles.sort(key=lambda x: (x[1],x[3]))
        nonoverlap = []

        for x,y,a,b in rectangles:
            if not nonoverlap or y >= nonoverlap[-1][1]:
                nonoverlap.append([y,b])
            else:
                nonoverlap[-1][1] = max(nonoverlap[-1][1], b)

        if len(nonoverlap) > 2: return True
        
        # check vertical cut
        rectangles.sort(key=lambda x: (x[0],x[1]))
        nonoverlap = []

        for x,y,a,b in rectangles:
            if not nonoverlap or x >= nonoverlap[-1][1]:
                nonoverlap.append([x,a])
            else:
                nonoverlap[-1][1] = max(nonoverlap[-1][1], a)

        return len(nonoverlap) > 2
