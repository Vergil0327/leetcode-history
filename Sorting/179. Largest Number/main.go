// https://leetcode.com/problems/largest-number/
package main

import (
	"sort"
	"strconv"
)

// neetcode: https://www.youtube.com/watch?v=WDx6Y4i4xJ8

// T:O(nlogn) M:O(n)
// Runtime: 0 ms, faster than 100.00% of Go online submissions for Largest Number.
// Memory Usage: 2.9 MB, less than 29.50% of Go online submissions for Largest Number.
func largestNumber(nums []int) string {
	sort.Slice(nums, func(i, j int) bool {
		str1 := strconv.Itoa(nums[i])
		str2 := strconv.Itoa(nums[j])

		if str1[0] == str2[0] {
			str1, str2 = str1+str2, str2+str1
			num1, _ := strconv.Atoi(str1)
			num2, _ := strconv.Atoi(str2)
			return num1 > num2
		}
		return str1[0] > str2[0]
	})

	str := ""
	for _, num := range nums {
		// remove leading zero
		if s := strconv.Itoa(num); s == "0" && str == "0" {
			continue
		}
		str += strconv.Itoa(num)
	}

	return str
}
