# Intuition

[詳細解說在這](https://www.youtube.com/watch?v=W7MyjXDE5xg)

## Part I - spirally outward

首先當小於兩個點時絕不可能相交

再來當目前這個邊比前一個對邊還大時，會螺旋式往外，永不可能相交

```
if n < 2: return False

i = 2
while i < n and distance[i] > distance[i-2]:
    i += 1
if i == n: return False
```

## Part II - start to inward spirally

一但當前這個邊比前一個對邊小時，代表這個螺旋開始往內收縮，而且絕不可能再往外

這時要注意兩種情況：

當前縮小的這個邊，他的對邊的對邊會介於中間(如果存在的話)

第一種情況 (type I)：

這時如果當前這個邊**小於**對邊及其對邊的對邊的差，也就是`edge[i] < abs(edge[i-2]-edge[i-4])`的話

那就是只要符合edge[i] < edge[i-2]的話，便能持續往內螺旋
只要判斷能不能用完所有的邊即可

```
----------
|     ___|
|___
```


第二種情況 (type II)：

```
----------
|     ___|
|______
```

這時如果當前這個邊**大於等於**對邊及其對邊的對邊的差，也就是`edge[i] >= abs(edge[i-2]-edge[i-4])`的話，那下一個邊edge[i+1]必須小於`edge[i-1]-edge[i-3]`，否則會交錯

如果`edge[i+1] < edge[i-1]-edge[i-3]`的話(沒有交錯)，那接下來就會回到上面的第一種情況
照第一種的判斷方式判斷有無交錯即可

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(1)$$