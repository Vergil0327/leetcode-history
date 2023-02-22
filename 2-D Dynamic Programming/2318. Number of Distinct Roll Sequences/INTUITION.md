# Intuition

首先這題是個動態規劃題目，對於合法的distinct sequence, 必須滿足下面三個條件

假設我們骰出來的數字依序是: _ _ _ _ _ X Y Z 

1. 對於當前骰出來的`Z`來說，必須 `Y != Z`
2. `gcd(Y, Z) == 1`
3. `X != Z`

首先最直覺想到的是 dp[i][Z] += dp[i][Y]
但由於還得滿足第三個條件，這代表我們必須知道前兩輪我們骰了什麼，然後才能判斷能不能進行狀態轉移
既然這樣，我們dp的狀態就在多紀錄一個，我們這樣定義:

dp[i][curr][last]: the number of distinct sequence which rolled `i` times and current roll is `curr` and previous roll is `last`.

那這樣狀態轉移就是:

`dp[i][Z][Y] += dp[i-1][Y][X] if Y != Z and X != Z and gcd(Y, Z) == 1`

所以我們最外層循環就會是i，然後內層循環就循環 X, Y, Z

```py
for i in range(1, n+1):
    for Z in range(1, 7):
        for Y in range(1, 7):
            if Y == Z or gcd(Y, Z) != 1: continue
            for X in range(1, 7):
                if X == Z: continue
                dp[i][Z][Y] += dp[i-1][Y][X]
```

最後答案就是考慮`n`次下的所有可能的方法數:

```py
total = 0
for i in range(1, 7):
    for j in range(1, 7):
        total += dp[n][i][j]
        total %= MOD
return total
```

**Base Case**

再來就是來看base case 跟檢查下標

首先我們狀態轉移方程是建立在，i, X, Y, Z都合法的情況下
首先從下標來看，i-1至少要大於等於零，至少為2

但dp[i][Z][Y]建立在dp[i-1][Y][X]是合法的時候才能從dp[i-1][Y][X]轉移過來
但`i=2`時，並不存在`X`
所以`i`至少必須從`3`開始

```py
for i in range(3, n+1): # i from 3 to n
    for Z in range(1, 7):
        for Y in range(1, 7):
            if Y == Z or gcd(Y, Z) != 1: continue
            for X in range(1, 7):
                if X == Z: continue
                dp[i][Z][Y] += dp[i-1][Y][X]
```

因此我們必須單獨考慮`i=1`跟`i=2`的情況

當`i=1`，distinct sequence其實骰1-6都是合法的，可以直接返回`6`
當`i=2`，合法的distinct sequence就是連續兩次骰出來的X, Y必須`X!=Y and gcd(X, Y) == 1`，因此:

```py
for X in range(1, 7):
    for Y in range(1, 7):
        if X != Y and gcd(X, Y) == 1:
            dp[2][X][Y] = 1
```
如果 n = 2，就直接返回 `sum(map(sum, dp[2]))`

# Optimized

甚至可以找出對於每個X來說(1-6)，GCD為1的合法數有哪些，就不用每次都遍歷1-6

```py
GCD_One = [[] for _ in range(7)]
for i in range(1, 7):
    for j in range(1, 7):
        if gcd(i, j) == 1:
            GCD_One[i].append(j)

for i in range(3, n+1): # i from 3 to n
    for Z in range(1, 7):
        for Y in GCD_One[X]:
            if Y == Z: continue
            for X in range(1, 7):
                if X == Z: continue
                dp[i][Z][Y] += dp[i-1][Y][X]
```

# Complexity

- time complexity
$$O(n*6*6*6)$$

- space complexity
$$O(n*6*6)$$

