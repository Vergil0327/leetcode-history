# Intuition

可以聯想到這麼定義:
**dp[n]: minimum # of perfect squares which sum to n by using perfect_square[:i]**

如果當前想要加總到dp[i], 那就遍歷所有可能perfect square `j`, 得到:
`dp[i] = min(dp[i], dp[i-j] + 1)`

由於目標是n, 所以最大的perfect square只到`int(sqrt(n))`

最終時間複雜度就是: O(n*sqrt(n))