// https://leetcode.com/problems/largest-rectangle-in-histogram/
package main

import "math"

/*
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
*/

// explanation: https://www.youtube.com/watch?v=zx5Sw9130L0
// monotonic increasing stack
// T:O(n) M:O(n)
func largestRectangleArea(heights []int) int {
	maxArea := 0
	stack := [][2]int{} // [index, height]
	for i, h := range heights {
		var pIdx int = -1
		for len(stack) > 0 && h < stack[len(stack)-1][1] {
			length := len(stack)
			pop := stack[length-1]
			stack = stack[:length-1]

			pIdx = pop[0]
			pHeight := pop[1]
			popArea := (i - pIdx) * pHeight
			maxArea = int(math.Max(float64(maxArea), float64(popArea)))
		}

		if pIdx == -1 {
			stack = append(stack, [2]int{i, h})
		} else {
			// because we can extend area from all the way from the begining to current or after
			// we need append the index of the very begining position
			stack = append(stack, [2]int{pIdx, h})
		}
	}

	for _, item := range stack {
		idx, h := item[0], item[1]
		extendArea := (len(heights) - idx) * h
		maxArea = int(math.Max(float64(maxArea), float64(extendArea)))
	}

	return maxArea
}

func largestRectangleAreaConcise(heights []int) int {
	maxArea := 0
	stack := [][2]int{} // [index, height]
	for i, h := range heights {
		var start int = i
		for len(stack) > 0 && h < stack[len(stack)-1][1] {
			pop := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			index, height := pop[0], pop[1]
			maxArea = int(math.Max(float64(maxArea), float64((i-index)*height)))

			// because we can extend area from all the way from the begining to current or after
			// we need append the index of the very begining position
			start = index
		}

		stack = append(stack, [2]int{start, h})
	}

	for _, item := range stack {
		i, h := item[0], item[1]
		maxArea = int(math.Max(float64(maxArea), float64((len(heights)-i)*h)))
	}

	return maxArea
}

// there is still an dynamic programming solution
// https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)
func largestRectangleAreaDP(heights []int) int {
	if len(heights) == 0 {
		return 0
	}

	// lessFromLeft: idx of the first bar the left that is lower than current
	// lessFromRight: idx of the first bar the right that is lower than current
	lessFromLeft, lessFromRight := make([]int, len(heights)), make([]int, len(heights))
	lessFromRight[len(heights)-1] = len(heights)
	lessFromLeft[0] = -1

	for i := 1; i < len(heights); i++ {
		prev := i - 1
		for prev >= 0 && heights[prev] >= heights[i] {
			prev = lessFromLeft[prev] // just like Union-Find to trace back
		}
		lessFromLeft[i] = prev
	}

	for i := len(heights) - 2; i >= 0; i-- {
		prev := i + 1
		for prev < len(heights) && heights[prev] >= heights[i] {
			prev = lessFromRight[prev] // just like Union-Find to trace back
		}
		lessFromRight[i] = prev
	}

	maxArea := 0
	for i := 0; i < len(heights); i++ {
		maxArea = int(math.Max(float64(maxArea), float64(heights[i]*(lessFromRight[i]-lessFromLeft[i]-1))))
	}

	return maxArea
}
