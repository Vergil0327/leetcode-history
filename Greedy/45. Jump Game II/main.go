// https://leetcode.com/problems/jump-game-ii/
package main

import "math"

// https://www.youtube.com/watch?v=dJ7sWiOoK7g
// BFS actually
func jump(nums []int) int {
	res := 0
	l, r := 0, 0

	for r < len(nums)-1 {
		farthest := 0
		for i := l; i < r+1; i++ {
			farthest = int(math.Max(float64(farthest), float64(i+nums[i])))
		}
		l = r + 1
		r = farthest
		res += 1
	}

	return res
}

// [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
func jumpSecondTry(nums []int) int {
	pos, times := 0, 0
	farthest := 0
	nextFarthest := 0
	for farthest < len(nums)-1 {
		nextFarthest = int(math.Max(float64(nextFarthest), float64(pos+nums[pos])))
		if pos == farthest {
			times += 1
			farthest = nextFarthest
		}
		pos += 1
	}

	return times
}

// [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
func jumpFirstTry(nums []int) int {
	pos, times := 0, 0
	farthest := pos + nums[pos]
	nextFarthest := farthest
	for farthest < len(nums)-1 {
		pos += 1
		nextFarthest = int(math.Max(float64(nextFarthest), float64(pos+nums[pos])))
		if pos == farthest {
			times += 1
			farthest = nextFarthest
		}
	}

	return times
}
