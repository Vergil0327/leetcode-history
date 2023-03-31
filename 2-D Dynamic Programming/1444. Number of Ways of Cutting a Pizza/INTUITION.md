# Intuition

這題要求的是有多少方法可以在切`k-1`刀分成k份後，每份都有蘋果
每次我們可以橫切或縱切，每次切完，剩下的Pizza也可以橫切或縱切，因此我們可以看到這是個遞歸形式的子問題，因此總共的方法數為:

total methods = 橫切 + 縱切
              = current row (has apple) * bottom piza + current col (has apple) * right pizza

定義 `DFS(row, col, k(刀))` 且因為是從上橫切，或從左縱切，所以我們的decision tree DFS從`(row, col)=(0, 0)`且有`k-1`刀可以切開始

每個決定就是橫切或縱切，總方法數就是全部加起來

```
methds = hasApple(current piaza with top slice) * DFS(bottom pizza, k-1) + hasApple(current pizza with left slice) * DFS(right pizza, k-1)
```

如果當前這份有蘋果，`hasApple()`則返回1，沒有則返回0
(或者也可以先用`hasApple()`判斷，有蘋果再遞歸)

**如何高速判斷有沒有蘋果? 如何實作hasApple?**

這題還有個最關鍵的是，我們必須要能快速知道當前切法有沒有蘋果

由於這題可以橫切或縱切，因此透過prefix sum row by row或column by column都沒能很有效解決

最好的方式是`leetcode 304`的方式： **prefix square sum**
再透過容斥原理(排容原理)可以很快求出當前matrix的prefix sum

# Complexity

- time complexity
$$O(ROWS * COLS * K)$$

- space complexity
$$O(ROWS * COLS)$$

# Intuition
first, it's really straightforward that we can simulate process by DFS.
then, we can observe that we need a method to check if we can cut or not.
that is, we need a method to check if there exists any apple or not in current cut.

since it's a 2-D array, we can use prefix sum 2D to get total apples in $O(1)$ and check if we can cut or not easily

# Complexity
- Time complexity:
$$O((m+n)*mnk)$$
time complexity of subproblem * (# of states) with cache

- Space complexity:
$$O(mnk)$$

# Code
```
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        presum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] + (1 if pizza[i-1][j-1] == "A" else 0) - presum[i-1][j-1]
        def hasApple(r1, c1, r2, c2):
            return presum[r2+1][c2+1] - presum[r2+1][c1] - presum[r1][c2+1] + presum[r1][c1]

        @lru_cache(None)
        def dfs(k, i, j):
            if k == 0:
                return 1 if hasApple(i, j, m-1, n-1) else 0
            if i >= m or j >= n: return 0

            res = 0
            for ii in range(i, m-1):
                if hasApple(i, j, ii, n-1):
                    res += dfs(k-1, ii+1, j)
            for jj in range(j, n-1):
                if hasApple(i, j, m-1, jj):
                    res += dfs(k-1, i, jj+1)

            return res % 1_000_000_007
        return dfs(k-1, 0, 0)
```