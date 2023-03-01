package leetcode912

func sortArray(nums []int) []int {
	// l, r := 0, len(nums)-1

	// return quicksort(nums, l, r)
	// return mergesort(nums, l, r)
	return shellsort(nums)
}

func quicksort(nums []int, l, r int) []int {
	if l < r {
		nums, p := partition(nums, l, r)
		nums = quicksort(nums, l, p-1)
		nums = quicksort(nums, p+1, r)
	}
	return nums
}

func partition(nums []int, l, r int) ([]int, int) {
	pivot, p := nums[r], l
	for i := l; i < r; i += 1 {
		if nums[i] < pivot {
			nums[i], nums[p] = nums[p], nums[i]
			p += 1
		}
	}
	nums[p], nums[r] = nums[r], nums[p]
	return nums, p
}

func mergesort(nums []int, l, r int) []int {
	if l == r {
		return []int{nums[l]}
	}
	mid := l + (r-l)/2
	return merge(mergesort(nums, l, mid), mergesort(nums, mid+1, r))
}

func merge(left, right []int) []int {
	m, n := len(left), len(right)
	res := make([]int, m+n, m+n)
	i, j := 0, 0
	for k := 0; k < m+n; k++ {
		if i == m {
			res[k] = right[j]
			j += 1
		} else if j == n {
			res[k] = left[i]
			i += 1
		} else if left[i] < right[j] {
			res[k] = left[i]
			i += 1
		} else {
			res[k] = right[j]
			j += 1
		}
	}
	return res
}

func shellsort(nums []int) []int {
	n := len(nums)

	// insertion sort with variant gap
	// start with a gap, then reduce it
	gap := n / 2
	for gap > 0 {
		for i := gap; i < n; i += 1 {
			curr := nums[i]
			j := i - gap
			for j >= 0 && nums[j] > curr {
				nums[j+gap] = nums[j]
				j -= gap
			}
			nums[j+gap] = curr
		}

		gap /= 2
	}
	return nums
}
