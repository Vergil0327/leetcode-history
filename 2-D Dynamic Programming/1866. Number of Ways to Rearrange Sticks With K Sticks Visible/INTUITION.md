# Intuition

我們從後往前擺放, 這樣的話在計算會有好處:

ex. n=3, k=2

1. 先放1: 那再來不管(2, 3)順序怎放, 2,3都會遮住1 => 下一輪目標還是要在n=2狀態下創造出k=2的排序
2. 先放2: 那再來不管(1, 3)順序怎放, 3都會遮住1 => 一樣sub-problem變為n=2, k=2
3. 先放3: 那再來不管(1, 2)順序怎放, 3都不會被遮住 => 最大的數一定不會被遮住, 所以當前sub-problem變成要處理n=2, k=1

那我們的base case是啥?
1. 當n=k時, n個數要有k個被看到, 那就只有**一種**排序方式, 就是由小到大排列. 所以`return 1 if n==k`
2. 那在不滿足第一個條件下, 當k=0或n=0時, 直接`return 0`即可, 因為k=0時肯定至少有一個會被看到, 而n=0時沒辦法排出看到`k`個的排序, 所以合法方法數為0

所以我們可以用這個回歸式表示:
只有n個數中**最大的數**會是self.rearrangeSticks(n-1, k-1)的狀態轉移
剩餘**n-1**個數都是self.rearrangeSticks(n-1, k)的狀態轉移

```py
self.rearrangeSticks(n, k) =  self.rearrangeSticks(n-1, k-1) + self.rearrangeSticks(n-1, k) * (n-1)
```