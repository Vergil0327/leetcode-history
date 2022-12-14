# Stack

## Intuition

用`stack`儲存左括號，`res`紀錄插入數，每當有右括號便Pop Out From Stack
如果左括號不夠，代表我們需要插入1個`"("`，因此`res+1`

最後的插入數為`res+剩餘的左括號數目` = `res + len(stack)`

## Complexity

- Time Complexity

$$O(n)$$

- Space Complexity

$$O(n)$$