# Intuition

for any nums[i], we want to find nums[j] in nums[i+m-1:] where nums[i] * nums[j] has max product
    
since nums[i] can be negative, maybe we should record suffix_max and suffix_min to find best nums[j]

time: O(n)
space: O(2n)

# Optimized

iterate nums[j] and only need to record max and min of nums[j-(m-1)+1]

```py
res = -inf
max_pref = nums[0]
min_pref = nums[0]

for j in range(m - 1, n):
    res = max(res,
                max_pref * nums[j],
                min_pref * nums[j])

    idx = j - (m - 1) + 1
    if idx < n:
        max_pref = max(max_pref, nums[idx])
        min_pref = min(min_pref, nums[idx])
```

time: O(n)
space:O(1)