class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        m, n = len(str(nums[0])), len(nums)
        digits = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                digits[j][i] = nums[i]%10
                nums[i] //= 10

        count = [defaultdict(int) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count[i][digits[i][j]] += 1

        res = 0
        for i in range(m):
            for num1 in range(10):
                for num2 in range(num1+1, 10):
                    numDiff = count[i][num1] * count[i][num2]
                    res += numDiff
        return res