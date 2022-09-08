// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/zigzag-iterator/

package main

/*
Example1
Input: v1 = [1, 2] and v2 = [3, 4, 5, 6]
Output: [1, 3, 2, 4, 5, 6]
Explanation:
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
*/

type ZigzagIterator struct {
	q *[][]int
}

func New(list1, list2 []int) ZigzagIterator {
	q := [][]int{}
	for _, list := range [][]int{list1, list2} {
		if len(list) > 0 {
			q = append(q, list)
		}
	}

	return ZigzagIterator{q: &q}
}

func (iter ZigzagIterator) HasNext() bool {
	return len(*iter.q) > 0
}

func (iter ZigzagIterator) Next() int {
	old := *iter.q
	list := old[0]
	*iter.q = old[1:]

	num := list[0]
	list = list[1:]

	if len(list) != 0 {
		*iter.q = append(*iter.q, list)
	}

	return num
}

// func ZigzagIterator(list1, list2 []int) []int {
// 	res := []int{}
// 	queue := [][]int{list1, list2}

// 	for len(queue) > 0 {
// 		for _, list := range queue {
// 			queue = queue[1:]

// 			num := list[0]
// 			list = list[1:]
// 			res = append(res, num)

// 			if len(list) != 0 {
// 				queue = append(queue, list)
// 			}
// 		}
// 	}

// 	return res
// }
