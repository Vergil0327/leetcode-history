# DFS

## Intuition

let's pick one node as root and calculate it's distance sum first.

we can see that:

```
   o
 A   B
o o
```

`distSum(root) = 6`

and let's see its child node, take `A` as example.

now we choose `A` as new root node.

its distance sum will be:
`distSum(A) = distSum(root) + 2 - 3`,
where `2` is size of A's size of right subtree(old root node as child) and `3` is size of left subtree including itself.

because after we re-root to `A`:
- every nodes in right subtree (old root node as root) need 1 extra step to reach new root
- every nodes in child subtree (including new root itself) can minus 1 step to reach new root

thus, we can use precomputed distSum(root) to calulate every child node's distSum from this formula:

```
n = tree.size
distSum(child) = distSum(root) + a - b
               = distSum(root) + (n-treeSize(child)) - treeSize(child)
               = distSum(root) + n - 2 * treeSize(child)
```

## Approach

1. pick one node as root first
2. calculate its distance sum
3. calculate every child node's subtree size
4. calculate every child node's distance sum from formula `distSum(child) = distSum(root) + (n-treeSize(child) - treeSize(child)`

## Complexity

- time complexity

$$O(n)$$ (amortized)

$$O(n)$$ for computing root node's distance sum and constructing hashmap storing every child node's tree size

$$O(1)$$ for computing child node's distance sum

- space complexity

$$O(n)$$

## Further

if we have a array `nums = [... A R B ...]`, and we want to calculate distance sum for each value.
we can use the same concept, choose R as root and calculate its distanc sum first.
then distanceSum(A) and distance(B) can calcusate from the same formula.

and we just iterate from `R` to left and from `R` to right to calculate every value's distance sum