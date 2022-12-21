# Intuition

首先將所有區間先由`startTime`小到大排序，再將`endTime`由大到小排序

這樣一來在我們遍歷的過程中，由第一個與前一個互不相交的區間作為代表(計數+1)
後續區間當它`startTime`小於等於區間重疊中最小的`endTime`時，代表他們相互重疊，我們可以一起射爆

我們射的位置，會是區間重疊部分最小的`endTime`位置，因此我們持續更新遍歷過程中的`endTime`，

ex.

..............
........
   .........
      ..............
       ^  ........
       |     ............
    shot here to make first 4 balloons burst

# Complexity

- time complexity:

$$O(nlogn)$$

- space complexity

$$O(1)$$

# Further Concise Version

但其實不用那麼複雜的排序
我們只需要以`endTime`由小到大排序後，找出互不重疊的區間即可
只要有重疊，亦即`current startTime <= previous endTime`，都可以一起射爆，因此我們只要遍歷過程中維護重疊區間的`endTime`，並計數不重疊的區間即可

基本上就是Leetcode[435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)的變形