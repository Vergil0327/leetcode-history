# Intuition

看到`min(max(...))`或`max(min(...))`, 首先想到用binary search去猜答案
然後再透過helper function `check`去判斷

問題就會轉換到如何去寫這個helper function

在我們透過binary search去猜測當前的max value後
當前的threshold代表的是group內任意兩點的距離必須**大於等於**這個threshold

由於我們要將所有點歸納到兩個group裡, 所以我們可以先遍歷一遍得出哪些點是互斥的
必須要在相異的組別裡:

```py
exclusive = [[0]*n for _ in range(n)]
for i in range(n):
    row1, col1 = points[i]
    for j in range(i+1, n):
        row2, col2 = points[j]
        if abs(row2-row1) + abs(col2-col1) < threshold:
            exclusive[i][j] = 1
            exclusive[j][i] = 1
```

那再來再透過DFS去嘗試分組, 看看是否能分出符合條件的兩組來
而這其實剛好就是在問`Bipartite`
而前面的`exclusive`其實就相當於是一個adjacency list
相斥的兩點中間連著一條邊, 查看最後是否能得到**Bipartite graph**

對於bipartite, 我們可以這麼判斷:

透過當前擁遠的adjacency list(亦即exclusive資訊), 把相斥的點標記成兩種不同group, `0`或`1`
然後用DFS去搜索所有可能, 只有當所有互斥點都可以準確分開成兩個相異group, 才是`True`

```py
def isBipartite(exclusive: List[List[int]]) -> bool:
    group = [0] * len(exclusive)
    visited = set()
    def dfs(node):
        for nei in range(n):
            if exclusive[node][nei]:    
                if nei in visited:
                    if group[nei] == group[node]: return False
                    continue
                visited.add(nei)

                group[nei] = 1 - group[node]
                if not dfs(nei): return False
        return True

    for node, _ in enumerate(exclusive):
        if node in visited: continue
        visited.add(node)

        if not dfs(node): return False
    return True
```

那最後helper function `check`為:

```py
def check(threshold):
    exclusive = [[0]*n for _ in range(n)]
    for i in range(n):
        row1, col1 = points[i]
        for j in range(i+1, n):
            row2, col2 = points[j]
            if abs(row2-row1) + abs(col2-col1) < threshold:
                exclusive[i][j] = 1
                exclusive[j][i] = 1
    return isBipartite(exclusive)
```