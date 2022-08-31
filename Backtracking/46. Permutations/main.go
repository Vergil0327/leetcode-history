// https://leetcode.com/problems/permutations/
package main

// Example 1:
// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
//  1         2         3
// 2, 3			 1, 3		 	 1, 2
// 3,  2    3 ,  1 		2			1

// Example 2:
// Input: nums = [0,1]
// Output: [[0,1],[1,0]]

// Example 3:
// Input: nums = [1]
// Output: [[1]]

// https://www.youtube.com/watch?v=s7AvT7cGdSo
// https://www.youtube.com/watch?v=CUzm-buvH_8&t=479s
func permute(nums []int) [][]int {
	solutions := [][]int{}

	visited := map[int]bool{}
	var dfs func(state []int)
	dfs = func(state []int) {
		if len(state) == len(nums) {
			cpy := make([]int, len(state))
			copy(cpy, state)
			solutions = append(solutions, cpy)
			return
		}

		for _, num := range nums {
			if visited[num] {
				continue
			}

			visited[num] = true
			state = append(state, num)
			dfs(state)
			state = state[:len(state)-1]
			visited[num] = false
		}
	}

	state := []int{}
	dfs(state)

	return solutions
}
