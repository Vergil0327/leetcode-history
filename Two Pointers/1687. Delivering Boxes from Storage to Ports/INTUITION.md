# Intuition

透過example比較容易觀察到的是
1. ship boxes as many as possible
2. if boxes[i][0] is same with boxes[i+1][0], we can try to group them together to next trip

[X] X X X X X
 i
[X X] X X X X
 i
[X X X] X X X
 i
[X X Y] Y Y X
 i
[X X] [Y Y Y] X
 i

除了第二種狀況以外，第一種都是適用的
這代表這個裝箱問題就是在這兩種決策裡抉擇

因此定義dp[i]: the minimum number of trips for first i boxes

- 首先第一種方式的狀態轉移:

X [X X X] X X X
   i   j  j+1

我們[i:j]區間只要符合maxBoxes跟maxWeight, 就盡可能裝箱
`dp[j] = dp[i-1] + trips[i:j] + 1 # +1 for return to port`

- 再來是第二種狀態轉移, 不裝到最滿，如果j可以跟後面併再一起，那我們就試著把第j個箱子留到下一趟

X [{X X}  Y]  Y   Y  X
   i  j'  j  j+1 j+2

所以狀態轉移為:
`dp[j'] = dp[i-1] + trips[i:j'] + 1, 其中trips[i:j'] 為 `(trips[i:j] + 1) - 1``

所以如果前一種方法已經計算好`trips[i:j] + 1`的話，再減一就是我們要的trips次數
但其實原因也是因為，由於我們是把第j個箱子讓到下一趟，所以我們就少跑那一趟

然後如果我們在前面第一種方法就記錄第一個與j相同的箱子的位置的話，我們就能以O(1)的時間找出`j'`的位置
不然我們再往前遍歷的話，就會是O(N^2)的時間複雜度
所以可以透過個`prevJ`變數來儲存這個資訊


由於每次裝箱都是一個區間，所以這其實會是個Two Pointers
然後最後答案就是考慮n個箱子: `dp[n]`