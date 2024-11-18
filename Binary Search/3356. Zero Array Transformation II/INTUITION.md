# Intuition

follow-up of [3355. Zero Array Transformation I](https://leetcode.com/problems/zero-array-transformation-i/description/)

直接用`leetcode 3355`的結果, 配合binary search去猜`k`即可

為什麼binary search可以? 因為符合單調性

- 如果`k-1`次已經可以zero array, 那麼`k`次肯定也可以
- 如果`k+1`次都還不能zero array, 那麼`k`次肯定也不行

有了單調遞增或單調遞減這特性, 我們就能利用binary search去逐步淘汰掉一半的可能去猜`k`