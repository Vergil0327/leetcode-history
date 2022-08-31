// https://leetcode.com/problems/detect-squares/
package main

import "math"

/**
 * Your DetectSquares object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(point);
 * param_2 := obj.Count(point);
 */

// Explanation: https://www.youtube.com/watch?v=bahebearrDc
type DetectSquares struct {
	count  map[[2]int]int
	points [][]int
}

func Constructor() DetectSquares {
	return DetectSquares{
		count:  map[[2]int]int{},
		points: make([][]int, 0),
	}
}

func (this *DetectSquares) Add(point []int) {
	this.count[[2]int{point[0], point[1]}] += 1
	this.points = append(this.points, point)
}

// ["DetectSquares","add","add","add","count","count","add","count"]
// [[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]]
// 找出對角即可同步找出另外兩點
// !!! 注意Edge Case: px,x 跟 py,y 不可是重合的
func (this *DetectSquares) Count(point []int) int {
	x, y := point[0], point[1]
	res := 0
	for _, p := range this.points {
		px, py := p[0], p[1]
		if math.Abs(float64(px-x)) != math.Abs(float64(py-y)) || px == x || py == y {
			continue
		}

		res += this.count[[2]int{px, y}] * this.count[[2]int{x, py}]
	}
	return res
}
