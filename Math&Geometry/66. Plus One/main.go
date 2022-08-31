package main

func plusOne(digits []int) []int {
	shouldPlusOne := false
	for i := len(digits) - 1; i >= 0; i-- {
		shouldPlusOne = false

		digits[i] += 1
		if digits[i] == 10 {
			digits[i] = 0
			if i == 0 {
				digits = append([]int{1}, digits...)
			} else {
				shouldPlusOne = true
			}
		}

		if !shouldPlusOne {
			break
		}
	}

	return digits
}

// Other Solution
func plusOneOther(digits []int) []int {
	last := len(digits) - 1
	add := true
	for x := last; x >= 0; x-- {
		if !add {
			break
		}
		if x == 0 && digits[x] == 9 {
			digits[0] = 0
			digits = append([]int{1}, digits...)
			break
		} else if digits[x] == 9 {
			digits[x] = 0
		} else {
			digits[x]++
			add = false
		}
	}

	return digits
}
