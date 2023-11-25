# Intuition

**1-indexed**下, 我們從`index=i`開始
花了prices[i]後, 接下來的`i`個都可以免費取得
但這後`i`個之中, 我們也可以選擇不免費取得
若是我們選擇花費買下`j`其中`i < j <= i+i`, 相當於再繼續讓後`j`之後的`j+j`個可以免費取得

所以很明顯有兩個狀態, 我們紀錄我們當前的位置`i`以及我們目前最遠可以取到的位置`freeMostFarAt`

定義dfs(i, freeMostFarAt): the minimum prices to get until `freeMostFarAt` position

那狀態轉移也很明顯了:

1. if i <= freeMostFarAt: 那麼我們可買可不買
   - 不買那就是`dfs(i+1, freeMostFarAt)`
   - 花費`prices[i]`買下後, 那就接下來i+i個都可以免費取得, 所以是: `dfs(i+1, max(freeMostFarAt, i+i)) + prices[i]`
   - 兩種決策取最佳, `res = min(dfs(i+1, freeMostFarAt), dfs(i+1, max(freeMostFarAt, i+i)) + prices[i])`
2. if i > freMostFarAt: 那們第`i`個肯定得花錢買下, `res = dfs(i+1, max(freeMostFarAt, i+i)) + prices[i]`

**base case**

當我們全部拿完`i>n`或是我們已經可以免費取完n個`freeMostFarAt > n`

`if i > n or freeMostFarAt > n: return 0`