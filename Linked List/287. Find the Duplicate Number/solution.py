# think as linked list cycle problem
# nums[i] is our pointer which tells where we should go
# once slow pointer meet fast pointer, we use another pointer and start from 0
# move step by step, once we meet, it's linked list cycle => it's duplicate number
# Floyd's Algorithm (slow fast pointer)
# time: O(n)
# space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# 數值範圍[1,n]去猜測mid
# 如果不是duplicate number, 小於等於mid的數值數目應該要小於等於mid

# ex. [1,2,3,3]
# mid = 1 => count should be 1
# mid = 2 => count = 2
# mid = 3 => count = 4
# time: O(nlogn)
# space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1 # n+1 nums
        l, r = 1, n

        while l < r:
            mid = l + (r-l)//2

            count = sum([1 for num in nums if num <= mid])
            if count <= mid:
                l = mid+1
            else:
                r = mid
        return l