# Intuition

transformed from [Leetcode 23. Merge K Sorted Lists](../../Linked%20List/23.%20Merge%20k%20Sorted%20Lists/)

for example, we have nums1 = [1,7,11], nums2 = [2,4,6]

we can turn it into three linked list:

```
[1, 2] -> [1, 4] -> [1, 6]
[7, 2] -> [7, 4] -> [7, 6]
[11, 2] -> [11, 4] -> [11, 6]
```

and store these list into min heap like this:

`[nums1[i]+nums2[index], nums1[i], current index of nums2]`,

since we need to pick minimum sum first, put sum in 1st position

whenever we pop out from min heap, we move index of nums2 to next and append back to min heap

## Complexity

- time complexity

$$O(klogm)$$

- space complexity

$$O(m)**