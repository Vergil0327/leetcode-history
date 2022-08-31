// https://leetcode.com/problems/subsets-ii/
package main

import (
	"sort"
)

/*
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

    []                  [1]
 []   [2] 		        []   [2]
[][2] [][2]		      [][2]  [][2]
----------- remove duplicate -------------
    []                  [1]
 []   [2] 		        []   [2]
[]   [][2]		       []   [][2]


Example 2:
Input: nums = [0]
Output: [[],[0]]
*/

// explanation: https://www.youtube.com/watch?v=Vn2v6ajA7U0
// another approch P(m, n) m取n: https://www.youtube.com/watch?v=-tCHAdfDYDE
func subsetsWithDup(nums []int) [][]int {
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })

	solutions := [][]int{}
	state := []int{}

	var dfs func(state []int, start int)
	dfs = func(state []int, start int) {
		if start == len(nums) {
			cpy := make([]int, len(state))
			copy(cpy, state)
			solutions = append(solutions, cpy)
			return
		}

		// all subsets include current one
		state = append(state, nums[start])
		dfs(state, start+1)
		state = state[:len(state)-1]

		// all subsets not include current one
		for start+1 < len(nums) && nums[start] == nums[start+1] {
			start += 1
		}
		dfs(state, start+1)
	}

	dfs(state, 0)
	return solutions
}
