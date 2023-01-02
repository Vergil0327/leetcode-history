# Sliding Window

## Intuition

找出最小subarray使得總和>=target，這很明顯是個Sliding Window的問題
只要我們維護一個window，當總和小於target時持續移動右邊界，當總和大於等於target時，縮小左邊界找最小subarray即可

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$

# Binary Search

## Intuition

另外這題也可用binary search
首先可以先想到如果要brute force的話，我們需要兩層循環遍歷所有可能的subbary[i:j]找出最小

但由於這題要的是總和大於等於target的subarray，因此我們可以先將原本的`nums`數組轉乘prefix sum的形式，然後遍歷一遍使得`i`作為subbary的起始點並透過**binary search**找出`j`使得`[0:j]的和恰好 >= presum[i-1] + target`，相當於用binary search找出upperbound

如此遍歷一遍後即可

核心程式碼為
```
for i in range(1, len(presum)):
    prefixSum = presum[i-1] + target
    j = bisect_left(presum, prefixSum)
    if j < len(presum):
        ans = min(ans, j-i+1) # 更新answer, subarray 長度為 j-i+1
```

## Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(n)$$