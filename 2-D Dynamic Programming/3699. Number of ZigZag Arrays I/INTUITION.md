# Intuition

直覺想到top-down dp => TLE
```py
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7

        @cache
        def dfs(i, prev1, needGreater):
            if i >= n: return 1

            start = prev1+1 if needGreater else l
            end = r+1 if needGreater else prev1
            res = 0
            for num in range(start, end):
                res += dfs(i+1, num, not needGreater)
                res %= mod
            return res

        res = 0
        for num in range(l, r+1):
            res += dfs(1, num, True)
            res += dfs(1, num, False)
            res %= mod
        return res
```

試了一下即使把`@cache`換成dp array也不會有更近一步的優化
時間複雜度O(n^3)實在是太慢了

再來試著換成bottom-up dp來看有沒有什麼能優化的地方
dp0[i][num]: 0代表`not needGreater == True`, 代表要取第i個數時, 該數需要小於num
dp1[i][num]: 0代表`needGreater == True`, 代表要取第i個數時, 該數需要大於num

```py
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7

        dp0 = [[0 for _ in range(r+1)] for _ in range(n)]
        dp1 = [[0 for _ in range(r+1)] for _ in range(n)]
        for i in range(l, r+1):
            dp0[0][i] = 1
            dp1[0][i] = 1
        
        for i in range(1, n):
            for num in range(l, r+1):
                dp1[i][num] += sum(dp0[i-1][x] for x in range(l, num))
                dp1[i][num] %= mod
                dp0[i][num] += sum(dp1[i-1][x] for x in range(num+1, r+1))
                dp0[i][num] %= mod
        return (sum(dp1[n-1]) + sum(dp0[n-1]))%mod
```

    
這邊會看到subarray sum可以換成prefix sum來達到O(1)計算
所以我們如果紀錄prefix sum dp, 就能讓下一輪O(1) update
那自然而然就能得出O(n^2) solution

```py

from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7

        dp0 = [[0 for _ in range(r+1)] for _ in range(n)]
        dp1 = [[0 for _ in range(r+1)] for _ in range(n)]
        for i in range(l, r+1):
            dp0[0][i] = 1
            dp1[0][i] = 1
        
        presumDp0 = list(accumulate(dp0[0], initial=0))
        presumDp1 = list(accumulate(dp1[0], initial=0))
        for i in range(1, n):
            next_presumDp0 = [0] * (r+2)
            next_presumDp1 = [0] * (r+2)
            for num in range(l, r+1):
                # dp1[i][num] += sum(dp0[i-1][x] for x in range(l, num))
                dp1[i][num] += presumDp0[num] - presumDp0[l]
                dp1[i][num] %= mod

                # dp0[i][num] += sum(dp1[i-1][x] for x in range(num+1, r+1))
                dp0[i][num] += presumDp1[r+1] - presumDp1[num+1]
                dp0[i][num] %= mod

                next_presumDp0[num+1] = next_presumDp0[num] + dp0[i][num]
                next_presumDp1[num+1] = next_presumDp1[num] + dp1[i][num]

            presumDp0 = next_presumDp0
            presumDp1 = next_presumDp1

        res = 0
        for i in range(l, r+1):
            res += dp1[n-1][i] + dp0[n-1][i]
            res %= mod
        return res
```

那剩下就是些枝微末節的優化了, 像是其實[0,l-1]這段都是不合法的, dp都會是0
其實我們只需要[l,r]這段區間
所以我們其實可以shift一下

```py
from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        
        # Shift range to [0, r-l]
        range_size = r - l
        r = range_size
        l = 0
        
        # Only keep current row, not all n rows
        dp0 = [1] * (r + 1)
        dp1 = [1] * (r + 1)
        
        presumDp0 = list(accumulate(dp0, initial=0))
        presumDp1 = list(accumulate(dp1, initial=0))
        
        for i in range(1, n):
            next_dp0 = [0] * (r + 1)
            next_dp1 = [0] * (r + 1)
            next_presumDp0 = [0] * (r + 2)
            next_presumDp1 = [0] * (r + 2)
            
            for num in range(l, r+1):
                # dp1[num] += sum(dp0[x] for x in range(l, num))
                next_dp1[num] = presumDp0[num] - presumDp0[l]
                next_dp1[num] %= mod

                # dp0[num] += sum(dp1[x] for x in range(num+1, r+1))
                next_dp0[num] = presumDp1[r+1] - presumDp1[num+1]
                next_dp0[num] %= mod

                next_presumDp0[num+1] = next_presumDp0[num] + next_dp0[num]
                next_presumDp1[num+1] = next_presumDp1[num] + next_dp1[num]

            dp0 = next_dp0
            dp1 = next_dp1
            presumDp0 = next_presumDp0
            presumDp1 = next_presumDp1

        res = 0
        for i in range(l, r+1):
            res += dp1[i] + dp0[i]
            res %= mod
        return res
```

然後再進一步優化, 把dp0, dp1分開處理
並將presum_dp降至O(1) space, 用一個變數`runngin_sum`處理

```py
from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        
        # Shift range
        range_size = r - l
        r = range_size
        l = 0
        
        # Initialize: all values are 1
        dp0 = [1] * (r + 1)
        dp1 = [1] * (r + 1)
        
        for iteration in range(1, n):
            next_dp0 = [0] * (r + 1)
            next_dp1 = [0] * (r + 1)
            
            # Compute all dp1 values efficiently
            running_sum = 0
            for num in range(r + 1):
                next_dp1[num] = running_sum
                running_sum = (running_sum + dp0[num]) % mod
            
            # Compute all dp0 values efficiently  
            running_sum = 0
            for num in range(r, -1, -1):
                next_dp0[num] = running_sum
                running_sum = (running_sum + dp1[num]) % mod
            
            dp0 = next_dp0
            dp1 = next_dp1
        
        # Sum all final values
        return sum(dp0[i] + dp1[i] for i in range(r + 1)) % mod
```