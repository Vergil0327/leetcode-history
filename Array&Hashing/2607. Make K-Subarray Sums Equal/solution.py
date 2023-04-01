class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            j = i
            nums = []
            while arr[j] != -1:
                nums.append(arr[j])
                arr[j] = -1
                j = (j+k)%n

            if not nums: continue
            
            nums.sort()
            mid = nums[len(nums)//2]
            for num in nums:
                res += abs(num-mid)
        return res