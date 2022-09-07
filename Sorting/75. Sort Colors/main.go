// https://leetcode.com/problems/sort-colors/
package main

/* Follow up: Could you come up with a one-pass algorithm using only constant extra space? */
// explanation: https://www.youtube.com/watch?v=4xbWSRZHqac&ab_channel=NeetCode
func sortColors(nums []int) {
	l, r := 0, len(nums)-1
	i := 0
	for i <= r {
		if nums[i] == 0 {
			nums[l], nums[i] = nums[i], nums[l]
			l += 1
			i += 1
		} else if nums[i] == 2 {
			nums[i], nums[r] = nums[r], nums[i]
			r -= 1
		} else {
			i += 1
		}
	}
}

// T:O(n) M:O(3)
func sortColorsCountingSort(nums []int) {
	count := map[int]int{}
	for _, num := range nums {
		count[num] += 1
	}

	for i := 0; i < len(nums); i++ {
		if count[0] > 0 {
			nums[i] = 0
			count[0] -= 1
		} else if count[1] > 0 {
			nums[i] = 1
			count[1] -= 1
		} else {
			nums[i] = 2
		}
	}
}

// T:O(nlogn) M:O(1)
func sortColorsQuickSort(nums []int) {
	quicksort(&nums, 0, len(nums)-1)
}

func quicksort(nums *[]int, l, r int) {
	if l > r {
		return
	}

	pivot := (*nums)[r]
	p := l
	for i := l; i < r; i++ {
		if (*nums)[i] < pivot {
			(*nums)[i], (*nums)[p] = (*nums)[p], (*nums)[i]
			p += 1
		}
	}
	(*nums)[p], (*nums)[r] = pivot, (*nums)[p]

	quicksort(nums, l, p-1)
	quicksort(nums, p+1, r)
}
