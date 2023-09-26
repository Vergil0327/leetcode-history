# Intuition

希望盡量趨近於中間值 => 首先想到可以先由小到大排個序, 小的往上加然後大的往下減
那麼應該會存在一個分界使得:

```
[X X X X X X] | [X X X X X X]
    left           right
```

- left[i]全往上加k
- right[i]全往下減k
- 此時min為min(left[0], right[0])
- max為(left[-1], right[-1])
那麼就能更新: res = min(res, max-min)

所以如果遍歷這個分界, 就能得知
```
    left           right
[X X X X X X] | [X X X X X X]
           i    i+1
```

left = nums[0:i]
right = nums[i+1:n-1]

mx = max(nums[i]+k, nums[n-1]-k)
mn = min(nums[0]+k, nums[i+1]-k)
res = min(res, mx-mn)

time: O(nlogn) for sorting