class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        counter = defaultdict(list)
        for i in range(n):
            counter[nums[i]].append(i)
            
        res = n
        for num, indices in counter.items():
            # interval for [indices[-1]: indices[0]]
            sec = ceil((indices[0] + n-1-indices[-1])/2)

            for i in range(len(indices)-1):
                sec = max(sec, ceil((indices[i+1]-indices[i]-1)/2))
                
            res = min(res, sec)
        return res