package main

func dailyTemperatures(temperatures []int) []int {
	res := make([]int, len(temperatures))

	stack := []int{}
	for i, temp := range temperatures {
		for len(stack) > 0 && temperatures[stack[len(stack)-1]] < temp {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			res[top] = i - top
		}

		stack = append(stack, i)
	}

	return res
}
