# Intuition

所有可以做的課一起做掉, 花費時間為`max(time[i] for i in range(n) if indeg[i] == 0)`
但如果有這狀況?

```
1 (inf month) -> 5
2 (1m) -> ... -> 5
3 (3m) -> 4 (4m) -> ... -> 5
```

花費時間其實就是**各個路徑的總花費時間取最大值**, 因為花更少時間的路徑都可以包涵在裡面任意做, 只會花費當前的current max time
所以我們用topological sort的概念找出當前的所有available course, 並配合`min heap = [time, node]`
再來我們就時間由小到大, 每個課程路徑持續做下去, 取globally maximum time即可

time: O(nlogn + mlogn) where n is number of courses and m is number of total edges