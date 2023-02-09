# Intuition

可以看出 x 的存在範圍就在`[0, len(nums)]`
我們就逐個試即可，要找出 `>= x` 的位置那就是透過bisect.bisect_left找出lowerbound
然後判斷 (n-i) 有沒有等於 x 即可
如果沒有任何的x能被找出來，那就返回`-1`