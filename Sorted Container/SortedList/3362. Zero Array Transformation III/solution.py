from sortedcontainers import SortedList
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        
        candidates = SortedList()
        current = SortedList()
        j = 0
        for i, num in enumerate(nums):
            # valid queires for us to decremenet num
            while j < len(queries) and queries[j][0] <= i:
                candidates.add(queries[j][1])
                j += 1

            # remove no-contribution-queries from current
            while current and current[0] < i:
                current.pop(0)

            while num > len(current):
                if not candidates or candidates[-1] < i: # no more queries can decrement num to 0
                    return -1

                current.add(candidates.pop())
            
        return len(candidates)
