package main

import "math"

// T:O(n^2)
func findMaxAverageSubarray(nums []int, k int) float64 {
	var res float64 = math.MinInt64
	for i := 0; i < len(nums)-k; i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			res = math.Max(res, float64(sum)/float64(j-i+1))
		}
	}

	return res
}

// use binary search to guess max average between min and max because this rule says that "The answer with the calculation error less than 10^-5 will be accepted"
// max average must exist between min and max value in nums array
func findMaxAverageSubarrayBinSearch(nums []int, k int) float64 {
	var min, max float64 = math.MaxFloat64, math.MinInt64
	for _, num := range nums {
		min = math.Min(min, float64(num))
		max = math.Max(max, float64(num))
	}

	prevMid := max
	err := math.MaxFloat64
	errors := math.Pow10(-5)
	for err > errors {
		var mid float64 = min + (max-min)/2

		if check(nums, mid, k) /* max average exists in right portion of nums */ {
			min = mid
		} else {
			max = mid
		}

		err = math.Abs(prevMid - mid)
		prevMid = mid
	}

	return min
}

//	(nums[0]+...nums[j])/j >= mid, length of left-side must be k at least
//
// -> check: average from 0 to j >= mid
// -> (nums[0]+...nums[j]) >= mid * j
// -> (nums[0]+...nums[j]) - mid*j >= 0
// -> (nums[0]-mid) + ... + nums[j]-mid >= 0
func check(nums []int, mid float64, k int) bool {
	var sum, prefixSum, minSum float64 = 0, 0, 0
	for i := 0; i < k; i++ {
		sum += float64(nums[i]) - mid
	}
	if sum > 0 {
		return true
	}

	for i := k; i < len(nums); i++ {
		sum += float64(nums[i]) - mid
		prefixSum += float64(nums[i-k]) - mid
		minSum = math.Min(minSum, prefixSum)
		if sum >= minSum {
			return true
		}
	}

	return false
}
