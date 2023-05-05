# Intuition

我們每個bit位來看

```
1 1 1 0
      1
```

如果我的當前的nums[i]要跟之前的每個數**AND**為0的話
代表nums[i]必須不再之前出現的所有bit位當中出現

因此我們在滑動窗口的時候, 可以用`OR`來存下當前window出現的每個bit位
一但最新的一個`nums[r]&window != 0`的話, 代表我們要移動左指針來縮小窗口, 直到`nums[r]&window == 0`

那在滑動窗口的同時, 在每個合法的sliding window下都能更新全局最佳解:
`res = max(res, r-l)` (`[l,r)`, 左閉右開)