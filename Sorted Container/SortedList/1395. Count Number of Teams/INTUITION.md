# Intuition

我們要找合法triplet (i, j, k), 直覺上我們可以遍歷中間`j`，然後看有多少個合法的左右`i`跟`k`

由於我們要比較`rating[i]<rating[j]<rating[k]`, 所以遍歷過程中用兩個有序容器
左邊持續放入遍歷過的rating[j], 右邊持續彈出遍歷過的rating[j]

如此一來就能透過binary search在兩邊容器找出:
1. 嚴格小於rating[j] / 嚴格大於[j]的數
2. 嚴格大於rating[j] / 嚴格小於[j]的數

兩個數目相乘就是對於的數[j]來說的合法triplet數目


time: O(nlogn)
space: O(n)