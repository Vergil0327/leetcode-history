// https://leetcode.com/problems/decode-ways/
package main

/*
11106:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
take: `2`        `22`
take: `2`,`26`   `6`
take: `6`

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
*/

// explanation: https://leetcode.com/problems/decode-ways/submissions/
func numDecodingsMemo(s string) int {
	memo := map[int]int{}

	var dfs func(i int) int
	dfs = func(i int) int {
		if _, ok := memo[i]; ok {
			return memo[i]
		}

		if i == len(s) {
			memo[i] = 1
			return 1
		}
		if s[i] == '0' {
			return 0
		}

		result := 0
		result += dfs(i + 1)
		if i+1 < len(s) {
			if s[i] == '1' {
				result += dfs(i + 2)
			} else if digit2 := s[i+1]; s[i] == '2' && (digit2 != '7' && digit2 != '8' && digit2 != '9') {
				result += dfs(i + 2)
			}
		}

		memo[i] = result
		return result
	}

	return dfs(0)
}

// TIMEOUT!!!!
func numDecodings(s string) int {
	var dfs func(i int) int
	dfs = func(i int) int {
		if i == len(s) {
			return 1
		}
		if s[i] == '0' {
			return 0
		}

		result := 0
		result += dfs(i + 1)
		if i+1 < len(s) {
			if s[i] == '1' {
				result += dfs(i + 2)
			} else if digit2 := s[i+1]; s[i] == '2' && (digit2 != '7' && digit2 != '8' && digit2 != '9') {
				result += dfs(i + 2)
			}
		}

		return result
	}

	return dfs(0)
}
