# Intuition

O(n) space的解法很簡單，但O(1) space的解法則是[leetcode 169. Major Element](../169.%20Majority%20Element/)的follow-up

leetcode 169的O(1) space解法可參考[這篇文章](https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html)

首先我們能想到的是，這題對於眾數的要求是`freq > len(nums)//3`，這但表對於一個`nums`來說:

`至多存在2個Major Element符合這要求，不會出現第三個`

因此我們可以將`leetcode 169. Major Element`的O(1) Space解法做延伸

我們用cnt1, maj1, cnt2, maj2來記錄出現最多次數的兩個眾數

邏輯是:

1. 每當當前的`num`等於`maj1`或`maj2`時，則相對應的cnt則加一
2. 當`cnt1`或`cnt2`為零時，則假設當前的`num`為major element
3. 當當前`num`不等於當前假設的`maj1`或`maj2`時，則`cnt1`和`cnt2`都減一

這樣最後會留下兩個眾數，分別記錄在`maj1`及`maj2`
這時我們在做一次確認，確認他們出現的頻率有大於`len(nums)//3`的話，即為答案之一

最後返回符合要求的答案即可