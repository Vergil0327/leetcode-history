# Digit DP
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        m = len(str(n))
        low, high = "1", str(n)
        while len(low) < len(high):
            low = "0" + low

        @cache
        def dfs(i, leading, lowerThanHigh, higherThanLow, state):
            if i >= m:
                return 1 if "2" in state else 0

            start = 0 if higherThanLow else int(low[i])
            end = 10 if lowerThanHigh else int(high[i])+1

            res = 0
            for d in range(start, end):
                new_state = state
                if d > 0 or not leading:
                    new_state = state[:d] + str(min(int(state[d])+1, 2)) + state[d+1:]

                res += dfs(i+1,
                           leading and d == 0,
                           lowerThanHigh or d < int(high[i]),
                           higherThanLow or d > int(low[i]),
                           new_state)
            return res
        
        return dfs(0, True, False, False, "0"*10)

# Math

def P(m, n):
    res = 1
    for i in range(n):
        res *= (m-i)
    return res
    
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        m = len(s)

        self.res = 0
        for length in range(1, m):
            self.res += P(10, length) - P(9, length-1)

        def count_no_repeat(i, visited):
            if i >= m: # 代表組出n位數並且沒有任何repeat的num
                self.res += 1
                return

            for d in range(10):
                if i == 0 and d == 0: continue # leading zero
                if visited[d]: continue
                if d < int(s[i]):
                    # 0-9共十個digit, 用去i+1個, 所以從剩下的10-(i+1)的digit裡分配到後面的m-(i+1)位
                    self.res += P(10-(i+1), m-(i+1))
                elif d == int(s[i]):
                    visited[d] = 1
                    count_no_repeat(i+1, visited)
                    visited[d] = 0

        count_no_repeat(0, [0]*10)
        return n-self.res