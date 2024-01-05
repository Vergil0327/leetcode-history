# Intuition 2

也有另一種想法是:
我們用binary search去猜測可能可以等待的`x`時間

因為如果我們能在等待`x`天後抵達, 那我們只等待`x-1`天肯定也可以抵達
所以這樣的單調性質讓我們可以用binary search去猜這個等待時間`x`

那在check這個`x`可不可行時
我們就先讓火進行BFS去蔓延`x`步, 之後我們再同步讓火跟人進行BFS (這邊注意要讓火先BFS, 這樣人在走才會是safe place)
如果人可以抵達那就是個可行解, 繼續用binary search找出`x`的上界

由於可能沒有解, 所以最後必須在確認一次, 無解則返回`-1`

```py
l, r = 0, m*n
while l < r:
    mid = (l + r + 1) // 2
    if check(mid):
        l = mid
    else:
        r = mid - 1

return l if check(l) else -1
```