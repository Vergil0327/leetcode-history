// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
package main

import "bytes"

type Word struct {
	c   byte
	cnt int
}

// T:O(n)
func removeDuplicates(s string, k int) string {
	stack := []Word{}

	i := 0
	for i < len(s) {
		if len(stack) == 0 || stack[len(stack)-1].c != s[i] {
			stack = append(stack, Word{c: s[i], cnt: 1})
		} else {
			cnt := stack[len(stack)-1].cnt + 1
			stack = append(stack, Word{c: s[i], cnt: cnt})
		}

		if stack[len(stack)-1].cnt == k {
			n := k
			for len(stack) > 0 && n > 0 {
				stack = stack[:len(stack)-1]
				n -= 1
			}
		}

		i += 1
	}

	str := bytes.NewBufferString("")
	for _, w := range stack {
		str.WriteByte(w.c)
	}

	return str.String()
}
