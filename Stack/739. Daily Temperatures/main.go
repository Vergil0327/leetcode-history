// https://leetcode.com/problems/daily-temperatures/
package main

/*
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
*/

// T:O(n)
func dailyTemperatures(temperatures []int) []int {
	result := []int{}
	for index, temp := range temperatures {
		for i := index; i < len(temperatures); i++ {
			if temperatures[i] > temp {
				result = append(result, i-index)
				break
			}
			if i == len(temperatures)-1 {
				result = append(result, 0)
			}
		}
	}

	return result
}

// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]
// If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.
// -> Monotonic Decreasing Stack

// https://www.youtube.com/watch?v=cTBiBSnjO3c
func dailyTemperaturesBetter(temperatures []int) []int {
	result := []int{}

	// initialize default value to 0
	for i := 0; i < len(temperatures); i++ {
		result = append(result, 0)
	}

	stack := []Item{}

	for i, t := range temperatures {
		for len(stack) > 0 && t > stack[len(stack)-1].Temp {
			popItem := pop(&stack)
			result[popItem.Index] = i - popItem.Index
		}
		stack = append(stack, Item{Temp: t, Index: i})
	}

	return result
}

type Item struct {
	Temp  int
	Index int
}

func pop(stack *[]Item) Item {
	length := len(*stack)
	popItem := (*stack)[length-1]
	*stack = (*stack)[:length-1]
	return popItem
}
