# Intuition


## DP definition

dp[k][i]: the maximum floor we can check with certainty with `k` eggs and `i` try

## Base Case

- dp[0][i] = 0 where i from 1 to N:

the maximum floor we can check with certainty with 0 egg and i try is zero.
we need 1 egg at least

- dp[k][0] = 0 where k from 1 to K:

the maximum floor we can check with certainty with k egg and i try is zero.
we need 1 try at least

# State Transfer Eq.

let's check x floor with i-th try:

- if egg breaks, the maximum floor we can cover is same as dp[k-1][i-1]

```
dp[k][i] = dp[k-1][i-1]
```

- if egg not breaks, keep trying with k eggs and i-1 try and we check 1 floor with certainty

```
dp[k][i] = dp[k][i-1] + 1
```

since we can keep trying if we still have eggs which means we didn't break the egg at current try, total floor we can check with certanty is their sum.

thus, `dp[k][i] = dp[k-1][i-1] + (dp[k][i-1] + 1)`

and we try every possible `k` from 1 to K and every possible `i` from 1 to N to see if the floor we can cover `dp[k][i]` is greater or equal to N or not

if `dp[k][i] >= N`, it means we found the minumum try `i`