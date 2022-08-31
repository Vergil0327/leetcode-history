// https://leetcode.com/problems/permutations-ii/
package main

// Input:
// [1,1,2]
// Expected:
// [[1,1,2],[1,2,1],[2,1,1]]

// Input:
// [1,3,2]
// Expected:
// [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

//  1					1				2
// 1, 2			1   2    1  1
// 2, 1     2   1    1  1
// -- remove duplicate --
//  1					X				2
// 1, 2			X   X    1  X
// 2, 1     X   X    1  X

// A key insight to avoid generating any redundant permutation is that at each step rather than viewing each number as a candidate, we consider each unique number as the true candidate.
// For instance, at the very beginning, given in the input of [1, 1, 2], we have only two true candidates instead of three.

func permuteUnique(nums []int) [][]int {
	solutions := [][]int{}

	selected := make(map[int]int)
	for _, num := range nums {
		selected[num] += 1
	}

	var dfs func(state []int)
	dfs = func(state []int) {
		if len(state) == len(nums) {
			cpy := make([]int, len(state))
			copy(cpy, state)
			solutions = append(solutions, cpy)
			return
		}

		for num := range selected {
			if selected[num] <= 0 {
				continue
			}

			state = append(state, num)
			selected[num] -= 1
			dfs(state)
			state = state[:len(state)-1]
			selected[num] += 1
		}
	}

	dfs([]int{})
	return solutions
}
