package main

// https://www.youtube.com/watch?v=fAsV6SIJ-GI
func scoreOfParentheses(s string) int {
	stack := []int{}

	curr := 0
	for _, c := range s {
		if c == '(' {
			stack = append(stack, curr)
			curr = 0
		} else {
			if curr == 0 {
				curr += 1
			} else {
				curr *= 2
			}
			if len(stack) > 0 {
				top := stack[len(stack)-1]
				curr += top
				stack = stack[:len(stack)-1]
			}
		}
	}

	return curr
}

// ()(()()()())
// stack: [],[0],[],[1],[1 0],[1],[1 1],[1],[1 2],[1],[1 3],[1]
// curr : 0   0   1  0    0   1     0.   2.   0.   3.   0.   4
