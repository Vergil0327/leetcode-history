class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        ROWS, COLS = len(seats), len(seats[0])
        
        # dp[row][state] = max(dp[row][state], dp[row-1][state'])
        dp = [[0] * (1<<COLS) for _ in range(ROWS)]

        def valid(row, state):
            bits = []
            for i in range(COLS):
                bits.append((state>>i)&1)
            for i in range(COLS):
                if bits[i] == 1 and ((i+1<COLS and bits[i+1] == 1) or (i>0 and bits[i-1] == 1)):
                    return False
                if bits[i] == 1 and seats[row][i] == "#": return False
            return True

        def canCheat(state, prevState):
            return (state&(prevState>>1)) or ((state>>1)&prevState)
            # bits1, bits2 = [], []
            # for i in range(COLS):
            #     bits1.append((state>>i)&1)
            #     bits2.append((prevState>>i)&1)

            # for i in range(COLS):
            #     if bits1[i] == 1 and ((i>0 and bits2[i-1] == 1) or (i+1<COLS and bits2[i+1] == 1)): return True
            # return False

        for row in range(ROWS):
            for state in range(1<<COLS):
                if not valid(row, state): continue

                oneBits = bin(state).count("1")
                for prevState in range(1<<COLS):
                    if row==0:
                        dp[row][state] = max(dp[row][state], dp[row-1][prevState]+oneBits)
                        continue

                    if not valid(row-1, prevState): continue
                    if canCheat(state, prevState): continue
                    dp[row][state] = max(dp[row][state], dp[row-1][prevState]+oneBits)

        return max(dp[ROWS-1])