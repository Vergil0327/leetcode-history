### Space O(n)

it's easy to use extra space to store pre-order results
then use a dummy node to append node one by one, starting from `root` to the end

ps. if we don't use extra dummy node, we need to consider this test case carefully:

```
root = [0]
```

### Space O(1) Solution

we can use post-order traversal to solve this problem in `O(1)` space

the core concepts is:

1. define subproblem
2. solve subproblem recursively
3. resursion will done all the work at each root node position

we can observe that we can get the final linked list from:

1. flatten left subtree
2. flatten right subtree
3. move left subtree to root node's right
4. append right subtree after tail of left subtree

if we implement these logic at each node, recursion will execute these 4 steps at each node and finally flatten the whole tree