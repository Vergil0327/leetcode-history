# Intuition

```
satisfaction in order: X X X X X X X X X
              time[i]: 1 2 3 4 5 6 7 8 9
```

since we can choose in any order and like-time coefficient is defined as `time[i] * satisfaction[i]`, it's intuitively to **sort** satisfaction in increasing order first.
then we can get larger coefficient by taking larger `time[i]` with `satisfaction[i]`

after sorting, it becomes a take or not-take problem and we can use dynamic programming technique to solve it.

**dp definition**

for each round of selection, we need to know how many satisfaction[i] we picked so far to know the `time[i]`.
thus, define `dp[i][j]: the maximum sum of like-time coefficient considering first i dishes and choose j dishes`

then, state transfer fn is clear

- if we don't choose i-th dish, $dp[i][j] = dp[i-1][j]$
- if we choose i-th dish, $dp[i][j] = dp[i-1][j-1] + satisfaction[i] * j$

and we choose maximum from these two strategies.

**base case**

because we want to get maximum, set initial value of dp[i][j] to -infinity first.

and we need to define dp[0][j] and dp[i][0] to update dp[i][j] where i from 1 to n

0 selection at 0-th round, max sum is zero:
`dp[0][0] = 0`

0 selection at i-th round, max sum is zero:
`dp[i][0] = 0`

>I use **1-indexed** to get rid of out-of-bound error when i==0, dp = dp[-1].
>also transform satisfaction to **1-indexed** to match with dp

# Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(n^2)$$
