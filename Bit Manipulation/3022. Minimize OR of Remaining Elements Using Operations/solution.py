class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        res = prefix_bits = 0
        for i in range(29, -1, -1):
            test = prefix_bits | (1<<i)
            cnt = cur = 0
            for num in nums:
                if cur == 0:
                    cur = test&num
                else:
                    cur &= test&num
                if cur > 0:
                    cnt += 1
            if cnt > k:
                res |= (1<<i)
            else:
                prefix_bits |= (1<<i)

        return res
