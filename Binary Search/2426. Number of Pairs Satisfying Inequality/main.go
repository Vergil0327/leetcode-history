package main

import (
	"math"
	"sort"
)

// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/discuss/2646606/Python-Reverse-Pairs
// A[i] - A[j] <= B[i] - B[j] + diff
// A[i] - B[i] <= A[j] - B[j] + diff

// Define C[i] = A[i] - B[i],
// we need to find the number of pair in sequence C,
// that C[i] <= C[j] + diff.

// Classical reverse pair question,
// reference 493. Reverse Pairs.

// Usually solved by
// solution 1: binary search tree
// solution 2: merge sort
// solution 3: this one
func numberOfPairs(nums1 []int, nums2 []int, diff int) int64 {
	// Iterate sequences a = A[j] and b = B[j],
	// Binary search the position a - b + diff in a sorted sortedList l.
	sortedList := []int{}

	var res int64
	for i := 0; i < len(nums1); i++ {
		// The position index is the number of C[i] that C[i] <= C[j] + diff.
		// Add this value to result res,
		c := nums1[i] - nums2[i]
		target := c + diff
		res += countSmallerEqual(sortedList, target)

		// and then add a - b to the sorted list l.
		// actually, we iterate through the array backwards to find all the C[i]
		// C1, C2, ..., C[i], C[j], C[j+1], ...
		// we start to find C[i] from C[j] where j = 0, then j=1, j=2, ...
		// therefore, list is empty when j=0, list got one when j=1
		insertIdx := countSmallerEqual(sortedList, c) // python's bisect_right
		if int(insertIdx) >= len(sortedList) {        // dynamic inserted value into slice
			sortedList = append(sortedList, c)
		} else {
			sortedList = append(sortedList[:insertIdx+1], sortedList[insertIdx:]...)
			sortedList[insertIdx] = c
		}
	}

	return res
}

// [c1, c2, c3, c3, c3, c3, c4], target: c3
// result:                   l, number of C[i] such that C[i] <= C[j] + diff
func countSmallerEqual(arr []int, target int) int64 {
	l, r := 0, len(arr)
	for l < r {
		mid := l + (r-l)/2
		if arr[mid] <= target {
			l = mid + 1
		} else {
			r = mid
		}
	}

	return int64(l)
}

// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/discuss/2646585/Easy-Merge-Sort-based-solution-or-C%2B%2B-or-O(NlogN)-time-complexity
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/discuss/2646522/Merge-Sort-logic
func numberOfPairsMergeSort(nums1 []int, nums2 []int, diff int) int64 {
	var count int64
	c := make([]int, len(nums1))
	for i := 0; i < len(nums1); i++ {
		c[i] = nums1[i] - nums2[i]
	}

	var checkCount func(start, mid, end int) = func(start, mid, end int) {
		l, r := start, mid+1
		// we've already check pairs before mid at each mergesort step
		// [1,2,3,4]
		//  s m   end
		//  s e
		//      s e

		for l <= mid && r <= end {
			if c[l] <= c[r]+diff { // if (nums[l]<=nums[r]+d) then all values from nums[r] to nums[end] will be greater than or equal to nums[l]
				count += int64(end - r + 1)
				l += 1
			} else { // otherwise we need to increment r so that we can find match for nums[l]
				r += 1
			}
		}

		sort.Ints(c[start : end+1]) // sorting
	}

	var mergesort func(start, end int)
	mergesort = func(l, r int) {
		if l < r {
			mid := (l + r) / 2

			mergesort(l, mid)
			mergesort(mid+1, r)

			checkCount(l, mid, r)
		}
	}

	mergesort(0, len(nums1)-1)

	return count
}

// Fenwick Tree (Binary Indexed Tree, BIT) solution
// used for prefix sum
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/discuss/2646911/Binary-Indexed-Tree-or-Rearrangements-in-equation

// ref: https://tobin.cc/blog/fenwick/
type BIT struct {
	tree []int
}

func (bit *BIT) sum(index int) int {
	sum := 0
	for index > 0 {
		sum += bit.tree[index]
		index -= bit.lsb(index)
	}

	return sum
}

func (bit *BIT) update(idx, delta int) {
	for idx < len(bit.tree) {
		bit.tree[idx] += delta
		idx += bit.lsb(idx)
	}
}

func (bit *BIT) lsb(num int) int {
	return num & -num
}

func NewBIT(n int) BIT {
	return BIT{
		tree: make([]int, n+1),
	}
}

// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/discuss/2646911/Binary-Indexed-Tree-or-Rearrangements-in-equation
// A[i] - B[i] <= A[j] - B[j] + diff
// C[i] <= C[j] + diff, where C[i] = A[i]-B[i]
func numberOfPairsBinarySearchTree(nums1 []int, nums2 []int, diff int) int64 {
	// to solve negative numbers case i.e range of num1-num2+diff = [-3*10^4,3*10^4]
	// add 3*10^4 so new Range  = [0, 6*10^4]
	OFFSET := int(3 * math.Pow10(4))
	bit := NewBIT(2 * OFFSET)

	// 相當於從 C[i] Array裡找
	// 從前面C[i]找符合條件的，每次都會需要遍歷全部
	// 從C[j] + diff往前找的話可以達到Linear time complexity
	var res int64
	for i := 0; i < len(nums1); i++ {
		res += int64(bit.sum(nums1[i] - nums2[i] + diff + OFFSET))
		bit.update(nums1[i]-nums2[i]+OFFSET, 1)
	}

	return res
}

func numberOfPairsBruteForce(nums1 []int, nums2 []int, diff int) int64 {
	var count int64
	for i := 0; i < len(nums1); i++ {
		for j := i; j < len(nums1); j++ {
			if i < j && (nums1[i]-nums1[j] <= nums2[i]-nums2[j]+diff) {
				count += 1
			}
		}
	}

	return count
}
