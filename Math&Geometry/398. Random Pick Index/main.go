// https://leetcode.com/problems/random-pick-index/
package main

import "math/rand"

type HashmapSolution struct {
	m map[int][]int
}

func ConstructorHashmapSolution(nums []int) HashmapSolution {
	m := map[int][]int{}
	for i, num := range nums {
		m[num] = append(m[num], i)
	}
	return HashmapSolution{m: m}
}

// T:O(1)
func (this *HashmapSolution) Pick(target int) int {
	i := int(rand.Int31n(int32(len(this.m[target]))))
	return this.m[target][i]
}

// https://leetcode.com/problems/random-pick-index/discuss/88072/Simple-Reservoir-Sampling-solution
type Solution struct {
	nums []int
}

func Constructor(nums []int) Solution {
	return Solution{nums: nums}
}

// reservoir sampling technique
// 1*1/2*2/3*...*n-1/n = 1/n
//
// example: [1, 2, 3, 3, 3]
// Pick(3):
// i=2 probility: 1 * 1/2 * 2/3
// i=3 probility: 1/2 * 2/3
// i=4 probility: 1/3
// T:O(n)
func (this *Solution) Pick(target int) int {
	randSize := 1
	idx := -1
	for i := 0; i < len(this.nums); i++ {
		if this.nums[i] != target {
			continue
		}

		if rand.Int31n(int32(randSize)) == 0 {
			idx = i
		}
		randSize += 1
	}

	return idx
}
