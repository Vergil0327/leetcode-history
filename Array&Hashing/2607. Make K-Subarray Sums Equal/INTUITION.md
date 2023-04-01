# Intuition

這題當初看的時候真的是毫無頭緒

```
example 2: Input: arr = [2,5,5,7], k = 3

2 5 5       -> sum = 12
  5 5 7     -> sum = 17
    5 7 2   -> sum = 14        
      7 2 5 -> sum = 14
```

但從上面觀察可知，如果要讓k-length的subarray sum一致的話
`nums[i]`必須等於`nums[i+k]`, `nums[i+2k]`, ..., `nums[i+nk]`
像是example 2的 [2 5 5] 跟 [5 5 7], 2跟7的位置必須是相同的數才能使subarray的和相同

代表我們應該把nums[i], nums[i+k], ..., nums[i+nk]當作一個group來考慮，透過最少操作使他們相同

所以首先我們可以把每個group找出來
找出來後我們對這整個group排序，再來我們要找出一個位置讓每個點能用最短操作抵達
那個點就是他們的中位數

所以最終答案就是找出每個Group後, 每個點到該group中位數的距離總和

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(n)$$