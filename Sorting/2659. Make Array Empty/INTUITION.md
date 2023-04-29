# Intuition

這題能想到的是, 只少需要`n`個remove operations
再來就是如果需要rotate, rotate的次數就是排在nums[i]前面並且比nums[i]還大的數
但不包含已經remove掉的數

所以如果我們對`nums`由小到大排序, 並記住nums[i]的原始index

- `n-i`就是我們把原本排在前面的數往後rotate的次數

```
# after sorted
X X X X X {X} X X X X X X
           i -> n-i 個比nums[i]還大的數
```

但當初weekly contest沒想到是, 該如何判斷有rotate還是沒rotate

但其實對於當前的nums[i]來說, 如果前一個nums[i-1]的原始index排在原始nums[i]前面的話
那代表nums[i]不需要rotate

但如果我們比較原本的index:
nums[i-1]原本是排在nums[i]後面的話, 那就代表nums[i]必須rotate到nums[i-1]後面

所以我們可以用個變數儲存nums[i-1]的原本index, 然後再用nums[i]的原本index做比較:
- if nums[i].original_index < nums[i-1].original_index: `res += n-i`

```py
arr = []
for i, num in enumerate(nums):
    arr.append((num, i))
arr.sort()

prevIdx = 0
for i, (num, originalIdx) in enumerate(arr):
    if originalIdx < prevIdx: # arr[i]原本排在arr[i-1]前面, 需要rotate
        res += n-i # rotate distance
    prevIdx = originalIdx
```

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(n)$$