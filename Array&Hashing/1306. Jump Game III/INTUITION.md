# Intuition

we can see it as a graph problem.

see each nums[i] as node and `i+arr[i]` is its neighbor

thus, we can just DFS with a `visited` hashset to check if we can reach `nums[i] == 0` or we'll stuck in cycle.

# Complexity

- time complexity:

$$O(n)$$

- space complexity:

$$O(n)$$