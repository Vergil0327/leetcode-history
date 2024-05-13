# Intuition

假設cost1 < cost2/2, 那就沒必要使用cost2, 全用cost1 operation即可
所以一開始我們能先對cost2進行一下處理: `cost2 = min(cost1*2, cost2)`
這樣後續使用cost2 operation時, 就會是最合算的cost

所以接下來我們的做法就是盡可能地使用cost2 operations
我們找出數量最少的min(nums)去跟其他作配對, 等到全部配對完如果還有剩下的min(nums), 那些在用cost1 op.來解決

但這題還有個關鍵是:
我們除了將每個nums[i]都拉高到max(nums)以外, 還可以選擇將全部拉高到max(nums)+x
將剩下的那些需要用cost1 op.處理的也全改成用cost2 op.
這情況會發生在: cost1 >>>> cost2時, 我們肯定避免使用cost1
所以我們可以拉高target limit來將cost1 op.轉換成cost2 op.
例如這例子: nums=[1,14,14,15], cost1=2, cost2=1
```
[1,14,14,15]
 2 15 14 15
 3 15 15 15
 4 16 15 15
 5 16 16 15
 6 16 16 16
 9 17 17 17
 12 18 18 18
 15 19 19 19
 18 20 20 20
 19 20 20 20
 20 20 20 20 => minimum step = 20
```

而這target limit是多少其實不確定, 但最高只會到max(nums)*2
因為將目標拉到兩倍後, 肯定會將最少的min(nums)給全部配對完, 僅剩最後1個或0個, 這得看整體數目是奇數或偶數

詳細說明可參看[@huifengGuan](https://www.youtube.com/watch?v=h6R2NEdwlQ8&ab_channel=HuifengGuan)

