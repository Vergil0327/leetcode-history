# Intuition

```
{X X X X X X X} X X X X
 l           r
```

當nums[l:r]為合法subarray時, 此時對於左端點`l`來說, `r`到`n-1`位置都會是合法右端點
這些subarray都會符合`# of distinct in subarray`等於`# of distinct in whole array`

所以我們只要sliding window去掃過一遍即可

### sliding window 模板

```py
while r < n:
    # add element nums[r]
    r += 1

    # might check condition and update result here

    while l < r and condition:
        # might check condition and update result here

        # remove element nums[l]
        l += 1

    # might check condition and update result here
```

# Complexity

time: O(n)
space: O(1)