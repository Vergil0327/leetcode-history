package main

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

type Node struct {
	value int
	min   int
}

type MinStack struct {
	items []*Node
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	if len(this.items) < 1 {
		this.items = append(this.items, &Node{value: val, min: val})
	} else {
		if min := this.items[len(this.items)-1].min; val < min {
			this.items = append(this.items, &Node{value: val, min: val})
		} else {
			this.items = append(this.items, &Node{value: val, min: min})
		}
	}
}

func (this *MinStack) Pop() {
	this.items = this.items[:len(this.items)-1]
}

func (this *MinStack) Top() int {
	return this.items[len(this.items)-1].value
}

func (this *MinStack) GetMin() int {
	return this.items[len(this.items)-1].min
}

type MinStackBetter struct {
	arr    []int
	minArr []int
}

/** initialize your data structure here. */
func ConstructorBetter() MinStackBetter {
	return MinStackBetter{}
}

func (this *MinStackBetter) Push(val int) {
	if len(this.minArr) == 0 || this.minArr[len(this.minArr)-1] >= val {
		this.minArr = append(this.minArr, val)
	}

	this.arr = append(this.arr, val)
}

func (this *MinStackBetter) Pop() {
	last := this.arr[len(this.arr)-1]

	if this.minArr[len(this.minArr)-1] == last {
		this.minArr = this.minArr[:len(this.minArr)-1]
	}
	this.arr = this.arr[:len(this.arr)-1]
}

func (this *MinStackBetter) Top() int {
	return this.arr[len(this.arr)-1]
}

func (this *MinStackBetter) GetMin() int {
	return this.minArr[len(this.minArr)-1]
}
