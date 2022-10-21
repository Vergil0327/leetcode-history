package main

import "math"

// see 2104. sum of subarray range
// sum of subarray's min = sum of arr[i]*(count of subarray when arr[i] is min) at each i
// => we can find prevSmaller[i] and nextSmallerOrEqal[i]
// => sum of subarray min = sum of (nextSmallerOrEqual[i]-prevSmaller[i]) * arr[i]
//
// we can even use some tricks to calculate sum of subarray min in one pass
// => we add math.MinInt as boundary to make sure we'll pop out every item in stack,
// since we'll calculate sum of subarray's min at nested for-loop
// Also, we can get rid of index-out-of-bound error since first math.MinInt will never be pop out. => len(stack) always > 0 => always has left boundary
// sum of subarray's min = sum of (arr[i] * every subarray which contains arr[i] as min)
// Explanation: https://www.youtube.com/watch?v=TZyBPy7iOAw
func sumSubarrayMins(arr []int) int {
	const mod int = 1e9 + 7

	sum := 0

	arrMin := append([]int{math.MinInt}, arr...)
	arrMin = append(arrMin, math.MinInt)
	stack := []int{}
	for i := range arrMin {
		for len(stack) > 0 && arrMin[stack[len(stack)-1]] > arrMin[i] {
			index := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			l, r := stack[len(stack)-1], i
			min := (index - l) * (r - index) * arrMin[index]
			sum += min
		}
		stack = append(stack, i)
	}

	return sum % mod
}

func sumSubarrayMinsBruteForce(arr []int) int {
	const mod int = 1e9 + 7

	sum := 0
	for i := range arr {
		minVal := math.MaxInt
		for j := i; j < len(arr); j++ {
			minVal = min(minVal, arr[j])
			sum += minVal
		}
	}

	return sum % mod
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
