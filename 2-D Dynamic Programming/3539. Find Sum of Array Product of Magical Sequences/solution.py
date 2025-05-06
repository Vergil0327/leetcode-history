MOD = 10**9 + 7
class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        @cache
        def dfs(size, k, i, carry):
            if size == M: return 1 if k==carry.bit_count() else 0
            if i >= len(nums): return 0
            remain = M-size
            if size > M or k<0 or remain+carry.bit_count() < k: return 0
            
            res = 0
            for cnt in range(remain+1):
                prod = math.comb(remain, cnt) * pow(nums[i], cnt, MOD) % MOD
                cur = carry+cnt
                res += prod * dfs(size+cnt, k-(cur%2), i+1, cur//2)
            return res%MOD
        return dfs(0, K, 0, 0)