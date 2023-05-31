# Intuition

pairs = [[0,3], ...]
A B C D E -> D B C A E

pairs tell us the next state we can get.
if current state is a node, then we can use BFS to explore all the state and find a minimum lexicographically string
but both pairs.length and s.legnth <= 10^5, BFS leads to TLE

so, we need to change a way to solve this problem.

if we can change these two indices, pairs[i][0] and pairs[i][1], it means these two indices are connected
we can swap any two indices which are in the same connected component, so we can just sort same group of characters lexicographically
and put thoses characters back into those indices

for those indices which didn't connect to any index, we just leave them unchanged
