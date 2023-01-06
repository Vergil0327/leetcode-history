# Preorder DFS

## Intuition

we can see lexicographcal numbers as a Trie, and what we want is preorder DFS in lexicographcal order.

since we've already know the rule, we don't need to construct Trie, we can just do DFS in lexicographical order.

```
   1       2
 /   \   /   \
0,...,9 0,...,9
```