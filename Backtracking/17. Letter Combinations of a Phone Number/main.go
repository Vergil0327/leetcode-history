// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
package main

/*
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
*/

var PHONEPAD = map[rune][]string{
	'2': {"a", "b", "c"},
	'3': {"d", "e", "f"},
	'4': {"g", "h", "i"},
	'5': {"j", "k", "l"},
	'6': {"m", "n", "o"},
	'7': {"p", "q", "r", "s"},
	'8': {"t", "u", "v"},
	'9': {"w", "x", "y", "z"},
}

func letterCombinations(digits string) []string {
	solutions := []string{}

	lettersGroup := [][]string{}
	for _, digit := range digits {
		lettersGroup = append(lettersGroup, PHONEPAD[digit])
	}

	var dfs func(state string, lettersGroup [][]string, i int)
	dfs = func(state string, lettersGroup [][]string, i int) {
		// !!! without this edge case: if len(lettersGroup) == 0 return
		// ! digits == ""
		// ! output: [""]
		// ! expected: []
		if len(lettersGroup) == 0 {
			return
		}

		if len(state) >= len(lettersGroup) && state != "" {
			solutions = append(solutions, state)
			return
		}

		for _, letter := range lettersGroup[i] {
			state += letter
			dfs(state, lettersGroup, i+1)
			state = state[:len(state)-1]
		}
	}
	dfs("", lettersGroup, 0)

	return solutions
}

// explanation: https://www.youtube.com/watch?v=0snEunUacZY
func letterCombinationsBetter(digits string) []string {
	solutions := []string{}

	var backtracking func(state string, i int)
	backtracking = func(state string, i int) {
		if len(state) == len(digits) {
			solutions = append(solutions, state)
			return
		}

		for _, c := range PHONEPAD[rune(digits[i])] {
			backtracking(state+c, i+1)
		}
	}

	// Handle Edge Case
	// input: digits: ""
	// expected: [] instead of [""] (base case)
	if len(digits) > 0 {
		backtracking("", 0)
	}

	return solutions
}
