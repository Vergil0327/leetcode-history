// https://leetcode.com/problems/subsets/
package main

/* Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

subset [1, []], [2, []], [3, []] -> 三選一 -> 剩下二選一 -> 最後一組
empty still a subset

1: choose 1 or [] -> [1], []
2: choose 2 or [] -> [1, 2], [1, []], [[], 2], [[], []]
3. choose 3 or [] -> [1, 2, 3], [1, 2, []], [1, [], 3], [1, [], []], [[], 2, 3], [[], 2, []], [[], [], 3], [[], [], []]
*/

// T:O(n2^n)
// Explanation: https://www.youtube.com/watch?v=CUzm-buvH_8
// Explanation: https://www.youtube.com/watch?v=REOH22Xwdkk
func subsets(nums []int) [][]int {
	solutions := [][]int{}
	state := []int{}
	index := 0
	dfs(state, &solutions, nums, index)

	return solutions
}

func dfs(state []int, solutions *[][]int, nums []int, idx int) {
	if idx >= len(nums) {
		// !!! state will be modified so we need to copy it
		// slice[:] -> Slicing does not copy the slice's data.
		// It creates a new slice value that points to the original array.
		// This makes slice operations as efficient as manipulating array indices.
		// Therefore, modifying the elements (not the slice itself) of a re-slice modifies the elements of the original slice

		cpy := make([]int, len(state))
		copy(cpy, state)
		*solutions = append(*solutions, cpy)
		return
	}

	// choose nums[idx]
	state = append(state, nums[idx])
	dfs(state, solutions, nums, idx+1)

	// choose not to include nums[idx]
	state = state[:len(state)-1]
	dfs(state, solutions, nums, idx+1)
}

// C3取0+C3取1+C3取2+C3取3
func subsets2(nums []int) [][]int {
	solutions := [][]int{}

	var dfs func(n, start int, curr []int)
	dfs = func(n, start int, curr []int) {
		if n == len(curr) {
			cpy := make([]int, len(curr))
			copy(cpy, curr)
			solutions = append(solutions, cpy)
			return
		}

		for i := start; i < len(nums); i++ {
			curr = append(curr, nums[i])
			dfs(n, i+1, curr)
			curr = curr[:len(curr)-1]
		}
	}

	// C(m, n)
	for i := 0; i < len(nums)+1; i++ {
		dfs(i, 0, []int{})
	}

	return solutions
}
