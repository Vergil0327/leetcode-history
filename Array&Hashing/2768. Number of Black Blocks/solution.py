class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        contrib = Counter()
        for r, c in coordinates:
            for i in range(r-1, r+1):
                for j in range(c-1, c+1):
                    if 0 <= i < m-1 and 0 <= j < n-1:
                        contrib[(i,j)] += 1

        blacks = Counter(contrib.values()) # blacks[i]: number of blocks with i black cells
        
        return [
            (m-1)*(n-1) - blacks[1] - blacks[2] - blacks[3] - blacks[4],
            blacks[1],
            blacks[2],
            blacks[3],
            blacks[4],
        ]
