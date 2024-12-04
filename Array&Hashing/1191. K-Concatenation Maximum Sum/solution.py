class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        
        # kadane
        mx_sum = cur = 0
        for num in arr:
            cur = max(0, cur+num)
            mx_sum = max(mx_sum, cur)

        if k == 1:
            return mx_sum%mod

        max_presum = cur = 0
        for num in arr:
            cur += num
            max_presum = max(max_presum, cur)

        max_sufsum = cur = 0
        for num in reversed(arr):
            cur += num
            max_sufsum = max(max_sufsum, cur)
        
        total = sum(arr)
        return max(mx_sum, total*k, (max_presum+max_sufsum+max(0, k-2) * max(0, total))) % mod
