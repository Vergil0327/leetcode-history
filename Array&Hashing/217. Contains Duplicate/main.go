package main

func containsDuplicateBetter(nums []int) bool {
	mCount := map[int]int{}

	for _, num := range nums {
		_, ok := mCount[num]
		if ok {
			return true
		} else {
			mCount[num] = 1
		}
	}

	return false
}

func containsDuplicate(nums []int) bool {
	mCount := map[int]int{}

	for _, num := range nums {
		_, ok := mCount[num]
		if ok {
			mCount[num] += 1
		} else {
			mCount[num] = 1
		}
	}

	for _, num := range nums {
		count := mCount[num]
		if count >= 2 {
			return true
		}
	}
	return false
}
