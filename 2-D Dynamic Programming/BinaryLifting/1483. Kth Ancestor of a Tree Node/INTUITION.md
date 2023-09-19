# Intuition

這題brute force其實就是每次query, 對`node`用k次循環`ancestor = parent[node]`找出k-th ancestor
那這樣每次query就是O(n) (worst case: linked-list-like tree)

但本題的數據範圍無法以O(n)時間來過, 因此如果要有個比O(n)更高效的解法的話, 就是O(log(n))了

本題也是經典的binary lifting, 本身是比較精妙定義的dynamic programming

首先我們這麼定義dp[i][node]: the 2^i-th ancestor of node

對於任意第`k`個ancestor來說, k都可以用二進制表示, 所以如果我們能有個二進制的跳轉表
如果k = 2^2 + 2^1
就能先跳2^2步後再跳2^1步, 也就是:`node -> dp[2][node] -> dp[2][dp[2][node]]`

所以狀態轉移就是:
```
mid = dp[i-1][node]
dp[i][node] = dp[i-1][mid]
```
這個意思是node走2^i步的ancestor = 先走$2^{i-1}$步抵達`mid`節點, 然後再從`mid`走$2^{i-1}$步
由於我們`i`從小到大更新, 所以對於dp[i][node]來說, `dp[i-1][mid]`跟`dp[i-1][node]`都是已知
所以我們既可以建出一個dp table以log(n)時間找出每個節點的第`j`個ancestor就是`dp[j][node]`

因此為了之後快速查找k-th ancestor, 得先建立dp table

**Initialization**

先求出這棵樹的最大可能高度: m = n.bit_length()

如同前面所述定義: `dp[i][node]: the 2^i-th ancestor of node`
因此:
```py
dp = [[-1]*n for _ in range(m+1)]
```

**state transfer**

```py
for i in range(1, m+1):
    for node in range(n):
        p = dp[i-1][node]
        dp[i][node] = -1 if p == -1 else dp[i-1][p]
```

**base case**

i = 0時, dp[i-1]會越界, 所以我們遍歷改成從`[1,m]`
然後base case就是`i=0`時, 也就是每個節點`node`的第$2^0=1$步為parent[node], 因此:
`dp[0][node] = parent[node] for node in range(n)`


**query**

那這樣我們每次query就查表就好

k-th ancestor -> 我們可以永遠可以將k表示成二進制: 2^a + 2^b + 2^c + ...

所以就能透過dp table以O(log(n))時間快速找出ancestor:
```py
for i in range(m):
    if (k>>i)&1:
        node = self.dp[i][node]
        if node == -1: return -1
```

# Complexity

- time complexity

$$O(log(n))$$

- space complexity

$$O(nlog(n))$$