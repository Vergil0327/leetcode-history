# Intuition

根據brute force solution:
把每個相同的nums[i]集合在一起後會各自得到index
group: { nums[i]: [i0, i1, i2, i3, i4, ...] }

所以觀察nums[i]來說:
distance_between_other[i0] = (i0-i0) + i1-i0 + i2-i0 + i3-i0 + i4-i0 + i5-i0 ...
distance_between_other[i1] = i1-i0 + (i1-i1) + i2-i1 + i3-i1 + i4-i1 + i5-i1 ...
distance_between_other[i2] = i1-i0 + i2-i1 + (i2-i2) + i3-i2 + i4-i2 + i5-i2 ...
...

```
所以 distance_between_other[ix] 
    = ix-i0 + ix-i1 + ix-i2 + ix-i3 + ... + ix-ix + i_{x+1}-ix + i_{x+2}-ix + ...
    = ix * left_count - (i0+i1+i2+...+i_{x-1}) + (i_{x+1} + i_{x+2} + ... + i_n) - ix * right_count
    = left_part + right_part
```

因此我們從左往右掃一遍可計算left_part的貢獻:

`left_part = ix * left_count - (i0+i1+i2+...+i_{x-1})`

```py
count = defaultdict(int)
prefix_sum = defaultdict(int)
for i, num in enumerate(nums):
    res[i] += count[num] * i - prefix_sum[num]
    prefix_sum[num] += i
    count[num] += 1
```

然後再從右往左掃一遍可計算right_part

`right_part = (i_{x+1} + i_{x+2} + ... + i_n) - ix * right_count`

```py
count = defaultdict(int)
post_sum = defaultdict(int)
for i in range(n-1, -1, -1):
    res[i] += post_sum[nums[i]] - count[nums[i]] * i
    post_sum[nums[i]] += i
    count[nums[i]] += 1
```