# Intuition

這題很明顯可以看出，當前這行的擺法取決於前一行座位的擺法，由於每一行最多就8個，因此我們可以用二進位bitmask來表示當前這行及前一行的座位坐了哪些人

ex. 100010 -> 1代表有人, 0代表沒人

定義dp[i][state]: the maximum students of first `i` rows with `state`

那這樣狀態轉移就是:
`dp[i][state] = max(dp[i][state], dp[i-1][state'] + countOne(state))`

所以會是三層循環，第一層遍歷ROWS，第二層遍歷所有可能state，會有`1<<COLS`種state，第三層則遍歷所有可能prevState

大體框架就會是:
```
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
```

最後所有可能擺法遍歷一遍取最大即為答案 `max(dp[ROWS-1])`

**helper functions**

1. `valid`: 判斷相鄰有沒有坐人，以及有沒有人坐到破椅子
2. `canCheat`: 判斷前後座位有沒有人坐到可以作弊的位置

# Other Optimized Solution

```py
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        """
        dp[i][s]: max number of students after filling the first i row, with row in state s (as a binary string, 0 <= s < 2^n)
        dp[i][s]: max{dp[i-1][t] + popcount(s)} if rowi-1 = t , row = s is a valid state
        time: o(m*2^zn) space: o(m * 2^2n)
        to verify if 0 and 1 sits across using ASSERT(s&(s>>1)==0)
        to verfiy upper left and upper right satisfy the condition, ASSERT(t&(s>>1)==0) ASSERT(s&(t>>1)==0)
        """
        m, n = len(seats), len(seats[0])
        s = [0] * (m + 1)
        for i in range(m+1):
            for j in range(n):
                s[i] |=((seats[i-1][j] == "#") << j) 
        
        dp = [[0 for _ in range(1<<n)] for _ in range(m+1)]

        for i in range(1,m+1):
            for c in range(1<<n):
                if c & (c>>1) or c & s[i]:
                    continue
                for l in range(1<<n):
                    if (not (l & s[i-1])) and (not (l & (c>>1))) and (not (c & (l>>1))):
                        dp[i][c] = max(dp[i][c], dp[i-1][l] + bin(c).count('1'))
        return max(dp[m])

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        numRows, numCols = len(seats), len(seats[0])

        def check(col: int, prevMask: int) -> bool:
            if col <= 0:
                if prevMask & (1 << (col + 1)):
                    return False
            elif col >= numCols - 1:
                if prevMask & (1 << (col - 1)):
                    return False
            else:
                if prevMask & (1 << (col - 1)) or prevMask & (1 << (col + 1)):
                    return False
            return True

        @cache
        def solve(row: int, col: int, prevMask: int, mask: int) -> int:
            if row >= numRows:
                return 0
            if col == numCols:
                return solve(row + 1, 0, mask, 0)
            ans = 0
            if seats[row][col] == '.' and check(col, prevMask):
                if col == 0:
                    ans = 1 + solve(row, col + 1, prevMask, mask | (1 << (col)))
                elif not (mask & (1 << (col - 1))):
                    ans = 1 + solve(row, col + 1, prevMask, mask | (1 << (col)))
            ans = max(ans, solve(row, col + 1, prevMask, mask))
            return ans

        return solve(0, 0, 0, 0)
```