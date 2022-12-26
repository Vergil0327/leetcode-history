# sorting
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # since it's subseq., don't need to care about order
        # let's pick from smallest one to lartest one until sum > queries[i]
        nums.sort()

        order = deque(sorted([[q, i] for i, q in enumerate(queries)]))
        seqSum, seqSize = 0, 0
        i = 0
        res = [0] * len(queries)
        while order:
            query, idx = order.popleft()
            while i < len(nums) and seqSum+nums[i] <= query:
                seqSum += nums[i]
                seqSize += 1
                i += 1
            res[idx] = seqSize
        return res

# binary search
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        res = []
        for q in queries:
            i = bisect.bisect_right(nums, q)
            res.append(i)
        return res