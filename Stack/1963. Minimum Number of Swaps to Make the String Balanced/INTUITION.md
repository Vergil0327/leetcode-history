# Stack

## Intuition

```
"][" 1 -> "[]"
"]][[" 1 -> "[[]]"
"]]][[[" 2 -> "[]][][" -> "[[][]]"
"]]]][[[[" 2 -> "[]]][[][" -> "[[]][[]]"
"]]]]][[[[[" 3
"]]]]]][[[[[[" 3
```

traverse once and pop out valid balanced pairs in stack first
and we can see that:

in optimcal swap way, each swap can fix 2 inbalanced pairs at most, which means

`n operations can cover 2n-1 or 2n inbalanced pairs`

thus, the minimum swaps is `pairs//2 + pairs%2`

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$

# Space Optimized

since the only thing we care is how many inbalanced pairs we have, therefore, we can use one variable to keep tracks of it and get rid of whole `stack`