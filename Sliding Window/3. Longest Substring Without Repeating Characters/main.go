// https://leetcode.com/problems/longest-substring-without-repeating-characters/
package main

import "math"

// Given a string s,
// find the length of the longest substring without repeating characters.
//
// Example 1:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
//
// Example 2:
// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
//
// Example 3:
// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// T:O(n) M:O(n)
func lengthOfLongestSubstring(s string) int {
	mUsed := map[byte]bool{}
	maxL := 0
	l, r := 0, 0

	for r < len(s) {
		if _, ok := mUsed[s[r]]; ok {
			delete(mUsed, s[l])
			l += 1
			continue
		}
		mUsed[s[r]] = true

		length := r - l + 1
		maxL = int(math.Max(float64(length), float64(maxL)))

		r += 1
	}

	return maxL
}

func lengthOfLongestSubstring2ndTry(s string) int {
	longest := 0
	set := map[byte]bool{}
	l := 0
	for r := range s {
		c := s[r]

		if existed, ok := set[c]; ok && existed {
			for l < r && set[c] {
				set[s[l]] = false
				l += 1
			}
		}

		set[c] = true

		longest = max(longest, r-l+1)
	}

	return longest
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
