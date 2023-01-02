# Intuition

we can replace current node's value with next node's value
we also use pointer `prev` to keep tracks of previous node of current

while we finish replacement of value, we can use `prev` pointer to remove last node.

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(1)$$