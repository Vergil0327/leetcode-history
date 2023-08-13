# Intuition

```
nums = [X X X X X X X X X X X X X X X]
        i      i+x    j
```

for nums[i], we want to find a nums[j] to make abs(nums[i]-nums[j]) is minimum where `i+x <= j < n`

if nums[i+x:n] is sorted, we can use binary search to find 2 candidates in nums[i+x:n] where nums[j1] <= nums[i] <= nums[j2] and i+x <= j1 < j2 < n

thus, we can use sorted list (or tree map in java) to maintain a sorted nums[i+x:n]

for nums[i]:
- we can find j2 = sorted_list.bisect_right(nums[i])
- j1 = j2-1
- find globally minimum:
  - res = min(res, abs(sorted_list[j2] - nums[i])) if j2 < n
  - res = min(res, abs(sorted_list[j1] - nums[i])) if j1 >= 0

- and don't forget to remove nums[i+x] for next round
  - sorted_list.remove(nums[i+x]) if i+x < n>

# Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(n)$$