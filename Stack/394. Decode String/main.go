package main

import (
	"strings"
)

func decodeString(s string) string {
	var stack []string
	var numStack []int
	var currStr strings.Builder
	n := 0

	for i := 0; i < len(s); i++ {
		ch := s[i]

		if ch >= '0' && ch <= '9' {
			// Build multi-digit number efficiently
			n = n*10 + int(ch-'0')
		} else if ch == '[' {
			// Push current state to stacks
			stack = append(stack, currStr.String())
			numStack = append(numStack, n)
			currStr.Reset()
			n = 0
		} else if ch == ']' {
			// Pop and decode
			prevStr := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			repeatCount := numStack[len(numStack)-1]
			numStack = numStack[:len(numStack)-1]

			// Use strings.Repeat for efficiency
			repeated := strings.Repeat(currStr.String(), repeatCount)
			currStr.Reset()
			currStr.WriteString(prevStr)
			currStr.WriteString(repeated)
		} else {
			// Regular character
			currStr.WriteByte(ch)
		}
	}

	return currStr.String()
}
