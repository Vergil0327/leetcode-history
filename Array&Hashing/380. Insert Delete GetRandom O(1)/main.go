// https://leetcode.com/problems/insert-delete-getrandom-o1/

package main

import (
	"math/rand"
)

// leetcode: https://www.youtube.com/watch?v=j4KwhBziOpg

type RandomizedSet struct {
	m    map[int]int // store array index
	list []int
}

func Constructor() RandomizedSet {
	return RandomizedSet{m: make(map[int]int), list: make([]int, 0)}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.m[val]; ok {
		return false
	}

	this.list = append(this.list, val)
	this.m[val] = len(this.list) - 1
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	if idx, ok := this.m[val]; ok {
		// swap with last one
		lastIdx := len(this.list) - 1
		this.list[idx], this.list[lastIdx] = this.list[lastIdx], this.list[idx]
		this.m[this.list[idx]] = idx

		// remove val
		delete(this.m, val)
		this.list = this.list[:lastIdx]
		return true
	}

	return false
}

func (this *RandomizedSet) GetRandom() int {
	idx := int(rand.Int31n(int32(len(this.list))))
	return this.list[idx]
}
