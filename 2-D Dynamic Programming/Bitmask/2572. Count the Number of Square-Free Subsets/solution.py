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
