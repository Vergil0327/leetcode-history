# Intuition

這題最重要的關鍵是: `if A^B=C, A = C^B`

而且一次考慮砍兩刀比較難辦的話我們先考慮一刀，砍第一刀後會切分成兩個子樹
如果我們稱它為A, B的話
首先整個數 A+B 的 XOR 我們可以提前算出來，就是把nums[i]全部XOR起來，得到`totalXOR`
再來可以透過post-order DFS算出A的 `XOR_A`
那麼B的XOR_B就等於`totalXOR^XOR_A`

因為 `XOR_A^XOR_B = totalXOR`

這邊我們的adjacency list用hashset來儲存
因為這樣我們才能 backtracking 第一刀
不然我們dfs會計算到整棵樹而非只有A那半邊

再來我們就在dfs A 跟dfs B一次，同樣post-order dfs
每次遞歸都能得到A子樹的子樹`XOR_SUBTREE`，我們在同樣地利用 `XOR_A^XOR_SUBTREE` 特性就能得到第三個connected component

所以每次遞歸都可以得到 `XOR_A`, `XOR_SUBTREE` 跟 `XOR_A^XOR_SUBTREE`
score 就等於 `max(XOR_A, XOR_SUBTREE, XOR_A^XOR_SUBTREE) - min(XOR_A, XOR_SUBTREE, XOR_A^XOR_SUBTREE)`

然後再以同樣方式改切B子樹即可得到全局最低分數

# Optimized Solution

1. 提早算出每個子樹的XOR
2. 找出每個節點底下包含哪些子節點
3. 遍歷兩個節點來做切分，如果兩個節點分別為`A`跟`B`，根據相對位置可透過XOR的特性找出三個子樹的XOR值並求分數
   1. xor[0]為總XOR的值
   2. 如果B是A的子節點，那麼A另半邊為`xor[0]^xor[A]`，然後B子樹為`xor[B]`，最後一個則為`xor[A]^xor[B]`
   3. 如果A是B的子節點，那麼B另半邊為`xor[0]^xor[B]`，然後A子樹為`xor[A]`，最後一個則為`xor[B]^xor[A]`
   4. 如果AB在兩側，那麼另半邊就是`xor[0]^xor[A]^xor[B]`，兩子樹為`xor[A]`, `xor[B]`

```py
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        xor = [0] * len(nums)
        def getXor(node,parent):
            xor[node] = nums[node]
            for child in graph[node]:
                if child == parent:
                    continue
                
                xor[node] ^= getXor(child,node) 
            return xor[node]
        
        parent = defaultdict(set)
        def dfs(node,p):
            parent[node] = set([node])
            for child in graph[node]:
                if child == p:
                    continue
                
                parent[node] |= dfs(child,node)
            
            return parent[node]
        getXor(0,-1)
        dfs(0,-1)

        res = float('inf')
        for rootA in range(1,len(nums)):
            for rootB in range(rootA+1, len(nums)):
                
                if rootB in parent[rootA]:
                    a = xor[0] ^ xor[rootA]
                    b = xor[rootA] ^ xor[rootB]
                    c = xor[rootB]
                    res = min(res,max(a,b,c) - min(a,b,c)) 
                elif rootA in parent[rootB]:
                    a = xor[0] ^ xor[rootB]
                    b = xor[rootB] ^ xor[rootA]
                    c = xor[rootA]
                    res = min(res,max(a,b,c) - min(a,b,c)) 
                else:
                    a = xor[0] ^ xor[rootA] ^ xor[rootB]
                    b = xor[rootA]
                    c = xor[rootB]
                    res = min(res,max(a,b,c) - min(a,b,c)) 
        return res
```