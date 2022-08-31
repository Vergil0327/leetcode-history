// https://leetcode.com/problems/removing-stars-from-a-string/
package main

import "strings"

// T:O(n) M:O(n)
func removeStars(s string) string {
	stack := []string{}
	for _, c := range s {
		if len(stack) > 0 && c == '*' {
			stack = stack[:len(stack)-1]
			continue
		}
		stack = append(stack, string(c))
	}

	return strings.Join(stack, "")
}
