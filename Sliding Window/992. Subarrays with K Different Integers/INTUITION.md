# Intuition

看到subarray with k distinct characters, 直覺想到的是透過sliding window/two pointers來找出合法subarray

但卻發現如果我們沒辦法有個合適的條件來限制移動`l`, `r`指針, 並使得我們能涵蓋**Example 1**跟**Example 2**

sliding window 能計算的只有在不超過**k** distinct characters的情況下有多少種subarray
如果是這樣子的話, 我們才能:
- 持續移動右邊界`r`
- 直到sliding window內的distinct characters > k後移動左邊界`l`
- 每次移動右邊界`r`時, 在左閉右開的slidwin window`[l:r)`內, 在不超過k distinct characters的情況下, 每次都有`r-l-1`個左邊界可形成不超過**k distinct characters**的subarray
  - 相當於右邊界固定在`r-1`時, l有`r-l-1`個位置所形成的subarray都是不超過k distinct characters的

程式碼及想法如下:
我們持續移動右邊界, 在distinct characters不超過k的情況下
相當於每次固定右邊界, 然後看有多少左邊界能形成不超過k distinct characters的subarray
```
[X X X X X]
 l       r
 X X X X X
   X X X X
     X X X
       X X
         X
count += r-l+1
```

```py
n = len(nums)
res = l = r = 0
window = defaultdict(int)

# [l:r) 左閉右開
while r < n:
    window[nums[r]] += 1
    r += 1

    while l < r and len(window) > k:
        window[nums[l]] -= 1
        if window[nums[l]] == 0:
            del window[nums[l]]
        l += 1

    res += r-l-1
        
return res
```

這時, 這題最重要的突破口就是
`Exactly K Distinct Characters = At Most K Distinct Characters - At Most K-1 Distinct Characters`

也就是說如果我們能求出最多為**K distinct characters**的所有subarray的話
我們只要將結果減去最多為**K-1 distinct characters**的所有subarray後
剩下的就是**Exactly K distinct characters**的所有subarray了

所以根據這個想法, 我們只要用一個helper function, 透過sliding window求出最多不超過k跟k-1的情況後
相減即為答案`answer = exactly(K) = slidingWindowAtMost(K) - slidingWindowAtMost(K-1)`

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$