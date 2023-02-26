package leetcode2576

import "sort"

func maxNumOfMarkedIndices(nums []int) int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	n := len(nums)

	var check func(targetNumPair int) bool
	check = func(targetNumPair int) bool {
		j := n - 1
		pairs := 0
		for i := j - targetNumPair; i >= 0; i -= 1 {
			if nums[i]*2 <= nums[j] {
				j -= 1
				pairs += 1
			}
		}
		return pairs >= targetNumPair
	}

	l, r := 0, n/2
	for l < r {
		mid := r - (r-l)/2
		if check(mid) {
			l = mid
		} else {
			r = mid - 1
		}
	}
	return l * 2
}
