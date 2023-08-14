class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)

        n = len(nums)
        if presum[n]%p == 0: return 0
        remainder = presum[n]%p

        res = inf
        seen = {0:-1}
        for i in range(n):
            if (subSum := ((presum[i+1]%p - remainder)+p)%p) in seen:
                j = seen[subSum]
                if i-j < n: # 如果i-j == n, 代表我們把整個nums都移除掉
                    res = min(res, i-j)
            seen[presum[i+1]%p] = i

        return res if res != inf else -1
