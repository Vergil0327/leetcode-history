class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        
        pos1 = []
        pos2 = []
        for r in range(N):
            for c in range(N):
                if img1[r][c] == 1:
                    pos1.append((r,c))
                if img2[r][c] == 1:
                    pos2.append((r,c))
        
        # vectorCount means if we move every 1-position in img1 by a vector,
        # how many overlapping position do we have?
        vectorCount = defaultdict(int)

        # try to overlapy (r1,c1) in img1 on every 1-position in img2
        for r1,c1 in pos1:
            for r2, c2 in pos2:
                vector = (r1-r2,c1-c2)
                vectorCount[vector] += 1 # if we got the same vector in different (row,col) position, it means those position will overlap if we shift vector to zero
        
        # edge case: [[0]], [[0]] => no overlapping position => empty vectorCount
        return max(vectorCount.values()) if vectorCount else 0
        