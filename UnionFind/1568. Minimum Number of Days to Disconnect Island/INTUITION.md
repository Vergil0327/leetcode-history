# Intuition

disconnected => the number of island != 1
鄰接最多4個land => 最多只需要4次就能讓一個grid不與其他連接
```
 X
XXXX
 X
```

再來在看任意幾何圖形, 在角落位置也就連接兩個land
所以最多僅需要兩天就可以剝離出一個單獨的land使得整個圖示disconnected
```
XXX

XX

 X
XXXX
 XX
```

所以我們可以用union-find來查看當前有多少個island => T:O(m*n) = 30*30 = 900
1. 如果island != 1, 直接返回0
2. 如果island == 1, 那就遍歷每個land, 試著移除掉他, 然後再用union-find查看一次 => O(m*n * m*n) = O(900*900) = O(810000) <= 10^6 不會超時
    - 如果可以disconnected, 返回1
    - 全部遍歷完都還是connected, 那就根據前面討論, 最多僅需要兩天, 直接返回2