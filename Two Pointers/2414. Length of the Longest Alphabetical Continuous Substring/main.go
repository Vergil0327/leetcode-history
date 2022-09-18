// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
package main

// Two Pointers
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/discuss/2590079/Two-Pointers
// T:O(n)
func longestContinuousSubstring(s string) int {
	length := 1

	l := 0
	for r := 0; r < len(s); r++ {
		// alphabet order
		if int(s[l]-'a')+(r-l) != int(s[r]-'a') {
			l = r
		} else {
			length = max(length, r-l+1)
		}
	}

	return length
}

// monotonically increasing stack
// T:O(2n)
func longestContinuousSubstringMonoStack(s string) int {
	if len(s) == 1 {
		return 1
	}

	length := 1
	res := []byte{}
	i := 0
	for i < len(s) {
		c := s[i]

		for len(res) > 0 && int(c)-int(res[len(res)-1]) != 1 {
			res = res[:len(res)-1]
		}

		res = append(res, c)
		length = max(length, len(res))
		i += 1
	}

	return length
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
