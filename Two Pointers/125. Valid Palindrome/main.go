package main

import (
	"strings"
	"unicode"
)

func isPalindrome(s string) bool {
	str := ""
	for _, char := range s {
		if (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9') || (char >= 'A' && char <= 'Z') {
			str += strings.ToLower(string(char))
		}
	}

	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		if str[i] != str[j] {
			return false
		}
	}

	return true
}

func isPalindrome2ndTry(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		if !((s[l] >= '0' && s[l] <= '9') || (s[l] >= 'a' && s[l] <= 'z') || (s[l] >= 'A' && s[l] <= 'Z')) {
			l += 1
			continue
		}

		if !((s[r] >= '0' && s[r] <= '9') || (s[r] >= 'a' && s[r] <= 'z') || (s[r] >= 'A' && s[r] <= 'Z')) {
			r -= 1
			continue
		}

		if toLower(string(s[l])) != toLower(string(s[r])) {
			return false
		}

		l += 1
		r -= 1
	}

	return true
}

func toLower(s string) string {
	var b strings.Builder
	b.Grow(len(s))

	for i := 0; i < len(s); i++ {
		c := s[i]
		if c >= 'A' && c <= 'Z' {
			c = c - 'A' + 'a'
		}
		b.WriteByte(c)
	}

	return b.String()
}

func isPalindromeBetter(s string) bool {
	i, j := 0, len(s)-1

	for i < j {
		leftChar, rightChar := rune(s[i]), rune(s[j])
		if !unicode.IsLetter(leftChar) && !unicode.IsDigit(leftChar) {
			i += 1
		} else if !unicode.IsLetter(rightChar) && !unicode.IsDigit(rightChar) {
			j -= 1
		} else if strings.EqualFold(string(leftChar), string(rightChar)) {
			i += 1
			j -= 1
		} else {
			return false
		}
	}

	return true
}
