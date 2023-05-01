# Intuition

這題要找的是讓這整段區間在數值上是連續的最小操作數是多少

首先因為index並不影響, 所以我們可以先對nums排序
排序後對於每個nums[i]來說, 以`nums[i]`作為左端點的區間, 其右端點為`nums[i]+n-1`

也就是說我們如果遍歷左端點, 右端點也會相對應的確定
我們這時就看`[nums[i], nums[i]+n-1]`這段區間已經有多少數值連續的元素

如下圖所示
那這樣我們需要的操作數就是將`nums[i]`之前的元素以及從`nums[j]`開始之後的每個元素
把他們全加進`nums[i:j)`區間的次數, 也就是這些元素的個數

所以是全部的個數`n`減去已經是連續區間的個數`j-i`, 亦即`n-(j-i)`
所以我們僅需要遍歷每個nums[i]找出以其為左端點所需要的操作數即可

```
X X X X X [X X X X X X X X X X] X X X X X
           i                    j
```

所以這其實是個sliding window problem
我們固定左端點`i`, 然後右端點持續走, sliding window右端點最遠走到小於等於`nums[i]+(n-1)`
然後看裡面已經有多少連續合法的數值在這sliding window裡
所需要的操作數就是總數目`n`減去sliding window內的個數`j-i` (nums[i:j) 左閉右開的區間)

但有個前提是, `nums[i:j)`這區間內的每個數必須是**unique**的
所以我們先將nums去除重複的數並排序
`arr = sorted(set(nums))`

這樣一來我們便能在`arr`上遍歷每個arr[i]作為左端點
然後滑動sliding window找出最小操作數
