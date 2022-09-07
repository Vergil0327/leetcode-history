// https://leetcode.com/problems/intersection-of-two-linked-lists/

package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

/* Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory? */

// explanation: https://www.youtube.com/watch?v=D0X0BONOQhI
// if these two intersect with each other, consider two as one linked list,
// we start at two different head, we'll reach the intersected node eventually
// if not, will reach nil finally
func getIntersectionNodeOptimal(headA, headB *ListNode) *ListNode {
	l1, l2 := headA, headB
	for l1 != l2 {
		if l1 == nil {
			l1 = headB
		} else {
			l1 = l1.Next
		}

		if l2 == nil {
			l2 = headA
		} else {
			l2 = l2.Next
		}
	}

	return l1
}

// T:O(m+n) M:O(m)
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	intersection := map[*ListNode]bool{}

	curr := headA
	for curr != nil {
		intersection[curr] = true
		curr = curr.Next
	}

	curr = headB
	for curr != nil {
		if _, ok := intersection[curr]; ok {
			return curr
		}
		curr = curr.Next
	}

	return nil
}
