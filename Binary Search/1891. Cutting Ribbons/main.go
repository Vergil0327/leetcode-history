package main

import "sort"

// T:O(nlogn)
func maxLength(ribbons []int, k int) int {
	sort.Ints(ribbons)
	l, r := ribbons[0], ribbons[len(ribbons)-1]

	// we can't get k ribbon
	if r < k {
		return 0
	}

	for l < r {
		mid := r - (r-l)/2
		if check(ribbons, mid, k) {
			l = mid
		} else {
			r = mid - 1
		}
	}

	return l
}

func check(ribbons []int, length, k int) bool {
	count := 0
	for _, rib := range ribbons {
		count += rib / length
	}
	return count >= k
}
