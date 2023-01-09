# Intuition

藉由這個例子，我們可以寫出模擬出整個流程(Brute Force)

```
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
```

整個過程中，我們輪流從最左邊或最右邊開始刪減掉一半的數
仔細看會發現，或者從Brute Force也會發現:
- 每當從左開始刪減時，首位數便會往右挪移**1個step**
- 而當從右開始刪減時:
  - 當總數為偶數的時候不變
  - 當總數為奇數的時候，首位也會往右挪移**1個step**

因此我們可以同樣模擬整個流程，但僅保留幾個必要的資訊來讓我們逐漸移除掉nums
為了讓我們能recursively or iteratively縮減n，我們必須知道這些資訊:
1. 目前總數 `n`
2. 目前首位數的index `i`
3. 當前操作是從左刪減還從右開始 `startFromLeft`
4. 以及每次移動的 `step` 是多少

由於一開始便會從index `0` 開始刪除，因此起始首位index `i` 為 **1**

而 `startFromLeft` 則是交替變換

雖然每次遞歸移動的step都是**1**，但每次都會刪減掉一半的數，因此移動的`step`每次操作後都會乘以2

# Complexity

- time complexity
$$O(logn)$$

- space complexity
$$O(1)$$