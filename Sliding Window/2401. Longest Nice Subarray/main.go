// https://leetcode.com/problems/longest-nice-subarray/
package main

import "math"

// https://leetcode.com/problems/longest-nice-subarray/discuss/2527272/Sliding-Window
// Intuition: each element in the nice array has unique bits.
// We use the sliding window approach, tracking used bits. We can use OR (or XOR) to combine bits.
// If the next number has a conflicting bit (used & nums[i] != 0), we shrink the window until there are no conflicts.
// T:O(n) M:O(1)
func longestNiceSubarrayOptimized(nums []int) int {
	maxLen := 0
	used := 0
	l := 0
	for r := range nums {
		for used&nums[r] != 0 {
			used ^= nums[l] // XOR: 0 ^ 0 = 0, 0 ^ 1 = 1, 1 ^ 0 = 1, 1 ^ 1 = 0
			l += 1
		}
		used |= nums[r] // OR: 0 | 0 = 0, 0 | 1 = 1, 1 | 0 = 1, 1 | 1 = 1
		maxLen = int(math.Max(float64(maxLen), float64(r-l+1)))
	}

	return maxLen
}

// T:O(n^2) M:O(1)
// meet each num once & for-loop iteration at each num only once
func longestNiceSubarray(nums []int) int {
	if len(nums) == 1 {
		return 1
	}

	l := 0
	for r := range nums {
	LOOP:
		for i := l; i < r; i++ {
			for j := i + 1; j <= r; j++ {
				if nums[i]&nums[j] != 0 {
					l += 1
					break LOOP
				}
			}
		}

	}

	return len(nums) - l
}
