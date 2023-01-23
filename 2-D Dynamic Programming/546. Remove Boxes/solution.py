class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        cache = [[[-1] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(l, r, tailNumCount):
            if l > r: return 0

            if cache[l][r][tailNumCount] != -1:
                return cache[l][r][tailNumCount]

            i = r
            count = tailNumCount
            while i >= l and boxes[i] == boxes[r]:
                count += 1
                i -= 1
            
            # OO XXXXXX OO XXX OO
            # l              i  r, where count = 2 (= # of O after i)
            cache[l][r][tailNumCount] = dfs(l, i, 0) + count * count

            # OOOO XXXXXX OO XXX OO
            # l  j         j   i  r
            for j in range(i, l-1, -1):
                if boxes[j] == boxes[r] and boxes[j+1] != boxes[r]:
                    cache[l][r][tailNumCount] = max(cache[l][r][tailNumCount], dfs(l, j, count) + dfs(j+1, i, 0))

            return cache[l][r][tailNumCount]
        
        return dfs(0, len(boxes)-1, 0)


# Brute Force - TLE
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        cache = {}
        def removed(boxes):
            if not boxes: return 0
            if tuple(boxes) in cache:
                return cache[tuple(boxes)]
            
            n = len(boxes)
            i = points = 0
            while i < n:
                curr = boxes[i]
                j = i+1
                while j < n and boxes[j] == curr:
                    j += 1
                points = max(points, removed(boxes[:i] + boxes[j:]) + (j-i) * (j-i))
                
                i = j

            cache[tuple(boxes)] = points
            return points
        return removed(boxes)