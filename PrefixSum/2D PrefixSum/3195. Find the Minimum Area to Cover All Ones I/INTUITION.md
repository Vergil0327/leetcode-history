# Intuition

直覺想到先求出2D-prefix sum
再來我們就分別對兩個方向(width & height)遍歷找起始與終點

- 起點: 第一個 row or column使得2D prefix sum不為0
- 終點: 第一個 row or column使得2D prefix sum為整個grid的和

知道起始跟終點後, **終點-起點+1 = width or height**, width, height兩者相乘即為答案