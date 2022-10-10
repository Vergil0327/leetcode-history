package main

// Time complexity : O(k). k refers to the number of valid permutations.
// Space complexity : O(n). visited array of size n is used.
// The depth of recursion tree will also go upto nn. Here, nn refers to the given integer n.
func countArrangement(n int) int {
	candidates := []int{}
	for i := 1; i <= n; i++ {
		candidates = append(candidates, i)
	}

	res := 0
	visited := map[int]bool{}
	var dfs func(state []int)
	dfs = func(state []int) {
		if len(state) == n {
			res += 1
			return
		}

		for i := 0; i < len(candidates); i++ {
			if visited[candidates[i]] {
				continue
			}

			n := len(state)

			if candidates[i]%(n+1) == 0 || (n+1)%candidates[i] == 0 {
				visited[candidates[i]] = true
				dfs(append(state, candidates[i]))
				visited[candidates[i]] = false
			}
		}
	}
	dfs([]int{})

	return res
}
