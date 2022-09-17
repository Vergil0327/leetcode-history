// https://leetcode.com/contest/biweekly-contest-87/problems/smallest-subarrays-with-maximum-bitwise-or/
package main

/* https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/discuss/2588015/JavaC%2B%2BPython-Bit-Solution-with-Explanation */
func smallestSubarrays(nums []int) []int {
	last := make([]int, 30)
	n := len(nums)
	res := make([]int, n)

	for i := n - 1; i >= 0; i-- {
		res[i] = 1 // base case

		// There will be at most 30 bits which will be set in the bitwise OR of elements. Since num[i] can go up to 10^9.
		for j := 0; j < 30; j++ {
			// update `1` position
			// `last` caches which i position we can make digit j is 1 by OR operation
			// `last` is the variation production of OR operation of nums[i -> n - 1], each digit last[j] cache the index to bring last[j] to 1,
			if nums[i]&(1<<j) > 0 {
				last[j] = i
			}

			// we need to get length of max possible OR result => res[i] = max(last[j])-i+1
			// only max(last[j]) position can make our array own maximum possible OR result
			res[i] = max(res[i], last[j]-i+1)
		}
	}

	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
