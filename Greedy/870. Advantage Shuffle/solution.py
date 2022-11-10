"""
Intuition:
    - preparation:
      we sort `num1` and `nums2` and compare from largest to smallest

    - comparison
      if sorted(nums1)[i] can win sorted(nums2)[i], we choose sorted(nums1)[i] as answer

      else we use smallest one in sorted(nums1) to pair with sorted(nums2)[i]
      then we get more chance to get advantage for next round

    - restore order
      since what we want is using nums1 to compare with original nums2,
      we need to know every element's index in nums2 after sorting
"""

# Deque + Sorting
# O(nlogn)
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        res = [0]*n
        deq = deque(sorted(nums1))
        sortedNums2 = sorted([[num, i] for i, num in enumerate(nums2)])

        for i in range(n-1, -1, -1):
            if deq[-1] > sortedNums2[i][0]:
                j = sortedNums2[i][1]
                res[j] = deq.pop()
            else:
                j = sortedNums2[i][1]
                res[j] = deq.popleft()
        return res

class ConciseSolution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1)
        deq = deque(sorted(nums1))
        for num, j in sorted([[num, i] for i, num in enumerate(nums2)], reverse=True):
            res[j] = deq.pop() if deq[-1] > num else deq.popleft()
        return res

# Two Pointers + MaxHeap
# O(nlogn)
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        res = [0]*n

        maxHeap = [[-num, i] for i, num in enumerate(nums2)]
        heapq.heapify(maxHeap)
        
        nums1.sort()
        l, r = 0, len(nums1)-1 # smallest & largest
        while maxHeap:
            num2, idx = heapq.heappop(maxHeap)
            
            if nums1[r] > -num2:
                res[idx] = nums1[r]
                r-=1
            else:
                res[idx] = nums1[l]
                l+=1
        return res