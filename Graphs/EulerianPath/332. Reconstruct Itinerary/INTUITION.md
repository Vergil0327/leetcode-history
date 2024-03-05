# Intuition

first of all, we know:
- directed graph
- should choose lexicographically smallest stop as next stop
- total `n` tickets, should use all of them => itinerary.size == n+1
- we can use DFS/BFS to explore all possible itinerary

since we want lexicographically smallest, sort edges, then backtracking all possible answer until we find first valid answer. first answer should be lexicographically smallest

=> In graph theory, an Eulerian path is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).