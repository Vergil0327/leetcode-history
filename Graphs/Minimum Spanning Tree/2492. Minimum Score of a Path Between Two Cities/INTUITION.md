Intuition

even though the minimum score is on the opposite side, we can still pass target node and come back later, see example 2.

since we can traverse back and forth and visit node multiple times to get minimum score, we can use all the score in connected graph.

the overall paths will build a minimum spanning tree(MST)
we find minimum score in MST

more generally speaking, we only need to find min score in connected component of node-1 to node-n

algorithm:

- build MST by kruskal algorithm
- find minimum score in disjoint set union of node-1