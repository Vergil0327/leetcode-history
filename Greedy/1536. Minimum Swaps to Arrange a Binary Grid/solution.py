class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rightmostOne = defaultdict(set) # index of rightmost 1: row
        for i in range(n):
            foundOne = False
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    foundOne = True
                    rightmostOne[j].add(i)
                    
                    break
            if not foundOne:
                rightmostOne[-1].add(i)

        res = 0
        validRows = set()
        j = -1 # index of rightmost 1
        shift = [0] * n
        for currentRow in range(n):
            while j <= currentRow:
                validRows |= rightmostOne[j]
                j += 1
            if not validRows: return -1
            
            swaps = inf
            pickedRow = -1
            for row in validRows:
                swaps = min(swaps, dist:=abs(row+shift[row]-currentRow))
                if swaps == dist:
                    pickedRow = row
            
            # add to result and remove picked row
            res += swaps
            validRows.remove(pickedRow)

            # for all the rows above picked row, their index are shifted down by 1 row
            for row in range(pickedRow):
                shift[row] += 1
            
        return res