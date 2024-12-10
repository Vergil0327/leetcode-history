# Intuition

subarray sum => 想到 prefix sum
要找maximum subarray sum and size is divisible by k => 把每個prefix sum以當前`size%k`為key儲存在hashmap
而且僅需儲存最小的, 亦即:

```
seen = {size%k: minimum prefix sum}
```

那這樣我們再遍歷subarray sum的時候就能直接利用:
- update res by prefix_sum[i] if (size:=i+1)%k == 0
- update res by prefix_sum[i] - seen[(size:=i+1)%k]
- update seen[size%k] = min(seen[size%k], presum[size])


time: O(n)
space: O(n)