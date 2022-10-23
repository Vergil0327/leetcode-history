
class Solution:
    def gcd(self, num1, num2):
            while num2:
                num1, num2 = num2, num1%num2
            return num1
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            gcd = nums[i]
                
            for j in range(i, len(nums)):
                gcd = self.gcd(gcd, nums[j])
                if gcd == k:
                    cnt += 1
                elif gcd < k: # boost performance by checking this since gcd only get smaller
                    break
        return cnt


class BruteForceSolution:
    def gcd(self, num1, num2):
            while num2:
                num1, num2 = num2, num1%num2
            return num1
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            gcd = nums[i]
                
            for j in range(i, len(nums)):
                gcd = self.gcd(gcd, nums[j])
                if gcd == k:
                    cnt += 1
        return cnt
