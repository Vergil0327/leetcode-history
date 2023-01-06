# Bucket Sort

## Intuition

首先從整個長度為`n`的數組當中找出`max(nums)`跟`min(nums)`

長度為`n`則有`n-1`個gap，我們可以把這個gap想成是個bucket
整個數組最大的差值為`diff = max(nums)-min(nums)`，把這個差值均攤給`n-1`個bucket後
每個bucket size則為 `ceil(diff / (n-1))`

例如: nums = [3,14,15,83,6,4,19,20,40]. 
這時 n=9，因此我們可以分成8個buckets，然後bucket size則為 `ceil((83-3)/8) = 10`

代表我們會有 [3,3+10), [13, 13+10), [13, 23) ..., 這些bucket
最後會分出這些來
i-th bucket     屬於該bucket range的數
  0           : [3, 6, 4]
  1           : [14, 15, 19, 20]
  3           : [40]
  7           : [83]

那在 `max(nums)` 不等於 `min(nums)`的情況下，我們勢必可以分出若干個bucket
那根據pigeon hole principle，就很簡單的概念，但nums個數大於pigeon hole時，一定會有數值裝不下，就代表一定大於該bucket的數存在(也就是那些沒裝進去的數)

因此我們將每個數分類至每個bucket的同時，維護每個bucket裡的最大及最小值
前一個bucket的最大值與後一個bucket的最小值必定相連，且根據前面的pigeon hole principle，這兩個數值必定大於bucket內各個連續數值的差，因此每個bucket遍歷一遍後即可得到最大連續數的差值

## Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$