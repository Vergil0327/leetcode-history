# Intuition

遍歷任兩個點darts[i], darts[j], 必能圈出2個圓使得這兩個點都在半徑為r的圓周上
這樣能將圓的面積最大效益化

這時問題就剩該如何判斷其他點也能落在圓裡?

(rx-darts[i][0])^2 + (ry-darts[i][1])^2 = r^2
(rx-darts[j][0])^2 + (ry-darts[j][1])^2 = r^2
=> 要求rx跟ry, 有兩個方程式, 照理說能解出兩個可能的圓心位置
ref> https://rosettacode.org/wiki/Circles_of_given_radius_through_two_points

=> 求出兩個圓心後, 再判斷其他點跟該圓心的距離有沒有小於等於r即可
=> 這邊注意個細節, 判斷兩個float大小時, 由於精度的關係, 建議用一個極小的數值(ex. 1e-6)來判斷
=> 如果圓心為(x0, y0)那麼判斷任意(x, y)與圓心的距離有沒有小於等於半徑r時, 應為:

```py
inCircle = (x-x0)**2 + (y-y0)**2 - r**2 <= 1e-6
if inCircle:
    # do your thing
```