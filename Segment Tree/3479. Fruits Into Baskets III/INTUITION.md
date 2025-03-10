# Intuition

遍歷每個fruits[i], 找到**合法**的leftmost baskets[j]

其中合法代表baskets[j]必須**大於等於**fruits[j], 並且拿走後就不能再被使用

這種要在區間內同時進行查詢跟更新的, 首先考慮segment tree

1. 對於整顆segment tree, 我們可以很快判斷當前整棵樹的最大值是不是符合**大於等於**fruits[i]
2. 如果符合, 那就往下找出leaf node, 並且再加上個條件 => 優先往左子樹找
3. 那這樣找到最後就會是leftmost valid leaf node, 我們返回index
4. 然後在反過頭來, 將該index更新為-1, 代表已被取用, 並更新整顆segment tree的max