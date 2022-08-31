// https://leetcode.com/problems/word-search/
package main

import "fmt"

/*
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
*/

// [["A","B","C","E"],
//  ["S","F","C","S"],
//  ["A","D","E","E"]]
// word: "ABCB"
// Expected: false

// [["C","A","A"],
//  ["A","A","A"],
//  ["B","C","D"]]
// "AAB"
// true

// Success
// Details
// Runtime: 2437 ms, faster than 5.09% of Go online submissions for Word Search.
// Memory Usage: 7.7 MB, less than 8.13% of Go online submissions for Word Search.
// T:O(m*n*4dfs) = O(m*n*4^dfs-height), dfs-height will be L which L is len(word) because dfs will run through every characters in word
// 							 = O(mn*4^L)
func exist(board [][]byte, word string) bool {
	visited := map[string]bool{}

	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[0]); col++ {
			if explore(board, word, row, col, visited) {
				return true
			}
		}
	}

	return false
}

func explore(board [][]byte, word string, row, col int, visited map[string]bool) bool {
	if len(word) == 0 {
		return true
	}

	rowInBounds := row >= 0 && row < len(board)
	colInBounds := col >= 0 && col < len(board[0])
	if !rowInBounds || !colInBounds {
		return false
	}

	letter := word[0]
	word = word[1:]
	if board[row][col] != letter {
		return false
	}

	key := fmt.Sprintf("%d,%d", row, col)
	if visited[key] {
		return false
	}

	visited[key] = true

	didExist := explore(board, word, row-1, col, visited)
	visited[key] = false
	if didExist {
		return true
	}

	visited[key] = true
	didExist = explore(board, word, row+1, col, visited)
	if didExist {
		return true
	}
	visited[key] = false

	visited[key] = true
	didExist = explore(board, word, row, col-1, visited)
	if didExist {
		return true
	}
	visited[key] = false

	visited[key] = true
	didExist = explore(board, word, row, col+1, visited)
	visited[key] = false

	return didExist
}

func exploreCompact(board [][]byte, word string, row, col int, visited map[string]bool) bool {
	if len(word) == 0 {
		return true
	}

	rowInBounds := row >= 0 && row < len(board)
	colInBounds := col >= 0 && col < len(board[0])
	if !rowInBounds || !colInBounds {
		return false
	}

	letter := word[0]
	word = word[1:]
	if board[row][col] != letter {
		return false
	}

	key := fmt.Sprintf("%d,%d", row, col)
	if visited[key] {
		return false
	}

	visited[key] = true

	didExist := explore(board, word, row-1, col, visited) ||
		explore(board, word, row+1, col, visited) ||
		explore(board, word, row, col-1, visited) ||
		explore(board, word, row, col+1, visited)

	visited[key] = false

	return didExist
}
