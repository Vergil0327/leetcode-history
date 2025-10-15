# Intuition

這是Leetcode Weekly Contest 471的第四題
這系列第二三題開始都是利用prefix sum + hashmap去計數的概念解題
而這題其實也是在此的延伸

首先我們要找的是每個節點`node_i`, 有多少個`ancestor_j`能兩者相乘為**perfect square**
亦即: **因數個數為偶數!**

這是最重要的一點, 所以我們眼中真正看重的是因數的個數
如同prefix sum + hashmap count
我們把每個nums[i]都找出remaining factors:

例如 `nums[i] = 8 = 2x2x2` => 把成雙的因數扣掉後, 只剩單獨一個`2`
以這作為key, 假設有另一個數`ancestor[j]`的key跟nums[i]相同
那代表兩者相乘即為**Perfect Square**

因此我們將每個nums[i]找出remaining factors後
剩下的就只要從根節點開始, DFS遍歷一遍, 並backtracking每個visited ancestor的key與個數
即可得到答案

就像是prefix sum + hashmap count那樣, 只是從遍歷array變成遍歷tree

主框架為:

```py
self.res = 0
visited = Counter() # {key: number of nums[i] with current key}
def dfs(node, prev):
    ti = visited[keys[node]]
    if node > 0:
        self.res += ti

    visited[keys[node]] += 1
    for nxt in graph[node]:
        if nxt == prev: continue
        dfs(nxt, node)
    visited[keys[node]] -= 1

dfs(0, 0)
return self.res
```

### find factors

```py
keys = []
for num in nums:
    remain_factors = []
    for i in range(2, isqrt(num)+1):
        if num%i == 0:
            cnt = 0
            while num%i == 0:
                cnt += 1
                num //= i
            if cnt%2:
                remain_factors.append(i)
    if num > 1:
        remain_factors.append(num)
    keys.append(tuple(remain_factors))
```