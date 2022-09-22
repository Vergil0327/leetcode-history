// https://leetcode.com/problems/max-consecutive-ones-iii/
package main

func longestOnes(nums []int, k int) int {
	count := [2]int{}
	longest := 0

	l := 0
	for r := range nums {
		count[nums[r]] += 1

		// we can't use `l < r`
		// edge case: [0,0,0,0], 0
		// expected: 0
		// output will be 1 if we use `for l < r && count[0] > k`
		for l <= r && count[0] > k {
			count[nums[l]] -= 1
			l += 1
		}

		longest = max(longest, r-l+1)
	}

	return longest
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
