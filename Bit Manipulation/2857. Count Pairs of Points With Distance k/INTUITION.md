# Intuition

`x1^x2 + y1^y2 = a + b = k` => `b = k-a`

since 0 <= k <= 100, we can iterate all possible combination `a` and `k-a` to check each coordinates[i]'s contribution

we know that:
`x1^x2 = a` => `x2 = a^x1`
`y1^y2 = b` => `y2 = a^y1`

thus, if current `coordinates[i] = x1, y1`, our target will be `[a^x1, b^y1]` or `[b^x1, a^y1]`

we can just use hashmap to check how many pairs we can make for `coordinates[i]`

# Complexity
- Time complexity:
$$O(kn)$$

- Space complexity:
$$O(n)$$
