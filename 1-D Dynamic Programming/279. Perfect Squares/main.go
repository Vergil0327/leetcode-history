package perfectsquares

func numSquares(n int) int {
	dp := make([]int, n+1)
	for i := 1; i < n+1; i++ {
		dp[i] = n
	}

	for total := 1; total <= n; total += 1 {
		for i := 1; i <= n; i++ {
			perf := i * i
			if perf > total {
				break
			}

			dp[total] = min(dp[total], dp[total-perf]+1)
		}
	}
	return dp[n]
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
