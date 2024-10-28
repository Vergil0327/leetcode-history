# Brute Force
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        res = 0
        for remove in range(-1, n):
            GCD, LCM = 0, 1
            for i in range(n):
                if i == remove: continue
                GCD = gcd(GCD, nums[i])
                LCM = lcm(LCM, nums[i])
            
            res = max(res, GCD*LCM)
        return res

# O(n)
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        preGCD = [0]
        preLCM = [1]
        for i in range(n):
            preGCD.append(gcd(preGCD[-1], nums[i]))
            preLCM.append(lcm(preLCM[-1], nums[i]))

        sufGCD = [0] * (n+1)
        sufLCM = [1] * (n+1)
        for i in range(n-1, -1, -1):
            sufGCD[i] = gcd(sufGCD[i+1], nums[i])
            sufLCM[i] = lcm(sufLCM[i+1], nums[i])

        res = preGCD[-1] * preLCM[-1]

        for i in range(n):
            GCD = gcd(preGCD[i], sufGCD[i+1])
            LCM = lcm(preLCM[i], sufLCM[i+1])

            res = max(res, GCD*LCM)
        return res