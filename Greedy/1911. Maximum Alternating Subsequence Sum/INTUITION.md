# Intuition

一開始先想一下該怎麼做
看看有沒有直覺greedy soluion

先挑第一個作為positive alternating sum, 再來如果有更大就換更大, 更小的話就選做negative alternating sum, 然後邏輯相似, 只是反過來, 下個更小就換掉, 更大就作為positive alternating sum

這樣我們總和就會持續往上, 由於我們選擇只跟前一個選擇有關, stack看起來是蠻適合的資料結構

```
nums = XXXXXX
stack = []
```

如果stack.size%2==0, 此時nums[i]為positive sum, stack[-1]為negative alternating sum
- 如果nums[i]比stack[-1]小, 那就持續更新stack[-1]
- 如果nums[i]比stack[-1]大, 那就選做positive sum

同樣地, 如果stack.size%2 == 1, 此時nums[i]為negative sum, stack[-1]為positive alternating sum
- 如果nums[i]比stack[-1]更大, 那就持續更新stack[-1]
- 如果nums[i]比stack[-1]小, 那就選做negative sum, 並重複上面邏輯

最後要注意的是: 如果最終找不到, 並且以negative sum結尾
那我們就應該pop掉最後的negative alternating sum

這樣我們的總和就會持續增加, 為最佳解


但其實這題跟這題類似:[122. Best Time to Buy and Sell Stock II](Array%26Hashing/122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II/README.md)

我們其實只真正需要:

```py
res = nums[0]
for i in range(1, len(nums)):
    res += max(0, nums[i]-nums[i-1])
return res
```

因為取完negative sum後, 我們肯定得找一個比原本negative sum還大的來讓總和增加
所以實際上就是將positive delta sum給加總起來

# Intuition 2 - DP

定義:
- odd: the maximum alternating sum ended at odd index
- even: the maximum alternating sum ended at even index

{XXXXXX}X

對於i-th element來說:
1. update even: even = max(even, odd+nums[i])
2. update odd: odd = max(odd, even-nums[i])

狀態轉移:
```py
odd = even = 0
for num in nums:
    odd, even = max(odd, even-num), max(even, odd+num)
return even
```

由於even是ended at positive nums[i], 所以even >= odd

所以最終答案就是even