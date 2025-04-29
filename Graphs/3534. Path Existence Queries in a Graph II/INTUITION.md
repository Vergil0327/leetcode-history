# Intuition

We're given an undirected graph where nodes i and j are connected if |nums[i] - nums[j]| <= maxDiff. Instead of building an adjacency list for the entire graph, this solution takes a clever approach by:

- Sorting the nodes based on their values.

- Using binary search to find how far a node can "jump" forward in the sorted list while staying within the maxDiff constraint.

- Defining a dfs function (with memoization) to recursively find if there's a path from one index to another in this sorted array-based interpretation of the graph.

The graph traversal is reduced to walking forward through a sorted list, where edges are implicit based on the value condition.

whenever `|nums[i] - nums[j]| <= maxDiff`, we can see them as a group with 1 edge between each other.
therefore, we can use `dfs` function to jump from group to group to calculate minimum distance