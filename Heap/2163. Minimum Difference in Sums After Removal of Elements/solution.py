class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3

        tot = sum(nums[:n])
        pq = [-v for v in nums[:n]] # max heap
        heapq.heapify(pq)

        min_sum = [0]*(n+1)
        min_sum[0] = tot
        for i in range(n, 2*n):
            heapq.heappush(pq, -nums[i])
            num = -heapq.heappop(pq)
            tot += nums[i]-num
            min_sum[i-n+1] = tot

        tot = sum(nums[-n:])
        pq = [v for v in nums[-n:]]
        heapq.heapify(pq)

        max_sum = [tot]
        for i in range(2*n-1, n-1, -1):
            heapq.heappush(pq, nums[i])
            num = heapq.heappop(pq)
            tot += nums[i] - num
            max_sum.append(tot)
        max_sum.reverse()

        res = inf
        for x, y in zip(min_sum, max_sum):
            res = min(res, x-y)
        return res
