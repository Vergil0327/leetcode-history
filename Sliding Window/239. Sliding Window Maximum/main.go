// https://leetcode.com/problems/sliding-window-maximum/
package main

import (
	"container/list"
	"math"
)

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

// use double-linked list instead of slice as deque
// underlying-array would grow larger and larger if we use slice as deque
func maxSlidingWindowList(nums []int, k int) []int {
	if k == 1 {
		return nums
	}

	res := []int{}
	deque := list.New()

	l, r := 0, 0
	for r < len(nums) {
		// reserve decreasing order for finding max
		for deque.Len() > 0 && nums[deque.Back().Value.(int)] < nums[r] {
			deque.Remove(deque.Back())
		}
		deque.PushBack(r)
		r += 1

		if r-l >= k {
			res = append(res, nums[deque.Front().Value.(int)])
			l += 1
		}

		if l > deque.Front().Value.(int) {
			deque.Remove(deque.Front())
		}
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
