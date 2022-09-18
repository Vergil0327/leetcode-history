// https://leetcode.com/problems/longest-palindrome/
package main

func longestPalindromeConcise(s string) int {
	m := map[byte]int{}
	for i := 0; i < len(s); i++ {
		m[s[i]] += 1
	}

	length := 0
	for _, v := range m {
		length += (v / 2) * 2 // round down

		// length&1==0 check: we haven't plus unique character
		if length&1 == 0 && v&1 == 1 {
			length += 1
		}
	}

	return length
}

func longestPalindrome(s string) int {
	m := map[byte]int{}
	for i := 0; i < len(s); i++ {
		m[s[i]] += 1
	}

	hasSingleCharacter := false
	length := 0
	for _, v := range m {
		if v%2 == 1 {
			hasSingleCharacter = true
		}
		length += (v / 2) * 2 // round down
	}

	if hasSingleCharacter {
		return length + 1
	}
	return length
}
