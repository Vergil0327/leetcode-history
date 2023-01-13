# Dijkstra or Bellman-Ford(TLE)

## Intuition

concepts for Dijkstra and Bellman is the same.
we keep tracking of weights for each node and pick those city whose weight <= threshold at last

bellman-ford will TLE and dijkstra can pass because it is a greedy algorithm

## Complexity

- time complexity

$$O(ElogV)$$ for dijkstra algorithm

- space complexity

$$O(n)$$

# Floyd–Warshall algorithm

## Intuition

[original post](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/solutions/490312/java-c-python-easy-floyd-algorithm/?orderBy=most_votes)

Becasue O(N^3) is accepted in this problem, we can simply use [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) to find the minium distance any two cities.

```
The Floyd–Warshall algorithm compares all possible paths through the graph between each pair of vertices. It is able to do this with O(V^3) comparisons in a graph, and every combination of edges is tested. It does so by incrementally improving an estimate on the shortest path between two vertices, until the estimate is optimal.

Floyd–Warshall algorithm 其實就是遍歷所有node並查看是不是起點與終點間的中間站，是的話便更新距離，以此逐步趨近極值
```

## Apporach

1. iterate throuth all the middle point `k`
2. iterate all pairs (u,v)
3. if it go through `k`, `distance[u][v] = distance[u][k] + distance[k][v]

## Complexity

- time complexity

$$O(n^3)$$

- space complexity

$$O(n^2)$$