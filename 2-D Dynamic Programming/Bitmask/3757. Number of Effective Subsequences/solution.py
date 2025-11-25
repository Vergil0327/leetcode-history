"""
# https://space.bilibili.com/206214

1. 求去掉子序列後, 剩下的子序列中, 符合OR(subseq) < OR(nums) 的所有子序列個數
2. 所有子序列個數為2^n, 子序列 OR(subseq) == OR(nums) 的所有子序列個數
    - 全部可能子序列 扣掉 OR(subseq)等於OR(nums)的子序列個數, 剩下的就是所求
    - 從子集合去找符合的個數

if OR = 1 1 1
    1.  000
        001
        010
        011
    2.  100
        101
        110
        111

dp: freq[i][subset]: subset大於i位置的bit都保留, 的子集元素個數
- i-th bit 是0: 只能不選, freq[i][subset] = freq[i-1][subset]
- i-th bit 是1:
    1. 選擇保留1, 大於i-1位置的都保留: freq[i][subset] = freq[i-1][subset]
    2. 選擇不保留, subset^(1<<i)的大於i-1位置都得保留: freq[i][subset] = freq[i-1][subset] + freq[i-1][subset^(1<<i)]

base value: freq[-1][x] = nums 中的 x 個數
"""

from functools import reduce


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 1_000_000_007

        OR = reduce(lambda x, y: x|y, nums)

        # 如果nums只有一種數字, 那麼這個數大魚0時可以把整個數組去掉得到OR=0, 否則無法去掉任何子序列
        if (len(set(nums))) == 1:
            return 1 if OR else 0
        
        mx = OR.bit_length()
        freq = [0] * (1 << mx)
        
        # base value
        for v in nums:
            freq[v] += 1
        
        # SOS DP (Sum over Subsets)
        for i in range(mx):
            for s in range(1 << mx):
                if s & (1 << i):
                    freq[s] += freq[s ^ (1 << i)]
        
        ans = 0
        sub = OR
        
        # Iterate through all subsets of XOR (including XOR itself)
        while True:
            sign = 1
            if (OR ^ sub).bit_count() % 2 > 0:
                sign = -1
            
            ans += sign * pow(2, freq[sub], MOD)
            ans %= MOD
            
            if sub == 0:
                break
            sub = (sub - 1) & OR
        
        ans = pow(2, len(nums), MOD) - ans
        ans = (ans % MOD + MOD) % MOD
        
        return ans