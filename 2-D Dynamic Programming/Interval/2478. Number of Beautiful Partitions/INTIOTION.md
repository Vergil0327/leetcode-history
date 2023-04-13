### How to Optimized O(N^3) Time Complexity ?

我們來看看這段主要的狀態轉移方程

```python
for i in range(1, n+1): # end index
    for j in range(1, k+1):
        if isprime(s[i]):
            dp[i][j] = 0 # can't be ending position
            continue

        # start index, 前面j-1份所以k從j開始
        # k+minLength-1 <= i -> k <= i-minLength+1
        for k in range(j, (i-minLength+1)+1):
            if isprime(s[k]):
                dp[i][j] += dp[k-1][j-1] # be aware of edge case
                dp[i][j] %= MOD
```

#### Step 1 - 觀察狀態轉移方程

首先我們可以看到我們的: `dp[i][j] += dp[k-1][j-1]`
dp[i][j]是一段連續的加總，並且`j`只跟前一個`j-1`有關

所以如果我們固定`j`的話，那`j-1`也固定
另外外面兩層循環，從是從1開始，所以互換也沒關係

因此把`line 6: for i in range(1, n+1)`跟`line 7: for j in range(1, k+1)`互換的話，
我們可以得到等價的結果

```python
for j in range(1, k+1):
    presum = 0
    for i in range(1, n+1): # end index
        if isprime(s[i]):
            dp[i][j] = 0 # can't be ending position
            continue

        # start index, 前面j-1份所以k從j開始
        # k+minLength-1 <= i -> k <= i-minLength+1
        for k in range(j, (i-minLength+1)+1):
            if isprime(s[k]):
                dp[i][j] += dp[k-1][j-1] # be aware of edge case
                dp[i][j] %= MOD
```

#### Step 2 - 計算presum

那既然`j`已經固定，我們現在僅需要知道我們的`presum`
我們可以在每輪`j`的開始定義一個`presum`
而原本的 `+=dp[k-1][j-1]`其實就是`j-1`時的前`k-1`個字符的個數加總

```
XXXXX[XXXXX]
      k   i
    k-1
dp[i][j] = dp[k-1][j-1] + current
```
`k-1`可以用`i-minLength`來表示

所以我們`presum`可以這樣來計算
```python
presum += dp[i-minLength][j-1]
```
其中`i-minLength`根據敘述必須**不為質數**並且`i-minLength+1`必須**為質數**(因為是下個partition的開頭)

所以我們的程式碼可以改成
```python
for j in range(1, k+1):
    presum = 0
    for i in range(1, n+1): # end index
        if i-minLength >= 0 and not isprime(i-minLength) and isprime(i-minLength+1):
        presum += dp[i-minLength][j-1]
        presum %= MOD
```

#### Step 3 - 更新dp

在得到`presum`後，我們便可以更新我們原本的`dp[i][j] += dp[k-1][j-1]`為

```python
# dp[i][j] += dp[k-1][j-1]
dp[i][j] = presum
dp[i][j] %= MOD
```

並且根據定義，在`i`這個位置`s[i]`必須**不為質數**

所以最終程式碼:
```python
for j in range(1, K+1):
    presum = 0
    for i in range(1, n+1): # end index
        if i-minLength >= 0 and (not isprime(s[i-minLength])) and isprime(s[i-minLength+1]):
            presum += dp[i-minLength][j-1]
            presum %= MOD
        
        if not isprime(s[i]):
            dp[i][j] = presum
            dp[i][j] %= MOD
```

成功透過前綴和降低一個order的時間複雜度
