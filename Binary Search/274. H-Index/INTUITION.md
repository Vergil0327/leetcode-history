# Intuition

it's straightforward to come up with `sorting` first.

then we can find a optimal value to make

`citations[i] >= n-i` and H-index is `n-i`

if H-index get bigger, possible answer get smaller and vice versa.

therefore, we can use this condition to binary search it.

ex. citations = [0,1,3,5,6]
```
if citations[mid] >= n-mid:
    lower upperbound and current upperbound is possible answer
else:
    upper lowerbound
```

be aware of that after we finish binary-search, we need to make sure what we found is valid H-index, we need to check again

ex. citations = [0], the answer is 0 not 1

0 = hIndex(citations), thus H-index = n-i = 1-0 = 1.
but citations[0] is not greater than H-index

# Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(1)$$