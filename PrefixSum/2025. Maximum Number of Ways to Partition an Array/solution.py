class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)

        presum = [0]*n
        for i in range(n):
            presum[i] = (presum[i-1] if i-1>=0 else 0)+nums[i]

        sufsum = [0]*(n+1)
        for i in range(n-1, -1, -1):
            sufsum[i] = sufsum[i+1]+nums[i]

        res = 0
        for p in range(1, n):
            a, b = presum[p-1], presum[n-1]-presum[p-1]
            if a == b:
                res += 1
        
        # case1: pivot before i
        count = Counter() # {presum: freq}
        ways = [0] * n
        for i in range(n):
            if (new_sum := presum[n-1]+k-nums[i])%2 == 0:
                ways[i] += count[new_sum//2]
            count[presum[i]] += 1

        # case2: pivot after i
        count = Counter() # {sufsum: freq}
        for i in range(n-1, -1, -1):
            if (new_sum := sufsum[0]+k-nums[i])%2 == 0:
                ways[i] += count[new_sum//2]
            count[sufsum[i]] += 1

        return max(res, max(ways))
