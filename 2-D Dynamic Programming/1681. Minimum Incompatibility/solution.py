# bitmask DP with preprocessing
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter(nums)
        if any(freq > k for freq in counter.values()): return -1

        def containDuplicate(state):
            values = []
            for i in range(n):
                if (state>>i)&1:
                    values.append(nums[i])
            values.sort()

            for i in range(1, len(values)):
                if values[i] == values[i-1]: return (True, 0) # contain duplicate

            return (False, values[-1] - values[0])

        states = []
        values = []
        
        # 遍歷所有含有 subsetSize 個1-bit的 n-bit state
        subsetSize = n//k
        state = (1<<subsetSize)-1
        while state < (1<<n):
            hasDuplicate, incomp = containDuplicate(state)
            if not hasDuplicate:
                states.append(state)
                values.append(incomp)

            c = state & -state
            r = state+c
            state = (((r^state)>>2)//c) | r

        m = len(states)
        dp = [inf] * (1<<n)
        dp[0] = 0

        # 去除所有不可能的state
        # 如果state上的1不是subsetSize的倍數，那就不可能藉由subset轉移過來
        # ex. subsetSize = 2, state = 111
        validStates = []
        for state in range(1<<n):
            if bin(state).count("1") % subsetSize == 0:
                validStates.append(state)

        for i in range(m):
            # for state in range((1<<n)-1, 0, -1):
            for state in validStates:
                if (state&states[i]) == states[i]:
                    if dp[state-states[i]] != inf:
                        dp[state] = min(dp[state], dp[state-states[i]]+values[i])
        return dp[(1<<n)-1]

# bitmask DP - TLE for python
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter(nums)
        if any(freq > k for freq in counter.values()): return -1

        def containDuplicate(state):
            values = []
            for i in range(n):
                if (state>>i)&1:
                    values.append(nums[i])
            values.sort()

            for i in range(1, len(values)):
                if values[i] == values[i-1]: return (True, 0) # contain duplicate

            return (False, values[-1] - values[0])

        states = []
        values = []
        
        # 遍歷所有含有 subsetSize 個1-bit的 n-bit state
        subsetSize = n//k
        state = (1<<subsetSize)-1
        while state < (1<<n):
            hasDuplicate, incomp = containDuplicate(state)
            if not hasDuplicate:
                states.append(state)
                values.append(incomp)

            c = state & -state
            r = state+c
            state = (((r^state)>>2)//c) | r

        m = len(states)
        dp = [inf] * (1<<n)
        dp[0] = 0

        for i in range(m):
            for state in range(1<<n, -1, -1):
                if (state&states[i]) == states[i]:
                    if dp[state-states[i]] != inf:
                        dp[state] = min(dp[state], dp[state-states[i]]+values[i])
        return dp[(1<<n)-1]

# backtracking - TLE for python
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        if any(freq > k for freq in counter.values()): return -1

        n = len(nums)
        subsetSize = n//k
        nums.sort()
        
        res = inf
        visited = set()
        # current choose i-th num
        def dfs(i, count, minNum, maxNum, accuIncompatialty):
            nonlocal res
            if count == subsetSize:
                j = 0
                while j < n and j in visited:
                    j += 1

                if j == n:
                    res = min(res, accuIncompatialty + maxNum-minNum)
                else:
                    visited.add(j)
                    dfs(j, 1, nums[j], nums[j], accuIncompatialty + maxNum-minNum)
                    visited.remove(j)
                return

            last = -1
            for j in range(i+1, n):
                if j in visited: continue
                if nums[j] == nums[i]: continue
                if last != -1 and nums[j] == last: continue # prune branches
                visited.add(j)
                dfs(j, count+1, minNum, nums[j], accuIncompatialty)
                last = nums[j]
                visited.remove(j)

        visited.add(0)
        dfs(0, 1, nums[0], nums[0], 0)

        return res