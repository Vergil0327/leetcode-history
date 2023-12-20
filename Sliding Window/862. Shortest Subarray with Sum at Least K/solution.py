class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = inf
        presum_j = deque() # store index `j` of presum
        presum = list(accumulate(nums, initial=0))
        for i in range(len(presum)):
            while presum_j and presum[presum_j[-1]] >= presum[i]:
                presum_j.pop()
            while presum_j and presum[i]-presum[presum_j[0]] >= k:
                res = min(res, i-presum_j.popleft())
            presum_j.append(i)

        return -1 if res == inf else res
