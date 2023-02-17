// https://leetcode.com/problems/longest-common-subsequence/
package main

import (
	"math"
)

/*
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

		abcde
	 a11111 Current LCS:a
	 c11222
	 e11223

	 [[0 0 0 0]
	 	[0 1 1 1]
		[0 1 1 1]
		[0 1 2 2]
		[0 1 2 2]
		[0 1 2 3]]
*/

/*
		"abcbcba"
		"abcba"
	 [[0 0 0 0 0 0]
	  [0 1 1 1 1 1]
	  [0 1 2 2 2 2]
	  [0 1 2 3 3 3]
	  [0 1 2 3 4 4]
	  [0 1 2 3 4 4]
	  [0 1 2 3 4 4]
	  [0 1 2 3 4 5]]
*/

// explanation: https://www.youtube.com/watch?v=Ua0GhsJSlWM
func longestCommonSubsequence(text1 string, text2 string) int {
	m, n := len(text1), len(text2)

	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			} else {
				dp[i][j] = int(math.Max(float64(dp[i][j-1]), float64(dp[i-1][j])))
			}
		}
	}

	return dp[m][n]
}

/*
Memory Optimized
JAVA: https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
Obviously, the above code in method 2 only needs information of previous and current columns of previous row to update current row.
So we just use a 1-row 1D array and 2 variables to save and update the matching results for chars in text1 and text2.

public int longestCommonSubsequence(String text1, String text2) {
			int m = text1.length(), n = text2.length();
			if (m < n) {
					return longestCommonSubsequence(text2, text1);
			}
			int[] dp = new int[n + 1];
			for (int i = 0; i < text1.length(); ++i) {
					for (int j = 0, prevRow = 0, prevRowPrevCol = 0; j < text2.length(); ++j) {
							prevRowPrevCol = prevRow;
							prevRow = dp[j + 1];
							dp[j + 1] = text1.charAt(i) == text2.charAt(j) ? prevRowPrevCol + 1 : Math.max(dp[j], prevRow);
					}
			}
			return dp[n];
	}
*/
