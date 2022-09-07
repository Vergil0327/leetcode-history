// https://leetcode.com/problems/reverse-linked-list-ii/
package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

/* Follow up: Could you do it in one pass? */
// explanation: https://www.youtube.com/watch?v=RF_M9tX4Eag&t=4s
func reverseBetweenBetter(head *ListNode, left int, right int) *ListNode {
	dummy := &ListNode{Next: head}

	// move current node to left
	dst := left - 1
	start, curr := dummy, head
	for dst > 0 {
		start, curr = curr, curr.Next
		dst -= 1
	}

	// reverse
	N := right - left + 1
	var prev *ListNode = nil
	for N > 0 {
		nxt := curr.Next
		curr.Next = prev
		prev, curr = curr, nxt
		N -= 1
	}

	start.Next.Next = curr // start.Next.Next is left node before reverse and becomes end of reversed linked list. curr is next node after reversed linked list
	start.Next = prev      // update start.Next to head of reversed link list
	return dummy.Next
}

// T:O(n) M:O(1)
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	dst := right - left
	slow, fast := head, head
	for dst > 0 {
		fast = fast.Next
		dst -= 1
	}

	var reversedHead *ListNode = nil // node before reversed section

	// 1-based position
	dst = left - 1
	for dst > 0 {
		reversedHead = slow
		slow = slow.Next
		fast = fast.Next
		dst -= 1
	}

	curr := slow
	prev := fast.Next
	fast.Next = nil
	for curr != nil {
		nxt := curr.Next
		curr.Next = prev
		prev = curr
		curr = nxt
	}

	// there exist nodes before reversed linked list
	if reversedHead != nil {
		reversedHead.Next = prev
		return head
	}

	// there is nothing before reversed linked list
	return prev
}
