# Intuition

there are two cases for invitation:

1. two long list (middle is cycle with size 2)

A likes B and B likes A and rest of employee sit side by side next to hisfavorite one

C likes D and D likes C and rest of employee sit side by side next to hisfavorite one

```
x -> x -> x -> A -> <- B <- o <- o <- o
'                                     '
'                                     '
x -> x -> x -> C -> <- D <- o <- o <- o
```

every list is independent from other list. each list can be invited and form a large round table, since everyone still sits next to his favorite

it there are 3 or more chain, all of them can be invited and sits in a large circle

therefore, `invitation = max(invitation, sum(chain_size))`

2. everyone sits next to his favorite one in a circle

```
 o -> o -> o -> o
 ^              |
 |              V
 o <- o <- o <- o
```

therefore, `invitation = max(invitation, cycle_size)`

# Approach

1. we can use topological sort to strip chain list and find size of chain list simultaneously
2. after we finish topological sort, rest of unvisited node should exists in cycle form, we can iteratue through each cycle
   1. if cycle size >= 3, find largest cycle size (case2 above)
   2. if cycle size == 2, we can see it as two long chain (case1 above)
3. choose `max(cycle_size, sum(chain_size))`

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$