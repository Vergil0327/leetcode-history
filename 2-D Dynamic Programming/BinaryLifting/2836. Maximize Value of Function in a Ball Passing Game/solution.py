class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        m, n = k.bit_length(), len(receiver)
        # pos[i][j] means the end point after move 2^i steps from j
        pos = [[receiver[i] for i in range(n)] for j in range(m)]
        # score[i][j] means the score after move 2^i steps from j, not include j itself
        score = [[receiver[i] for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(n):
                x = pos[i-1][j]
                pos[i][j] = pos[i-1][x]
                score[i][j] = score[i-1][j] + score[i-1][x]
        def calculate(now, p):
            if p == -1: return 0
            if (k & (1 << p)) == 0: return calculate(now, p - 1)
            return score[p][now] + calculate(pos[p][now], p - 1)

        return max([calculate(i, m - 1) + i for i in range(n)])
