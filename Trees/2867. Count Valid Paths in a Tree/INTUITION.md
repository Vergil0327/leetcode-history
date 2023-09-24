# Intuition

首先我必須得知道當前節點是不是prime number
所以我們可以用埃氏篩選求出`isPrime[num]: True/False`

```py
isPrime = [0, 0] + [1] * (n-1)
for i in range(2, int(math.sqrt(n))+1):
    if not isPrime[i]: continue
    # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
    for j in range(i*i, n+1, i):
        isPrime[j] = 0
```

再來對於一棵樹的path, 我們可以用DFS然後看他的左右子樹路徑

再來我們觀察一下

- 如果當前節點是Prime:
  - 那麼下面子樹的所有不含prime number的路徑, 都可以跟當前節點組成valid path
- 如果當前節點不是Prime
  - 那麼下面子樹的所有含有1個prime number的路徑, 都可以跟當前節點組成valid path

所以我們比較直覺的猜想是, 我們的dfs可能要返回兩個值:
1. 完全不含有prime number的路徑數
2. 含有**1個**prime number的路徑數

所以如果我們DFS返回`[x, y]`, 其中x代表不含有prime的路徑而y代表含有prime的路徑

那麼對於當前節點來說, 我們可以寫成:
- if isPrime[node] == True, cur = [x, y] = [0, 1]
- if isPrime[node] == False, cur = [x, y] = [1, 0]
那當前節點能組成的valid path就是: `res += cur[0] * y + cur[1] * x`

```py
def dfs(node, prev):
    # not_prime, prime
    cur = [0, 1] if isPrime[node] else [1, 0]

    for nei in graph[node]:
        if nei == prev: continue
        x, y = dfs(nei, node)
        self.res += res[0]*y + res[1]*x
```

再來我們考慮下個DFS的狀態轉移

- 如果當前節點是prime number, 那麼當前所有不含有prime的子路徑都可以跟當前節點組成含有**1個**prime number的路徑. 而不含有prime的路徑就為0
  - `cur[1] += x for x, y in every dfs(nei, node)`
 
- 如果當前節點不是prime number, 那麼所有合法子路徑`x`, `y`都可跟當前節點組成合法路徑
  - `(cur[0] += x, cur[1] += y) for x, y in every dfs(nei, node)`

所以最終:

- 定義dfs(node, prev): return (x, y) where x is number of path containing 0 prime, y is number of path containing exactly 1 prime

```py
def dfs(node, prev):
    # not_prime, prime
    res = [0, 1] if isPrime[node] else [1, 0]

    for nei in graph[node]:
        if nei == prev: continue

        x, y = dfs(nei, node)
        self.res += res[0]*y + res[1]*x
        if isPrime[node]:
            res[1] += x
        else:
            res[0] += x
            res[1] += y
        
    return res[0], res[1]
```