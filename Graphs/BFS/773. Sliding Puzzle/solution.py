# BFS
class Solution:
    # [1, 2, 3, 
    #  4, 5, 0]
    def genNext(self, string):
        arr = list(string)
        i = arr.index("0")
        res = []

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
            return arr

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        for nei in neighbors[i]:
            cpy = arr.copy()
            swap(cpy, i, nei)
            res.append(cpy)

        return ["".join(arr) for arr in res]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def flatten(board):
            return [el for subarr in board for el in subarr]
        def check(boardStr):
            return boardStr == "123450"

        visited = set()
        queue = deque(["".join(map(str, flatten(board)))])
        moves = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr in visited: continue
                visited.add(curr)

                if check(curr):
                    return moves

                for neighbor in self.genNext(curr):
                    if neighbor not in visited:
                        queue.append(neighbor)
            moves += 1
        return -1

class Solution:
    # [1, 2, 3,
    #  4, 5, 0]
    def genNext(self, string):
        arr = list(string)
        i = arr.index("0")
        res = []

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
            return arr

        if i == 0:
            cpy = arr.copy()
            swap(cpy, i, 3)
            res.append(cpy)
            
            cpy = arr.copy()
            swap(cpy, i, 1)
            res.append(cpy)
        elif i == 1:
            cpy = arr.copy()
            swap(cpy, i, 0)
            res.append(cpy)

            cpy = arr.copy()
            swap(cpy, i, 2)
            res.append(cpy)

            cpy = arr.copy()
            swap(cpy, i, 4)
            res.append(cpy)
        elif i == 2:
            cpy = arr.copy()
            swap(cpy, i, 1)
            res.append(cpy)
            
            cpy = arr.copy()
            swap(cpy, i, 5)
            res.append(cpy)
        elif i == 3:
            cpy = arr.copy()
            swap(cpy, i, 0)
            res.append(cpy)

            cpy = arr.copy()
            swap(cpy, i, 4)
            res.append(cpy)
        elif i == 4:
            cpy = arr.copy()
            swap(cpy, i, 3)
            res.append(cpy)

            cpy = arr.copy()
            swap(cpy, i, 5)
            res.append(cpy)

            cpy = arr.copy()
            swap(cpy, i, 1)
            res.append(cpy)
        else:
            cpy = arr.copy()
            swap(cpy, i, 4)
            res.append(cpy)

            cpy = arr.copy()
            swap(cpy, i, 2)
            res.append(cpy)
        return ["".join(arr) for arr in res]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def flatten(board):
            return [el for subarr in board for el in subarr]
        def check(board):
            return all(a==b for a, b in zip(["1", "2", "3", "4", "5", "0"], board))

        visited = set()
        board = flatten(board)
        queue = deque(["".join(map(str, board))])
        moves = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr in visited: continue
                visited.add(curr)
                if check(list(curr)):
                    return moves

                for neighbor in self.genNext(curr):
                    if neighbor not in visited:
                        queue.append(neighbor)
            moves += 1
        return -1