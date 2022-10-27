package main

import "math"

func largestOverlap(img1 [][]int, img2 [][]int) int {
	N := len(img1)

	// find valid pixel
	pos1, pos2 := [][2]int{}, [][2]int{}
	for r := 0; r < N; r++ {
		for c := 0; c < N; c++ {
			if img1[r][c] == 1 {
				pos1 = append(pos1, [2]int{r, c})
			}
			if img2[r][c] == 1 {
				pos2 = append(pos2, [2]int{r, c})
			}
		}
	}

	// find vector
	vectorCount := map[[2]int]int{}
	for _, p1 := range pos1 {
		for _, p2 := range pos2 {
			r1, c1 := p1[0], p1[1]
			r2, c2 := p2[0], p2[1]

			// if we got same vector, it means if we shift vector to zero
			// those pixel with same vector will overlap with target img
			vectorCount[[2]int{r1 - r2, c1 - c2}] += 1
		}
	}

	maxV := math.MinInt
	for _, v := range vectorCount {
		if v > maxV {
			maxV = v
		}
	}

	if maxV == math.MinInt {
		return 0
	} else {
		return maxV
	}
}
