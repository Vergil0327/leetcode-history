package main

import "math"

// T:O(n)
func maxScore(cardPoints []int, k int) int {
	if k > len(cardPoints) {
		return sum(cardPoints)
	}

	prefixSum := make([]int, len(cardPoints)+1)
	for i, score := range cardPoints {
		prefixSum[i+1] = prefixSum[i] + score
	}

	maxPoints := 0
	N := len(prefixSum)

	for i := 1; i < N; i++ {
		if i >= 1 && i < 1+k {
			pt := prefixSum[i] + (prefixSum[N-1] - prefixSum[N-1-k+i])
			maxPoints = max(maxPoints, pt)
		}

		if i >= N-k && i < N {
			pt := (prefixSum[N-1] - prefixSum[i-1]) + prefixSum[i-(N-k)]
			maxPoints = max(maxPoints, pt)
		}
	}

	return maxPoints
}

func sum(nums []int) (total int) {
	for _, num := range nums {
		total += num
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

// reverse thinking
// We can find the smallest subarray sum of length `len(cardPoints) - k`
func maxScoreSlidingWindow(cardPoints []int, k int) int {
	windowSize := len(cardPoints) - k
	minSubarraySum := math.MaxInt
	currSum := 0

	l := 0
	for r, pt := range cardPoints {
		currSum += pt
		if r-l+1 > windowSize {
			currSum -= cardPoints[l]
			l += 1
		}
		if currSum < minSubarraySum {
			minSubarraySum = currSum
		}
	}

	return sum(cardPoints) - minSubarraySum
}
