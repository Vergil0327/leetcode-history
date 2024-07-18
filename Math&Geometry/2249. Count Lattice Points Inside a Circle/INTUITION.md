# Intuition

其實就是brute force, 而這邊會需要知道點數學小知識

我們用來判斷該點(i, j) 在不在 circles[k]裡的方法是確認(i, j)到該circle中心的距離
有沒有**小於等於**半徑`r`

也就是要滿足: distance = sqrt(pow(i-circles[k][0], 2) + pow(j-circles[k][1], 2)) <= r
但由於sqrt會產生浮點數, 為了避免精度問題應當盡量避免
所以我們用`pow(i-circles[k][0], 2) + pow(j-circles[k][1], 2) <= r*r` 來判斷

那這邊有兩種做法:

1. 遍歷圓圈所佔用的矩形面積裡的所有點, 然後將距離`<= r`的點全加入到hashset裡(去除重複計算), 最終hashset.size就是答案
   - time: O(circles.size * r * r)
   - space: O(x * y)
2. 由於`1 <= xi, yi <= 100`且`1 <= ri <= min(xi, yi)`, 所以我們遍歷[0, 200]範圍內所有(i, j), 然後在遍歷circles[k]去確認有沒有存在於任何一個圓圈裡
   - time: O(x * y * circles.size)
   - space: O(1)
