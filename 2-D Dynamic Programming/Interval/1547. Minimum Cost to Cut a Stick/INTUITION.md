# Intuition

```
X X X X X X X X X X X X X X X X X X X X
i                cut                  j
```

```py
|--|--|--|--|--|--|--|
0  1  2  3  4  5  6  7

|--|--|--|  |--|--|--|--|
0  1  2  3  3  4  5  6  7

|--|--|--|   |--|--| |--|--|
0  1  2  3   3  4  5 5  6  7

|--| |--|--|   |--|--| |--|--|
0  1 1  2  3   3  4  5 5  6  7

|--| |--|--|   |--| |--|  |--|--|
0  1 1  2  3   3  4 4  5  5  6  7
```

根據題意和example 1, 我們可知這是個區間型的DP
並且狀態轉移很快能得知
`dp[i][j] = dp[i][cut] + dp[cut][j] + cost, where cost = j-i and i < cut < j`

只是我們的cut只能從`cuts`裡面找並且 i < cut < j
所以我們可以對cuts先排個序然後用binary search找出對於區間[i:j], 有哪些位置我們可以cut

由於感覺bottom-up會需要建立每個dp[i][j]的值但我們binary search又會跳過部分區間, 所以某些dp[i][j]可能不會更新到

看起來top down方式比較好寫, 就用top-down+memorization的方式繼續
然後配合binary search來剪枝

我們可以透過binary search找出valid cut, valid cut會落於[start,end)這區間
```py
start = bisect.bisect_right(cuts, i)
end = bisect.bisect_left(cuts, j)

for k in range(start, end):
    cut = cuts[k]
    left, right = dfs(i, mid), dfs(mid, j)
    res = left+right+cost
```

所以DFS的base case就是當沒有任何位置可以cut時, 返回cost=0
```py
def dfs(i, j):
    start = bisect.bisect_right(cuts, i)
    end = bisect.bisect_left(cuts, j)
    if end-start < 1: return 0

    # ... find valid cut and calculate cost
```

time complexity: $O(n^3)$

# Other Solution

如果是bottom up的話, 那就是遍歷所有可能

我們關注的就是我們能切哪些位置
由於0, n也是合法的位置, 所以我們先加入這兩個點
然後一樣排個序

```py
cuts = [0] + cuts + [n]
cuts.sort()

m = len(cuts)

dp = [[inf]*m for _ in range(m)]

# length=1
for i in range(m):
    dp[i][i] = 0

# length=2
for i in range(m-1):
    dp[i][i+1] = 0

for length in range(3, m+1):
    for i in range(n-length+1):
        j = i+length-1
        cost = j-i
        for k in range(i+1, j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+cost)
return dp[0][m-1]
```