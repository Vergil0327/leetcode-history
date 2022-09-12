// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
package main

import "bytes"

/*
Two Pointers Solution
	ref: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392933/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
	explanation: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/294893/JavaC++Python-Two-Pointers-and-Stack
	Java:
   public String removeDuplicates(String s, int k) {
       int i = 0, n = s.length(), count[] = new int[n];
       char[] stack = s.toCharArray();
       for (int j = 0; j < n; ++j, ++i) {
           stack[i] = stack[j];
           count[i] = i > 0 && stack[i - 1] == stack[j] ? count[i - 1] + 1 : 1;
           if (count[i] == k) i -= k;
       }
       return new String(stack, 0, i);
   }
*/

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
