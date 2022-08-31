package main

func search(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for l < r {
		if idx := (l + r) / 2; nums[idx] == target {
			return idx
		} else if target > nums[idx] {
			l = idx + 1
		} else if target < nums[idx] {
			r = idx - 1
		} else {
			return -1
		}
	}
	if nums[l] == target {
		return l
	} else {
		return -1
	}
}

func searchBetter(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for l <= r {
		// if both l & r are greater than int64, sum of them may be wrong because of overflow.
		// if that would happen, change equation to idx := l + ((r - l) / 2)
		if idx := (l + r) / 2; nums[idx] == target {
			return idx
		} else if target > nums[idx] {
			l = idx + 1
		} else if target < nums[idx] {
			r = idx - 1
		}
	}

	return -1
}
