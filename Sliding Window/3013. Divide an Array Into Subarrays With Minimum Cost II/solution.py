from sortedcontainers import SortedList
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        k -= 1

        sl = SortedList(nums[1:dist+2])
        sl1, sl2 = SortedList(sl[:k]), SortedList(sl[k:])
        res = ksum = sum(sl1)
        
        for l in range(1, n - dist - 1):
            r = l+dist+1

            if nums[l] in sl1:
                ksum -= nums[l]
                sl1.remove(nums[l])
            else:
                sl2.remove(nums[l])

            if len(sl1) == 0 or sl1[-1] >= nums[r]:
                sl1.add(nums[r])
                ksum += nums[r]
            else:
                sl2.add(nums[r])

            while len(sl1) > k:
                ksum -= sl1[-1]
                sl2.add(sl1.pop())
            while len(sl1) < k:
                ksum += sl2[0]
                sl1.add(sl2.pop(0))
            res = min(res, ksum)
        return nums[0] + res
