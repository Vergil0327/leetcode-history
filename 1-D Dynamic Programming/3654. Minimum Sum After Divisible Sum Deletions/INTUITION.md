# Intuition

盡可能刪除可被k整除的最大contiguous subarray sum

nums = {O O O O O O O O} {O O O O O O O O} X X X X X X
如果有連續contiguous subarray sum是能被k給整除
那麼一整段也會是能被k給整除, 所以其實我們一但找到可以被k整除的合法contiguous subarray, 我們可以立即移除掉

那麼對於當前的prefix_sum[i]來說, 餘數為prefix_sum[i]%k, 只要往前找到一段餘數同樣為prefix_sum[k]%k的contiguous subarray, 那麼這整段就會是能被k整除的subarray
prefix + hashmap的概念

所以我們這邊定義dp[r]: the minimum remaining sum when remainder is `r`

那這樣我們在遍歷nums, 計算prefix sum時, 也能同時更新:

- 當前prefix sum: presum
- 當前remainder: r = presum%k
- 那麼對於當前的dp[r]就能更新: dp[r] = min(dp[r], presum)
- 最後假設發現dp[r]小於presum, 那麼代表可以移除掉**current presum - previous same remainder presum (dp[r])**這段subarray. 那麼這時剩下的remaining sum就剛好會是dp[r]
    - 所以一但發現小於presum的dp[r], 我們就能更新running presum = min(presum, dp[remainder])

- 整個遍歷完後, 剩餘的running prefix sum `presum`就是最終答案