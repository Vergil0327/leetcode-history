// https://leetcode.com/problems/container-with-most-water/
package main

import "math"

// Ex.1
// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation:
// The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
// In this case, the max area of water (blue section) the container can contain is 49.
//
// T: O(n^2) M:O(1)
func maxArea(height []int) int {
	area := 0

	for _, x1 := range height {
		x2 := x1 + 1

		for x2 < len(height) {
			h := int(math.Min(float64(height[x1]), float64(height[x2])))
			curr := (x2 - x1) * h
			area = int(math.Max(float64(curr), float64(area)))

			x2 += 1
		}
	}

	return area
}

// T: O(n) M: O(1)
func maxAreaTwoPointer(height []int) int {
	area := 0

	x1, x2 := 0, len(height)-1 // start maximum width to find max height
	for x1 < x2 {
		h := int(math.Min(float64(height[x1]), float64(height[x2])))
		curr := (x2 - x1) * h
		area = int(math.Max(float64(curr), float64(area)))

		h1 := height[x1]
		h2 := height[x2]
		h1Next := height[x1+1]
		h2Next := height[x2-1]

		if h2 > h1 {
			x1 += 1
		} else if h2 < h1 {
			x2 -= 1
		} else {
			// or just choose anyone from x1, x2. it doesn't matter
			// x -= 1 or x1 += 1
			if h1Next > h2Next {
				x1 += 1
			} else {
				x2 -= 1
			}
		}

	}

	return area
}
