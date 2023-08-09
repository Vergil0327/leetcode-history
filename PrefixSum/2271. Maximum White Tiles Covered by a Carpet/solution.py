class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        
        n = len(tiles)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + tiles[i-1][1]-tiles[i-1][0]+1

        res = j = 0
        for i in range(n):
            start, end = tiles[i][0], tiles[i][0]+carpetLen-1
            while j < n and tiles[j][1] <= end:
                j += 1

            covered = presum[j]-presum[i]
            if j < n:
                covered += max(0, end-tiles[j][0]+1)

            res = max(res, covered)
        return res
