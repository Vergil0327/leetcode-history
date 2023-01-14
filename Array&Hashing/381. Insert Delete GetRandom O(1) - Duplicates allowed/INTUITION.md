# Intuition

為了達到三個操作都O(1)

首先`getRandom`可以想到的是，我們必須用list來儲存插入的數，這樣透過random.choice即可達到O(1)的操作

再來是`insert`，既然我們用list來儲存數值，要在list上達到的O(1)操作那就是將target value移到最後在pop掉
代表我們插入時還必須要儲存每個數在list的index，因此我們需要一個hashmap `val2idx`
這樣我們才能透過 swap & pop 達到O(1)的移除，並且可以透過`val2idx`以O(1)時間判斷要插入的target是否已經存在

再來比較複雜的就是`remove`
我們考慮兩種case:
1. 如果target已經在list的尾端，在list[n-1]位置，那麼就直接list.pop就好.
   但別忘記從`val2idx`中清除. 為了能夠以O(1)時間移除，這邊我們選用Hashset來儲存index，這樣移除就只要 `val2idx[target].remove(n-1)` 即可
   有個要特別注意的重點是，如果val2idx[target]為空的話，記得從hashmap中移除target這個key，這樣在insert時才不會誤判target還存在

2. 如果target不在n-1的位置，那我們就swap & pop

**這邊有個最重要的一點要知道的是，如何在python 如何在 hashset 裡任意取出一個value出來?**

```python
idx = next(iter(val2idx[target]))
```

一但知道idx之後，後面就簡單了
- 更新 list[n-1] 的 val2idx
  - val2idx[list[n-1]].add(idx)
  - val2idx[list[n-1]].remove(n-1)
- list[n-1]跟list[idx]互換
- list.pop() 移除target value
- 更新target value的val2idx
  - val2idx[target].remove(idx)
  - 一樣別忘記一但val2idx[target]為空的話，將target從val2idx中移除.
  - `if not val2idx[target]: del val2idx[target]`

# Complexity

- time complexity

$$O(1)$$

- space complexity

$$O(n)$$