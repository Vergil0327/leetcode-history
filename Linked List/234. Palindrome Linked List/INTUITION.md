# Intuition

用O(n)空間比較很簡單, 掃過一遍存到array再來判斷即可
但follow-up就有點有趣了

## Approach 1

第一個解法是巧妙利用遞歸性質, 遞歸從後往前, 再配合另一個pointer指向開頭
達到雙pointer比較的效果

## Approach 2

那既然可以用遞歸, iterative way肯定也行, 只需分三個步驟

1. 透過slow, fast pointer找出middle位置
2. reverse 2nd-half linked list
3. compare side-by-side

示意圖:
```
O -> O -> O -> O -> O -> O -> O -> O
O -> O -> O -> O -> M -> O -> O -> O; M for middle
O -> O -> O -> O <- O <- O <- O <- P; P for prev
X -> O -> O -> O <- O <- O <- O <- Y; compare X.val == Y.val
```

time: $O(n)$
space: $O(1)$