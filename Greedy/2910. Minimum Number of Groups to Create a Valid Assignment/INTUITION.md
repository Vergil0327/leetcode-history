# Intuition

只有相同的數能分類到同個groups, 所以首先我們僅需要關注每個distinct num它們的freqency

```py
freq = sorted(Counter(nums).values())
```

ex. freqency = 5, 7, 9, 10, ...
由於第二個constraint, 所以我們目標是要將他們拆分成兩個group, x或x-1
由於我們只能將大的group分成若干個小group, 所以這個x的範圍為[1, min(freqency)], min(frequency)沒辦法往上拆

所以這時我們遍歷一下可能的x, 那麼我們對於每個nums[i]就試著拆分看看
由於我們要minimum number of groups, 所以我們先試著對`x`拆分
```py
a, b = nums[i]//x, nums[i]%x
```

如果b==0, 那很好, 我們將每個groups都拆分成`x`個, 總共有a groups
如果b!=0, 那代表我們必須將部份`x`拆分成`x-1`, 直到將b補成x-1的group
所以首先我們需要`x-1-b`個x-group:
    - 如果x-1-b < 0, 代表我們沒有辦法拆分部分x-group將餘數b補成x-1 => 當前x, x-1不適用
    - 如果x-1-b >= 0, 代表我們可以將`x-1-b`個x-group轉成x-1-group並將b補成x-1-group, 所以共分成a+1個groups