package main

import "math"

// from brute force, we can know that:
//
//	for i := range nums {
//	    maxVal, minVal := math.MinInt, math.MaxInt
//	    for j:=i; j<len(nums); j++ {
//	        maxVal = max(maxVal, nums[j])
//	        minVal = min(minVal, nums[j])
//	        sum += int64(maxVal-minVal)
//	    }
//	}
//
//	sum of subarray range
//	= sum of subarray (maxVal-minVal)
//	= total subarray maxVal - total subarray minVal
//
// It implies that we can calculate these two partial sums separately.
// Edge Case: has duplicate values, ex. [1, 3, 3]
// => only count one time by using "less than or equal", "greater than or equal"
//
// explanation: https://www.youtube.com/watch?v=xba0NzSbuas
// from brute force, we can know that:
//
//	for i := range nums {
//	    maxVal, minVal := math.MinInt, math.MaxInt
//	    for j:=i; j<len(nums); j++ {
//	        maxVal = max(maxVal, nums[j])
//	        minVal = min(minVal, nums[j])
//	        sum += int64(maxVal-minVal)
//	    }
//	}
//
//	sum of subarray range
//	= sum of subarray (maxVal-minVal)
//	= total subarray maxVal - total subarray minVal
//
// It implies that we can calculate these two partial sums separately.
// Edge Case: has duplicate values, ex. [1, 3, 3]
// => only count one time by using "less than or equal", "greater than or equal"
//
// explanation: https://www.youtube.com/watch?v=xba0NzSbuas
func subArrayRanges(nums []int) int64 {
	N := len(nums)

	nextSmallerOrEqual := make([]int, N)
	for i := range nextSmallerOrEqual {
		nextSmallerOrEqual[i] = N // default value
	}

	stack := []int{}
	for i := 0; i < N; i++ {
		num := nums[i]
		for len(stack) > 0 && nums[stack[len(stack)-1]] >= num {
			top := stack[len(stack)-1]
			nextSmallerOrEqual[top] = i

			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}

	prevSmaller := make([]int, N)
	for i := range prevSmaller {
		prevSmaller[i] = -1 // default value
	}

	stack = nil // clear slice
	for i := len(nums) - 1; i >= 0; i-- {
		num := nums[i]
		for len(stack) > 0 && nums[stack[len(stack)-1]] > num {
			top := stack[len(stack)-1]
			prevSmaller[top] = i

			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}

	nextGreaterOrEqual := make([]int, N)
	for i := range nextGreaterOrEqual {
		nextGreaterOrEqual[i] = N
	}

	stack = nil // clear slice
	for i, num := range nums {
		for len(stack) > 0 && nums[stack[len(stack)-1]] <= num {
			top := stack[len(stack)-1]
			nextGreaterOrEqual[top] = i

			stack = stack[:len(stack)-1]
		}

		stack = append(stack, i)
	}

	prevGreater := make([]int, N)
	for i := range prevGreater {
		prevGreater[i] = -1
	}

	stack = nil
	for i := len(nums) - 1; i >= 0; i-- {
		num := nums[i]
		for len(stack) > 0 && nums[stack[len(stack)-1]] < num {
			top := stack[len(stack)-1]
			prevGreater[top] = i

			stack = stack[:len(stack)-1]
		}

		stack = append(stack, i)
	}

	var sum int64

	// total sum of subarray's max
	for i := range nums {
		l, r := prevGreater[i], nextGreaterOrEqual[i]
		combinations := (i - l) * (r - i)
		sum += int64(nums[i] * combinations)
	}

	// total sum of subarray's min
	for i := range nums {
		l, r := prevSmaller[i], nextSmallerOrEqual[i]
		combinations := (i - l) * (r - i)
		sum -= int64(nums[i] * combinations)
	}

	return sum
}

// O(n^2)
func subArrayRangesBruteForce(nums []int) int64 {
	var sum int64
	for i := range nums {
		maxVal, minVal := math.MinInt, math.MaxInt
		for j := i; j < len(nums); j++ {
			maxVal = max(maxVal, nums[j])
			minVal = min(minVal, nums[j])
			sum += int64(maxVal - minVal)
		}
	}

	return sum
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
