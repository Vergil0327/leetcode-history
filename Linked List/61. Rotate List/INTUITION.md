# Deque

## Intuition

1. break node's link and store nodes in deque.

2. rotate deque `k % len(deque)` times
   - be aware of edge case: deque can be null. ex. head = None, then deque = []

3. link nodes in deque

## Complexity

- time complexity:
$$O(n)$$

- space complexity:
$$O(n)$$

# Space Optimized

## Intuititon

1. know total length first
2. link tail to head to form a cycle
3. rotate
   1.  find new tail, break cycle, return new head (new tail's next node)
   2. new head is `len(list)-k%len(list)`-th node (0-based index)
   3. new tail is its previous node.
   4. A->B->C, k=2 -> B->C->A. (3-2%3=1 => 1-th node `B` is new head.)

- time complexity:
$$O(n)$$

- space complexity:
$$O(1)$$