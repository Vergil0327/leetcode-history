// https://leetcode.com/problems/implement-queue-using-stacks/
package main

type MyQueue struct {
	rev []int // reversed stack
	stk []int
}

func Constructor() MyQueue {
	return MyQueue{stk: make([]int, 0), rev: make([]int, 0)}
}

// T:O(1)
func (this *MyQueue) Push(x int) {
	if len(this.rev) == 0 {
		this.rev = append(this.rev, x)
	} else {
		this.stk = append(this.stk, x)
	}
}

// T:O(1) amortized
func (this *MyQueue) Pop() int {
	val := this.rev[len(this.rev)-1]
	this.rev = this.rev[:len(this.rev)-1]

	if len(this.rev) == 0 {
		for len(this.stk) > 0 {
			this.rev = append(this.rev, this.stk[len(this.stk)-1])
			this.stk = this.stk[:len(this.stk)-1]
		}
	}

	return val
}

// T:O(1)
func (this *MyQueue) Peek() int {
	return this.rev[len(this.rev)-1]
}

// T:O(1)
func (this *MyQueue) Empty() bool {
	return len(this.rev)+len(this.stk) == 0
}

/**
* Your MyQueue object will be instantiated and called as such:
* obj := Constructor();
* obj.Push(x);
* param_2 := obj.Pop();
* param_3 := obj.Peek();
* param_4 := obj.Empty();
 */
