# Intuition

Because each node has and only has a father, so this problem is the continuous jumping on the only path
=> thinks of the binary lifting.

# k <= 10^10 < 2^34

define dp[i][j][0]: the end position from j after move 2^i steps
define dp[i][j][1]: the score from j after move 2^i steps

state transfer:
```
iterate i (means 2^i steps):
    iterate each j starting position:
        prev = dp[i-1][j][0]
        dp[i][j][0] = dp[i-1][prev][0]
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][prev][1]
```

then we can calculate scores from dp table

k can represent as binary: 2^a + 2^b + 2^c + ...

if we start from `i` and k = 6 = 4 + 2
then, dp[4][i] + dp[2][j] where j' = 4 steps from i and j = 2 steps from j, i.e. i -> 4 steps -> j' -> 2 steps -> j