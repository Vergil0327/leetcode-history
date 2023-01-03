class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        # two bits for [next_state, current_state]
        for y in range(m):
            for x in range(n):
                live = 0

                for i in range(max(y-1, 0), min(y+1, m-1)+1):
                    for j in range(max(x-1, 0), min(x+1, n-1)+1):
                        if i == y and j == x: continue
                        
                        if board[i][j]&1 == 1: # judge current state
                            live += 1

                if board[y][x]&1 == 1: # current state = 1
                    if live == 2 or live == 3: # bit representation: "11"
                        board[y][x] |= 1<<1
                    else: # bit representation: "01"
                        continue
                else: # current state = 0
                    if live == 3: # bit representation: "10"
                        board[y][x] |= 1<<1
                    else: # bit representation: "00"
                        continue

        for y in range(m):
            for x in range(n):
                board[y][x] >>= 1