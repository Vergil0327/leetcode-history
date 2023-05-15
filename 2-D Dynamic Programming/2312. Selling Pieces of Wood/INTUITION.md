# Intuition

since m, n are small, we can try all the possible cuts
for each cut, the state transfer has already been told in desciption:

```
X X X X | X X X X
       cut      j

dp[i][j] = dp[i][j-cut] + dp[cut]
```

```
X X X X X X X X
_______________ cut
X X X X X X X X 
X X X X X X X X i

dp[i][j] = dp[i-cut][j] + dp[cut][j]
```


thus, we can update dp[i][j] like this, try to cut in every possible (i,j) shape.
since there are multiple dp[i][j], we choose maximum

```
for i in range(1, m+1):
    for j in range(1, n+1):
        for cut in range(1, i):
            dp[i][j] = max(dp[i][j], dp[i-cut][j] + dp[cut][j])

        for cut in range(1, j):
            dp[i][j] = max(dp[i][j], dp[i][j-cut] + dp[i][cut])
```

and the base case is our prices array
```py
for h, w, p in prices:
    dp[h][w] = p
```