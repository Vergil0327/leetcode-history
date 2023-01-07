// https://leetcode.com/problems/implement-strstr/
package main

// T: O(m*n) M:O(1)
func strStr(haystack string, needle string) int {
	if needle == "" {
		return 0
	}

	if len(needle) > len(haystack) {
		return -1
	}

	for i := 0; i < len(haystack); i++ {
		for j := 0; j < len(needle); j++ {
			if i+j >= len(haystack) {
				break
			}

			if haystack[i+j] != needle[j] {
				break
			}

			if j == len(needle)-1 {
				return i
			}
		}
	}

	return -1
}

// KMP algorithm T: O(m+n) M: O(m)
// explanation: https://www.youtube.com/watch?v=JoF0Z7nVSrA&t=1121s
func strStrBETTER(haystack string, needle string) int {
	if needle == "" {
		return 0
	}

	// longest prefix suffix
	lps := make([]int, len(needle))
	lps[0] = 0 // whole string can't be suffix or prefix

	// LPS generation T:O(m)
	// prevLPS: ptr to LPS
	// i: ptr to i-th str of needle
	// think if needle == AAACAAA
	prevLPS, i := 0, 1
	for i < len(needle) {
		if needle[i] == needle[prevLPS] {
			lps[i] = prevLPS + 1
			prevLPS += 1
			i += 1
		} else {
			if prevLPS == 0 /* think case AB */ {
				lps[i] = 0
				i += 1
			} else {
				prevLPS = lps[prevLPS-1]
			}
		}
	}

	// KMP
	// T: O(n)
	i = 0  // ptr to haystack
	j := 0 // ptr to needle
	for i < len(haystack) {
		if haystack[i] == needle[j] {
			i, j = i+1, j+1
		} else {
			if j == 0 /* haystack[i] can't match with any letter in needle */ {
				i += 1
			} else {
				j = lps[j-1] // compare haystack[i] with previous LPS value
			}
		}
		if j == len(needle) /* we find match string */ {
			return i - len(needle)
		}
	}
	return -1
}
