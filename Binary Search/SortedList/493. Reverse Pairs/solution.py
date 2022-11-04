from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        l = SortedList()
        
        cnt = 0
        for i in range(len(nums)-1, -1, -1):
            cnt += l.bisect_left(nums[i]/2)
            l.add(nums[i])
        return cnt

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        l = []
        
        cnt = 0
        for i in range(len(nums)-1, -1, -1):
            cnt += bisect.bisect_left(l, nums[i]/2)
            bisect.insort_left(l, nums[i]) 
        return cnt