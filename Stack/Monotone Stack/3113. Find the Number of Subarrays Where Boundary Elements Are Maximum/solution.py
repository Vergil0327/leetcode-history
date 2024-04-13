class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        v2idx = defaultdict(list)
        for l in range(n):
            v2idx[nums[l]].append(l)
        
        nextGreater = [n]*n
        stack = []
        for l in range(n):
            while stack and nums[stack[-1]] < nums[l]:
                nextGreater[stack.pop()] = l
            stack.append(l)

        res = 0
        for indices in v2idx.values():
            for l in range(len(indices)):
                k = nextGreater[indices[l]]
                r = bisect_left(indices, k)
                res += r-l
        return res
