package main

import (
	"sort"
)

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.
// https://www.youtube.com/watch?v=jzZsG8n2R9A

func threeSum(nums []int) [][]int {
	result := [][]int{}

	// T:O(n logN)
	// sorted: [-4,-1,-1,0,1,2]
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	// T: O(n^2)
	for i, num := range nums {
		// !!! because we've already sorted the array
		if num > 0 {
			break
		}

		// prevent duplicate triplet
		if i > 0 && num == nums[i-1] {
			continue
		}

		l := i + 1
		r := len(nums) - 1
		for l < r {
			sum := nums[i] + nums[l] + nums[r]
			if sum > 0 {
				r -= 1
			} else if sum < 0 {
				l += 1
			} else {
				result = append(result, []int{nums[i], nums[l], nums[r]})
				l += 1

				// prevent duplicate triplet
				for l < r && nums[l] == nums[l-1] {
					l += 1
				}
			}
		}
	}

	return result
}
