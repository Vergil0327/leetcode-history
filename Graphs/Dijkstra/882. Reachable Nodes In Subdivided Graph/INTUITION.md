# Intuition

first thought: BFS within maxMoves? but how to calculate reachable nodes without duplication?

see example 1, we can travel from 0->1 or 1->0
if we start from both end and over middle, how to avoid duplicate calculation?

首先先往BFS去想
從根節點0開始, 在maxMoves下可以經歷哪些節點, 而分割的cnt其實就像是這條邊的權重
由於有權重, 所以我們能用Dijkstra求出根節點到每個點的最短路徑

see example1, 透過Dijkstra可求出:
dist[0] = 0
dist[1] = 5
dist[2] = 2

那知道這訊息之後呢, 我們就能遍歷整個edges[i] = [u, v, cnt]
首先我們方向可以是u->v或v->u, 那我們知道dist[u]跟dist[v]後我們就知道我們在走到這條邊的兩端後還剩多少moves:
1. u->v: 還剩下maxMoves - dist[u]步
2. v->u: 還剩下maxMoves - dist[u]步
那這樣我們就能知道從兩端往前走能拜訪的小節點為min((maxMoves - dist[u]) + (maxMoves - dist[u]), cnt)

把這些小節點全加總起來後,
最後再遍歷一次每個節點, 把有拜訪過的大節點數目再加上去即可: res += 1 for node in range(n) if visited[node]