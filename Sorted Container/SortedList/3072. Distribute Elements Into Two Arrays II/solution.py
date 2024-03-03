from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = SortedList([(nums[0], 0)])
        arr2 = SortedList([(nums[1], 1)])
        for i in range(2, n):
            x = len(arr1) - arr1.bisect_right((nums[i], i))
            y = len(arr2) - arr2.bisect_right((nums[i], i))

            if x > y:
                arr1.add((nums[i], i))
            elif x < y:
                arr2.add((nums[i], i))
            else:
                if len(arr1) <= len(arr2):
                    arr1.add((nums[i], i))
                else:
                    arr2.add((nums[i], i))

        res = []
        for v, _ in sorted(list(arr1), key=lambda x:x[1]):
            res.append(v)
        for v, _ in sorted(list(arr2), key=lambda x:x[1]):
            res.append(v)
        return res
        
        