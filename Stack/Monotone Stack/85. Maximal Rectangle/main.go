package main

import "math"

func maximalRectangle(matrix [][]byte) int {
	histogram := make([]int, len(matrix[0])+2) // append math.MinInt as boundary at left-most and right-most position
	histogram[0], histogram[len(histogram)-1] = math.MinInt, math.MinInt

	maxRec := 0
	for r := range matrix {
		for c := range matrix[0] {
			if matrix[r][c] == '0' {
				histogram[c+1] = 0
			} else {
				histogram[c+1] += 1
			}
		}

		rec := caluculateHistogramMaxArea(histogram)
		maxRec = max(maxRec, rec)
	}

	return maxRec
}

func caluculateHistogramMaxArea(histogram []int) int {
	maxRec := 0

	// leetcode 84.
	// calculate maximum histogram: height * (nextSmaller-prevSmaller-1)
	stack := []int{}
	for i := range histogram {
		for len(stack) > 0 && histogram[stack[len(stack)-1]] > histogram[i] {
			index := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			prevSmaller, nextSmaller := stack[len(stack)-1], i
			maxRec = max(maxRec, histogram[index]*(nextSmaller-prevSmaller-1))
		}
		stack = append(stack, i)
	}

	return maxRec
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
