package main

func twoSum(nums []int, target int) []int {
	if len(nums) == 2 {
		return []int{0, 1}
	}

	mTarget := map[int]int{}

	for i, num := range nums {
		if idx, ok := mTarget[num]; ok {
			return []int{idx, i}
		} else {
			mTarget[target-num] = i
		}
	}

	return []int{}
}
