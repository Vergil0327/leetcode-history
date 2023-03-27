# Intuition

首先三角形的特性是兩邊和必大於第三邊，由於我們要找三個邊
因此我們可以遍歷其中一個邊，然後找另外兩個

由於要符合這個關係式: `nums[i] + nums[j] > nums[k]`
因此我們可以遍歷`k` 然後找`i`跟`j`

因此我們可以先**排序**，然後nums[k]由大到小遍歷from `n-1` to `2`
那根據上面的關係是，其實剩下的兩個邊就是`two sum larger than nums[k]`
我們可以用雙指針來找配對, 起始值為:`i, j = 0, k-1`

這樣當前第三邊為nums[k]時:
- 如果此時`nums[i]+nums[j] > nums[k]`, 代表當第二個邊為nums[j]時，有`j-i`個nums[i]邊可以跟nums[j]及nums[k]配對，然後再繼續往左移動`j`
- 反之我們則移動`i`往右, 找nums[i]的合法配對

就相當於我們遍歷第三個邊nums[k]後，一步一步往左移動右邊界nums[j], 然後看有多少個左邊界nums[i]可以配對

```
示意圖
X [X X X X X X X X X X X X X X] X X X X
                                 <- k
   i                      <- j

由於我們已經由小大到排序
所以當nums[i] + nums[j] > nums[k]時, 有`j-i`個nums[i]邊可以跟nums[j]及nums[k]配對
因為nums[i], nums[i+1], ..., nums[j-1] 加上 nums[j]後都會大於nums[k]
```

2,2,3,4
      k
i   j