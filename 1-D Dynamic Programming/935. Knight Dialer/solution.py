class Solution:
    def knightDialer(self, n: int) -> int:
        adjacencyList = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        dp = [[0] * 10 for _ in range(n)]

        for num in range(10): # phonepad: 0-9
            dp[0][num] = 1
        
        for i in range(1, n): # n-1 jumps
            for num in range(10):
                for prev in adjacencyList[num]:
                    dp[i][num] += dp[i-1][prev]
                    dp[i][num] %= 1_000_000_007

        res = 0
        for num in range(10):
            res = (res + dp[n-1][num]) % 1_000_000_007
        return res