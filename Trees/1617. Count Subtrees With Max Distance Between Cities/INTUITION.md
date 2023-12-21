# Intuition

floyd algorithn can calculate distance between any 2 nodes in O(n^3)

since 2 <= n <= 15, we iterate subset in bitmask form
and use union-find to union subset to check if they are valid connected subset.
which means only 1 connected component
we also can use BFS to travel those edge which connected nodes in subset
and the the number of nodes we travel by BFS should equal to the number of nodes in subset

once they are valid, we iterate every pair in O(n^2) to find max distance
time complexity: O(n^3) + O(2^n * n^2)
