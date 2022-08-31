// https://leetcode.com/problems/trapping-rain-water/

package main

import "math"

/*
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
*/

// explanation: https://www.youtube.com/watch?v=ZI2z5pq0TqA
// water[i] = min(LeftMaxHeight, RightMaxHeight) - h[i] for every i position
// T:O(n) M:O(1)
func trapTwoPointer(height []int) int {
	// !!! edge case
	if len(height) == 0 {
		return 0
	}

	water := 0
	l, r := 0, len(height)-1
	maxLeftHeight, maxRightHeight := height[l], height[r]
	for l < r {
		if maxLeftHeight <= maxRightHeight {
			l += 1
			maxLeftHeight = int(math.Max(float64(maxLeftHeight), float64(height[l])))
			// ! redundant check, maxLeftHeight always >= height (already take math.Max)
			// water += int(math.Max(0, float64(maxLeftHeight-height[l])))
			water += maxLeftHeight - height[l]
		} else {
			r -= 1
			maxRightHeight = int(math.Max(float64(maxRightHeight), float64(height[r])))
			// ! redundant check, maxRightHeight always >= height (already take math.Max)
			// water += int(math.Max(0, float64(maxRightHeight-height[r])))
			water += maxRightHeight - height[r]
		}
	}

	return water
}

// T:O(n), M:O(n)
func trap(height []int) int {
	leftMaxHeight := make([]int, len(height)+1)
	rightMaxHeight := make([]int, len(height)+1)

	for i := 1; i < len(height)+1; i++ {
		leftMaxHeight[i] = int(math.Max(float64(height[i-1]), float64(leftMaxHeight[i-1])))
	}
	leftMaxHeight = leftMaxHeight[1:]

	for i := len(height) - 1; i >= 0; i-- {
		rightMaxHeight[i] = int(math.Max(float64(height[i]), float64(rightMaxHeight[i+1])))
	}
	rightMaxHeight = rightMaxHeight[:len(rightMaxHeight)-1]

	water := 0
	for i := 0; i < len(height); i++ {
		minBoundaryHeight := int(math.Min(float64(leftMaxHeight[i]), float64(rightMaxHeight[i])))
		water += int(math.Max(0, float64(minBoundaryHeight-height[i])))
	}

	return water
}
