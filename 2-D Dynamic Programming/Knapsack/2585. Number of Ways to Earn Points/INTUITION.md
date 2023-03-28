# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Basic DP problem, it's easier than [3rd problem](https://leetcode.com/problems/split-the-array-to-make-coprime-products/description/)...

we can define dp as:
dp[i][j]: the number of ways you can earn exactly j points in the exam considering types[:i]

and the state transfer fn is straightforward.

- since we choose types[i] based on previous choice only, it means each state only depends on previous state. dp[i] only depends on dp[i-1]
- if current points is `j`, then previous points should be `j-cnt*mark`

```
[count, mark] = types[i]
dp[i][j] += dp[i-1][j-cnt*mark] where cnt from 0 to count
```

**Base Case**

choose nothing to make `0` points is also **ONE** valid way
dp[0][0] = 1

# Complexity
- Time complexity:
$$O(n*target*count)$$

- Space complexity:
$$O(n*target)$$

# Optimized

we can further optimize by:

由於j-cnt*mark 必須 >= 0
推導一下關係式可得: cnt <= j//mark
所以下方for-loop可改為
```py
for cnt in range(count+1):
    dp[i][j] += dp[i-1][j-cnt*mark] if j-cnt*mark>=0 else 0
    dp[i][j] %= MOD

# 改為 
for cnt in range(min(j//mark, count)+1):
    dp[i][j] += dp[i-1][j-cnt*mark]
    dp[i][j] %= MOD
```

# Space-Optimization - 1-D DP

owing to the fact that dp[i] only depends on dp[i-1], we can further reduce space complexity by using only 2 dp array

if we update dp state from largest to smallest, we can even just use 1 dp array.

```py
dp = [0]*(target+1)
dp[0] = 1

types = [[-1, -1]] + types
for i in range(1, n+1):
    count, mark = types[i][0], types[i][1]
    for j in range(target, -1, -1):
        for cnt in range(1, min(j//mark, count)+1):
            dp[j] += dp[j-cnt*mark]
            dp[j] %= MOD

return dp[target]
```

be aware of this line: `for cnt in range(1, min(j//mark, count)+1):`

dp[i][j] = dp[i-1][j] if cnt = 0,
it means if cnt = 0, dp[i][j] inherits value from dp[i-1][j].
 => dp[j] = prevdp[j] when cnt = 0

since we only use 1 dp array, we can't update dp[0] like below at each iteration when cnt = 0:
```py
for j in range(target, -1, -1):
    for cnt in range(1, min(j//mark, count)+1):
        # when cnt == 0
        dp[0] += dp[0]
```

thus, we iterate cnt from 1 to min(j//mark, count)+1.