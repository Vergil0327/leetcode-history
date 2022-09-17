package main

// T: (n-L)*L*logn
// M:(n-L)*logn
// https://www.youtube.com/watch?v=Tf_mD59DLf0
func longestRepeatedSubstring(s string) int {
	// longest length ranges from l to r
	l, r := 0, len(s)-1 // the longest substr should be n-1. ex. aaaaa -> answer is aaaa
	for l < r {
		mid := r - (r-l)/2

		/* if we found longest repeated substring, we keep looking for longest one */
		if findLRS(s, mid) {
			l = mid
		} else {
			r = mid - 1
		}
	}

	return l
}

// aaaaa, length: 3
// index: 0, 1, 2
// T:O((n-L)*L), L is length
func findLRS(s string, length int) bool {
	seen := map[string]int{}
	// T:O(n-L)
	for i := 0; i <= len(s)-length; i++ {
		substr := s[i : i+length] // T:O(L)
		seen[substr] += 1
		if seen[substr] > 1 {
			return true
		}
	}

	return false
}

// https://www.youtube.com/watch?v=FQ8hcOOzQMU
// T:O(n^2 * n)
func longestRepeatedSubstringBruteForce(s string) int {
	seen := map[string]int{}

	maxLen := 0
	for i := 0; i < len(s); i++ {
		for j := i; j < len(s); j++ {
			substr := s[i : j+1] // T:O(n)

			seen[substr] += 1
			if seen[substr] > 1 {
				maxLen = max(maxLen, len(substr))
			}
		}
	}

	return maxLen
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

/*
Example 1:
Input: "abcd"
Output: 0
Explanation: There is no repeating substring.

Example 2:
Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

Example 3:
Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.

Example 4:
Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
*/
