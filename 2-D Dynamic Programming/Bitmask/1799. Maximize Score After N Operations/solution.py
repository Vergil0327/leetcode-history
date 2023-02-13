# TLE
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        # iterate m-1-bit in n-bit bitmask
        scores = {}
        m = 2
        state = (1<<m)-1
        while state < (1<<n):
            curr = state
            arr = []
            for i in range(n):
                if curr&1:
                    arr.append(nums[i])
                curr >>= 1
                if len(arr) == 2: break
            scores[state] = gcd(*arr)

            c = state & -state
            r = state+c
            state = (((r^state)>>2)//c) | r

        maxState = 1<<n
        dp = [[-inf]*maxState for _ in range(n+2)]
        dp[0][0] = 0

        validStates = []
        for state in range(maxState):
            if state != 0 and bin(state).count("1")%2 != 0: continue
            validStates.append(state)

        for i in range(2, n+2, 2):
            for state in validStates:
                if state != 0 and bin(state).count("1")%2 != 0: continue
                curr = (1<<m)-1
                while curr < maxState:
                    if curr&state == curr:
                        dp[i][state] = max(dp[i][state], dp[i-2][state-curr] + (i//2)*scores[curr])

                    c = curr & -curr
                    r = curr+c
                    curr = (((r^curr)>>2)//c) | r

        return dp[n][maxState-1]
    
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        # iterate m-1-bit in n-bit bitmask
        scores = {}
        m = 2
        state = (1<<m)-1
        while state < (1<<n):
            curr = state
            arr = []
            for i in range(n):
                if curr&1:
                    arr.append(nums[i])
                curr >>= 1
                if len(arr) == 2: break
            scores[state] = gcd(*arr)

            c = state & -state
            r = state+c
            state = (((r^state)>>2)//c) | r

        maxState = 1<<n
        dp = [[-inf]*maxState for _ in range(n+2)]
        dp[0][0] = 0

        validStates = []
        possibleSubstates = defaultdict(list)
        for state in range(maxState):
            if state != 0 and bin(state).count("1")%2 != 0: continue
            validStates.append(state)

            curr = (1<<m)-1
            while curr < maxState:
                if curr&state == curr:
                    possibleSubstates[state].append(curr)

                c = curr & -curr
                r = curr+c
                curr = (((r^curr)>>2)//c) | r

        for i in range(2, n+2, 2):
            for state in validStates:
                if state != 0 and bin(state).count("1")%2 != 0: continue
                for curr in possibleSubstates[state]:
                    dp[i][state] = max(dp[i][state], dp[i-2][state-curr] + (i//2)*scores[curr])

        return max(dp[n])