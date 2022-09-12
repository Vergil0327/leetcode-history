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
// 1,2,3,4 ... 100 ... 200
// check if num is the beginning of sequence
// -> YES: check if next one exists in our set
// -> NO: next one
// visit each num twice at most, T:O(n) M:O(n)
//
// Analysis:
// Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer inspection reveals it to be linear.
// Because the while loop is reached only when currentNum marks the beginning of a sequence (i.e. currentNum-1 is not present in nums), the while loop can only run for nn iterations throughout the entire runtime of the algorithm.
// This means that despite looking like O(n⋅n) complexity, the nested loops actually run in O(n + n) = O(n) time. All other computations occur in constant time, so the overall runtime is linear.
// think:
// 		if all the numbers are discrete, iteration is n
// 		if all belong to one sequence, iteration is still n
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
