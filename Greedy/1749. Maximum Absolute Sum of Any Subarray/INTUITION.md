# Intuition

絕對值後要最大, 有正有負肯定不會是極值, 所以我們要找的應該是
1. 正值裡的max
2. 負值裡的min

所以我們遍歷nums[i], 然後找出最positive跟最negative的subarray sum
再來我們用`x`紀錄**maxpositive max sum**, 用`y`紀錄**negative min sum**
其中, 在`+=nums[i]`後, 我們持續對:
- `x`取`max(0, x)`, 這是因為假設到目前為止的subarray是負數, 那麼也沒必要後面再繼續append nums[i]了, 不如另起爐灶作為新的subarray開頭
- 同理持續對`y`取`min(0, y)`, 如果目前為止的y是正值, 那不如另起爐灶作為新的subarray開頭, 這樣值會更小

而這其實就是找最大子數列, Kadane's algorithm

time: O(n)
space: O(1)