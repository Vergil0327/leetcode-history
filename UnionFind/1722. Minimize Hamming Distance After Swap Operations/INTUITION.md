# Intuition
1 2 3 4 -> 2 1 3 4 -> 2 1 4 3
2 1 4 5

x, y = allowedSwaps[i] => allowedSwaps[i]相當於是x, y之間的edge
或者x, y可以想成是同一個group

代表每個index `i` 都可以透過allowedSwaps組成一個group
再來我們可以遍歷target來看target[i]存不存在於group內
如果存在的話, 就`group[traget[i]] -= 1`
最後看有哪些位置找不到不在group內即可計算出minimum hamming distance

所以我們要透過allowedSwaps把source給集合起來
感覺可以利用union-find來連通各個index並透過hashmap來計數

一開始: parent = list(range(n)), counter = [Counter([source[i]]) for i in range(n)]
再來用union-find把所有allowedSwaps的連通起來
並且同時把hashmap合併在一塊

最後檢查每個target[i]有沒有在group內, 有的話代表找得到一個source[i] == target[i]
沒有的話則hamming distance += 1

# Optimization

但其實我們沒必要在每次union的步驟就更新hashmap
```py
for x, y in allowedSwaps:
    px, py = find(x), find(y)
    if px == py: continue
    
    if len(counter[px]) >= len(counter[py]):
        parent[py] = px
        for k, v in counter[py].items():
            counter[px][k] += v
        
    else:
        parent[px] = py
        for k, v in counter[px].items():
            counter[py][k] += v
```

我們最後分組完後, 我們再一次更新每個group有哪些數值即可
```py
parent = list(range(n))
rank = [1] * n
for x, y in allowedSwaps:
    px, py = find(x), find(y)
    if px == py: continue
    
    if rank[px] >= rank[py]:
        parent[py] = px
        rank[px] += rank[py]
    else:
        parent[px] = py
        rank[py] += rank[px]

counter = [Counter() for i in range(n)]
for i in range(n):
    counter[find(i)][source[i]] += 1
```