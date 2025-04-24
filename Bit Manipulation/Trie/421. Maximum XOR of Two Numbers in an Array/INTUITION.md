# Intuition

we want `max(nums[i] XOR nums[j])`

bit=1 => find bit=0 elements
bit=0 => find bit=1 elements
=> 2 branches
=> we can store every elements in XOR tree, then we can do DFS traversal
=> also store/search max significant bit first for finding maximum XOR element
