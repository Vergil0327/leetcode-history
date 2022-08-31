package main

import (
	"sort"
)

func topKFrequent(nums []int, k int) []int {
	// T:O(n)
	m := map[int]int{}
	for _, num := range nums {
		m[num] += 1
	}

	// T:O(n)
	// the largest k == len(nums)
	list := [][2]int{} // [num, k]
	for num, freq := range m {
		list = append(list, [2]int{num, freq})
	}

	// T:O(N LogN)
	sort.Slice(list, func(i, j int) bool {
		return list[i][1] > list[j][1]
	})

	// T:O(k)
	result := []int{}
	for i := 0; i < k; i++ {
		result = append(result, list[i][0])
	}

	return result
}

// T:O(n)
// https://www.youtube.com/watch?v=YPTqKIgVk-k
func topKFrequentBetter(nums []int, k int) []int {
	// T:O(n)
	m := map[int]int{}
	for _, num := range nums {
		m[num] += 1
	}

	// the largest k == len(nums)
	// T:O(n)
	bucket := make([][]int, len(nums)+1)
	for num, freq := range m {
		bucket[freq] = append(bucket[freq], num)
	}

	result := []int{}
	for i := len(bucket) - 1; i >= 0; i-- {
		result = append(result, bucket[i]...)
	}
	return result[:k]
}

// T:O(n)
// https://www.youtube.com/watch?v=YPTqKIgVk-k
func topKFrequentBest(nums []int, k int) []int {
	// T:O(n)
	m := map[int]int{}
	for _, num := range nums {
		m[num] += 1
	}

	// the largest k == len(nums)
	// T:O(n)
	bucket := make([][]int, len(nums)+1)
	for num, freq := range m {
		bucket[freq] = append(bucket[freq], num)
	}

	result := []int{}
	for i := len(bucket) - 1; i >= 0; i-- {
		for _, item := range bucket[i] {
			result = append(result, item)
			if len(result) == k {
				return result
			}
		}
	}
	return result
}
