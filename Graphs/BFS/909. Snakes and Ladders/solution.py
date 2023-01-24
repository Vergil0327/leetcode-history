class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dest = n ** 2

        def getRowCol(nxt):
            row = n-1 - (nxt-1) // n
            inorder = row%2 == (n-1)%2
            col = (nxt-1) % n if inorder else n-1 - (nxt-1)%n
            return row, col

        visited = [0] * (dest+1)
        queue = deque([(n-1, 0, 1)])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c, curr = queue.popleft()

                if curr == dest: return steps
                if visited[curr]: continue
                visited[curr] = 1

                for i in range(1, 7):
                    nxt = min(curr+i, dest)
                    row, col = getRowCol(nxt)

                    if board[row][col] != -1:
                        nxt = board[row][col]
                        row, col = getRowCol(nxt)

                    queue.append((row, col, nxt))
            steps += 1
        return -1