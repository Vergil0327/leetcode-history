### Intuition

if we brute force by DFS at each node to find duplicate, it would be O(N^2) to check and compare

so, maybe we can mark every subtree first, then compare or find if there exists a duplicate subtree later.

I think `hashset` or `hashmap` would be a possible data structre for us to find duplicate.

also, think [leetcode 297](../297.%20Serialize%20and%20Deserialize%20Binary%20Tree/) again.

if we serialze each subtree into string and store in `hashmap`, we should be able to find duplicate by checking if there is already an identical serialzed string in our `hashmap`

thus, our algorithm is:

1. post-order DFS traversal and serialize at each position
2. if not in our hashmap, add and increment count by 1
3. if there is already a duplicate in hashmap, current subtree should be answer
4. don't forget to increment count by 1 again. we shouldn't append duplicate answer again