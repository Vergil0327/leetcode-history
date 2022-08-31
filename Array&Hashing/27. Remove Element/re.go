package re

func removeElement(nums []int, val int) int {
	count := 0

	for i := 0; i < len(nums); i += 1 {
		el := nums[i]
		if el != val {
			nums[count] = el
			count += 1
		}
	}

	return count
}

func removeElementBetter(nums []int, val int) int {
	count := 0
	total := len(nums)

	for count < total {
		if nums[count] == val {
			nums[count] = nums[total-1]
			total -= 1
		} else {
			count += 1
		}
	}

	return count
}
