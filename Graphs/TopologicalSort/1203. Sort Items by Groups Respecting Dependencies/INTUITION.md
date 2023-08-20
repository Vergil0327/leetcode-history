# Intuition

if we see beforeItems is and directed edge, i-th items should come after beforeTimes[i] which means an edge where beforeTimes[i] points to i-th.

then we use topological sort to generate correct order and put item in its group

but now we still left group order to decide.

thus, we should think this as a graph and use topological sort to define group's order and item's order.