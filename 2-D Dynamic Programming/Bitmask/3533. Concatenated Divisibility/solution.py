class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        digit_len = [len(str(num)) for num in nums]

        final = (1<<n)-1
        @cache
        def dfs(state, remainder):
            if state == final:
                return [] if remainder == 0 else None

            res = None
            for i in range(n):
                if (state>>i)&1: continue

                new_remainder = (remainder * pow(10, digit_len[i]) + nums[i]) % k
                arr = dfs(state | (1<<i), new_remainder)
                if arr is None: continue

                if res is None:
                    res = [nums[i], *arr]
                else:
                    res = min(res, [nums[i], *arr])
                
            return res
        
        ans = dfs(0, 0)
        return ans if ans is not None else []