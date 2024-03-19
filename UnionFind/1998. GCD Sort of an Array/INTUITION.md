# Intuition

gcd > 1的為同個group, 可自由swap

如果gcd(X, Y) > 1, gcd(X, Z) > 1 => 那(X, Y, Z)可自由swap

所以最後會union出很多sorted group:
group1: [idxA1, idxA2, idxA3, ...] => 代表這些index位置可以自由排序/換位
group2: [idxB1, idxB2, idxB3, ...]
group3: [idxC]

這些group我們可以先對每個nums[i]找出prime factors去分類
然後再將同個group裡的每個元素都union起來

那如果最終答案是sorted_nums所對應的index分別對應是: [idxB1, idxA1, idxB2, idxB3, ...]
就看原本的index [0,     1,     2,     3, ...]
跟相對應的      [idxB1, idxA1, idxB2, idxB3, ...]
能不能swap, 也就是看nums[0]有沒有跟nums[idxB1]在同個group裡

也就是我們就遍歷sorted_nums然後看sorted_nums[i]跟nums[i]有沒有在同個union裡即可
有duplicate也沒關係, 因為相同nums[i]必定在同個group, 所以有duplicate的話用hashmap `v2idx`去紀錄任一個nums[i]的位置即可

```py
v2idx = {nums[i]:i for i in range(n)}
sorted_nums = sorted(nums)
for i in range(n):
    if find(i) != find(v2idx[sorted_nums[i]]): return False
return True
```


time: $O(n*sqrt(n) + nlogn)$