package main

// Given an integer n
// return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
func countBits(n int) []int {
	ans := make([]int, n+1)
	for i := 0; i < n+1; i++ {
		count := countOne(i)
		ans = append(ans, count)
	}

	return ans
}

func countOne(num int) int {
	total := 0
	for num > 0 {
		num &= num - 1
		total += 1
	}
	return total
}

// 0 0000 -> 0
// 1 0001 -> 1 = 1 + dp[0] = 1 + dp[n-1]
// 2 0010 -> 1 = 1 + dp[0] = 1 + dp[n-2]
// 3 0011 -> 2 = 1 + dp[1] = 1 + dp[n-2]
// 4 0100 -> 1 = 1 + dp[0] = 1 + dp[n-4]
// 5 0101 -> 2 = 1 + dp[1] = 1 + dp[n-4]
// 6 0110 -> 2 = 1 + dp[2] = 1 + dp[n-4]
// 7 0111 -> 3 = 1 + dp[3] = 1 + dp[n-4]
// 8 1000 -> 4 = 1 + dp[0] = 1 + dp[n-8]
// ... dp[i] = 1 + dp[i-offset], offset == most significant bit, [1, 2, 4, 8, ..., 2^n] ps. Most Siginificant Bit (MSB) = The leftmost non-zero digit
// 末兩位每四組一個循環 00 -> 01 -> 10 -> 11, 可以用前面已知的答案來做計算
// explanation: https://www.youtube.com/watch?v=RyBM56RIWrM
func countDynamicProgamming(n int) []int {
	dp := make([]int, n+1)

	offset := 1
	for i := 1; i < n+1; i++ {
		if i == offset*2 {
			offset = 2
		}
		dp[i] = dp[i-offset] + 1
	}

	return dp
}

// if i is even, dp[i] = numOfOne(i/2)
// if i is odd, least siginificant bit (LSB) will always be set, dp[i] = numOfOne(i/2 >> 1) + 1 (LSB we removed)
// https://leetcode.com/problems/counting-bits/discuss/1808016/C%2B%2B-oror-Vectors-Only-oror-Easy-To-Understand-oror-Full-Explanation
func countDynamicProgammingBetter(n int) []int {
	dp := make([]int, n+1)

	for i := 1; i < n+1; i++ {
		dp[i] = dp[i/2] + i%2
	}

	return dp
}
