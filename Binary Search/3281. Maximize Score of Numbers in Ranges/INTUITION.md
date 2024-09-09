# Intuition

看到要求什麼min max, 先試想binary search

首先對start數列做排序, 我們取最左端點作為起點

再來就是用binary search去猜正確值, search range為[0, start[-1]+d - start[0]]

整體框架也很簡單, 就是用binary search猜max

```py
l, r = 0, start[-1]+d-start[0]
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```

一但寫成這形式, 問題就轉換為: 確認`mid`是否是個可行的score?
那解法也呼之欲出

起點為start[0], 再來我們往右遍歷看`start[0]+mid`是否超出下個區間範圍

- 如果start[0]+mid > start[i]+d: 那麼mid肯定不會是可行解, 實際score應該要更小
- 那如果start[0]+mid <= start[i]+d, 這時就看
  - 如果start[0]+mid >= start[i], 那麼下個起點位置就是start[0]+mid
  - 如果start[0]+mid < start[i], 那麼下個起點位置就是start[i]

反覆更新起點位置然後去做判斷, 如果全數通過那就代表當前score為可行解