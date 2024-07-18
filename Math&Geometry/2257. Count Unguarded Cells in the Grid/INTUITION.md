# Intuition

m*n <= 10^5, 這代表我們產生一個m*n的grid去做標記是沒問題的

直覺來看, 我們可以遍歷每個guard然後沿著視線去在grid上做標記
- 一開始每個grid[i][j] = 1
- 由於視線會停於guards[i]或walls[j]上, 所以我們在grid上的每個gurds[i]跟walls[j]都標上特殊標記`-1`

再來我們來看一下, 如果我們遍歷guard的話, 然後再沿著四個方向的視線, 那麼時間複雜度會是如何?

由於m*n = 10^5, 所以我們計算`sqrt(10^5) = 316.22`
O(m+n) 上限為 `316.22 + 316.22`

所以time complexity: O(guards.length) * O(m + n) = 5*10^4 * O(316.22 + 316.22)
這時間複雜度約為10^7 (一般leetcode時間複雜度會落在10^6, 10^7算極限)

但由於實際上每個guards[i]都會佔用掉格子, 所以gaurds.size越大, 遮蔽視線越多
如果再加上walls[j]的存在的話, 那遮蔽視線的障礙就又更多了
所以實際上時間複雜度並不會高到10^7, 值得一試

最後結果:
- Runtime: 1733 ms Beats 100.00%
    - O(guards.size * (m+n))
- Memory: 45.24 MB Beats 32.80%
    - O(m * n)
