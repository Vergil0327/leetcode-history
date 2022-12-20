class Solution:
    # CtrlA CtrlC佔了兩步，剩下全部CtrlV的話會有n-2次
    # Print A 跟 CtrlV剛好會是trade-off
    # Print A 太多太少都不會是最佳，Print A應當要跟CtrlV次數接近，因此全部試過一遍取最大
    @functools.lru_cache(None)
    def maxA(self, n: int) -> int:
        res = n
        for i in range(1, n-2):
            res = max(res, self.maxA(i) * (n-1-i))
        return res

    def maxA(self, n: int) -> int:
        # 對於 (n, a_num, copy) 這些狀態，
        # 螢幕上最终最多能有 dp(n, a_num, copy) 個 A
        @functools.lru_cache(None)
        def dfs(n, a_num, copy):
            # base case
            if n <= 0: return a_num
            # 3種選擇全試一遍，選最大
            return max(
                    dfs(n - 1, a_num + 1, copy),    # A
                    dfs(n - 1, a_num + copy, copy), # C-V
                    dfs(n - 2, a_num, a_num)        # C-A C-C
                )

        # 可以按 N 次按鍵，螢幕和Clipboard裡都還沒有 A，所以起始值為(n,0,0)
        return dfs(n, 0, 0)

    # optimized by greedy
    # there are 2 optimized way:
    # 1. A A A A A .... A A A, keep printing A when n is small
    # 2. A A A CA CC CV CV CV CV..., keep pasting when n is large
    def maxA(self, n: int) -> int:
        # dp[i]: the maximum number of A after i operations
        dp = [0] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            # print A
            dp[i] = dp[i-1] + 1
            for j in range(2, i):
                # CA, CC two steps, dp[j-2]
                # i-j 次 Paste，再加上自己，總共(i-j+1)個dp[j]
                dp[i] = max(dp[i], dp[j] * (i-j+1))
        return dp[n]

        
    
    def maxA(self, n: int) -> int:
        # dp[i]: the maximum number of A after i steps
        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = i
            for j in range(1, i-2): # i-2 operations (CtrlA, CtrlC)
                dp[i] = max(dp[i], dp[j]*(i-j+1))
        return dp[n]


