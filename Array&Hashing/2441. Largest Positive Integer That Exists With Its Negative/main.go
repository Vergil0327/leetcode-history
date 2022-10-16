package main

func findMaxK(nums []int) int {
	maxVal := -1
	set := map[int]bool{}
	for _, num := range nums {
		if _, ok := set[-num]; ok {
			if v := abs(num); v > maxVal {
				maxVal = v
			}
		}

		set[num] = true
	}

	return maxVal
}

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}
