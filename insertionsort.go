package leetcode

// 在長度小於大概24~36左右時，排序較quicksort快
// golang則是選定24
func insertionSort(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		j := i
		for j > 0 {
			if nums[j-1] > nums[j] {
				nums[j-1], nums[j] = nums[j], nums[j-1]
			}
			j -= 1
		}
	}
	return nums
}
