package main

import "sort"

func makeSimilar(nums []int, target []int) int64 {
	sort.Ints(nums)
	sort.Ints(target)

	numOdd, numEvn := []int{}, []int{}
	tgtOdd, tgtEvn := []int{}, []int{}

	for i, num := range nums {
		if num&1 == 0 {
			numEvn = append(numEvn, num)
		} else {
			numOdd = append(numOdd, num)
		}

		if target[i]&1 == 0 {
			tgtEvn = append(tgtEvn, target[i])
		} else {
			tgtOdd = append(tgtOdd, target[i])
		}
	}

	ops := 0
	for i, num := range numEvn {
		ops += abs(num-tgtEvn[i]) / 2
	}
	for i, num := range numOdd {
		ops += abs(num-tgtOdd[i]) / 2
	}
	return int64(ops / 2)
}

func abs(num int) int {
	if num < 0 {
		return -num
	}

	return num
}
