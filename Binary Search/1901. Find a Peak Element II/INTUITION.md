# Intuition

最基本想到的是 Brute force: O(m*n*4)

```py
m, n = len(mat), len(mat[0])

for i in range(m):
    for j in range(n):
        top = mat[i-1][j] if i-1 >= 0 else -1
        bot = mat[i+1][j] if i+1 < m else -1
        left = mat[i][j-1] if j-1 >= 0 else -1
        right = mat[i][j+1] if j+1 < n else -1

        if mat[i][j] > top and mat[i][j] > bot and mat[i][j] > left and mat[i][j] > right:
            return [i,j]
```

要進一步優化時間複雜度的話, 那只剩mlog(n) => 代表會需要用到binary search

但該如何在一個無序的數列裡應用binary search?
就像find peak element I 一樣, 本質是找出合理的方式去除掉search space

可以先這麼想, 假設只有一row的情況下, 該怎麼辦?

ex. [l, X, X, X, X, mid, X, X, X, X, r] where search space is [l, r]

我們猜測這個mid, 這時我們就看mid-1跟mid+1
如果`mid > mid-1 and mid > mid+1`, 那麼mid就是peak element

那如果不是的話呢?
就看哪邊大, 我們search space就往那邊靠
- if mid < mid-1: search space becomes [l, mid-1]
- if mid < mid+1: search space becomes [mid+1, r]

好那接下來如果有多個rows呢?

由於2-D peak還必須符合`mat[row][mid] > mat[row-1][mid] and mat[row+1][mid]`
所以對於當前binary search guess column: `mid`, 對於該column我們可以遍歷整個row找出最大值, 最大值必定是row方向的peak
之後再回到前面所述的部分去找出column方向的peak即可

如此一來, 整體時間複雜度便是`O(rows * log(columns))

```py
m, n = len(mat), len(mat[0])

def findMaxIndex(col):
    idx = mx = -1
    for i in range(m):
        if mat[i][col] > mx:
            mx = mat[i][col]
            idx = i
    return idx

l, r = 0, n-1
while l <= r:
    mid = l + (r-l)//2
    
    mxRowIdx = findMaxIndex(mid)
    left, right = mat[mxRowIdx][mid-1] if mid-1 >= 0 else -1, mat[mxRowIdx][mid+1] if mid+1 < n else -1

    if mat[mxRowIdx][mid] > left and mat[mxRowIdx][mid] > right:
        return [mxRowIdx, mid]
    elif mat[mxRowIdx][mid] < left:
        r = mid-1
    else:
        l = mid+1
return [-1, -1]
```

## Optimization

如果說還有沒有能更進一步優化的點的話, 那便是判斷`rows.size`, `columns.size`來決定要`rows*log(cols)`或是`cols * log(rows)`