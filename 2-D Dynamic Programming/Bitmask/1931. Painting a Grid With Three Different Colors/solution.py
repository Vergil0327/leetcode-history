class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = int(1e9+7)
        def conflict(currState, prevState):
            for _ in range(m):
                if currState%3 == prevState%3: return True
                currState //= 3
                prevState //= 3
            return False
        
        def selfConflict(state):
            cur = []
            for i in range(m):
                if cur and state%3 == cur[-1]: return True
                cur.append(state%3)
                state //= 3
            return False

        maxState = 3**m
        dp = [0] * maxState
        nextDp = [0] * maxState

        validStates = []
        for state in range(maxState):
            if selfConflict(state): continue
            validStates.append(state)
            dp[state] = 1

        for _ in range(n):
            for colorState in validStates:
                # !!! initial value should be 0 because of `+=`
                nextDp[colorState] = 0

                for prevState in validStates:
                    if conflict(colorState, prevState): continue
                    nextDp[colorState] = (nextDp[colorState] + dp[prevState])%MOD
            dp, nextDp = nextDp, dp

        total = 0
        for num in nextDp:
            total = (total+num)%MOD
        return total


# Optimized Solution
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def getColor(mask, pos):  # Get color of the `mask` at `pos`, use 2 bits to store a color
            return (mask >> (2 * pos)) & 3
        
        def setColor(mask, pos, color):  # Set `color` to the `mask` at `pos`, use 2 bits to store a color
            return mask | (color << (2 * pos))

        def dfs(r, curColMask, prevColMask, out):
            if r == m:  # Filled full color for this column
                out.append(curColMask)
                return

            for color in [1, 2, 3]:  # Try colors i in [1=RED, 2=GREEN, 3=BLUE]
                if getColor(prevColMask, r) != color and (r == 0 or getColor(curColMask, r - 1) != color):
                    dfs(r + 1, setColor(curColMask, r, color), prevColMask, out)

        @lru_cache(None)
        def neighbor(prevColMask):  # Generate all possible columns we can draw, if the previous col is `prevColMask`
            out = []
            dfs(0, 0, prevColMask, out)
            return out

        @lru_cache(None)
        def dp(col, prevColMask):
            if col == n: return 1  # Found a valid way
            ans = 0
            for nei in neighbor(prevColMask):
                ans = (ans + dp(col + 1, nei)) % 1_000_000_007
            return ans

        return dp(0, 0)