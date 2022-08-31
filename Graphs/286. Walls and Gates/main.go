package main

import (
	"fmt"
	"math"
)

const WALL int = -1
const GATE int = 0
const ROOM int = math.MaxInt

func WallAndGates(rooms [][]int) {
	ROWS, COLS := len(rooms), len(rooms[0])
	visited := map[string]bool{}
	queue := [][]int{}
	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if rooms[r][c] == GATE {
				queue = append(queue, []int{r, c})
				visited[fmt.Sprintf("%d,%d", r, c)] = true
			}
		}
	}

	dist := 0
	directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(queue) > 0 {
		for _, room := range queue {
			r, c := room[0], room[1]
			queue = queue[1:]
			rooms[r][c] = dist

			for _, direction := range directions {
				dr, dc := direction[0], direction[1]
				row, col := r+dr, c+dc

				rowInBounds := row >= 0 && row < ROWS
				colInBounds := col >= 0 && col < COLS
				if !rowInBounds || !colInBounds {
					continue
				}

				if rooms[row][col] == WALL {
					continue
				}

				if visited[fmt.Sprintf("%d,%d", row, col)] {
					continue
				}

				visited[fmt.Sprintf("%d,%d", r, c)] = true
				queue = append(queue, []int{row, col})
			}
		}
		dist += 1
	}
}
