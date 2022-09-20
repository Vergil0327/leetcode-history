package main

// mock
func knows(i, j int) bool {
	graph := [][]int{
		{1, 1, 0},
		{0, 1, 0},
		{1, 1, 1},
	}
	// graph := [][]int{
	// 	{1, 0, 1},
	// 	{1, 1, 0},
	// 	{0, 1, 1},
	// }

	return graph[i][j] == 1
}

func findCelebritySolution(n int) int {
	candidate := 0
	for i := 1; i < n; i++ {
		if knows(candidate, i) {
			candidate = i
		}
	}

	for j := 0; j < n; j++ {
		if (j != candidate && knows(candidate, j)) || knows(j, candidate) {
			return -1
		}
	}

	return candidate
}

func findCelebrity(n int) int {
	l, r := 0, n-1
	for l < r {
		if knows(l, r) {
			l += 1
		} else if knows(r, l) {
			r -= 1
		} else {
			r += 1
		}
	}

	for i := 0; i < n; i++ {
		if (i != l && knows(l, i)) || !knows(i, l) {
			return -1
		}
	}

	return l
}
