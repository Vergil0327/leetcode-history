package main

func nextGreaterElements(nums []int) []int {
	arr := append(nums, nums...)
	nextGreater := map[int]int{}

	stack := [][]int{} // [index, num]
	for i, num := range arr {
		nextGreater[i] = -1

		for len(stack) > 0 && stack[len(stack)-1][1] < num {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			nextGreater[top[0]] = num
		}
		stack = append(stack, []int{i, num})
	}

	res := []int{}
	for i := range nums {
		res = append(res, nextGreater[i])
	}

	return res
}
