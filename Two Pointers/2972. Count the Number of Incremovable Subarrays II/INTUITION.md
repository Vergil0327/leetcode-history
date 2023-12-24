# Intuition

目標是移除一段subarray後, 剩餘的array為strictly increasing
這代表移除後的頭跟尾, **"必須是"** strictly increasing subarray
如下所示:
```
[X X X X X X X X X] X X X X X X X X[X X X X X X X X X]
 increasing part                     increasing part
```

這樣就代表我們strictly increasing array after removing the subarray的左右端點必定落在前後的increasing part裡
隨著左端點往右, 右端點也會相應往右 => two pointers
那左右兩pointers間的那段即是incremovable subarrays
那有多少個?

[X X X X X X X X X] XXXXX [X X X X X X X X X]
 l               L         r              n-1

此時nums[l] < nums[r] => [l+1, r-1]為removable subarray
代表固定左端點為`l`時, 右端點r可以是[r-1, n) => 共有n-(r-1)個subarray