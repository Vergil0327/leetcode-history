## DFS

first, let's define two groups `A` & `B` set
and we can use DFS to traverse every node to categorize nodes into 2 groups

case:
  1. if node is undefined, categorize to `A` and its neighbor to `B`
  2. if node belongs to `A`, then its neighbor must belong to  `B`, and vice versa

once we found invalid neighbor node, we just return `False` and don't need to traverse further

**Another way to solve**

we can use a `bool` array to categorize nodes. `True` or `False`

and we use `visited` to check if the neighbor has been categorized or not

- if we've visited neighbor once, check equality of current node and neighbor node
- if not, categorize neighbor to opposite group