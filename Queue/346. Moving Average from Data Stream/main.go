// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/moving-average-from-data-stream/
package main

/*
Example 1:
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
*/

type MovingAverage struct {
	sum  int
	q    []int
	size int
}

func New(size int) MovingAverage {
	return MovingAverage{size: size, q: make([]int, 0)}
}

func (this MovingAverage) Next(num int) float64 {
	if this.size == 0 {
		return 0
	}

	this.q = append(this.q, num)
	this.sum += num
	if len(this.q) > this.size {
		this.sum -= this.q[0]
		this.q = this.q[1:]
	}

	return float64(this.sum) / float64(len(this.q))
}
