# Intuition

看到min(max)或max(min), 先想一下能不能用binary search
如果我們要用binary search的話, 會需要一個check function來檢查能不能在不超過maxOperations次內條件下滿足`max(nums) <= mid`

但首先得知道, 如果每個operation能分成兩堆, 那該怎麼分?

```
9 => 4,5 => 4,2,3
9 => 3,6 => 3,3,3
```
從example1可知, 如果直接對半分的話, 只分一次比較好
但分兩次就吃虧了
但實際上比起怎麼分, 我們應該更關注在能不能分出一個滿足`max(nums) <= mid`的合法解就好

所以如果我們對nums排序並挑出所有nums[i] > mid的數, 目標是讓這些數 <= mid
這邊應該思考有沒有什麼greedy的方式能找出合法解來

我們可以試著將nums[i]分成 mid, mid, mid, ... => nums[i] = k*mid + nums[i]%mid

ex. 如果binary search => mid = 3
nums[i] = 2 => operation = 0
nums[i] = 3 => operation = 0
nums[i] = 4 => [3,1] => operation = 1
nums[i] = 5 => [3,2] => operation = 1
nums[i] = 6 => [3,3] => operation = 1
nums[i] = 7 => [3,3,1] => operation = 2
所以operations = nums[i]//mid if nums[i]%mid!=0 else nums[i]//mid-1
              = (nums[i]-1)//mid