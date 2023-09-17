# Intuition

since 1 <= n <= 12, we can use bitmask to represent visited state
use BFS to find minimum length and see bitmask if we've already visited all the nodes.
once we visit all the nodes which means bitmask equals (1<<n)-1, return BFS steps

still use a hashset to avoid duplicate state (node, bitmask) since we don't want to visit node with same state(bitmask) multiple times.

time: O(n * (n * 2^n))

但其實我們可以不用一個一個起點單獨找
我們要找的是最短路徑, 所以我們可以把所有可能起始點一開始就放入到queue裡
然後找最短路徑