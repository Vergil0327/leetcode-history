// https://leetcode.com/problems/permutations/
package main

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
