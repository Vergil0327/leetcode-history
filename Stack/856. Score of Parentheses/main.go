package main

// https://www.youtube.com/watch?v=tiAaVfMcL9w
func scoreOfParenthesesRecursive(s string) int {
	var score func(l, r int) int
	score = func(l, r int) int {
		if r-l == 1 { // one ()
			return 1
		}

		balance := 0
		for i := l; i < r; i++ {
			if s[i] == '(' {
				balance += 1
			} else {
				balance -= 1
			}
			if balance == 0 { // () + remaining string
				return score(l, i) + score(i+1, r)
			}
		}

		// if we don't see any balance parentheses happening inside for-loop
		// then it must be outer parentheses
		return 2 * score(l+1, r-1)
	}

	return score(0, len(s)-1)
}

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
