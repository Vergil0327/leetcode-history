# Intuition

min-product = min(arr) * sum(arr)

對於每個nums[i]: 如果我們知道他的prevSmaller跟nextSmaller

```
X X X X  ...          X     ...      X
  prevSmaller[i]      i         nextSmaller[i]
```

我們就能鎖定min value為nums[i]的subarray範圍為[prevSmaller[i]+1, nextSmaller[i]-1] (both inclusive)
在配合prefix sum, 就能求出該subarray sum為: presum[nextSmaller[i]] - presum[prevSmaller[i]+1] (1-indexed)

那這樣只要遍歷nums[i]就能求出含有nums[i]的最大min-product為, 在取全局最大即可:

```py
minProduct = max(nums[i] * (presum[nextSmaller[i]] - presum[prevSmaller[i]+1]))
```

而prevSmaller跟nextSmaller我們可以用monotonic stack來以O(n)的時間求得
prefix sum也是O(n)
所以最後時間複雜度為: $O(n)$

最後注意一下, prevSmaller[i]的初始值應為`-1`而nextSmaller[i]則為`n`
