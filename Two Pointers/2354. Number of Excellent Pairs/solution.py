class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        SET = set(nums)
        arr = sorted([bin(num).count("1") for num in SET])
        n = len(arr)

        res = 0
        j = n-1
        for i in range(n):
            while j >= 0 and arr[i] + arr[j] >= k:
                j -= 1
            res += n-1-j

        return res


        # X X X X X X X X X
        # Y Y Y Y Y Y Y Y Y
        # OR: get every non duplicate 1-bit
        # AND: get every duplicate 1-bit

        # num1: 1 1 1 1 1 0 0 0 1 0 1
        # num2: 0 1 1 1 0 1 1 0 1 1 0
        # AND: 4
        # OR: 10
        # count1(num1) + count1(num2) = 7 + 7 = 14

        # Therefore:
        # count1(num1&num2) + count1(num1|num2) >= k
        # => count1(num1) + count1(num2) >= k