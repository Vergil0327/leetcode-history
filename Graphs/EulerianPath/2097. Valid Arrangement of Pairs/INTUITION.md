# Intuition

constraint: 
- There exists a valid arrangement of pairs.
- No two pairs are exactly the same.

{X END1} {START2 END2} {START3 END3} ... X
一開始先想能不能利用hashmap去做對應
MAP1 = { end: index }
MAP2 = { start: index }
以index作為ID的話, MAP1, MAP2就相當於告訴我們兩個節點是否有edge連接
從起始點開始, 利用endi能找出下個節點`for nxt in MAP2[endi]`
下個就變成從MAP1去找與當前節點相對應的下個節點
所以這題其實是graph problem, 要找出一條合法路徑

brute force的話就是用dfs去遍歷搜索

但這樣會是O(n^2)

雖然知道可以看作graph, 但卻卡在這
但實際上這是一道求Eulerian Path/Circuit的一道題目

## Eulerian Path

Eulerian Path: 從一點出發到另一點, 所有的邊都經過並且只經過一次
如果Eulerian Path最終回到起點, 那這個就是Eulerian Circuit

那該如何判斷Eulerian Path?

1. indirected graph
   - 只有兩個節點的degree是奇數, 其他節點的degree都是偶數, 那這兩個奇數degree節點存在一條Eulerian Path
   - 每個節點的degree都是偶數 => Eulerian Circuit
2. directed graph:
   - 最多有一個節點A的outdegree比indegree大1 (如果沒有那就可以任意節點作為起點)
   - 最多有一個節點B的indegree比outdegree大1 (如果沒有那就可以任意節點作為起點)
     - 那麼存在一條A -> B的Eulerian Path 
   - 如果每個點的indegree == outdegree, 那就存在Eulerian Circuit
   
**Algorithm**

Eulerian Path: 對於起點A, 中間可能會有很多cycle, 但只會有一個dead end位於B

```
A ----- X --- X -- X -- B
      /   \
     X --- X
```

所以我們從A開始任意遍歷, 最終肯定只會走到B
如果進行dfs遍歷, 那就只會是第一條走到dead end B, 其他邊通往的路徑都會是個環

所以我們能這麼做:

我們任意遍歷起點的路徑

```py
def dfs(start, path):
    while graph[start]:
        nxt = graph[start].pop()
        dfs(nxt, path)
```

那我們該如何找出Eulerian Path?
我們在dfs遍歷完後, 把節點加入到path裡
還記得我們說過, 第一條路徑才會是通往dead end的路徑
所以我們最後得到的, 會是個逆序的Eulerian Path
所以最後我們在reverse一下就會得到正確的Eulerian Path

```py
path = []
def dfs(start, path):
    while graph[start]:
        nxt = graph[start].pop()
        dfs(nxt, path)
    path.append(start)
path.reverse()
```