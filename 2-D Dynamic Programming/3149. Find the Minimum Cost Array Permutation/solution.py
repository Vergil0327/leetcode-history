class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final_state = (1<<n)-1

        dp = defaultdict(list)

        @cache
        def dfs(prev, bitmask):
            if bitmask == final_state:
                return abs(prev-nums[0])

            # score = |perm[i] - nums[perm[i+1]]| for i in range(n)
            # use recursion to find every possibilities => |perm[i] - nums[perm[i+1]]| = |prev - nums[i]| for i in range(n) if (bitmask>>i)&1 == 0
            min_score, num = inf, -1
            for v in range(1, n):
                if (bitmask>>v)&1: continue
                sc = dfs(v, bitmask|(1<<v)) + abs(prev - nums[v])
                if sc < min_score:
                    min_score = sc
                    num = v

            dp[prev, bitmask] = [num] + dp[num, bitmask | (1<<num)]

            return min_score

        dfs(0, 1)
        return [0] + dp[0, 1]