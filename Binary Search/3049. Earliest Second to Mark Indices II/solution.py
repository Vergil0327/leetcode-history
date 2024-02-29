class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)

        # firsts[changeIndices] = sec
        firsts = {}
        for i in range(m):
            j = changeIndices[i]-1 # 1-indexed to 0-indexed
            if j not in firsts and nums[j] > 0:
                firsts[j] = i

        # firsts_rev[sec]: i => 當前sec是第一次能對nums[i] zero-out的位置
        first_zero_out = {sec:i for i, sec in firsts.items()}

        def is_possible(sec):
            free_op = 0
            pq = [] # min heap
            for i in range(sec-1, -1, -1):
                if i not in first_zero_out:
                    free_op += 1
                else:
                    heapq.heappush(pq, nums[first_zero_out[i]])
                    if free_op > 0:
                        free_op -= 1
                    else:
                        heapq.heappop(pq)
                        free_op += 1
            return (sum(nums)-sum(pq)) + (len(nums)-len(pq)) <= free_op

        l, r = 0, m+1
        while l < r:
            mid = l + (r-l)//2
            if is_possible(mid):
                r = mid
            else:
                l = mid+1
        return l if l <= m else -1