# Intuition

首先想到的是要如何檢查是不是sub sequence?

只要用two pointers紀錄在`s`跟`p`的位置即可
我們遍歷`s`, 只要s[i] == p[j], 就能移動`j`，看我們能不能讓`j`走到`len(p)`即可，時間複雜度為O(n)

既然這樣，那最笨的方式就是暴力解，O(n*k)，逐個刪減逐個搜索

既然可以linear search，我們能進一步想一下能不能binary search

但由於這題要求`k`是前`k`個都要刪除才是合法的`k`，也就是removable[:k]都要從`s`中移除
這下就符合binary search的單調性質了

因為k越大，`p`越不可能是`s`的subsequence，因為removable[i]都是distinct的，`s`的字符只會越來越少