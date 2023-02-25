package leetcode_978

func maxTurbulenceSize(arr []int) int {
	n := len(arr)

	dp := [][2]int{}
	for i := 0; i <= n; i++ {
		dp = append(dp, [2]int{1, 1})
	}

	arr = append(arr, arr[n-1])

	for i := n - 1; i >= 0; i-- {
		if i%2 == 0 {
			if arr[i] < arr[i+1] {
				dp[i][0] = dp[i+1][0] + 1
			} else if arr[i] > arr[i+1] {
				dp[i][1] = dp[i+1][1] + 1
			}
		} else {
			if arr[i] > arr[i+1] {
				dp[i][0] = dp[i+1][0] + 1
			} else if arr[i] < arr[i+1] {
				dp[i][1] = dp[i+1][1] + 1
			}
		}
	}

	res := 0
	for i := 0; i <= n; i++ {
		res = max(res, max(dp[i][0], dp[i][1]))
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
