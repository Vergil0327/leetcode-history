from sortedcontainers import SortedList
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        count = Counter()
        sl = SortedList()
        
        res = []
        for num, f in zip(nums, freq):
            if count[num] in sl:
                sl.remove(count[num])
                
            count[num] += f
            if count[num] > 0:
                sl.add(count[num])
                
            res.append(sl[-1] if sl else 0)
        return res