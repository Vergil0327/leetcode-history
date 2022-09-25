package main

// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/discuss/2620481/count-maximum-number-of-the-array-%2B-MEME
// the bitwise AND of two different numbers will always be strictly less than the maximum of those two numbers
// so the longest subarray with max bitwise AND would be the subarray containing only the max numbers

// let k be the maximum value of the bitwise AND of any subarray of nums.
// "only subarrays with a bitwise AND equal to k should be considered".
func longestSubarray(nums []int) int {
	maxNum := 0
	for _, num := range nums {
		maxNum = max(maxNum, num)
	}

	longest := 0
	currLen := 0
	for _, num := range nums {
		// subarray that contains max AND
		if num == maxNum {
			currLen += 1
		} else {
			// no need to consider
			currLen = 0
		}
		longest = max(longest, currLen)
	}

	return longest
}

func longestSubarrayBruteForce(nums []int) int {
	longest := 0

	maxAnd := -1
	for i := 0; i < len(nums); i++ {
		curr := nums[i]
		for j := i; j < len(nums); j++ {

			curr &= nums[j]

			if curr > maxAnd {
				maxAnd = curr
				longest = j - i + 1
			} else if curr == maxAnd {
				longest = max(longest, j-i+1)
			} else {
				break
			}
		}
	}

	return longest
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
