class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        maxHeap = []
        count = Counter()
        res = []
        for num, f in zip(nums, freq):
            count[num] += f
            heappush(maxHeap, [-count[num], num])
            while maxHeap and count[maxHeap[0][1]] != -maxHeap[0][0]:
                heappop(maxHeap)
            res.append(-maxHeap[0][0] if maxHeap else 0)
        return res