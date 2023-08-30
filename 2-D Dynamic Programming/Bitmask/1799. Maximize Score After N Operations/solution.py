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

# Optimzed from TLE solution
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
    
# Concise
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)//2
        scores = {}
        for i in range(2*n):
            for j in range(2*n):
                scores[(i,j)] = gcd(nums[i], nums[j])
        
        stateSet = defaultdict(list)
        for i in range(1, n+1):
            state = (1 << (2*i))-1
            while state < (1 << 2*n):
                stateSet[i].append(state)
                c = state & -state
                r = state+c
                state = (((r^state)>>2)//c) | r
        stateSet[0].append(0)

        dp = [0] * (1<<(2*n))
        for i in range(1, n+1):
            for state in stateSet[i]:
                for subState in stateSet[i-1]:
                    if state & subState != subState: continue

                    x = y = -1
                    currState = state - subState
                    for j in range(14):
                        if (currState>>j)&1:
                            if x == -1:
                                x = j
                            else:
                                y = j
                    dp[state] = max(dp[state], dp[subState] + i*scores[(x,y)])

        return dp[(1<<(2*n))-1]
    
# top-down dp + bitmask
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)

        scores = {}
        for i in range(m):
            for j in range(i+1, m):
                scores[(i,j)] = gcd(nums[i], nums[j])

        @cache
        def dfs(i, state):
            if state == 0: return 0
            
            res = 0
            for j in range(m):
                if (state>>j)&1 == 0: continue
                for k in range(j+1, m):
                    if (state>>k)&1 == 0: continue
                    nxt = state^(1<<j)
                    nxt ^= (1<<k)
                    # res = max(res, dfs(i+1, nxt) + i * gcd(nums[j], nums[k]))
                    res = max(res, dfs(i+1, nxt) + i * scores[(j, k)])
            return res


        return dfs(1, (1<<m) - 1)
