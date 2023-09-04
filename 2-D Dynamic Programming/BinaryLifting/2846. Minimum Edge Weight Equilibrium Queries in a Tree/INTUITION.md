# Intuition

對於每個queries[i] = [u,v]:
我們需要知道`u -> v`有多少edges, 以及他們的**weight**各是多少
然後我們要做的操作是保留出現最多次weight的edges

所以如果我們知道LCA(u, v) = k, 那麼`u -> v`就能轉化成`k -> u`跟`k -> v`
`u -> v`之間的edges就會是`root -> u的edges + root -> v的edges - 2 * root -> k`
所以這邊我們可用個`count[u] = # of edges from root -> u`來紀錄
由於這是棵樹, `root -> node`的edges就是node的深度(depth)

相同概念, 我們也能紀錄`root -> u`, `root -> v`每個weight有多少個edges
由於`1 <= wi <= 26`, 所以如果我們紀錄occurence[u][wi], 跟occurence[v][wi]為`root -> u`跟`root -> v`有多少edges

再來就是類似prefix sum的概念, 記得扣掉`root -> LCA(u,v)`的每個edges即可知道
`wi` from 1 to 26每個weight的edges有多少

所以對於queries[i]:

1. 我們透過count[u] + count[v] - 2 * count[lca(u,v)]得到`u -> v`有多少個edges
2. 我們再遍歷occurence[u][wi]跟occurence[v][wi] where wi from 1 to 26, 找出max occurence
3. queries的答案res[i] = answer of 1. - answer of 2.

high-level框架為:
```py
res = []
for u, v in queries:
    k = lca(u, v)

    numEdges = count[u] + count[v] - 2 * count[k]
    numMaxEdges = max(occurence[u][w] + occurence[v][w] - 2 * occurence[k][w] for w in range(1, 27))
    res.append(numEdges - numMaxEdges)
return res
```

但由於`1 <= queries.length == m <= 2 * 10^4`並且`1 <= n <= 10^4`
我們在找LCA(u,v)時會需要O(n)的時間
```py
# find LCA in O(n)
def lca(root, prev, u, v):
    if root == u or root == v: return root
    
    res = None
    cnt = 0
    for w, nei in graph[root]:
        if nei == prev: continue
        children = lca(nei, root, u, v)
        if children:
            cnt += 1
            res = children

    if cnt == 2:
        return root
    return res
```
那這樣時間複雜度會變成O(mn)會超時, 所以我們需要一個比較高效的方式來找LCA

這時就需要binary lifting來將O(n)拆解成二進制`n = 2^a + 2^b + 2^c ...`將找尋LCA的時間複雜度降成O(logn)