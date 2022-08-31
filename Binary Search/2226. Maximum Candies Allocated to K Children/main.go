// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
package main

// Input: candies = [5,8,6], k = 3
// Output: 5

// Input: candies = [2,5], k = 11
// Output: 0

// Solution: https://www.youtube.com/watch?v=TBTvnyMLgng
func maximumCandies(candies []int, k int64) int {
	sum := 0
	for _, v := range candies {
		sum += v
	}

	lowerBound, upperBound := 0, sum/int(k)+1

	for lowerBound < upperBound {
		mid := upperBound - (upperBound-lowerBound)/2 // choose the one that don't enter dead loop when even length ex. [0, 1]
		// mid := lowerBound + (upperBound-lowerBound)/2

		if checkIfOK(candies, k, mid) {
			lowerBound = mid
		} else {
			upperBound = mid - 1
		}
	}

	return lowerBound
}

// 確認至少有k堆且每一堆都能分成m個
func checkIfOK(candies []int, k int64, m int) bool {
	count := 0
	for _, v := range candies {
		count += v / m
		if count >= int(k) {
			return true
		}
	}

	return false
}
