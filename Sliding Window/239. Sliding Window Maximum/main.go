// https://leetcode.com/problems/sliding-window-maximum/
package main

import "math"

/*
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
*/

// T:O(n) by using deque
// monotonically decreasing deque
// explanation: https://www.youtube.com/watch?v=DfljaUwZsOk
func maxSlidingWindow(nums []int, k int) []int {
	res := []int{}
	deque := []int{}

	l, r := 0, 0
	for r < len(nums) {
		// reserve decreasing order for finding max
		for len(deque) > 0 && nums[deque[len(deque)-1]] < nums[r] {
			deque = deque[:len(deque)-1]
		}
		deque = append(deque, r)

		// if window passed, popLeft
		if l > deque[0] {
			deque = deque[1:]
		}

		// only append result after window size reached k
		if r+1 >= k {
			res = append(res, nums[deque[0]])
			l += 1
		}

		r += 1
	}

	return res
}

// brute force T:O((n-k)*k)
func maxSlidingWindowBruteForce(nums []int, k int) []int {
	res := []int{}

	max := 0
	for i := 0; i < len(nums)-k+1; i++ {
		for j := i; j < i+k; j++ {
			max = int(math.Max(float64(max), float64(nums[j])))
		}
		res = append(res, max)
		max = math.MinInt
	}

	return res
}
