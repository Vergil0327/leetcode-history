# Intuition

我們可以換掉一個元素, 所以假設我們換掉nums[i]
那麼我們只需要知道:
1. 以nums[i-1]結尾的longest non-decreasing subarray length
2. 以nums[i+1]開頭的longest non-decreasing subarray length

知道後我們就能更新`res = max(res, left[i-1] + 1 + right[i+1])`

然後再考慮單獨存在的`non-decreasing subarray length + 1`