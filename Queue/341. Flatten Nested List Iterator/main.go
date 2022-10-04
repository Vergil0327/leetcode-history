package main

type NestedIterator struct {
	i    int
	nums []int
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	queue := []*NestedInteger{}
	for _, nest := range nestedList {
		queue = append(queue, nest)
	}

	res := []int{}
	for len(queue) > 0 {
		nested := queue[0]
		queue = queue[1:]

		if nested.IsInteger() {
			res = append(res, nested.GetInteger())
		} else if len(nested.GetList()) > 0 {
			queue = append(nested.GetList(), queue...)
		}
	}

	return &NestedIterator{nums: res}
}

func (this *NestedIterator) Next() int {
	nxt := this.nums[this.i]
	this.i += 1
	return nxt
}

func (this *NestedIterator) HasNext() bool {
	return this.i < len(this.nums)
}

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
type NestedInteger struct {
}

// Return true if this NestedInteger holds a single integer, rather than a nested list.
func (this NestedInteger) IsInteger() bool { return false }

// Return the single integer that this NestedInteger holds, if it holds a single integer
// The result is undefined if this NestedInteger holds a nested list
// So before calling this method, you should have a check
func (this NestedInteger) GetInteger() int { return 0 }

// Set this NestedInteger to hold a single integer.
func (n *NestedInteger) SetInteger(value int) {}

// Set this NestedInteger to hold a nested list and adds a nested integer to it.
func (this *NestedInteger) Add(elem NestedInteger) {}

// Return the nested list that this NestedInteger holds, if it holds a nested list
// The list length is zero if this NestedInteger holds a single integer
// You can access NestedInteger's List element directly if you want to modify it
func (this NestedInteger) GetList() []*NestedInteger { return nil }
