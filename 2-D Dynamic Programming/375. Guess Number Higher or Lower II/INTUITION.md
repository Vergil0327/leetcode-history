# Top-Down

## Intuition

這題要求的是，在能確保正確答案的情況下，最少需要花多少point
首先第一個example就告訴我們，二分猜法不會是最佳解
既然不知道從何下手，那我們就每個答案都猜過一遍

這時想想我們的top-down decision tree會是如何

對於1到n的數中，每次從中猜一個數`i`後，我們會知道**higher**或**lower**，也就是[1,n]這區間會分成[1,i-1]和[i+1,n]後然後再繼續猜

由於我們是要找出最少的花費使得正確答案能夠確保，也就是在花費最小的情況下猜完Worst Case
因此我們要對每個決策取`max`，找出猜任意數所能得到的worst case
然後再對所有worst case的花費取`min`，找出最少需花費多少才能猜完worst case

因此這時遞歸方程就出現了:

```
cost = inf
i from 1 to n:
    cost = min(cost, max(DFS(1,i-1),DFS(i+1,n)) + i)

DFS(1, n) = cost
```
