package main

// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
// You must write an algorithm that runs in O(n) time.
// T:O(n^2)
func longestConsecutive(nums []int) int {
	m := map[int]int{}

	result := 0
	for _, num := range nums {
		curr, j, k := 1, 1, 1
		m[num] = 1

		for _, ok := m[num+j]; ok; _, ok = m[num+j] {
			curr += 1
			j += 1
		}

		for _, ok := m[num-k]; ok; _, ok = m[num-k] {
			curr += 1
			k += 1
		}

		if curr > result {
			result = curr
		}
	}

	return result
}

// https://www.youtube.com/watch?v=P6RZZMu_maU
// T: O(n) M: O(n)
func longestConsecutiveBetter(nums []int) int {
	m := map[int]interface{}{}
	for _, num := range nums {
		m[num] = struct{}{}
	}

	result := 0
	for _, num := range nums {
		// check if num is beginning of sequence
		currLen := 0
		if _, ok := m[num-1]; !ok {
			currLen = 1
			for _, ok := m[num+currLen]; ok; _, ok = m[num+currLen] {
				currLen += 1
			}

			// or result = int(math.Max(float64(result), float64(currLen)))
			if currLen > result {
				result = currLen
			}
		}
	}

	return result
}
