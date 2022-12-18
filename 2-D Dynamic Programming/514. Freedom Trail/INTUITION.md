# Top-Down DP (Recursion + Memorization)

## Intuition

we can rotate ring left or rotate ring right at each `key[i]`

just DFS it and choose minimum one

*minimum step=1 because we need to press button*

## Complexity
- Time complexity: O($n^2*K$) = O($n^2*K$) where K is length of key and n is length of ring

O($(2*n^2)^K$) without memorization

$O(n)$ for rightRotate, leftRotate

O($n^2$) for while loop + rotate

two branch for decision tree (left rotate or right rotate)

and decision tree height is K

- Space complexity:
$$O(nK)$$

# Top-Down DP (Optimized)

## Intuition

use hashmap `charAt` to store index of each character in `ring`

for each `key[i]` character, we can use `charAt` to quickly find target ring character's index `ringAt`

and our left-rotate and right-rotate steps are:

```
delta = abs(j-ringAt) where j is current index of ring[0]

delta, len(ring)-delta are the steps for either left-rotate or right-rotate

and we choose minimum step to target character
```

if we have two or more same character, which means `len(charAt[key[j]]) > 1`, we choose option with minimum steps

ex. key[i] = "g" and there exists mulitple `"g"` in `ring`, we need to try both of them and choose one with minimum total steps

# Complexity

since we use hashmap to store index information

- time complexity: O($RK$) where R is length of ring and K is length of key