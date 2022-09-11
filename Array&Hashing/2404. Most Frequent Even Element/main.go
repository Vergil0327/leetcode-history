// https://leetcode.com/contest/weekly-contest-310/problems/most-frequent-even-element/

package main

import "math"

func mostFrequentEvenConcise(nums []int) int {
	mFreq := map[int]int{}
	val, freq := math.MaxInt, 0

	for _, num := range nums {
		if num%2 == 0 {
			mFreq[num] += 1

			if f, ok := mFreq[num]; ok {
				if f > freq || (f == freq && num < val) {
					val = num
					freq = f
				}
			}
		}
	}

	if freq == 0 {
		return -1
	}
	return val
}

func mostFrequentEvenFirst(nums []int) int {
	m := map[int]int{}
	cnt := 0
	for _, num := range nums {
		if num%2 == 0 {
			cnt += 1
			m[num] += 1
		}
	}
	if cnt == 0 {
		return -1
	}

	max := 0
	for _, v := range m {
		if v > max {
			max = v
		}
	}

	key := math.MaxInt
	for k, v := range m {
		if v == max && k < key {
			key = k
		}
	}

	return key
}
