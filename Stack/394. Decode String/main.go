package main

import (
	"strings"
	"unicode"
)

// two types
// k[k[k[]]]
// k[k[]k[]k[]]

// explanation: https://www.youtube.com/watch?v=qB0zZpBJlh8
func decodeString(s string) string {
	stack := []string{}
	for _, ch := range s {
		if ch != ']' {
			stack = append(stack, string(ch))
		} else {
			substr := ""
			for len(stack) > 0 && stack[len(stack)-1] != "[" {
				// pop character from stack
				str := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				substr = str + substr
			}
			stack = stack[:len(stack)-1] // pop '['

			n := 0
			multiply := 1
			// pop digit from stack
			for len(stack) > 0 && unicode.IsDigit([]rune(stack[len(stack)-1])[0]) {
				c := []rune(stack[len(stack)-1])[0]
				n += multiply * int(c-'0')
				multiply *= 10

				stack = stack[:len(stack)-1]
			}

			// decode string
			for n > 0 {
				stack = append(stack, substr)
				n -= 1
			}
		}
	}

	return strings.Join(stack, "")
}
