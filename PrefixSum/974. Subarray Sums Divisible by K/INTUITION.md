# Intuition

key point is:

`sum[j:i] = prefix_sum[i] - prefix_sum[j-1]`

```
in order to make sum[j:i]%k = 0,
if prefix_sum[i] % k = m, prefix_sum[j-1] % k must equal m
```

for every prefix_sum[i] whose **sum%k = M**, if we know there are `N` subarray whose **prefix_sum % k = M** before, then we have `N` subarray to make **sum(array[:i])%k = 0**


```
nums = [_ _ k _ _ j _______ i]
sum(nums[:k])%k = m
sum(nums[:j])%k = m
sum(nums[:i])%k = m

-> sum[k:i] % k = 0
-> sum[j:i] % k = 0
```

**Edge Case / Base Case**

we must add `hashmap[0] = 1` as base case because if **prefix_sum[i]%k = 0**, it's already a valid cound

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$