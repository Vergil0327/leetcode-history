class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i]%=value
        
        counter = Counter(nums)
        MEX = 0
        while True:
            if MEX%value in counter:
                counter[MEX%value] -= 1
                if counter[MEX%value] == 0:
                    del counter[MEX%value]
                MEX += 1
            else:
                break
        
        return MEX