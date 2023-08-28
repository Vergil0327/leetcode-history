class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors < 4: return primeFactors
        
        count2 = count3 = 0

        if primeFactors%3 == 0:
            count3 = primeFactors // 3
        elif primeFactors%3 == 1: # 拿出4拆成2個2, 其餘全分成3
            count3 = (primeFactors-4)//3
            count2 = 2
        elif primeFactors%3 == 2:
            count3 = (primeFactors-2)//3
            count2 = 1

        return pow(3, count3, 1_000_000_007) * pow(2, count2, 1_000_000_007) % 1_000_000_007
