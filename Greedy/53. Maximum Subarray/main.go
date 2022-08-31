package main

import "math"

// T:O(n^2)
func maxSubArrayTerrible(nums []int) int {
	max := 0
	for i := 0; i < len(nums); i++ {
		currentSum := 0
		for j := i; j < len(nums); j++ {
			currentSum += nums[j]
			if currentSum > max {
				max = currentSum
			}
		}
	}

	return max
}

// T:O(n)
func maxSubArrayLinear(nums []int) int {
	max := nums[0] // initiate as default value
	currentSum := 0

	for _, num := range nums {
		if currentSum < 0 {
			currentSum = 0
		}

		currentSum += num
		if currentSum > max {
			max = currentSum
		}
	}
	return max
}

// Follow up:
// If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

// Divide & Conquer, T:O(n)
func maxSubArrayDac(nums []int) int {
	_, _, _, maxSum := DivideAndConquer(nums, 0, len(nums)-1)
	return maxSum
}

// This function returns four values
// 1) headSum - maximum sum if we start adding from head
// 2) tailSum - maximum sum if we start adding from tail
// 3) sum - total sum of this section
// 4) maxSum - maximum sum we have seen so far anywhwere
func DivideAndConquer(nums []int, l, r int) (int, int, int, int) {
	if l == r /* base case */ {
		return nums[l], nums[l], nums[l], nums[l]
	}

	mid := (l + r) / 2

	// find values for left and right section
	headSumL, tailSumL, sumL, maxSumL := DivideAndConquer(nums, l, mid)
	headSumR, tailSumR, sumR, maxSumR := DivideAndConquer(nums, mid+1, r)

	// headSum is maximum of headSum left or entire sum of left array + headSum right
	headSum := int(math.Max(float64(headSumL), float64(sumL+headSumR)))

	// tailSum is maximum of tailSum right or tailSum left + sum of entire right array
	tailSum := int(math.Max(float64(tailSumR), float64(sumR+tailSumL)))

	// sum is just sum of left and right
	sum := sumL + sumR

	// maxSum is either maxSum seen so far on left or right or the middle (tail of left and head of right)
	// maxSumL, maxSumR, tailSumL+headSumR(i.e. middleMaxSum)
	maxSum := int(math.Max(math.Max(float64(maxSumL), float64(maxSumR)), float64(tailSumL+headSumR)))

	return headSum, tailSum, sum, maxSum
}

// Another Divide & Conquer, T:O(n)
// Reference: https://www.youtube.com/watch?v=yBCzO0FpsVc&list=LL&index=6
func maxSubArrayDacBetterComprehension(nums []int) int {
	return findMaxSum(nums, 0, len(nums)-1)
}

func findMaxSum(nums []int, l, r int) int {
	if l == r {
		return nums[l]
	}

	mid := (l + r) / 2
	leftMax := findMaxSum(nums, l, mid)
	rightMax := findMaxSum(nums, mid+1, r)
	arrMax := findMaxCrossSum(nums, l, mid, r)
	return int(math.Max(float64(leftMax), math.Max(float64(rightMax), float64(arrMax))))
}

func findMaxCrossSum(nums []int, l, m, r int) int {
	sumL, sumR := 0, 0
	maxL, maxR := math.MinInt, math.MinInt

	for i := m; i >= l; i-- {
		sumL += nums[i]
		maxL = int(math.Max(float64(maxL), float64(sumL)))
	}

	for i := m + 1; i <= r; i++ {
		sumR += nums[i]
		maxR = int(math.Max(float64(maxR), float64(sumR)))
	}

	return maxL + maxR
}
