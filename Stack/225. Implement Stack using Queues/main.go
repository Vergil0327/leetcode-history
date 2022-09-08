// https://leetcode.com/problems/implement-stack-using-queues/
package main

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */

/* Follow-up: Can you implement the stack using only one queue? */

type MyStack struct {
	top int
	q   []int
}

func Constructor() MyStack {
	stack := MyStack{q: make([]int, 0)}
	return stack
}

// T:O(1)
func (this *MyStack) Push(x int) {
	this.q = append(this.q, x)
	this.top = x
}

// T:O(n)
func (this *MyStack) Pop() int {
	length := len(this.q)
	for i := 0; i < length-1; i++ {
		item := this.q[0]
		this.q = this.q[1:]
		this.q = append(this.q, item)
		this.top = item
	}
	pop := this.q[0]
	this.q = this.q[1:]
	return pop
}

// T:O(1)
func (this *MyStack) Top() int {
	return this.top
}

// T:O(1)
func (this *MyStack) Empty() bool {
	return len(this.q) == 0
}

/* type MyStack struct {
	top     int
	q1      []int
	q2      []int
	current *[]int
	empty   *[]int
}

func Constructor() MyStack {
	stack := MyStack{q1: make([]int, 0), q2: make([]int, 0)}
	stack.current = &stack.q1
	stack.empty = &stack.q2
	return stack
}

func (this *MyStack) Push(x int) {
	*this.current = append(*this.current, x)
	this.top = x
}

func (this *MyStack) Pop() int {
	for len(*this.current) > 1 {
		old := *this.current
		item := old[0]
		*this.current = old[1:]
		*this.empty = append(*this.empty, item)
		this.top = item
	}
	pop := (*this.current)[0]
	*this.current = make([]int, 0)
	this.current, this.empty = this.empty, this.current
	return pop
}

func (this *MyStack) Top() int {
	return this.top
}

func (this *MyStack) Empty() bool {
	return len(*this.current) == 0
}
*/
