package main

// 2, 7, 11, 15, target:9
// T:O(n^2)
func twoSum(numbers []int, target int) []int {
	i := 0
	for i < len(numbers) {
		search := target - numbers[i]

		j := i + 1
		for j < len(numbers) {
			if numbers[j] == search {
				return []int{i + 1, j + 1}
			}

			j += 1
		}
		i += 1
	}

	return nil
}

// 2, 7, 11, 15, target:9
// T:O(n), using sorted ascending array
// https://www.youtube.com/watch?v=cQ1Oz4ckceM
func twoSumBetter(numbers []int, target int) []int {
	i, j := 0, len(numbers)-1

	for i < j {
		if numbers[i]+numbers[j] > target {
			j -= 1
		}
		if numbers[i]+numbers[j] < target {
			i += 1
		}
		if numbers[i]+numbers[j] == target {
			return []int{i + 1, j + 1}
		}
	}

	return []int{i + 1, j + 1}
}
