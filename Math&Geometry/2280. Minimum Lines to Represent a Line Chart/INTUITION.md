# Intuition

這題本質上很簡單, 就是去比較斜率
但問題是在數學計算上, 斜率是個floating number, 遇到浮點數的相互比較就要特別注意
在精度上可能會導致計算出錯

所以理想上, 最好避免浮點數的比較

因此對於三個點, 兩條連線來說

points = [x1, y1], [x2, y2], [x3, y3]
slope1 = (y2-y1) / (x2-x1)
slope2 = (y3-y2) / (x3-x2)

如果 slope1 == slope2, 那麼就還會是同一條線
所以根據這條件: slope1 == slope2 -> (y2-y1) / (x2-x1) == (y3-y2) / (x3-x2)
但為了避免除法產生的浮點數, 所以我們調換一下式子可得出:

slope1 == slope2
-> (y2-y1) / (x2-x1) == (y3-y2) / (x3-x2)
-> (y2-y1) * (x3-x2)  == (y3-y2) * (x2-x1)

因此比起判斷浮點數, 我們直接判斷`(y2-y1) * (x3-x2)  == (y3-y2) * (x2-x1)`這個條件即可

因此我們能得知:

1. len(stockPrices) < 2: return 0
2. 否則的話, 我們至少有1條線, 然後我們在遍歷[1, n-2]然後看points[i-1], points[i], points[i+1]這三個點的連線是不是在同的斜率上, 如果不是那就`+= 1`

但別忘了重要的一點, stockPrices是沒有排序的
所以我們得先對stockPrices做排序, 在判斷各點的斜率

time: O(nlogn)
space: O(1)