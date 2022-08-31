// explanation: https://www.youtube.com/watch?v=bNvIQI2wAjk
package main

// T:O(n^2)
func productExceptSelfBrutal(nums []int) []int {
	m := map[int]int{}

	for i, num := range nums {
		m[i] = num
	}

	result := make([]int, len(nums))
	for i := 0; i < len(result); i++ {
		result[i] = 1
	}

	for i := 0; i < len(nums); i++ {
		// need to memorize this section
		for j := 0; j < len(nums); j++ {
			if j == i {
				continue
			}
			result[i] *= m[j]
		}
	}
	return result
}

// Example 1:									Example 2:
// Input: nums = [1,2,3,4]		Input: nums = [-1,1,0,-3,3]
// Output: [24,12,8,6]				Output: [0,0,9,0,0]
// T:O(n) M:O(2n)
func productExceptSelfBetter(nums []int) []int {
	mFront := []int{1}
	for i := 0; i < len(nums); i++ {
		mFront = append(mFront, mFront[i]*nums[i])
	}

	mBehind := []int{1}
	for i := len(nums) - 1; i >= 0; i-- {
		mBehind = append(mBehind, mBehind[len(nums)-i-1]*nums[i])
	}

	// input:[1,2,3,4]
	// [1, 1, 2, 6, 24]
	// [1, 4, 12, 24, 24]
	// [[2*3*4], [1*(3*4)], [(1*2)*4], [1*2*3]]
	// result[i] = value in front of index * value behind index
	result := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		result[i] = mFront[i] * mBehind[len(nums)-i-1]
	}
	return result
}

// input:[1,2,3,4]
// T:O(n) M:O(1)
func productExceptSelfBest(nums []int) []int {
	result := make([]int, len(nums))

	frontValue := 1
	for i := 0; i < len(nums); i++ {
		result[i] = frontValue
		frontValue *= nums[i]
	}

	valueBehind := 1
	for i := len(nums) - 1; i >= 0; i-- {
		result[i] *= valueBehind
		valueBehind *= nums[i]
	}

	return result
}
