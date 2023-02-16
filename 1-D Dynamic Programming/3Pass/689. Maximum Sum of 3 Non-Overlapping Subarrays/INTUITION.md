# Intuition

最主要的想法是遍歷中間的subarray sum，然後找出左側存在的最大subarray以及存在於右側的最大subarray

1. 我們可以透過兩次遍歷找出左側在每個`i`位置的最大subarray sum以及右側在`i`位置的最大subarray sum
   - 分別是leftMax以及rightMax
   - 並同時紀錄該最大subarray的起始座標位置於leftIdx及rightIdx
2. 然後在合法區間遍歷中間subarray sum即可

由於左右兩側至少得有`k`個，中間subarray也至少是`k`個，所以遍歷的合法區間為:

```py
MAX = 0
for i in range(k, n-2*k+1): # i+2*k <= n
    currMax = leftMax[i-1] + (presum[i+k]-presum[i]) + rightMax[i+k]
    if currMax > MAX:
        MAX = currMax
        res = [leftIdx[i-1], i, rightIdx[i+k]]
return res
```