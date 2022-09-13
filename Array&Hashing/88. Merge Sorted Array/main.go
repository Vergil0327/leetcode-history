// https://leetcode.com/problems/merge-sorted-array/
package main

/* Follow up: Can you come up with an algorithm that runs in O(m + n) time? */

// https://www.youtube.com/watch?v=P1Ic85RarKY
// just like merge sort but place each number reversely
// why merge two list reversely?
// because if we start at empty space, we can get rid of annoying things such as where we should put the unused value
func merge(nums1 []int, m int, nums2 []int, n int) {
	if len(nums2) == 0 {
		return
	}

	idx := len(nums1) - 1
	p1, p2 := m-1, n-1
	for p1 >= 0 && p2 >= 0 {
		if nums1[p1] >= nums2[p2] {
			nums1[idx] = nums1[p1]
			p1 -= 1
		} else {
			nums1[idx] = nums2[p2]
			p2 -= 1
		}
		idx -= 1
	}

	for p1 >= 0. {
		nums1[idx] = nums1[p1]
		p1 -= 1
		idx -= 1
	}

	for p2 >= 0 {
		nums1[idx] = nums2[p2]
		p2 -= 1
		idx -= 1
	}

}
