# Intuition

substring -> 直覺想到用sliding window
常用sliding window來找的就是**至少幾次**條件的substring

所以如果我們記錄有多少個字母至少出現`k`次
一但出現substring滿足至少有`1個`字母出現**至少k次**, 我們就移動左邊界`l`
這時對於固定左邊界`l`來說, 合法右邊界有`n-r`個

ex. 假設[l:r]已滿足條件, 對於左邊界`l`來說, `r`從`r`到`n-1`都可以滿足條件
所以`answer += n-r`

```
{X X X X X X X} X X X X X
 l           r ->
```

整個O(n)掃過一遍後即得到每個`l`位置所能貢獻的合法右邊界`r`, 相當於合法substring的數目了

time: O(n)
space: O(1)