# Intuition

其實就是找出每個source[i] -> target[i]的最短距離
距離的權重可透過(original[i], changed[i], cost[i])得到: `original[i] -> changed[i]的權重為cost[i]`

```py
MAP = defaultdict(lambda: defaultdict(lambda: inf))
for i in range(len(original)):
    MAP[original[i]][changed[i]] = min(MAP[original[i]][changed[i]], cost[i])
```

那再來就是逐步對進行dijkstra(source[i], target[i])即可

那記得對`dijkstra`做memorization, 最多就26*26個結果