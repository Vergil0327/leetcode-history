# Intuition

```
next_greater[l] = r

X X X X X X X X X X
l     r     r2
```

對於`l`來說, valid point只有`r`
假設還有個r2 > l, 但這樣對[l, r2]來說, 必定存在一個`r`使得`r > l`, 如此一來[l, r2]並不符合bowl的條件
因此我們只要建立nextGreater[i] by monotonic stack, 並確認長度是否符合至少3個, 即可計算出有多少個valid bowl

並別忘了, 當前情況是**左端點 < 右端點** (nums[l] < nums[r])

還得考慮**左端點 > 右端點**的情況, 所以還得需要一個prevGreater去計算, 對於`r`來說, 是否存在個合法`l` (nums[l] > nums[r])

