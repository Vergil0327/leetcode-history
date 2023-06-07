# Intuition

use BFS to find how long for each node to reach root node and store in `time` array
that is , complete back-and-forth need `time[node]` sec

for each node, it'll re-send time[node] // patience[node] messages and `minus 1` messages if reply come back at the moment we want to re-send, i.e. time[node] % patience[node] == 0.
thus, `required time = time[node] + # of msg * patience[node] + 1`

and we find globally maximum required time

# Complexity

- time complexity
$$O(n)$$
