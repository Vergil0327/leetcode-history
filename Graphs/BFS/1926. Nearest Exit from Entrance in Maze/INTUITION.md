### Intuition

main idea: find shortest path -> `BFS`

1. add obstacles to `hashset` to prevent us from crossing it
2. start BFS traversal step by step when we reach border
3. be aware of that we can't count it as an exit if entrance is on the border

time: O(mn)
space: O(mn)
