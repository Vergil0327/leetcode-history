
# Intuition

### Brute Force

```py
def beautifulSplits(self, nums: List[int]) -> int:
    # convert nums[i] into single string for comparison
    SHIFT = 48
    s = "".join((chr(SHIFT+n) for n in nums))  # list -> str
    
    res = 0
    for i in range(1, len(s)-1):  # first split
        if s[i:].startswith(s[:i]):  # first satisfies
            res += len(s)-2*i  # second does not matter
            for j in range(i+1, 2*i):  # special case!!!
                if s[j:].startswith(s[i:j]):
                    res += 1
        else:  # first does not satisfy
            for j in range(i+1, len(s)):
                if s[j:].startswith(s[i:j]):
                    res += 1
    return res
```

那要高效率檢查一連串數字是否存在prefix, 可以用z_function預處理, 然後以O(1)時間檢查prefix (取代startswith)

首先我們如果有: `z1 = z_function(nums)`
那麼z1[i]代表從nums[i]與nums[0]重合的長度
因此如果z1[i] >= i, 代表: nums[0:i]是nums[i:]的prefix

```
XXXXXX{XXXXXX}[OOOO...]
0      i      

[OOOO...]: 可以是2nd split的位置
```

這時我們就不用管第二個split, 因此第二個split合法位置為`n-2*i` => `res += n - 2*i`


以上是第一種情況: 第一個split使得`nums1 = prefix of nums2`的情形

再來在計算第二種情況: 第二個split使得`nums2 = prefix of nums3`的情形

我們僅需要在計算一次z_function(nums[i:]), 然後再遍歷2nd split並確認即可
但這邊要注意重複計算的問題

假設前面第一次split, 已經滿足`nums1 = prefix of nums2`
那麼2nd split的合法位置為[2*i, 2*i+1, 2*i+2, ..., n-1]

所以如果我們2nd split再遍歷到[2*i, 2*i+1, 2*i+2, ..., n-1]這段範圍的話, 那就會重複計算
因此我們在第一種情況的時候, 記錄一下我們第二次split的遍歷範圍:

1. 如果前面已經滿足z1[i] >= i, 那麼為了避免重複計算[2*i, ..., n-1]這段, 我們2nd split僅需遍歷[i+1, 2*i-1]
2. 如果前面不滿足z1[i] >= i, 那麼我們2nd split就遍歷整個[i+1, n-1]範圍找尋合法位置使得`nums2 = prefix of nums3`

```py
for i in range(1, n): # iterate first split
    if z1[i] >= i:
        maxSize = 2*i
    else:
        maxSize = n

    z2 = z_function(nums[i:])
    for j in range(i+1, maxSize):
        if z2[j-i] >= j-i:
            res += 1
```
