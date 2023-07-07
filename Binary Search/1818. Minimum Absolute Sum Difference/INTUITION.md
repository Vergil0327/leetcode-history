# Intuition

try binary search to find minimum absolute sum difference

```py
l, r = 0, mod
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

now, we need to think if we can have a `check` function to check whether `mid` is a valid answer or not:

we can iterate from i=0 to i=n-1 and see if we can get lower diff by replace nums1[i]:
    => first, sort nums1
    => use binary search to find replacement of nums1[i] by searching nums2[i] becuase replacement of nums1[i] should be as close to nums2[i] as possible
    => if idx = bisect_left(sorted_nums1, nums2[i]), we can try replacing nums1[i] with sorted_nums1[idx] and sorted_nums1[idx-1]

=> we have correctness, but TLE. => logn * nlong with largest number summation

or we don't try to search answer directly using binary search, we iterate through nums1 and nums2 and try to find best replacement at each position.

at i position:
    - origin = abs(nums1[i]-nums2[i])
    - replace = abs(x-nums2[i]) where x can be found by binary search
        - if j = bisect.bisect_left(sorted_nums1, nums2[i])
        - replace can be sorted_nums1[j] or sorted_nums1[j-1]

# Complexity

- time complexity
$$O(nlogn)$$