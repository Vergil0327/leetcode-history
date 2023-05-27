# Intuition

我們目標是要找出最少操作數使得兩邊的**diff**為0

首先將兩邊`A=sum(nums1)`, `B=sum(nums2)`求出來

再來可以先想一下有沒有貪心的最佳策略

我們肯定是要盡可能的減少diff, 所以我們可以先對`nums1`, `nums2`排序
然後根據`A-B`的結果可以分出三種情形討論

- **A = B**: 直接返回0
- **A > B**
  - 我們可以decrease A
  - 可以increase B
  - 所以我們肯定是優先從這兩個操作中找最優的
- **A < B**
  - 可以increase A
  - 可以decrease B
  - 一樣從兩者中找最優的

以**A>B**為例:

如果要decrease A的話, 我們就盡可能減少, 所以是把nums1的數變為`1`, 這樣減少的diff為:
`dec = nums1[i]-1 if i >= 0 else 0`

反之如果要increaseB的話, 我們最多能增加:
`inc = 6-nums2[j] if j < m else 0`

我們優先移動較大的那邊:
```py
while i >= 0 or j < m:
    dec = nums1[i]-1 if i >= 0 else 0
    inc = 6-nums2[j] if j < m else 0
    if dec > inc:
        diff -= dec
        i -= 1
    elif dec < inc:
        diff -= inc
        j += 1
    elif dec > 0:
        diff -= dec
        i -= 1
    elif inc > 0:
        diff -= inc
        j += 1
```

所以我們就移動雙指針`i`, `j`直到成功讓
- `diff為0`
    ```py
    if diff <= 0: return res
    ```
- 或無法再有合法操作為止, 也就是當`inc`跟`dec`都無法在減少diff的時候
  ```py
  if inc == 0 and dec == 0: return -1
  ```
