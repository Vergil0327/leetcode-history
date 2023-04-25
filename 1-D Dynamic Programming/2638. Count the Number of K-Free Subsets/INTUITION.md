# Intuition

沒有任何元素相差為k, 首先必須得想到的是我們可以將每個nums[i]對k取餘數來分組
餘數不同, 必定不可能相差為k
這樣最後答案就是各組的取法相乘即為答案

```
nums[i]%k=0   nums[i]%k=1 ...
{X X X X X } {X X X X X } ...
```

```py
arr = [[] for _ in range(k)]
for num in nums:
    arr[num%k].append(num)

res = 1
for i in range(k):
    res *= count(arr[i])
return res
```

至於各組內該如何取, 那就是個house robber的問題了

首先我們可以排個序, 然後看nums[i]跟nums[i-1]
- if nums[i] == nums[i-1] + k
  - 當下取nums[i]的方法為前一輪不取nums[i-1]的方法
  - 當下不取nums[i]的方法為前一輪取或不取都行
- if nums[i] != nums[i-1] + k
  - 當前這輪取或不取都跟前一輪無關