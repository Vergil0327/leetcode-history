# find answer from right to left and keep array sorted
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, arr = [], []
        
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            cnt = bisect.bisect_left(arr, num)
            res.append(cnt)
            bisect.insort_left(arr, num)

        return reversed(res)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, arr = [], []
        
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            j = bisect.bisect_left(arr, num)
            res.append(j)
            arr.insert(j, num) # insort_left is just bisect_left again then insert

        return reversed(res)

from sortedcontainers import SortedList

# nlog(n)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, arr = [], SortedList()
        
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            cnt = arr.bisect_left(num)
            res.append(cnt)
            arr.add(num)

        return reversed(res)
