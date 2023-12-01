# Intuition

想一下如果是我們用肉眼看該如何判斷這些顏色原本可能的大小範圍
=> 遍歷一遍看每個顏色四個方向最遠到哪, 這樣就能推測每個顏色的原本塗抹矩形範圍

如此一來我們就能知道每格**grid[i][j]**被塗抹過的次數
再來我們也能知道每格grid[i][j]塗抹次數與顏色的對應關係
塗抹次數最少的肯定是第一個塗抹的顏色
我們就依著塗抹次數由小到大把顏色塗抹上去, 最後看是不是跟targetGrid相同即可
但會發現在這test case出錯: 
ex. targetGrid = [[1,1,1,1,1,1,3,3,3],[1,1,1,1,1,1,3,3,3],[1,1,2,2,2,4,5,5,3],[1,1,2,2,2,2,5,5,2],[1,1,2,2,2,2,2,2,2],[1,1,1,1,1,6,6,6,6]]

這是因為color-3, color-2塗抹次數都是一樣的, 因為塗抹先後關係的不同而導致我們結果出錯
所以根據最後targetGrid[i][j]的顏色, 我們可以知道顏色塗抹的先後關係
ex. targetGrid[i][j]有三種顏色`x`, `y`, `z`塗過, 而最後的顏色為`y`
這代表`x`跟`z`必須比`y`還要先塗抹上去

所以我們可以從每一格targetGrid[i][j]得到顏色的先後塗抹順序
這時會發現這就像topological sort, 每個顏色有先後順序的依賴關係, 所以我們可以依據這關係建構出acyclic directed dependency graph

1. 首先先看每一格有被塗上哪些color
2. 然後在透過最終顏色targetGrid[i][j]求出每個顏色的先後順序, 建構出adjacency list
```py
paintedColor = [[set() for _ in range(n)] for _ in range(m)]
for color, (l, r, top, bot) in coordinate.items():
    for i in range(top, bot+1):
        for j in range(l, r+1):
            paintedColor[i][j].add(color)

graph = defaultdict(set)
indeg = [-1]*61 # 1 <= targetGrid[row][col] <= 60
for color in coordinate:
    indeg[color] = 0

for i in range(m):
    for j in range(n):
        for nei in paintedColor[i][j]:
            if nei == targetGrid[i][j]: continue
            if targetGrid[i][j] in graph[nei]: continue

            graph[nei].add(targetGrid[i][j])
            indeg[targetGrid[i][j]] += 1
```

之後就是簡單的topological sort (BFS) 了

# Other Solution

topological sort也能用DFS的形式來解, 一樣先建立adjacency list
本質其實就是查看有沒有環(cycle)的產生, 把每種顏色都查看一遍, 如果都沒有環那就對了

```py
adj = defaultdict(list) # adjacency list
visited = defaultdict(int)

VALID, CYCLE = 1, 2
def dfs(node):
    if visited[node] == VALID: return True

    visited[node] = CYCLE
    for nei in adj[node]:
        if visited[nei] == VALID: continue
        if visited[nei] == CYCLE: return False
        if not dfs(nei): return False

    visited[node] = VALID
    return True
```