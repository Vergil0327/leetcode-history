package main

import "math/rand"

// https://www.geeksforgeeks.org/reservoir-sampling/
func reservoirSampling(stream []int, k, n int) []int {
	i := 0
	reservoir := make([]int, k)

	for i < k {
		reservoir[i] = stream[i]
		i += 1
	}

	for i < n {
		j := int(rand.Int31n(int32(i + 1)))
		if j < k {
			reservoir[j] = stream[i]
		}

		i += 1
	}

	return reservoir
}
