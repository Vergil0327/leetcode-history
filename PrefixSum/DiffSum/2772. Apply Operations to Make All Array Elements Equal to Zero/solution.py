class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        diffArr = [0]*(n+1)
        diffArr[0] += nums[0]
        diffArr[k] -= nums[0]
        for i in range(1, n):
            diffArr[i] += diffArr[i-1]
            
            if diffArr[i] == nums[i]: continue
                
            if nums[i] < diffArr[i]: return False
            if i+k-1 >= n: return False # 往後沒辦法透過操作來讓nums[i]減成0
            
            diff = nums[i]-diffArr[i]
            diffArr[i] += diff
            diffArr[i+k] -= diff
        return True
            
class OtherSolution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        operations = 0
        for i in range(n):
            if nums[i] < operations: return False
                
            nums[i] -= operations
            operations += nums[i]
            if i-k+1 >= 0:
                operations -= nums[i-k+1]
        return operations == 0    

