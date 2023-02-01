# Intuition

這題算是 [leetcode 241](https://leetcode.com/problems/different-ways-to-add-parentheses/) 的進階題

首先這類型的加減乘除題目應該首先要想到的是`遞歸處理`，括號的作用可以想成我們任意分成兩邊，然後兩邊的數進行加減乘除

並且一個運算符號左右兩邊一定就只有一個數字，因此我們我們遞歸目標就是找出放運算符號的位置，k個數就有`k-1`個位置可以放運算符號，我們就全部遍歷一遍進行加減乘除

例如將[1,2,3,4]遞歸分成[1]跟[2,3,4]兩邊的話，兩邊進行加減乘除就相當於`(1) +-*/ (2,3,4)`

所以這樣這題就可以簡化成利用divide and conquer的概念，分成兩邊然後進行加減乘除，得出所有可能，在確認有沒有24這個答案在裡頭

```py
def dfs(nums, l, r):
    if l == r: return {nums[l]}

    res = set()
    for i in range(l, r):
        left = dfs(nums, l, i)
        right = dfs(nums, i+1, r)
        for x in left:
            for y in right:
                res.add(x+y)
                res.add(x-y)
                res.add(x*y)
                if y != 0:
                    res.add(x/y)
    return res
```

那為什麼加入到hashset是因為，這樣我們可以去除duplicate避免遍歷加上DFS的時候，太多重複可能性導致遞歸爆炸

那這題由於cards裡的四張牌並不一定是給定的排序，所以所有排列組合都要嘗試
因此首先得找出所有可能排列，然後在進行divide & conquer