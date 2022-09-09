// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/max-stack/
package main

type MaxStack struct {
	values   []int
	maximums []int
}

func New() MaxStack {
	return MaxStack{values: make([]int, 0), maximums: make([]int, 0)}
}

// T:O(1)
func (stk *MaxStack) Push(x int) {
	if len(stk.maximums) == 0 || x >= stk.maximums[len(stk.maximums)-1] {
		stk.maximums = append(stk.maximums, x)
	}

	stk.values = append(stk.values, x)
}

// T:O(1)
func (stk *MaxStack) Pop() int {
	val := stk.values[len(stk.values)-1]
	stk.values = stk.values[:len(stk.values)-1]
	if val == stk.maximums[len(stk.maximums)-1] {
		stk.maximums = stk.maximums[:len(stk.maximums)-1]
	}

	return val
}

// T:O(1)
func (stk *MaxStack) Top() int {
	return stk.values[len(stk.values)-1]
}

// T:O(1)
func (stk *MaxStack) PeekMax() int {
	return stk.maximums[len(stk.maximums)-1]
}

// T:O(n)
func (stk *MaxStack) PopMax() int {
	val := stk.maximums[len(stk.maximums)-1]
	stk.maximums = stk.maximums[:len(stk.maximums)-1]

	for i := len(stk.values) - 1; i >= 0; i-- {
		if stk.values[i] == val {
			stk.values = append(stk.values[:i], stk.values[i+1:]...)
			break
		}
	}

	return val
}
