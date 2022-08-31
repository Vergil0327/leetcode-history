package main

import "fmt"

// [["5","3",".",".","7",".",".",".","."]
// ,["6",".",".","1","9","5",".",".","."]
// ,[".","9","8",".",".",".",".","6","."]
// ,["8",".",".",".","6",".",".",".","3"]
// ,["4",".",".","8",".","3",".",".","1"]
// ,["7",".",".",".","2",".",".",".","6"]
// ,[".","6",".",".",".",".","2","8","."]
// ,[".",".",".","4","1","9",".",".","5"]
// ,[".",".",".",".","8",".",".","7","9"]]
// T:O(n^2) (9^2)
func isValidSudoku(board [][]byte) bool {
	mGrid := make(map[byte]map[byte]bool, 9)
	mCol := make(map[byte]map[byte]bool, 9)

	for i, row := range board {
		mRow := map[byte]bool{}
		for j, str := range row {
			if str == '.' {
				continue
			}
			// check row
			if _, ok := mRow[str]; ok {
				return false
			}
			mRow[str] = true

			// check col
			if _, ok := mCol[byte(j)]; !ok {
				mCol[byte(j)] = map[byte]bool{}
			}
			m := mCol[byte(j)]
			if _, ok := m[str]; ok {
				return false
			}
			m[str] = true

			// check grid [i, j]
			// [0, 0] [0, 1] [0, 2] | [0, 3] [0, 4] [0, 5] | [0, 6] [0, 7] [0, 8]
			// [1, 0] [1, 1] [1, 2] | [1, 3] [1, 4] [1, 5] | [1, 6] [1, 7] [1, 8]
			// [2, 0] [2, 1] [2, 2] | [2, 3] [2, 4] [2, 5] | [2, 6] [2, 7] [2, 8]
			// ------------------------------------------------------------------
			// [3, 0] [3, 1] [3, 2] |
			// [4, 0] [4, 1] [4, 2] |
			// [5, 0] [5, 1] [5, 2] |
			// ------------------------------------------------------------------
			// [6, 0] [6, 1] [6, 2] |
			// [7, 0] [7, 1] [7, 2] |
			// [8, 0] [8, 1] [8, 2] |
			if i >= 0 && i < 3 {
				if j < 3 {
					if _, ok := mGrid[0]; !ok {
						mGrid[0] = map[byte]bool{}
					}
					m := mGrid[0]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
				if j >= 3 && j < 6 {
					if _, ok := mGrid[1]; !ok {
						mGrid[1] = map[byte]bool{}
					}
					m := mGrid[1]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
				if j >= 6 && j < 9 {
					if _, ok := mGrid[2]; !ok {
						mGrid[2] = map[byte]bool{}
					}
					m := mGrid[2]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
			}

			if i >= 3 && i < 6 {
				if j < 3 {
					if _, ok := mGrid[3]; !ok {
						mGrid[3] = map[byte]bool{}
					}
					m := mGrid[3]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
				if j >= 3 && j < 6 {
					if _, ok := mGrid[4]; !ok {
						mGrid[4] = map[byte]bool{}
					}
					m := mGrid[4]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
				if j >= 6 && j < 9 {
					if _, ok := mGrid[5]; !ok {
						mGrid[5] = map[byte]bool{}
					}
					m := mGrid[5]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
			}

			if i >= 6 && i < 9 {
				if j < 3 {
					if _, ok := mGrid[6]; !ok {
						mGrid[6] = map[byte]bool{}
					}
					m := mGrid[6]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
				if j >= 3 && j < 6 {
					if _, ok := mGrid[7]; !ok {
						mGrid[7] = map[byte]bool{}
					}
					m := mGrid[7]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
				if j >= 6 && j < 9 {
					if _, ok := mGrid[8]; !ok {
						mGrid[8] = map[byte]bool{}
					}
					m := mGrid[8]
					if _, ok := m[str]; ok {
						return false
					}
					m[str] = true
				}
			}
		}
	}

	return true
}

func isValidSudokuBetter(board [][]byte) bool {
	mRow := make(map[int]map[byte]bool, 9)
	mCol := make(map[int]map[byte]bool, 9)
	mGrid := make(map[string]map[byte]bool, 9)

	for r, row := range board {
		for c, str := range row {
			if str == '.' {
				continue
			}

			if mRow[r] == nil {
				mRow[r] = map[byte]bool{}
			}
			if _, ok := mRow[r][str]; ok {
				return false
			}

			if mCol[c] == nil {
				mCol[c] = map[byte]bool{}
			}
			if _, ok := mCol[c][str]; ok {
				return false
			}

			if mGrid[fmt.Sprintf("%d%d", r/3, c/3)] == nil {
				mGrid[fmt.Sprintf("%d%d", r/3, c/3)] = map[byte]bool{}
			}
			if _, ok := mGrid[fmt.Sprintf("%d%d", r/3, c/3)][str]; ok {
				return false
			}

			mRow[r][str] = true
			mCol[c][str] = true
			mGrid[fmt.Sprintf("%d%d", r/3, c/3)][str] = true
		}
	}

	return true
}
