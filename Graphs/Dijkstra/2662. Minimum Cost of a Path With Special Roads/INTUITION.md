# Intuition

without using any special roads:
`res = calCost(start[0], start[1], target[0], target[1])` at least

for each special roads, we can use it or skip it.

I don't know which strategy is better, so use BFS to traverse them all, and seems that **Dijkstra** is a nice way to use. (no negative cost)

once we use it, we store destination in `visited` hashset because if we reach same position again, its cost must be higher.

and we check cost from every position after using special roads to target, choose minimum cost amoung them.

>actually, we can think that every possible position as a node in graph and every node in graph has special roads as its directed edges.

- Time complexity:
$$O(VlogV+ElogV)$$
