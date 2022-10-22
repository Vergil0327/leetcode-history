# keep nextGreater information in deque and all the index in deque must within sliding window
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        deq = collections.deque()
        res = []
        l, r = 0, 0
        while r < len(nums):
            num = nums[r]
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(r)
            r += 1

            if r-l >= k:
                # nums[deq[0]] is max value since we maintain monotonically decreasing deque
                res.append(nums[deq[0]])
                l += 1
                if deq and deq[0] < l:
                    deq.popleft()

        return res
