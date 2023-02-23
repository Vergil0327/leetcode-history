from typing import List

class Solution:
     def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 1000000007
        OFFSET = max(sum(nums1), sum(nums2))
        
        n = len(nums1)
        nums1 = [0] + nums1
        nums2 = [0] + nums2
        
        res = 0
        dp = [[0] * (2*OFFSET+1) for _ in range(n+1)]

        for i in range(1, n+1):
            dp[i][OFFSET+nums1[i]] += 1
            dp[i][OFFSET-nums2[i]] += 1
            for subSum in range(-OFFSET, OFFSET+1):
                # 選擇nums1[i]後, 即加上nums1[i] DIFF 為0，可以從DIFF-nums1[i]轉移過來
                if -OFFSET <= subSum-nums1[i] <= OFFSET:
                    dp[i][subSum+OFFSET] += dp[i-1][subSum-nums1[i]+OFFSET]
                
                # 選擇nums2[i]後, 即扣掉nums2[i] DIFF 為0，可以從DIFF+nums1[i]轉移過來
                if -OFFSET <= subSum+nums2[i] <= OFFSET:
                    dp[i][subSum+OFFSET] += dp[i-1][subSum+nums2[i]+OFFSET]
            
            res += dp[i][0+OFFSET] # 考慮nums1[:i], nums2[:i], diff為0
            res %= MOD
        return res
