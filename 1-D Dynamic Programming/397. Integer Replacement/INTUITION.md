# Top-Down

## Intuition

由上往下的Top-Down DFS Decision Tree很顯而易見的，舊照個操作就好:
- 當n為偶數，肯定除以二
- 當n為奇數，`n+1`, `n-1`兩個決定取最小操作

持續遞歸直到 n = 1即可

## Complexity

- time complexity

$$O(logn)$$ approximately

- space complexity

$$O(logn)$$


# Bottom-Up

## Intuition

由於n可以到很大($2^31$-1)，Bottom-Up的方式會在leetcode上TLE，但還是能研究一下

**Definition**
首先我們這樣定義:
`dp[i] = the minimum operations for i`

**Base Case**
`dp[1] = 0`

**State Transfer Fn**

- 當i為偶數
```py
dp[i] = dp[i//2]+1
```

- 當i為奇數
```py
dp[i] = min(dp[i-1], dp[i+1])+1
```

但對於i來說dp[i+1]是未知的，無法透過未知來求未知的i

不過由於i為奇數時，i+1為偶數，因此我們可以套用上面偶數的關係式使得:
`dp[i+1] = dp[(i+1)//2]+1`
在代回原本關係式即得:

```py
dp[i] = min(dp[i-1], dp[i+1])+1
      = min(dp[i-1], dp[(i+1)//2]+1)+1
```

```py
if i%2 == 0: # i is even
    dp[i] = dp[i//2] + 1
else: # i is odd
    dp[i] = min(dp[(i-1)//2]+1, dp[(i+1)//2]+1)+1
```

## Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$