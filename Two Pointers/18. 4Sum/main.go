// https://leetcode.com/problems/4sum/
package main

import (
	"sort"
)

/*
generic k-Sum solution
neetcode: https://www.youtube.com/watch?v=EYeR-_1NRlQ&ab_channel=NeetCode
*/
func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)

	res, quadruplet := [][]int{}, []int{}

	var kSum func(k, start, target int)
	kSum = func(k, start, target int) {
		if k > 2 {
			// i<len(nums)-k+1: reserve valid quadruplets
			for i := start; i < len(nums)-k+1; i++ {
				// remove duplicate
				if i > start && nums[i] == nums[i-1] {
					continue
				}

				// just like backtracking
				quadruplet = append(quadruplet, nums[i])
				kSum(k-1, i+1, target-nums[i])
				quadruplet = quadruplet[:len(quadruplet)-1]
			}
			return
		}

		// base case: 2Sum II
		l, r := start, len(nums)-1
		for l < r {
			sum := nums[l] + nums[r]
			if sum > target {
				r -= 1
			} else if sum < target {
				l += 1
			} else {
				quad := append(quadruplet, nums[l], nums[r])

				res = append(res, quad)
				l += 1
				// remove duplicate
				for l < r && nums[l] == nums[l-1] {
					l += 1
				}
			}
		}
	}

	kSum(4, 0, target)
	return res
}

// T:O(n^3)
func fourSum1stTry(nums []int, target int) [][]int {
	// nlogn
	sort.Ints(nums)

	// n^3
	res := [][]int{}
	for i, num := range nums {
		// remove duplicate
		if i > 0 && num == nums[i-1] {
			continue
		}

		for j := i + 1; j < len(nums); j++ {
			// remove duplicate
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}

			l, r := j+1, len(nums)-1
			for l < r {
				sum := num + nums[j] + nums[l] + nums[r]
				if sum > target {
					r -= 1
				} else if sum < target {
					l += 1
				} else {
					res = append(res, []int{num, nums[j], nums[l], nums[r]})
					l += 1

					// remove duplicate
					for l < r && nums[l] == nums[l-1] {
						l += 1
					}
				}
			}
		}
	}

	return res
}
