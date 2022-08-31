// https://leetcode.com/problems/median-of-two-sorted-arrays/
package main

import "math"

/*
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

123 567
4

1234 567
4

1234 3456
12334456

1234567  345678
123344 5 566778

A:.....medium.....
B:...............medium...............
					|					|
*/

// explanation: https://www.youtube.com/watch?v=q6IEA26hvXc
// T:O(log(min(m,n)))
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// A is shorter length array
	var A, B []int
	if len(nums1) < len(nums2) {
		A = make([]int, len(nums1))
		copy(A, nums1)
		B = make([]int, len(nums2))
		copy(B, nums2)
	} else {
		A = make([]int, len(nums2))
		copy(A, nums2)
		B = make([]int, len(nums1))
		copy(B, nums1)
	}
	total := len(A) + len(B)
	half := total / 2 // half size of merged array

	l, r := 0, len(A)-1

	for /* answer is guarenteed */ {
		// ! i := l + (r-l)/2 => DEAD LOOP
		i := r - (r-l)/2
		j := (half - (i + 1)) - 1 // half size - midA size - 1 to zero-based array index of B

		// each one could be out of bound, so we add default value for comparison
		leftA := math.MinInt
		if i >= 0 {
			leftA = A[i]
		}

		rightA := math.MaxInt
		if i+1 < len(A) {
			rightA = A[i+1]
		}

		leftB := math.MinInt
		if j >= 0 {
			leftB = B[j]
		}

		rightB := math.MaxInt
		if j+1 < len(B) {
			rightB = B[j+1]
		}

		// [..., leftA, rightA, ...]
		// [......, leftB, rightB, ......]
		// => [........., [leftA,leftB],[rightA,rightB], .........]
		if leftA <= rightB && leftB <= rightA {
			if isEven := total%2 == 0; isEven {
				return (math.Max(float64(leftA), float64(leftB)) + math.Min(float64(rightA), float64(rightB))) / 2
			} else /* odd length */ {
				return math.Min(float64(rightA), float64(rightB))
			}
		} else if leftA > rightB {
			r = i - 1
		} else /* leftA < rightB */ {
			l = i + 1
		}
	}
}
