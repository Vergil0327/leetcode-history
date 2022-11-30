### Union-Find

我們可以先把nums加入到hashset
然後遍歷的同時找每個值的`num-1`和`num+1`
如果存在，那就`union(num, num-1)`
最後再從`rank`陣列(數組)裡找出最大值即可

注意corner case:
- 找parent的時候可能存在key error (parent尚未加入到hashmap裡)
- `max()`不可接受empty list, 使用`max([], default=0)`或`max([] or [0])`