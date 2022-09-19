// https://leetcode.com/problems/4sum/
package main

import (
	"sort"
)

/*
	neetcode: https://www.youtube.com/watch?v=EYeR-_1NRlQ&ab_channel=NeetCode
*/

// T:O(n^3)
func fourSum(nums []int, target int) [][]int {
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
