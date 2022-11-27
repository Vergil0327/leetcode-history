### iterative solution with monotonic stack

1. use array to store linked list
2. use monotonically increasing stack
3. use dummy node to link all the existed nodes together

### Recursion

post-order DFS traversal to remove node
- if node.val < node.next.val: return node.next
- if node.val >= node.next.val: return node