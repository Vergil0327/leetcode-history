# Intuition

這題主要分兩個部分

首先能想到的是我們如果先不考慮折價的情況該如何處理?

由於這是顆樹，所以兩點之間只會有一條路徑
所以我們可以遍歷`trips`然後用DFS去找出這條路徑

沿路的路徑和為`sum(price[node])`
而這邊我們可以把每個node經過的次數記錄到`count[node]`裡
這樣我們之後只要遍歷DFS一遍，每個node所需要的費用則為`count[node]*price[node]`, 即可得到總旅行的cost

那再來就是考慮哪些節點需要折價哪些不用

當初這邊一開始看題目以為是只有第一次trip的時候，於起點的時可以決定起點相鄰的節點折價
但並不是!!!

其實是所有不相鄰的節點都可以自由選擇:
- 折價
- 或不折價

也就是說，這其實是個house robber的問題，只是應用在tree上

如此一來我們可以定義一個DFS函式叫`dp`
`dp`是在一般的無向圖DFS上再加上當前節點有折價還是沒折價的資訊
然後我們定義`dp`返回的是最小花費
dp returns the minimum cost required by trips with halve operation

```py
# 一般無向圖的DFS
def dp(node, prev, isHalf):
    for nei in graph[node]:
        if nei == prev: continue
```

每當遍歷到節點時，當前節點所需要的花費為:
```py
currentPrice = count[node]*price[node]
if isHalf:
    currentPrice //= 2
```

然後我們在DFS時:
- 如果當前節點折價的話, 那麼接下來的相鄰節點肯定不能折價, 所以:
  - `if isHalf: dp(nei, node, False)`
- 那如果當前節點沒有折價的話，那麼接下來的節點可以選擇折價, 也可以選擇不折價
  - 選擇折價: `dp(nei, node, True)`
  - 選擇不折價: `dp(nei, node, False)`
  - 然後由於返回的是最小花費, 所以我們在這兩個決策取最小的
- 返回子節點的花費加上自身花費
  - `res + currentPrice`

因此整個DFS為:

```py
def dp(node, prev, isHalf):
    currentPrice = count[node]*price[node]
    if isHalf:
        currentPrice //= 2


    res = 0
    for nei in graph[node]:
        if nei == prev: continue
        if isHalf:
            res += dp(nei, node, False)
        else:
            res += min(dp(nei, node, True), dp(nei, node, False))
    return res + currentPrice
```

這樣一來, 我們再來只需要遍歷每個節點比較折價跟不折價哪個花費最小, 然後再取全局最小的花費即為答案

```py
res = inf
for node in range(n):
    res = min(res, min(dp(node, node, True), dp(node, node, False)))
return res
```