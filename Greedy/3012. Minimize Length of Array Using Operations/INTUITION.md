# Intuition

一旦餘數為0就不能再挑
找最大跟比他小的數取餘數, 會持續移除掉較大的數而留下較小的那個
所以greedy來想, 就是持續找最大跟比他小的數, 最終只會剩最小的那個數
而自身對自身取餘數, 產生的0為自身數目的一半:

總體思想: we can always remove bigger elements, leave smallest. find least number of the smallest

所以我們先對nums進行排序:
```py
nums.sort()
```

盡可能兩兩消除後最後剩下的就是nums[0]
而最後再自身對自身取餘數為0, 0的個數為總個數的一半: ceil(cnt/2)

但如果nums[1:]之中任何一個數對nums[0]取餘數如果不為0的話, 那麼產生的餘數必定小於nums[0]
這時我們可以用這`一個`產生的餘數對其他所有的數進行操作後, 如同前面所說留下的會是最小的那個數, 所以最終長度會是最佳解1
所以一但nums[1:]之中任何一個數對nums[0]取餘數後不為零, 我們就直接返回1即可
不然就是原本的ceil(nums[0]的個數 / 2)