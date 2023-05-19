# Intuition

凡事要找subarray, 先想說有沒有辦法固定一個邊界, 然後移動另一個邊界來高效找出答案
因為只要有兩個邊界`l`&`r`就可以描述一個subarray

所以對於一個`nums`來說
對於一個合法的sliding window來說
每次移動`r`, 只要window是合法的, 此時`l`有`r-l+1`種位置來形成合法subarray
代表固定當前的右邊界`r`能貢獻`r-l+1`個合法subarray
```
[X X X X] X X X X X
 l     r
   l   r
     l r
      l/r
```

我習慣用`[l:r)` 左閉右開的方式來看sliding window
所以就是對於每個右邊界`r`來說, 可貢獻`r-l`個合法subarray

```
[X X X] X X X X X X
 l      r
   l    r
     l  r
```