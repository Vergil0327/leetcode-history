class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if target > sum(nums): return -1

        bits = [0] * 32
        for num in nums:
            bits[int(log2(num))] += 1

        res = 0
        need = inf
        for i in range(31):
            if (target>>i)&1:
                if bits[i]:
                    bits[i] -= 1
                else:
                    need = min(need, i)

            if bits[i] > 0 and need < i:
                bits[i] -= 1
                res += i-need
                need = inf

            bits[i+1] += bits[i]//2
        return res
