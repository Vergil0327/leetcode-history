package vp

func isValid(s string) bool {
	m := map[rune]int{
		'{': 1,
		'}': -1,
		'[': 2,
		']': -2,
		'(': 3,
		')': -3,
	}

	if len(s)%2 != 0 {
		return false
	}

	var history []int

	for _, v := range s {
		if pt := m[v]; pt > 0 {
			history = append(history, pt)
		} else if pt < 0 {
			if len(history) < 1 {
				return false
			}
			if history[len(history)-1]+pt != 0 {
				return false
			} else {
				history = history[:len(history)-1]
			}
		}
	}

	return len(history) == 0
}

func isValidBetter(s string) bool {
	m := map[rune]rune{
		'}': '{',
		']': '[',
		')': '(',
	}

	if len(s)%2 != 0 {
		return false
	}

	var stack []rune

	for _, ch := range s {
		if closedPair, ok := m[ch]; ok {
			if len(stack) > 0 && stack[len(stack)-1] == closedPair {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, ch)
		}
	}

	return len(stack) == 0
}
