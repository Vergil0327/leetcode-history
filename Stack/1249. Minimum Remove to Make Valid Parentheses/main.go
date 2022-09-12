// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

package main

import "strings"

func minRemoveToMakeValidConcise(s string) string {
	stack := []string{}
	openIdx := []int{}
	const plcaeholder string = "*"
	for i, c := range s {
		if c >= 'a' && c <= 'z' {
			stack = append(stack, string(c))
		} else if c == '(' {
			stack = append(stack, string(c))
			openIdx = append(openIdx, i)
		} else /* c == ')' */ {
			if len(openIdx) > 0 {
				openIdx = openIdx[:len(openIdx)-1]
				stack = append(stack, string(c))
			} else {
				stack = append(stack, plcaeholder)
			}
		}
	}

	for i := len(stack) - 1; i >= 0; i-- {
		if stack[i] == plcaeholder {
			stack[i] = ""
		} else if len(openIdx) > 0 && i == openIdx[len(openIdx)-1] {
			stack[i] = ""
			openIdx = openIdx[:len(openIdx)-1]
		}
	}

	return strings.Join(stack, "")
}

func minRemoveToMakeValid(s string) string {
	stack := []string{}

	openParen := 0
	for _, c := range s {
		if c >= 'a' && c <= 'z' {
			stack = append(stack, string(c))
		} else {
			if c == '(' {
				stack = append(stack, string(c))
				openParen += 1
			} else if c == ')' {
				if openParen > 0 {
					openParen -= 1
					stack = append(stack, string(c))
				}
			}
		}
	}

	tmp := []string{}
	for openParen > 0 {
		if str := stack[len(stack)-1]; str == "(" {
			openParen -= 1
		} else {
			tmp = append(tmp, stack[len(stack)-1])
		}
		stack = stack[:len(stack)-1]

		if openParen == 0 {
			for len(tmp) > 0 {
				stack = append(stack, tmp[len(tmp)-1])
				tmp = tmp[:len(tmp)-1]
			}
		}
	}

	return strings.Join(stack, "")
}
