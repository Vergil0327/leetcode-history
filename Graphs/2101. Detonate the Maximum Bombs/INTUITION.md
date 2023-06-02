# Intuition

如果把每個`bombs[i]`都畫在grid上然後逐個引爆看看
`bombs[i]`能引爆所有bombs[j] where manhattan distance <= bombs[i][2]**2
這就相當於bombs[i] 有個directed edge指向bombs[j]

由於數據規模很小(<= 100)
代表我們能用O(n^2)時間建立adjacency list
然後在遍歷每個節點嘗試用dfs以O(n^2)時間找出該節點涵蓋的所有節點

```py
res = 1
for i in range(n):
    cnt = dfs(i, set()) # dfs return the number of nodes which bombs[i] can detonate
    res = max(res, cnt)
return res
```

最後再取全局最大的即可