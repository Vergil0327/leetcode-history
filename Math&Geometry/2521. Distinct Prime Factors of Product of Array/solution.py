class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factor = set()
        for num in nums:
            for i in range(2, ceil(sqrt(num))+1):
                if num%i == 0:
                    factor.add(i)
                    while num%i == 0:
                        num //= i

            if num > 1: factor.add(num)

        return len(factor)
