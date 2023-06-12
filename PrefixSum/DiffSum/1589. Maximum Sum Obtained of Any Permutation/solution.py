class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * (n+1)
        for start, end in requests:
            diff[start] += 1
            diff[end+1] -= 1

        for i in range(1, n+1):
            diff[i] += diff[i-1]

        nums.sort(reverse=True)
        diff.sort(reverse=True)
        res = 0
        mod = 10**9+7

        for num, cnt in zip(nums, diff):
            res = (res + num * cnt) % mod
        return res

        # numContribution = [-contrib for contrib in diff if contrib > 0]
        # heapq.heapify(numContribution)

        # maxNumHeap = [-num for num in nums]
        # heapq.heapify(maxNumHeap)
        
        # mod = 10**9+7
        # res = 0
        # while numContribution:
        #     cnt = -heapq.heappop(numContribution)
        #     currMaxNum = -heapq.heappop(maxNumHeap)
        #     res = (res + cnt * currMaxNum) % mod
        # return res
