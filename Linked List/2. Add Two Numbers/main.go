// https://leetcode.com/problems/add-two-numbers/
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
*/

// Explanation: https://www.youtube.com/watch?v=wgFPrzTjm7s
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	iter1 := l1
	iter2 := l2
	iterResult := dummy
	carryNum := 0
	for iter1 != nil || iter2 != nil {
		var val int
		if iter1 != nil && iter2 != nil {
			val = iter1.Val + iter2.Val + carryNum
		} else if iter1 != nil {
			val = iter1.Val + carryNum
		} else {
			val = iter2.Val + carryNum
		}
		carryNum = 0

		if val >= 10 {
			carryNum = val / 10
			val = val % 10
		}

		iterResult.Next = &ListNode{Val: val}

		if iter1 != nil {
			iter1 = iter1.Next
		}
		if iter2 != nil {
			iter2 = iter2.Next
		}
		iterResult = iterResult.Next
	}

	if carryNum > 0 {
		iterResult.Next = &ListNode{Val: carryNum}
	}

	return dummy.Next
}

func addTwoNumbersBetter(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	iter1 := l1
	iter2 := l2
	iterResult := dummy
	carryNum := 0
	for iter1 != nil || iter2 != nil || carryNum != 0 {
		val, val1, val2 := 0, 0, 0
		if iter1 != nil {
			val1 = iter1.Val
		}
		if iter2 != nil {
			val2 = iter2.Val
		}
		val = val1 + val2 + carryNum

		carryNum = val / 10
		val = val % 10
		iterResult.Next = &ListNode{Val: val}

		if iter1 != nil {
			iter1 = iter1.Next
		}
		if iter2 != nil {
			iter2 = iter2.Next
		}
		iterResult = iterResult.Next
	}

	return dummy.Next
}
