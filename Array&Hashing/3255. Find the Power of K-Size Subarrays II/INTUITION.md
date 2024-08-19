# Intuition

我們可以遍歷的過程中紀錄當前的最大連續subarray size, `consecutive`
有了這資訊後我們就能很簡單判斷:

**只要滿足`consecutive >= k`, 那麼[i-k+1:i]這段範圍就是合法的subarray, 並且nums[i-k+1]的power為nums[i]


所以我們只要以O(n)時間維護好`consecutive`這個變數, 並在滿足條件情況下更新即可:

```py
consecutive = 1
for i in range(n):
    if i and nums[i] == nums[i-1]+1:
        consecutive += 1
    else:
        consecutive = 1

    if consecutive >= k:
        res[i-k+1] = nums[i]
```