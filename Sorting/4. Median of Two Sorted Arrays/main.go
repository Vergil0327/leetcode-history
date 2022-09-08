package main

import (
	"math"
)

// https://www.youtube.com/watch?v=q6IEA26hvXc&ab_channel=NeetCode
func findMedianSortedArraysBinarySearch(nums1 []int, nums2 []int) float64 {
	var A, B []int
	if len(nums1) < len(nums2) {
		A = make([]int, len(nums1))
		copy(A, nums1)
		B = make([]int, len(nums2))
		copy(B, nums2)
	} else {
		B = make([]int, len(nums1))
		copy(B, nums1)
		A = make([]int, len(nums2))
		copy(A, nums2)
	}

	total := len(nums1) + len(nums2)
	half := total / 2

	// A is array with shorter length
	l, r := 0, len(A)-1
	for {
		// l = midA + 1
		// r = midA - 1
		// if l,r = 0,1 => midA = 0
		// midA = 0 + (1-0)/2 = 0 => dead loop
		// midA = 1 - (1-0)/2 = 1 => l = 2, r = 0
		midA := r - (r-l)/2

		// why we substract by 2? -> convert lengths into indexes.
		// E.x. A =  1 2 3 4 5 and B = 1 2 3 4 5
		// A's midpoint would be index 2. We need midpoint in B to be index 1.
		// So 5 (avg length) - midpointA - 2 = midpointB
		midB := half - midA - 2

		// use math.MinInt, math.MaxInt as default value for comparison afterwards
		// ex. if A = [], B[1, 2, 3]; we want this comparison `Aleft <= Bright && Bleft <= Aright` is still be valid
		Aleft, Aright := math.MinInt, math.MaxInt
		if midA >= 0 {
			Aleft = A[midA]
		}
		if midA+1 < len(A) {
			Aright = A[midA+1]
		}

		Bleft, Bright := math.MinInt, math.MaxInt
		if midB >= 0 {
			Bleft = B[midB]
		}
		if midB+1 < len(B) {
			Bright = B[midB+1]
		}

		// partition is correct
		if Aleft <= Bright && Bleft <= Aright {
			if isOdd := total/2 == 1; isOdd {
				return float64(min(Aright, Bright))
			} else {
				return float64(max(Aleft, Bleft)+min(Aright, Bright)) / 2
			}
		} else if Aleft > Bright /* we need to shrink A size */ {
			r = midA - 1
		} else {
			l = midA + 1
		}
	}
}

func min(a, b int) int {
	if a <= b {
		return a
	}

	return b
}

func max(a, b int) int {
	if a >= b {
		return a
	}

	return b
}
