# Intuition

根據**Hint 2: For each edge, find two sums: one including the edge and one excluding it.**

代表對於當前節點, 我們有兩個選擇, **包含**或**排除**

由於我們最多可以選`k`個edges, 因此對於當前edge來說:
- 如果選擇包含該edge, 那就看其他最大的前k-1個edge加上該weight的sum多少
- 如果選擇排除該edge, 那就看其他最大的前k個edge的weight sum多少

那兩種選擇, 我們必定是取大的
因此我們可以寫出我們的recursion decision tree來遍歷整棵樹:

`let dfs(node, prev): return (sum with k-1 atmost edge's weight, sum with k atmost edge's weight) considering current node `

因此主體框架可以得出:

```py
def dfs(node, prev):
    res = 0
    for nxt in graph[node]:
        if nxt == prev: continue
        sumKminus1, sumK = dfs(nxt, node)
        res += sumK
```

那再來就是要判斷當前納入node<->nxt edge跟不納入哪個比較好
所以我們用`diff`來紀錄每個edge包含跟不包含的差值
> 也可想成紀錄: 如果包含當前edge, 會額外貢獻多少weight
> 
> contribution = (sumKminus1+weight) - sumK

```py
diff = []
for nxt in graph[node]:
    if nxt == prev: continue
    sumKminus1, sumK = dfs(nxt, node)
    
    contrib = sumKminus1+graph[node][nxt] - sumK
    diff.append(max(0, contrib))
```

在有了`diff`這項資訊後, 我們先由大到小排序, 然後我們就能得到每個edge由大到小排序的貢獻
再來就一樣遞歸返回:

1. 包含最大的前`k-1`個edges: res + sum(diff[:k-1])
2. 包含最大的前`k`個edges: res + sum(diff[:k])

持續遞歸考慮完美個節點後, 最終答案就是包含最多`k`個的max weight sum: `dfs(0, -1)[1]`


另外補充一下, 由於遞歸過程中我們有`res += sum2`
那麼後面看diff時, 我們在做的其實是判斷是否有貢獻更多weight的edge


如果有, 那就把weight補上, 補到至多k個變成`sum2' = res + sum(diff[:k])`

那為了繼續遞歸處理下個點, 所以我們對於當前節點我們也得返回至多`k-1`個點的`weight sum1' = res + sum(diff[:k-1])`


time: O(nlog(edges))