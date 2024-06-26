# Intuition

一開始先注意到 cols <= 5, 而rows <= 10^4
代表rows其實會有很多重複, 如果去除重複後其實最多就2^5種可能的rows
那這下O(n^2), O(n^3)就都是可接受的時間複雜度了

再來就是想一下有沒有什麼Greedy的方法
就先想到0肯定是越多越好 (1越少越好)
所以或許根據這點對rows做排序後, 從1越少的開始判斷

再來的情況就是:
1. 如果有row = [0,0,0,0,0], 那可以直接返回該index

2. 再來我們持續增加row來看看

當挑row=2時, 這時每個column最多能不超過1
由於事binary grid, 任意兩兩配對相互進行bit operation **AND** 後為0則為答案

而row=3還是最多不能超過1, 所以挑3個row毫無益處
直接看row=4的情況, 這時每個column和不能超過2

我們看看有沒有需要4個row才合法的答案
=> 代表每個column的和最多為`2`
=> 但看了一下會發現, 在滿足rows=4的情況時, **必定存在著兩個row可以滿足row=2的條件**
=> 也就是必定存在著兩個row相互 **AND** 後為0

[0,1,1,0,0]
[0,0,0,1,1]
[1,1,0,0,1]
[1,0,1,1,0]

那這時我們就能greedily的想一下, 這是不是代表其實我們只要找任意兩個row來檢查即可?
並且透過hashmap去除重複後, O(n^2)也會是可行解

所以我們只需要將每個row轉成bitmask後, 利用hashmap存{bitmask: index}
1. 再來兩兩配對, 以O(N^2)的時間就能找出是否有滿足row=2的情況
2. 而在轉成bitmask的同時, 能同時檢查有沒有任意row全部column都為零的情況

只要上述兩點有滿足條件的情況即可直接返回合法解的index
都沒有則返回`[]`