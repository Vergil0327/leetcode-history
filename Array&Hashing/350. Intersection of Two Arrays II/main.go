// https://leetcode.com/problems/intersection-of-two-arrays-ii/
package main

func intersect(nums1 []int, nums2 []int) []int {
	m := map[int]int{}

	for _, num := range nums1 {
		m[num] += 1
	}

	res := []int{}
	for _, num := range nums2 {
		if val, ok := m[num]; ok && val > 0 {
			res = append(res, num)
			m[num] -= 1

			if m[num] == 0 {
				delete(m, num)
			}
		}
	}

	return res
}
