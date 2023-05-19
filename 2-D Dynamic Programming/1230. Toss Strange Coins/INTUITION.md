# Intuition

define `dp[i][j]`: prob of j coins face up after tossing first i coins.

considering previous `i-1` coins:
- if i-th coins is j-th facing head coin, then `dp[i][j] = dp[i-1][j-1]*(prob[i])` where prob[i] is the probability of facing head of i-th coin

- if i-th coins is not j-th facing head coin, then `dp[i][j] = dp[i-1][j]*(1-prob[i])` where 1-prob[i] is the probability of NOT facing head of i-th coin

thus, dp[i][j] is the sum of these two cases's probabilities

**Base case**
considering 0 coin to get 0 facing-head coin, the probability is 1
dp[0][0] = 1