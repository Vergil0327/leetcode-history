package main

// 0000
// 0001
// 0010
// 0011
// 0100
// 0101
// 0111
// 1000
// 1001
// 1010
// [2, 1, 3, 4]
// T:O(2n) M:O(n)
func missingNumber(nums []int) int {
	m := map[int]bool{}
	for i := 0; i < len(nums); i++ {
		m[nums[i]] = true
	}

	for i := 0; i < len(nums); i++ {
		if _, ok := m[i]; !ok {
			return i
		}
	}

	return len(nums)
}

// T:O(n) M:O(1)
// https://www.youtube.com/watch?v=WnPLSRLSANE
func missingNumberFollowUp(nums []int) int {
	// sum(nums+missingNumber) - sum(nums) = missing number
	result := len(nums)

	// we only loop through len(nums)-1, so we add len(nums) back to result
	for i := 0; i < len(nums); i++ {
		result += i - nums[i]
	}

	return result
}
