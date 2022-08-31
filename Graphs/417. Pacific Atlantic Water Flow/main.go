// https://leetcode.com/problems/pacific-atlantic-water-flow/
package main

import (
	"fmt"
)

/*
Example 1:
Input: heights = [[1,2,2,3,5],
									[3,2,3,4,4],
									[2,4,5,3,1],
									[6,7,1,4,5],
									[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
*/

/*
P  P,P,P,P,P  A
P[[1,2,2,3,5],A
P [3,2,3,4,4],A
P [2,4,5,3,1],A
P [6,7,1,4,5],A
P [5,1,1,2,4]]A
A  A,A,A,A,A  A

Pacific: row < 0 || col < 0
Atlantic: row >= len(grid) || col >= len(grid[0])

[[1,2,3],
 [8,9,4],
 [7,6,5]]
*/

type any = interface{}

func genVisitedKey(r, c int) string {
	return fmt.Sprintf("%d,%d", r, c)
}

/*
Explanation: https://www.youtube.com/watch?v=s-VkcjHqkGI
反向思考:
第一排跟第一列能流向Pacific
最後一排跟最後一列能流向Atalantic
反找回去哪些高處能流向這幾個地方
然後找出交集的位置即是我們要的

似乎無法從每個Cell往四個方向找能流向Atalantic Ocean或Pacific Ocean
T:O(m*n)
*/
func pacificAtlantic(heights [][]int) [][]int {
	canFlow := [][]int{}
	pac := map[string]any{}
	atl := map[string]any{}

	ROWS, COLS := len(heights), len(heights[0])

	for r := 0; r < ROWS; r++ {
		dfs(heights, r, 0, heights[r][0], pac)
		dfs(heights, r, COLS-1, heights[r][COLS-1], atl)
	}

	for c := 0; c < COLS; c++ {
		dfs(heights, 0, c, heights[0][c], pac)
		dfs(heights, ROWS-1, c, heights[ROWS-1][c], atl)
	}

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			curr := genVisitedKey(r, c)

			if _, ok := pac[curr]; ok {
				if _, ok := atl[curr]; ok {
					canFlow = append(canFlow, []int{r, c})
				}
			}
		}
	}

	return canFlow
}

func dfs(heights [][]int, r, c, prevHeight int, visited map[string]any) {
	rowInBounds := r >= 0 && r < len(heights)
	colInBounds := c >= 0 && c < len(heights[0])
	if !rowInBounds || !colInBounds {
		return
	}

	if heights[r][c] < prevHeight {
		return
	}

	key := genVisitedKey(r, c)
	if _, ok := visited[key]; ok {
		return
	}

	visited[key] = struct{}{}

	dfs(heights, r+1, c, heights[r][c], visited)
	dfs(heights, r-1, c, heights[r][c], visited)
	dfs(heights, r, c+1, heights[r][c], visited)
	dfs(heights, r, c-1, heights[r][c], visited)
}
