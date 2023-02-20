class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:       
        MOD = int(1e9+7)

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        countNums = Counter(nums)
        counter = defaultdict(int)
        validStates = []
        for num, cnt in countNums.items():
            if num == 1: continue

            invalid = False
            bit = 0
            for i, p in enumerate(primes):
                if num%p == 0:
                    bit |= (1<<i)
                    num //= p
                    if num % p == 0:
                        invalid = True
                        break
            if invalid: continue
            
            validStates.append(bit)
            counter[bit] = cnt

        n = len(validStates)
        @lru_cache(None)
        def dfs(i, bitmask):
            if i == n: return 1

            res = dfs(i+1, bitmask)%MOD
            if bitmask & validStates[i] == 0:
                res += dfs(i+1, bitmask | validStates[i]) * counter[validStates[i]]
            return res%MOD

        return (dfs(0, 0)*(2**countNums[1])-1) %MOD


# TLE for python
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = int(1e9+7)

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        def encode(num):
            bitmask = 0
            for i, p in enumerate(primes):
                if num%p == 0:
                    num //= p
                    if num % p == 0:
                        return -1
                    
                    bitmask |= (1<<i)
            return bitmask

        # dp[i][state] : the number of square-free non-empty subsets of the array nums[:i] with choosing_state is `state`
        m, n = len(nums), len(primes)
        maxState = 1<<n
        dp = [[0] * (maxState) for _ in range(m+1)]
        
        # base case
        dp[0][0] = 1
        # nums = [0] + nums # shift to 1-indexed

        res = 0
        for i in range(1, m+1):
            for state in range(maxState):
                if nums[i-1] == 1: # 1取都不取都是合法的subset，所以方法數 * 2
                    dp[i][state] = dp[i-1][state] * 2
                    dp[i][state] %= MOD
                else:
                    dp[i][state] = dp[i-1][state] # 不選nums[i]
                    
                    numState = encode(nums[i-1])
                    if numState != -1 and (numState&state) == numState:
                        dp[i][state] += dp[i][state-numState]
                        dp[i][state] %= MOD

                if i == m:
                    res += dp[i][state]
                    res %= MOD
        
        # res = 0
        # for state in range(maxState):
        #     res += dp[m][state]
        #     res %= MOD
        return res-1 # -1 扣掉空subset