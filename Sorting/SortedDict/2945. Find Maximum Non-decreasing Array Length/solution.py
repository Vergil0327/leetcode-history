from sortedcontainers import SortedDict


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 1)
        length = [0] * (n + 1)

        nums = [0] + nums  # to 1-indexed
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i]

        mono_map = SortedDict()
        mono_map[0] = 0  # presum[0]+dp[0] = 0
        for i in range(1, n + 1):
            idx = mono_map.bisect_right(presum[i]) - 1
            if idx >= 0:
                _, j = mono_map.peekitem(idx)
                length[i] = length[j] + 1
                dp[i] = presum[i] - presum[j]

            while mono_map and mono_map.peekitem()[0] >= presum[i] + dp[i]:
                mono_map.popitem()

            mono_map[presum[i] + dp[i]] = i
        return length[n]

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        stk = [(0, 0, 0)]  # last + presum, presum, dp

        presum, res = 0, 0
        i = j = 0
        while i < n:
            presum += nums[i]
            j = min(j, len(stk) - 1)

            while j + 1 < len(stk) and presum >= stk[j + 1][0]:
                j += 1
            (val, pre_presum, pre_dp) = stk[j]
            res = curr_dp = pre_dp + 1

            last = presum - pre_presum
            while len(stk) > 0 and stk[-1][0] >= last + presum:
                stk.pop()
            stk.append((last + presum, presum, curr_dp))
            i += 1
        return res