# Intuition

這題目標就是將整個array均分成 `sum(array)//n = target`
既然已經知道每個index需要的數目 `machines[i] - target`，最有效率的方式就是一次送出需要的數量，並且可以的話，整個區間往同個方向遞送dress過去最有效率

ex. [0,0,11,5], target = 4
-> [0,1,11,4], operations = 1
-> [0,4,8,5], operations = 3
-> [4,4,4,4], operations = 4
最少可以在8個步驟完成

因此我們可以找出每個machines[i]要往左往右送出多少，找出必要的最大淨輸出，即為最少步驟

對於每個machines[i]來說，他們的淨輸出，我們可以定義為:
`left[i] + right[i] = machines[i] - target`,
其中left[i]為往左側的淨輸出，right[i]為往右側的淨輸出

由於只能往鄰近的machine送，因此我們還有這個關係式:
`left[i] = -right[i-1]`
往左送出left[i] 相當於左邊往右輸出-right[i-1] (也就是需要right[i-1]個)

而最左、最右兩側machines[0] & machines[i]只能往一方遞送，因此
```
left[0] = 0
right[0] = machines[0] - target

left[n-1] = machines[n-1] - target
right[n-1] = 0
```

所以我們可以求得每個 `i` 位置的左右淨輸出為 left[i] 及 right[i]

遍歷取max及得答案:
`res = max(res, max(0, left[i]) + max(0, right[i]))`

ex. [0,0,11,5], target = 4

index =   0,  1,  2, 3
left  = [ 0,  4,  8, 1]
right = [-4, -8, -1, 0]

最少步驟為machines[2]往左遞送8個，其中有1個是右側machines[3]往左送過來的
但由於最高效率是整個區間同步往左遞送，因此不會產生額外步驟