# Intuition

first we can easily check if we can possibly get an answer or not.

```py
n = len(stones)
size = n%k + n//k
while size >= k:
    size = size%k + size//k
if size != 1: return -1
```

but actually, we can check in O(1) time

since we want to reduce n to 1 pile and each time we merge stones, we remove k-1 stones.
in other words, we want to remove n-1 stones totally by taking M operations and each operations remove k-1 stones.
thus, n-1 = M * (k-1)
(n-1)%(k-1) must be 0

```py
if (n-1)%(k-1) != 0: return -1
```


[X X [X X X] X X X X X X X X X X X X]
 l    i i+k-1                          r

[3,2],4,1
[5,4],1 | 5,[4,1]
9,1 | 5,5

3,[2,4],1
[3,6],1 | 3,[6,1]
9,1 | 3,7

3,2,[4,1]
[3,2],5 | 3,[2,5]
5,5 | 3,7

dp[l][r][k] = dp[l][i][1] + dp[i+1][r][k-1] + sum(stones[l:r+1])


# Intuition

first we can easily check if we can possibly get an answer or not.

```py
n = len(stones)
size = n%k + n//k
while size >= k:
    size = size%k + size//k
if size != 1: return -1
```

but actually, we can check in O(1) time

since we want to reduce n to 1 pile and each time we merge stones, we remove k-1 stones.
in other words, we want to remove n-1 stones totally by taking M operations and each operations remove k-1 stones.
thus, n-1 = M * (k-1)
(n-1)%(k-1) must be 0

```py
if (n-1)%(k-1) != 0: return -1
```


```
[X X X X X] X X X X X X X X X X X X
 l      mid                       r
   1 pile         k-1 piles

[3,2],4,1
[5,4],1 | 5,[4,1]
9,1 | 5,5  -> cost=5+4+1

3,[2,4],1
[3,6],1 | 3,[6,1]
9,1 | 3,7  -> cost=3+6+1

3,2,[4,1]
[3,2],5 | 3,[2,5]
5,5 | 3,7  -> cost=3+2+5

dp[l][r][k] = dp[l][i][1] + dp[i+1][r][k-1] + sum(stones[l:r+1])
```

總共`n`個stones, 最後要變成 `k` piles, 然後`k`piles在合併為`1` pile

所以我們關注當前這一個pile的cost, 那剩下的組成 `k-1` piles
最後那一份的合併就是前面k份的cost加上合併整段的cost

所以:
```py
dp[l][r][k] = dp[l][mid][1] + dp[mid+1][r][k-1]
dp[l][r][1] = dp[l][r][k] + cost(stones[l:r+1])
```

最終答案就看[0:n-1]這區間分成1份的cost為多少, 所以是`dp[0][n-1][1]`

所以我們區間跟切分的份數都由小到大, bottom-up的方式來更新dp

```py
for length in range(1, n+1):
    for l in range(n-length+1): # r = l+length-1 < n
        r = l+length-1
        for k in range(1, K+1):
            for mid in range(l, r):
                dp[l][r][k] = dp[l][mid][1] + dp[mid+1][r][k-1] + cost(stones[l:r+1])
```

再來注意邊界條件
當k=1時, dp[mid+1][r][k-1] = dp[mid+1][r][0]
也就是從[mid+1:r]分成0份的cost, 這沒有意義, 所以我們k從2開始遍歷

那k=1就單獨處理, k=1的cost就是dp[l][r][K] + sum(stones[l:r+1])

```py
for length in range(1, n+1):
    for l in range(n-length+1): # r = l+length-1 < n
        r = l+length-1
        for k in range(2, K+1):
            for mid in range(l, r):
                dp[l][r][k] = dp[l][mid][1] + dp[mid+1][r][k-1]
        dp[l][r][1] = dp[l][r][k] + cost(stones[l:r+1])
```

另外k大於length時也是不合理的, 所以length也從2開始遍歷, length=1單獨處理

對於length=1, 分成1份cost=0

```py
for i in range(n):
    dp[i][i][1] = 0
```