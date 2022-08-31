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
