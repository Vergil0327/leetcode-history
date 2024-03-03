class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(num^k) - num for num in nums]
        delta.sort(reverse=True)
        n = len(delta)

        max_diff = total_diff = 0
        for i in range(0, n-1, 2):
            total_diff += delta[i]+delta[i+1]
            if total_diff > max_diff:
                max_diff = total_diff
        return sum(nums) + max_diff

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res = sum(max(num, num^k) for num in nums)

        cnt = 0
        for num in nums:
            cnt += int(num^k > num)

        if cnt%2 == 0: return res

        sacrifice = inf
        for num in nums:
            sacrifice = min(sacrifice, abs(num - (num^k)))
        return res - sacrifice