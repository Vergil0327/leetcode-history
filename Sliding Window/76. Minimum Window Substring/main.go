// https://leetcode.com/problems/minimum-window-substring/

package main

import "math"

/*
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
*/

// explanation: https://www.youtube.com/watch?v=jSto0O4AJbM
// T:O(n)
func minWindow(s string, t string) string {
	if len(s) < len(t) || s == "" {
		return ""
	}

	countT, window := map[rune]int{}, map[rune]int{}
	for _, c := range t {
		countT[c] += 1
	}

	// ! WRONG ! we need len(countT) to get unique string
	// have, need := 0, len(t)
	have, need := 0, len(countT)
	candidate, candidateLen := [2]int{}, math.MaxInt
	l := 0
	for r, c := range s {
		window[c] += 1

		if _, ok := countT[c]; ok && window[c] == countT[c] {
			have += 1
		}

		for have == need {
			// update result
			if currLen := r - l + 1; currLen < candidateLen {
				candidate[0] = l
				candidate[1] = r
				candidateLen = currLen
			}

			// pop from left of our window
			window[rune(s[l])] -= 1
			if _, ok := countT[rune(s[l])]; ok &&
				/* it's fine if we have more than countC. only minus 1 from have when what we have is less than target */
				window[rune(s[l])] < countT[rune(s[l])] {
				have -= 1
			}
			l += 1
		}
	}

	if candidateLen == math.MaxInt {
		return ""
	}
	return s[candidate[0] : candidate[1]+1]
}
