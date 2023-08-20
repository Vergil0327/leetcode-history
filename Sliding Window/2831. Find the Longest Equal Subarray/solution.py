class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        MAP = defaultdict(lambda: deque())
        res = 0
        for i, num in enumerate(nums):
            MAP[num].append(i)
            
            # l, r = MAP[num][0], MAP[num][-1]
            # subarray size = r-l+1
            # subarray size after deletion = len(MAP[num])
            # deletion = subarray size - subarray size after deletion
            #          = r-l+1 - len(MAP[num])
            # if deletion > k, we should pop left-most num to maintain a valid window for num
            while MAP[num] and MAP[num][-1]-MAP[num][0]+1 - len(MAP[num]) > k:
                MAP[num].popleft()

            res = max(res, len(MAP[num]))
        return res
