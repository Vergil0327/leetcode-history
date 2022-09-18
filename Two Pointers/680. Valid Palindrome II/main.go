// https://leetcode.com/problems/valid-palindrome-ii/submissions/
package main

func validPalindromeConcise(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		if s[l] == s[r] {
			l, r = l+1, r-1
		} else {
			return isPalindrome(s, l+1, r) || isPalindrome(s, l, r-1)
		}
	}

	return true
}

func isPalindrome(s string, l, r int) bool {
	for l < r {
		if s[l] == s[r] {
			l, r = l+1, r-1
		} else {
			return false
		}
	}

	return true
}

// T:O(n)
func validPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		if s[l] != s[r] {
			break
		}

		l, r = l+1, r-1
	}

	l1, r1 := l+1, r
	nextRound := false
	for l1 < r1 {
		if s[l1] != s[r1] {
			nextRound = true
			break
		}

		l1, r1 = l1+1, r1-1
	}

	if nextRound {
		l2, r2 := l, r-1
		for l2 < r2 {
			if s[l2] != s[r2] {
				return false
			}

			l2, r2 = l2+1, r2-1
		}
	}

	return true
}
