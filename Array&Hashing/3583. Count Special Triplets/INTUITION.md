# Intuition - 1

記錄每個nums[i]的index位置到`defaultdict(list)`裡
然後遍歷nums[i], 利用binary search找尋target(=nums[i]*2)的`大於i`, `小於i`的index位置

那麼就能得出nums[i]的貢獻: `res = (res + L * R) % 1000000007` 其中:

- R = bisect_right(count[target], i)
- L = bisect_left(count[target], i)

time: O(nlogn)
space: O(n)

# Optimized

將每個nums[i]當作一個bucket, 去記錄每個nums[i]的數目


```py
mx = 2 * 10**5 # nums[i] <= 10^5

left = [0] * (mx + 1)
right = [0] * (mx + 1)
for x in nums:
    right[x] += 1
```

然後遍歷nums[i]: `res = (res + left[need] * right[need]) % mod`
並更新left[need], right[need]

time: O(n)
space:O(max(nums[i]))