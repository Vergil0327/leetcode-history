# Intuition

```  
X X X X X X X X X X X
          i
```

當prefix sum + nums[i] < 0的話, 代表我們必須要選一個nums[j] 其中 0 <= j <= i放到最後
使得prefix sum > 0

既然如此, 那肯定是挑一個到目前為止, 最小的負數移到最後
既然要找最小值, 我們可以用min heap來挑這個最小的負數移到最後
那就相當於`prefix sum -= min_heap[0]`

由於test case保證答案肯定存在, 並且我們僅需要知道操作數
所以我們不用考慮再把min_heap[0]移到nums最後

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(n)$$