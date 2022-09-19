// https://leetcode.com/problems/3sum-closest/

package main

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)

	diff := math.MaxInt
	candidate := 0
	for i, num := range nums {
		l, r := i+1, len(nums)-1
		for l < r {
			sum := num + nums[l] + nums[r]
			if sum < target {
				l += 1
			} else if sum > target {
				r -= 1
			} else {
				return target
			}
			if curr := Abs(sum - target); curr < diff {
				diff = curr
				candidate = sum
			}
		}
	}

	return candidate
}

func Abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}
