package main

type StockSpanner struct {
	stack [][]int // [price, span]
}

func Constructor() StockSpanner {
	return StockSpanner{stack: make([][]int, 0)}
}

// [100,1] [80,1] [60,1]
// [100,1] [80,1] [70,2]
// [100,1] [80,1] [70,2] [60,1]
// [100,1] [80,1] [70,2] [60,1] [75, span]
// price=75, span=1+1+2
// worst case: O(n), amortized O(1)
func (this *StockSpanner) Next(price int) int {
	span := 1

	for len(this.stack) > 0 && this.stack[len(this.stack)-1][0] <= price {
		span += this.stack[len(this.stack)-1][1]
		this.stack = this.stack[:len(this.stack)-1]
	}

	this.stack = append(this.stack, []int{price, span})
	return span
}

/**
* Your StockSpanner object will be instantiated and called as such:
* obj := Constructor();
* param_1 := obj.Next(price);
 */
