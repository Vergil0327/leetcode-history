// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
package main

import (
	"math"
	"sort"
)

// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463306/JavaC%2B%2BPython-Just-Sort-O(nlogn)
// T: nlogn
func findBestValueJustSorting(arr []int, target int) int {
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))

	maxVal := arr[0]

	// target - min(arr) and pop min(arr)
	for len(arr) > 0 && target >= arr[len(arr)-1]*len(arr) {
		target -= arr[len(arr)-1]
		arr = arr[:len(arr)-1]
	}

	// if A is empty means it's impossible to reach target so we just return maximum element.
	if len(arr) == 0 {
		return maxVal
	}

	// If A is not empty, intuitively the answer should be the nearest integer to target / len(A)
	// Since we need to return the minimum such integer if there is a tie
	// if target / len(A) = 0.5, we should round down
	// i.e. 必須在 target/len(arr) and target/len(arr)+1 之間二選一
	if float64(target)/float64(len(arr))-float64(target/len(arr)) <= 0.5 {
		return target / len(arr)
	}

	return target/len(arr) + 1
}

func findBestValueOptimized(arr []int, target int) int {
	sum := 0
	maxVal := math.MinInt
	for _, num := range arr {
		sum += num
		maxVal = max(maxVal, num)
	}

	// EDGE CASE: we can't lower sum anymore
	if sum <= target {
		return maxVal
	}

	// 1 <= arr[i], target <= 10^5
	// 注意: l不可設1
	// EDGE CASE EXAMPLE: target = n, arr's size >>> n
	// target = 4000, arr's size: 10000, then
	// l=2, sum=20000
	// l=1, sum=10000
	// l=0, sum=0
	l, r := 0, int(math.Pow10(5))
	for l < r {
		mid := r - (r-l)/2

		sum = 0
		for _, num := range arr {
			sum += min(num, mid)
		}

		// find smallest mid that sum <= target
		if sum > target {
			r = mid - 1
		} else if sum < target {
			l = mid
		} else {
			return mid
		}
	}

	sum1, sum2 := 0, 0
	for _, num := range arr {
		sum1 += min(num, l)
		sum2 += min(num, l+1)
	}

	// condense to `<=`
	if abs(target-sum1) <= abs(target-sum2) {
		return l
	}
	return l + 1
}

// T:O(nlog(max(arr)))
func findBestValue(arr []int, target int) int {
	sum := 0
	maxVal := math.MinInt
	for _, num := range arr {
		sum += num
		maxVal = max(maxVal, num)
	}

	// EDGE CASE: we can't lower sum anymore
	if sum <= target {
		return maxVal
	}

	// 1 <= arr[i], target <= 10^5
	// 注意: l不可設1
	// EDGE CASE EXAMPLE: target = n, arr's size >>> n
	// target = 4000, arr's size: 10000, then
	// l=2, sum=20000
	// l=1, sum=10000
	// l=0, sum=0
	l, r := 0, int(math.Pow10(5))
	for l < r {
		mid := r - (r-l)/2

		sum = 0
		for _, num := range arr {
			sum += min(num, mid)
		}

		// find smallest mid that sum <= target
		if sum > target {
			r = mid - 1
		} else if sum < target {
			l = mid
		} else {
			return mid
		}
	}

	// we need to find the index such that sum is as close as possible (in absolute difference) to target
	// sum <= target
	lowerbound := l
	sumLower := 0

	// sum > target
	upperbound := l + 1
	sumUpper := 0

	for _, num := range arr {
		sumLower += min(num, lowerbound)
		sumUpper += min(num, upperbound)
	}

	if absLo, absHi := abs(target-sumLower), abs(target-sumUpper); absLo < absHi {
		return lowerbound
	} else if absLo > absHi {
		return upperbound
	} else {
		// In case of a tie, return the minimum such integer
		return min(lowerbound, upperbound)
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func abs(num int) int {
	if num < 0 {
		return -num
	}

	return num
}
