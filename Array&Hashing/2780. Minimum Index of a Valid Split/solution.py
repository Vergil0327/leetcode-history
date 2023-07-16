class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        dominant = [-1] * n
        freq1 = defaultdict(int)
        maxFreq = 0
        for i in range(n-1):
            size = i+1
            freq1[nums[i]] += 1
            if freq1[nums[i]] > maxFreq:
                maxFreq = freq1[nums[i]]
                if maxFreq*2 > size:
                    dominant[i] = nums[i]
               
        res = -1
        freq2 = defaultdict(int)
        maxFreq = 0
        domiElem = -1
        for i in range(n-1, 0, -1):
            size = n-i
            freq2[nums[i]] += 1
            if freq2[nums[i]] > maxFreq:
                maxFreq = freq2[nums[i]]
                domiElem = nums[i]
            if maxFreq*2 > size and dominant[i-1] == domiElem:
                res = i-1
        return res