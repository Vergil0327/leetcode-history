package main

import (
	"sort"
)

type KthLargest struct {
	k          int
	sortedList []int
}

// list insertion T:(logN), sorting: T:(NlogN) if quick sort
func Constructor(k int, nums []int) KthLargest {
	sort.Sort(sort.IntSlice(nums))
	return KthLargest{k: k, sortedList: nums}
}

func (this *KthLargest) Add(val int) int {
	if len(this.sortedList) == 0 {
		this.sortedList = append(this.sortedList, val)
		return this.sortedList[0]
	}

	for i := len(this.sortedList) - 1; i >= 0; i -= 1 {
		if val > this.sortedList[i] {
			this.sortedList = append(this.sortedList[:i+1], this.sortedList[i:]...)
			this.sortedList[i+1] = val
			if idx := len(this.sortedList) - this.k; idx > 0 {
				return this.sortedList[idx]
			} else {
				return this.sortedList[0]
			}
		}
	}

	this.sortedList = append([]int{val}, this.sortedList...)
	if idx := len(this.sortedList) - this.k; idx > 0 {
		return this.sortedList[idx]
	}
	return this.sortedList[0]
}
