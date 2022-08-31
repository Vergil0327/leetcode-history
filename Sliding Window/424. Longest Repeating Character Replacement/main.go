// https://leetcode.com/problems/longest-repeating-character-replacement/
package main

import (
	"math"
)

/*
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
*/

// T:O(26n) M:O(n)
func characterReplacement(s string, k int) int {
	contain := map[byte]int{}
	longest := 0

	l := 0
	for r := range s {
		contain[s[r]] += 1

		windowSize := r - l + 1
		maxCount := getMaxCount(contain)
		if windowSize-maxCount <= k /* window is valid */ {
			longest = int(math.Max(float64(longest), float64(windowSize)))
			r += 1
		} else {
			contain[s[l]] -= 1
			l += 1
		}
	}

	return longest
}

// T:O(26), 26 English characters
func getMaxCount(contain map[byte]int) int {
	maxCount := 0
	for _, count := range contain {
		if count > maxCount {
			maxCount = count
		}
	}
	return maxCount
}

// optimization: T:O(n)
func characterReplacementBetter(s string, k int) int {
	contain := map[byte]int{}
	longest := 0

	l := 0
	maxCount := 0 // we maintain maximum count
	for r := range s {
		contain[s[r]] += 1
		maxCount = int(math.Max(float64(maxCount), float64(contain[s[r]])))

		windowSize := r - l + 1
		if windowSize-maxCount <= k /* window is valid */ {
			longest = int(math.Max(float64(longest), float64(windowSize)))
			r += 1
		} else {
			contain[s[l]] -= 1
			l += 1
		}
	}

	return longest
}
