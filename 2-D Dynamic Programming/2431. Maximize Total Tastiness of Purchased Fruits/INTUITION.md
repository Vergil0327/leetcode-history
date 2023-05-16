# Intuition

dp[i][j][k]: the maximum total tastiness that can be purchased considering first i fruits. (price: [:i], tastiness[:i]) and has j amount with k coupons used.

then the state transfer fn probably be:
```py
price = [0] + price
tastiness = [0] + tastiness
for i in range(1, n+1):
    p, t = price[i], tastiness[i]
    for j in range(maxAmount+1):
        for k in range(maxCoupons+1):
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k]) # don't pick
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-p][k]+t) # pick
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-floor(p/2)][k-1] + t) # pick with coupon
return dp[n][maxAmount][maxCoupons]
```

**edge case**

be aware of `j-p`, `j-floor(p/2)` and `k-1`

**base case**

consider dp[0][j][k]:
- dp[0][0][0] = 0 # zero fruit, zero spent, zero coupon -> 0 tastiness
- dp[0][j][0] = invalid # zero fruit can't cause j amount used
- dp[0][0][k] = invalid

# Complexity

- time complexity
$$O(N*maxAmount*maxCoupons)$$
`100 * 1000 * 5 = 5 * 10^5`

- space complexity
$$O(N*maxAmount*maxCoupons)$$