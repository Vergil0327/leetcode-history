
# Intuition

既然是要挑一段subsequence, 那麼順序就不再重要
首先我們可以把所有even number跟odd number區分開來並且由大到小排序

想法:

```
even = X X X X X X X X
 odd = Y Y Y Y Y Y Y Y
```

如果一開始我們even取0個, 那odd就要取k個
even取1個, 那odd就要取k-1個

所以我們遍歷even
當even由大到小取前1到k個, 剩下用odd來替代, 如此一來只要總數可以湊成k個, 並且sum為偶數的話
那便是合法的挑選, 我們從中挑最大的即可