# Intuition

我們可以很直覺地想出:
push/pop: O(1)
increment: O(k)
的解法

但其實這題能實作出全O(1), 關鍵點在於:
我們用**list + pointer**去紀錄當前push的位置

```py
self.stk = [0] * maxSize
self.i = 0
```

並且再額外用個array `self.add`紀錄bottom i elements的增益量:

```
self.add[i] = increment for self.stk[:i]
            = self.stk[j] + self.add[j] for j in range(i)

self.add = [0] * maxSize # self.add[i]: increment for self.stack[:self.i]
```

那這樣我們`def increment(self, k: int, val: int) -> None`只需要

```py
def increment(self, k: int, val: int) -> None:
    i = min(self.i, k)
    if i >= 0:
        self.add[i] += val
```

並且在pop的時候只要相當前self.stk[self.i-1] + self.add[self.i-1]即為返回答案
但別忘了pop後我們的`self.i -= 1`, 同時也要維護`self.add[i-1] += self[self.i]`

```py
def pop(self) -> int:
    if self.i <= 0: return -1

    self.i -= 1
    ans = self.stk[self.i] + self.add[self.i]
    if self.i > 0:
        self.add[self.i - 1] += self.add[self.i]
    self.add[self.i] = 0
    return ans
```